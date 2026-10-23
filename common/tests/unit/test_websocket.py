import asyncio
import hashlib
import hmac
import aiohttp
import json
import logging
import pytest_asyncio
import pytest
import ssl
import time

from collections import defaultdict
from pydantic import BaseModel, ConfigDict
from typing import Optional, Set, Union
from unittest.mock import AsyncMock, call, MagicMock, patch
from types import SimpleNamespace
from urllib.parse import parse_qsl

from binance_common.configuration import (
    ConfigurationWebSocketAPI,
    ConfigurationWebSocketStreams,
)
from binance_common.constants import (
    DEFAULT_RECONNECT_ATTEMPTS,
    MAX_RECONNECT_ATTEMPTS,
    WebsocketMode,
)
from binance_common.websocket import (
    RequestStream,
    RequestStreamHandle,
    StreamConnectionsMap,
    WebSocketStreamBase,
    WebSocketAPIBase,
    WebSocketCommon,
    WebSocketConnection,
)
from binance_common.models import (
    WebsocketApiResponse,
    WebsocketApiRateLimit,
    WebsocketApiUserDataEndpoints,
)


class OrderTradeUpdate(BaseModel):
    """Futures `ORDER_TRADE_UPDATE` event."""

    e: Optional[str] = None
    E: Optional[int] = None
    i: Optional[int] = None


class ListenKeyExpired(BaseModel):
    """Futures `listenKeyExpired` event."""

    e: Optional[str] = None
    E: Optional[int] = None
    listenKey: Optional[str] = None


class UserDataStreamEventsResponse(BaseModel):
    """Mirrors the generated oneOf wrapper for user data stream events."""

    oneof_schema_1_validator: "Optional[OrderTradeUpdate]" = None
    oneof_schema_2_validator: "Optional[ListenKeyExpired]" = None
    actual_instance: "Optional[Union[OrderTradeUpdate, ListenKeyExpired, dict]]" = None
    one_of_schemas: "Set[str]" = {"OrderTradeUpdate", "ListenKeyExpired"}

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


# ========== Fixtures ==========
@pytest.fixture
def config():
    cfg = ConfigurationWebSocketAPI()
    cfg.mode = "single"
    cfg.compression = None
    cfg.proxy = None
    cfg.time_unit = None
    cfg.https_agent = None
    cfg.timeout = 10
    cfg.stream_url = "wss://test.com/ws"
    cfg.reconnect_delay = 0
    cfg.reconnect_attempts = 1
    cfg.pool_size = 2
    return cfg


@pytest.fixture
def mock_websocket():
    ws = AsyncMock()
    ws.__aiter__.return_value = []
    ws._response = MagicMock()
    ws._response.headers = {"x-mbx-uuid": "mock-uuid"}
    return ws


@pytest.fixture
def mock_config():
    config = MagicMock()
    config.mode = "single"
    config.api_key = "test-api-key"
    config.api_secret = "test-secret"
    config.stream_url = "wss://example.com/ws"
    config.mode = WebsocketMode.SINGLE
    config.proxy = None
    config.compression = None
    config.timeout = 10
    config.reconnect_delay = 0
    config.reconnect_attempts = 1
    config.pool_size = 1
    return config


@pytest.fixture
def mock_connection():
    conn = MagicMock()
    conn.id = 1
    conn.reconnect = False
    conn.websocket = AsyncMock()
    conn.stream_callback_map = {}
    conn.connection_callback_map = defaultdict(list)
    conn.response_types = {}
    conn.is_open = True
    conn.close_initiated = False
    conn.is_session_log_on = False
    conn.scheduled_reconnect_task = None
    return conn


def _share_registry(monkeypatch, attribute: str) -> StreamConnectionsMap:
    """Hand one stream map to every client created during the test."""

    registry = StreamConnectionsMap()
    original_init = WebSocketCommon.__init__

    def init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        setattr(self, attribute, registry)

    monkeypatch.setattr(WebSocketCommon, "__init__", init)
    return registry


@pytest.fixture
def mock_registry(monkeypatch):
    return _share_registry(monkeypatch, "stream_connections")


@pytest.fixture
def mock_user_registry(monkeypatch):
    return _share_registry(monkeypatch, "user_stream_connections")


@pytest.fixture
def websocket_stream(mock_config, mock_connection, mock_registry):
    instance = WebSocketStreamBase(mock_config)
    instance.connections = [mock_connection]
    instance.reconnect_tasks = []
    return instance


@pytest.fixture
def ws_api(mock_config, mock_user_registry):
    return WebSocketAPIBase(mock_config)


@pytest_asyncio.fixture(autouse=True)
async def cleanup_after_test():
    """Cleanup after each test to ensure no lingering tasks."""
    yield
    current_task = asyncio.current_task()
    tasks = [t for t in asyncio.all_tasks() if t is not current_task]
    for task in tasks:
        task.cancel()
    await asyncio.sleep(0.1)


# ========== WebSocketStreamBase Tests ==========


class TestWebSocketCommon:

    @pytest.mark.asyncio
    @patch(
        "binance_common.websocket.aiohttp.ClientSession.ws_connect",
        new_callable=AsyncMock,
    )
    async def test_connect_pool_mode(self, mock_ws_connect, config, mock_websocket):
        config.mode = WebsocketMode.POOL
        config.pool_size = 3
        mock_ws_connect.return_value = mock_websocket

        ws_common = WebSocketCommon(config)
        await ws_common.connect("wss://test.com/ws", config)

        assert len(ws_common.connections) == 3
        await ws_common.close_connection(close_session=True)

    @pytest.mark.asyncio
    async def test_ping(self, mock_websocket):
        ws_common = WebSocketCommon(MagicMock())
        connection = MagicMock()
        connection.websocket = mock_websocket
        connection.id = "123"

        await ws_common.ping(connection)
        mock_websocket.ping.assert_called_once()

    @pytest.mark.asyncio
    async def test_ping_raises_exception(self, caplog):
        ws_common = WebSocketCommon(MagicMock())
        mock_websocket = AsyncMock()
        mock_websocket.ping.side_effect = Exception("ping failed")

        connection = MagicMock()
        connection.websocket = mock_websocket
        connection.id = "123"

        await ws_common.ping(connection)

        mock_websocket.ping.assert_awaited_once()
        assert (
            f"Error sending ping to WebSocket {connection.id}: ping failed"
            in caplog.text
        )

    @pytest.mark.asyncio
    async def test_close_connection(self, mock_websocket):
        ws_common = WebSocketCommon(MagicMock())
        connection = MagicMock()
        connection.websocket = mock_websocket
        connection.id = "123"

        ws_common.connections.append(connection)

        await ws_common.close_connection(connection)
        mock_websocket.close.assert_called_once()
        assert ws_common.session is None

    @pytest.mark.asyncio
    async def test_close_connection_warns_when_no_connections(self, caplog):
        ws_common = WebSocketCommon(MagicMock())
        ws_common.connections = []

        with caplog.at_level("WARNING"):
            await ws_common.close_connection()

        assert "No WebSocket connections to close." in caplog.text

    @pytest.mark.asyncio
    async def test_close_connection_raises_exception_for_single_connection(
        self, caplog
    ):
        ws_common = WebSocketCommon(MagicMock())
        mock_websocket = AsyncMock()
        mock_websocket.close.side_effect = Exception("close error")

        connection = MagicMock()
        connection.websocket = mock_websocket
        connection.id = "123"
        ws_common.connections = [connection]

        with caplog.at_level("ERROR"):
            await ws_common.close_connection(connection)

        assert mock_websocket.close.await_count == 1
        assert f"Error closing WebSocket {connection.id}: close error" in caplog.text

    @pytest.mark.asyncio
    async def test_close_connection_raises_exception_in_loop(self, caplog):
        ws_common = WebSocketCommon(MagicMock())
        mock_websocket = AsyncMock()
        mock_websocket.close.side_effect = Exception("loop close error")

        connection = MagicMock()
        connection.websocket = mock_websocket
        connection.id = "123"
        ws_common.connections = [connection]

        with caplog.at_level("ERROR"):
            await ws_common.close_connection(connection=None)

        assert mock_websocket.close.await_count == 1
        assert (
            f"Error closing WebSocket {connection.id}: loop close error" in caplog.text
        )

    @pytest.mark.asyncio
    async def test_close_connection_closes_session_when_no_connections(self, caplog):
        session_mock = AsyncMock()
        ws_common = WebSocketCommon(MagicMock())
        ws_common.session = session_mock

        mock_websocket = AsyncMock()
        connection = MagicMock()
        connection.websocket = mock_websocket
        connection.id = "123"
        ws_common.connections = [connection]

        await ws_common.close_connection(connection, close_session=True)

        session_mock.close.assert_awaited_once()
        assert ws_common.session is None

    @pytest.mark.asyncio
    @patch(
        "binance_common.websocket.aiohttp.ClientSession.ws_connect",
        new_callable=AsyncMock,
    )
    async def test_schedule_reconnect(
        self, mock_ws_connect, config, mock_websocket, mock_registry
    ):
        mock_ws_connect.return_value = mock_websocket
        ws_common = WebSocketCommon(config)
        await ws_common.connect("wss://test.com/ws", config)
        connection = ws_common.connections[0]

        callback = {"foo": lambda x: x}

        mock_registry.stream_connections_map = {"foo": connection}
        connection.stream_callback_map = callback

        await ws_common.schedule_reconnect(connection, config, delay=0)
        new_conn = mock_registry.stream_connections_map["foo"]

        assert new_conn.id == connection.id
        assert new_conn is not connection
        assert new_conn.stream_callback_map == callback
        assert connection.id not in ws_common.reconnect_tasks

    @pytest.mark.asyncio
    @patch(
        "binance_common.websocket.WebSocketCommon.receive_loop", new_callable=AsyncMock
    )
    @patch(
        "binance_common.websocket.aiohttp.ClientSession.ws_connect",
        new_callable=AsyncMock,
    )
    async def test_send_message_with_promised_response(
        self, mock_ws_connect, mock_receive_loop, config, mock_websocket
    ):
        mock_ws_connect.return_value = mock_websocket
        mock_websocket.send_str = AsyncMock()

        ws_common = WebSocketCommon(config)
        await ws_common.connect("wss://test.com/ws", config)

        connection = ws_common.connections[0]
        connection.ws_type = "ConfigurationWebSocketAPI"
        connection.pending_request = {}

        payload = {"id": "abc123"}
        future = asyncio.Future()
        future.set_result({"result": '{"success": true}', "rateLimits": []})
        connection.pending_request["abc123"] = future

        result = await ws_common.send_message(payload, connection)

        mock_websocket.send_str.assert_awaited_once_with(json.dumps(payload))
        assert isinstance(result, asyncio.Future)
        resolved_value = await result
        assert resolved_value == {"result": '{"success": true}', "rateLimits": []}

    @pytest.mark.asyncio
    @patch(
        "binance_common.websocket.aiohttp.ClientSession.ws_connect",
        new_callable=AsyncMock,
    )
    async def test_connect_single_mode(self, mock_ws_connect, config, mock_websocket):
        mock_ws_connect.return_value = mock_websocket

        ws_common = WebSocketCommon(config)
        await ws_common.connect("wss://test.com/ws", config)

        assert len(ws_common.connections) == 1
        connection = ws_common.connections[0]
        assert isinstance(connection, WebSocketConnection)
        assert connection.id == "mock-uuid"
        assert connection.url_path is None

    @pytest.mark.asyncio
    @patch(
        "binance_common.websocket.aiohttp.ClientSession.ws_connect",
        new_callable=AsyncMock,
    )
    async def test_connect_streams_disables_autoping(
        self, mock_ws_connect, mock_websocket
    ):
        mock_ws_connect.return_value = mock_websocket

        streams_config = ConfigurationWebSocketStreams(stream_url="wss://test.com/ws")
        streams_config.mode = "single"

        ws_common = WebSocketCommon(streams_config)
        await ws_common.connect("wss://test.com/ws", streams_config)

        _, kwargs = mock_ws_connect.call_args
        assert kwargs["autoping"] is False

    @pytest.mark.asyncio
    @patch(
        "binance_common.websocket.aiohttp.ClientSession.ws_connect",
        new_callable=AsyncMock,
    )
    async def test_connect_api_disables_autoping(
        self, mock_ws_connect, mock_websocket, config
    ):
        mock_ws_connect.return_value = mock_websocket

        ws_common = WebSocketCommon(config)
        await ws_common.connect("wss://test.com/ws", config)

        _, kwargs = mock_ws_connect.call_args
        assert kwargs["autoping"] is False

    @pytest.mark.asyncio
    @patch(
        "binance_common.websocket.aiohttp.ClientSession.ws_connect",
        new_callable=AsyncMock,
    )
    async def test_connect_verifies_certificates_by_default(
        self, mock_ws_connect, mock_websocket, config
    ):
        """An unset `https_agent` must reach `aiohttp` as a verified context."""
        mock_ws_connect.return_value = mock_websocket

        ws_common = WebSocketCommon(config)
        await ws_common.connect("wss://test.com/ws", config)

        _, kwargs = mock_ws_connect.call_args
        assert kwargs["ssl"] is True

    @pytest.mark.asyncio
    @patch(
        "binance_common.websocket.aiohttp.ClientSession.ws_connect",
        new_callable=AsyncMock,
    )
    async def test_connect_passes_an_ssl_context_through(
        self, mock_ws_connect, mock_websocket, config
    ):
        mock_ws_connect.return_value = mock_websocket
        context = ssl.create_default_context()
        config.https_agent = context

        ws_common = WebSocketCommon(config)
        await ws_common.connect("wss://test.com/ws", config)

        _, kwargs = mock_ws_connect.call_args
        assert kwargs["ssl"] is context

    @pytest.mark.asyncio
    @patch(
        "binance_common.websocket.aiohttp.ClientSession.ws_connect",
        new_callable=AsyncMock,
    )
    async def test_connect_warns_when_certificate_verification_is_disabled(
        self, mock_ws_connect, mock_websocket, config
    ):
        mock_ws_connect.return_value = mock_websocket
        config.https_agent = False

        ws_common = WebSocketCommon(config)
        with pytest.warns(UserWarning, match="disables TLS certificate verification"):
            await ws_common.connect("wss://test.com/ws", config)

        _, kwargs = mock_ws_connect.call_args
        assert kwargs["ssl"] is False

    @pytest.mark.asyncio
    @patch(
        "binance_common.websocket.aiohttp.ClientSession.ws_connect",
        new_callable=AsyncMock,
    )
    async def test_connect_streams_verifies_certificates_by_default(
        self, mock_ws_connect, mock_websocket
    ):
        mock_ws_connect.return_value = mock_websocket

        streams_config = ConfigurationWebSocketStreams(stream_url="wss://test.com/ws")
        streams_config.mode = "single"

        ws_common = WebSocketCommon(streams_config)
        await ws_common.connect("wss://test.com/ws", streams_config)

        _, kwargs = mock_ws_connect.call_args
        assert kwargs["ssl"] is True

    @pytest.mark.asyncio
    @patch(
        "binance_common.websocket.aiohttp.ClientSession.ws_connect",
        new_callable=AsyncMock,
    )
    async def test_connect_single_mode_with_url_path(
        self, mock_ws_connect, config, mock_websocket
    ):
        mock_ws_connect.return_value = mock_websocket

        ws_common = WebSocketCommon(config)
        await ws_common.connect("wss://test.com/ws", config, url_paths=["path1"])

        assert len(ws_common.connections) == 1
        connection = ws_common.connections[0]
        assert isinstance(connection, WebSocketConnection)
        assert connection.id == "mock-uuid"
        assert connection.url_path == "path1"

    @pytest.mark.asyncio
    @patch(
        "binance_common.websocket.aiohttp.ClientSession.ws_connect",
        new_callable=AsyncMock,
    )
    async def test_connect_pool_mode_with_url_paths(
        self, mock_ws_connect, config, mock_websocket
    ):
        mock_ws_connect.return_value = mock_websocket
        config.pool_size = 2
        config.mode = WebsocketMode.POOL

        ws_common = WebSocketCommon(config)
        await ws_common.connect(
            "wss://test.com/ws", config, url_paths=["path1", "path2"]
        )

        assert len(ws_common.connections) == 4
        for i, connection in enumerate(ws_common.connections):
            assert isinstance(connection, WebSocketConnection)
            assert connection.id == "mock-uuid"
            expected_path = "path1" if i < 2 else "path2"
            assert connection.url_path == expected_path

    @pytest.mark.asyncio
    async def test_receive_loop_handles_text_with_id(self):
        msg_data = {"id": "123", "result": "ok"}
        msg = MagicMock()
        msg.type = aiohttp.WSMsgType.TEXT
        msg.data = json.dumps(msg_data)

        ws_mock = AsyncMock()
        ws_mock.__aiter__.return_value = [msg]

        conn = WebSocketConnection(ws_mock, "test_id", "ConfigurationWebSocketAPI")
        future = asyncio.Future()
        conn.pending_request["123"] = future

        ws_common = WebSocketCommon(None)
        await ws_common.receive_loop(conn)

        assert future.done()
        assert future.result() == msg_data

    @pytest.mark.asyncio
    async def test_receive_loop_stream_calls_callbacks(self):
        ws_mock = AsyncMock()
        callback = MagicMock()
        msg_data = {"stream": "ticker", "data": {"price": "100"}}
        msg = MagicMock()
        msg.type = aiohttp.WSMsgType.TEXT
        msg.data = json.dumps(msg_data)
        ws_mock.__aiter__.return_value = [msg]

        conn = WebSocketConnection(ws_mock, "test_id", "ConfigurationWebSocketStreams")
        conn.stream_callback_map["ticker"] = [callback]

        ws_common = WebSocketCommon(None)
        await ws_common.receive_loop(conn)

        callback.assert_called_once_with(msg_data)

    @pytest.mark.asyncio
    async def test_receive_loop_stream_parses_one_of_response_model(self):
        ws_mock = AsyncMock()
        callback = MagicMock()
        event = {"e": "ORDER_TRADE_UPDATE", "E": 1568879465650, "i": 8886774}
        msg = MagicMock()
        msg.type = aiohttp.WSMsgType.TEXT
        msg.data = json.dumps({"stream": "listen-key", "data": event})
        ws_mock.__aiter__.return_value = [msg]

        conn = WebSocketConnection(ws_mock, "test_id", "ConfigurationWebSocketStreams")
        conn.stream_callback_map["listen-key"] = [callback]
        conn.response_types["listen-key"] = UserDataStreamEventsResponse

        ws_common = WebSocketCommon(None)
        await ws_common.receive_loop(conn)

        callback.assert_called_once()
        parsed = callback.call_args[0][0]
        assert isinstance(parsed, UserDataStreamEventsResponse)
        assert isinstance(parsed.actual_instance, OrderTradeUpdate)
        assert parsed.actual_instance.i == 8886774

    @pytest.mark.asyncio
    async def test_receive_loop_stream_parses_one_of_response_model_list(self):
        ws_mock = AsyncMock()
        callback = MagicMock()
        events = [
            {"e": "ORDER_TRADE_UPDATE", "E": 1, "i": 1},
            {"e": "listenKeyExpired", "E": 2, "listenKey": "abc"},
        ]
        msg = MagicMock()
        msg.type = aiohttp.WSMsgType.TEXT
        msg.data = json.dumps({"stream": "listen-key", "data": events})
        ws_mock.__aiter__.return_value = [msg]

        conn = WebSocketConnection(ws_mock, "test_id", "ConfigurationWebSocketStreams")
        conn.stream_callback_map["listen-key"] = [callback]
        conn.response_types["listen-key"] = UserDataStreamEventsResponse

        ws_common = WebSocketCommon(None)
        await ws_common.receive_loop(conn)

        parsed = callback.call_args[0][0]
        assert [type(item.actual_instance) for item in parsed] == [
            OrderTradeUpdate,
            ListenKeyExpired,
        ]

    @pytest.mark.asyncio
    async def test_receive_loop_stream_unknown_one_of_event_keeps_raw_payload(self):
        ws_mock = AsyncMock()
        callback = MagicMock()
        event = {"e": "SOME_FUTURE_EVENT", "foo": "bar"}
        msg = MagicMock()
        msg.type = aiohttp.WSMsgType.TEXT
        msg.data = json.dumps({"stream": "listen-key", "data": event})
        ws_mock.__aiter__.return_value = [msg]

        conn = WebSocketConnection(ws_mock, "test_id", "ConfigurationWebSocketStreams")
        conn.stream_callback_map["listen-key"] = [callback]
        conn.response_types["listen-key"] = UserDataStreamEventsResponse

        ws_common = WebSocketCommon(None)
        await ws_common.receive_loop(conn)

        callback.assert_called_once()
        assert callback.call_args[0][0].actual_instance == event

    @pytest.mark.asyncio
    async def test_receive_loop_subscription_id_calls_callbacks(self):
        ws_mock = AsyncMock()
        callback = MagicMock()
        msg_data = {"subscriptionId": 0, "event": {"test": "test"}}
        msg = MagicMock()
        msg.type = aiohttp.WSMsgType.TEXT
        msg.data = json.dumps(msg_data)
        ws_mock.__aiter__.return_value = [msg]

        conn = WebSocketConnection(ws_mock, "test_id", "ConfigurationWebSocketAPI")
        conn.stream_callback_map[0] = [callback]

        ws_common = WebSocketCommon(None)
        await ws_common.receive_loop(conn)

        callback.assert_called_once_with(msg_data["event"])

    @pytest.mark.asyncio
    async def test_receive_loop_handles_ping_and_pong(self):
        ping_msg = MagicMock()
        ping_msg.type = aiohttp.WSMsgType.PING
        ping_msg.data = b"ping-payload"

        pong_msg = MagicMock()
        pong_msg.type = aiohttp.WSMsgType.PONG
        pong_msg.data = b"pong-payload"

        ws_mock = AsyncMock()
        ws_mock.pong = AsyncMock()
        ws_mock.__aiter__.return_value = [ping_msg, pong_msg]

        conn = WebSocketConnection(ws_mock, "test_id", "ConfigurationWebSocketStreams")

        ws_common = WebSocketCommon(None)
        ws_common._emit_connection_event = MagicMock()

        await ws_common.receive_loop(conn)

        ws_mock.pong.assert_awaited_once_with(b"ping-payload")

        ws_common._emit_connection_event.assert_has_calls(
            [
                call(conn, "ping", b"ping-payload"),
                call(conn, "pong", b"pong-payload"),
            ]
        )

    @pytest.mark.asyncio
    async def test_receive_loop_pongs_before_ping_callback_runs(self):
        """A failing ping callback must not prevent the pong reply."""

        ping_msg = MagicMock()
        ping_msg.type = aiohttp.WSMsgType.PING
        ping_msg.data = b""

        ws_mock = AsyncMock()
        ws_mock.pong = AsyncMock()
        ws_mock.__aiter__.return_value = [ping_msg]

        conn = WebSocketConnection(ws_mock, "test_id", "ConfigurationWebSocketStreams")
        conn.connection_callback_map["ping"].append(
            MagicMock(side_effect=Exception("boom"))
        )

        ws_common = WebSocketCommon(None)
        await ws_common.receive_loop(conn)

        ws_mock.pong.assert_awaited_once_with(b"")
        assert conn.is_open is False

    @pytest.mark.asyncio
    async def test_receive_loop_server_error_keeps_loop_alive(self):
        """A server error payload must not tear down the receive loop."""

        error_msg = MagicMock()
        error_msg.type = aiohttp.WSMsgType.TEXT
        error_msg.data = json.dumps({"error": {"code": -1121, "msg": "Invalid symbol"}})

        data_msg = MagicMock()
        data_msg.type = aiohttp.WSMsgType.TEXT
        data_msg.data = json.dumps({"stream": "ticker", "data": {"price": "100"}})

        ws_mock = AsyncMock()
        ws_mock.__aiter__.return_value = [error_msg, data_msg]

        conn = WebSocketConnection(ws_mock, "test_id", "ConfigurationWebSocketStreams")
        error_cb = MagicMock()
        conn.connection_callback_map["error"].append(error_cb)
        stream_cb = MagicMock()
        conn.stream_callback_map["ticker"] = [stream_cb]

        ws_common = WebSocketCommon(None)
        await ws_common.receive_loop(conn)

        error_cb.assert_called_once_with({"code": -1121, "msg": "Invalid symbol"})
        stream_cb.assert_called_once()

    @pytest.mark.asyncio
    async def test_receive_loop_stream_callback_error_keeps_loop_alive(self):
        """A throwing user callback must not tear down the receive loop."""

        msg_data = {"stream": "ticker", "data": {"price": "100"}}
        first = MagicMock()
        first.type = aiohttp.WSMsgType.TEXT
        first.data = json.dumps(msg_data)

        second = MagicMock()
        second.type = aiohttp.WSMsgType.TEXT
        second.data = json.dumps(msg_data)

        ws_mock = AsyncMock()
        ws_mock.__aiter__.return_value = [first, second]

        conn = WebSocketConnection(ws_mock, "test_id", "ConfigurationWebSocketStreams")
        failing = MagicMock(side_effect=Exception("callback boom"))
        conn.stream_callback_map["ticker"] = [failing]
        error_cb = MagicMock()
        conn.connection_callback_map["error"].append(error_cb)

        ws_common = WebSocketCommon(None)
        await ws_common.receive_loop(conn)

        assert failing.call_count == 2
        assert error_cb.call_count == 2
        assert conn.connection_callback_map["close"] == []

    @pytest.mark.asyncio
    async def test_receive_loop_request_error_only_rejects_future(self):
        """A per-request error goes to the awaiting caller, not the error event."""

        error = {"code": -1121, "msg": "Invalid symbol"}
        msg = MagicMock()
        msg.type = aiohttp.WSMsgType.TEXT
        msg.data = json.dumps({"id": "123", "error": error})

        ws_mock = AsyncMock()
        ws_mock.__aiter__.return_value = [msg]

        conn = WebSocketConnection(ws_mock, "test_id", "ConfigurationWebSocketAPI")
        future = asyncio.Future()
        conn.pending_request["123"] = future
        error_cb = MagicMock()
        conn.connection_callback_map["error"].append(error_cb)

        ws_common = WebSocketCommon(None)
        await ws_common.receive_loop(conn)

        error_cb.assert_not_called()
        assert isinstance(future.exception(), ValueError)
        assert future.exception().args[0] == error

    @pytest.mark.asyncio
    async def test_receive_loop_error_emits_connection_error(self):
        error_msg = MagicMock()
        error_msg.type = aiohttp.WSMsgType.ERROR

        ws_mock = AsyncMock()
        ws_mock.__aiter__.return_value = [error_msg]

        exc = Exception("test error")
        ws_mock.exception = MagicMock(return_value=exc)

        conn = WebSocketConnection(ws_mock, "test_id", "ConfigurationWebSocketStreams")
        ws_common = WebSocketCommon(None)
        ws_common._emit_connection_event = MagicMock()

        await ws_common.receive_loop(conn)

        assert conn.is_open is False
        ws_common._emit_connection_event.assert_has_calls(
            [
                call(conn, "error", exc),
                call(conn, "close"),
            ]
        )

    @pytest.mark.asyncio
    async def test_receive_loop_emits_close_on_normal_exit(self):
        ws_mock = AsyncMock()
        ws_mock.__aiter__.return_value = []

        conn = WebSocketConnection(ws_mock, "test_id", "ConfigurationWebSocketStreams")
        ws_common = WebSocketCommon(None)
        ws_common._emit_connection_event = MagicMock()

        await ws_common.receive_loop(conn)

        ws_common._emit_connection_event.assert_called_once_with(conn, "close")

    @pytest.mark.asyncio
    async def test_receive_loop_emits_close_once_on_close_frame(self):
        close_msg = MagicMock()
        close_msg.type = aiohttp.WSMsgType.CLOSE

        ws_mock = AsyncMock()
        ws_mock.__aiter__.return_value = [close_msg]

        conn = WebSocketConnection(ws_mock, "test_id", "ConfigurationWebSocketStreams")
        ws_common = WebSocketCommon(None)
        ws_common._emit_connection_event = MagicMock()

        await ws_common.receive_loop(conn)

        ws_common._emit_connection_event.assert_called_once_with(conn, "close")

    @pytest.mark.asyncio
    async def test_reconnect_resubscribes(
        self, mock_connection, mock_registry, mock_user_registry
    ):
        ws_common = WebSocketCommon(MagicMock())

        old_conn = mock_connection
        old_conn.id = "abc"
        old_conn.url_path = None
        old_conn.pending_request = {"1": MagicMock()}
        old_conn.session_logon_request = {
            "method": "session.logon",
            "params": {},
            "id": "1",
        }
        old_conn.stream_callback_map = {"user_stream": ["cb1"], "trade": ["cb2"]}
        old_conn.response_types = {"user_stream": "rtype1", "trade": "rtype2"}

        new_conn = MagicMock()
        new_conn.id = "abc"
        ws_common.connections = [new_conn]

        ws_common.close_connection = AsyncMock()
        ws_common.init_connection = AsyncMock()
        ws_common.session_re_log_on = AsyncMock()
        ws_common._resubscribe_user_streams = AsyncMock()
        ws_common._resubscribe_global_streams = AsyncMock()
        ws_common.reconnect_tasks = ["abc"]

        config = MagicMock()
        config.stream_url = "wss://test.com/ws"
        config.reconnect_delay = 0
        config.reconnect_attempts = 1

        await ws_common.reconnect(old_conn, config)

        ws_common.close_connection.assert_awaited_once_with(old_conn, False)
        ws_common.init_connection.assert_awaited_once_with(
            config.stream_url, config, old_conn.url_path, old_conn.id
        )
        ws_common.session_re_log_on.assert_awaited_once_with(
            old_conn.session_logon_request, new_conn
        )
        ws_common._resubscribe_user_streams.assert_awaited_once_with(old_conn, new_conn)
        ws_common._resubscribe_global_streams.assert_awaited_once_with(
            old_conn, new_conn
        )
        assert "abc" not in ws_common.reconnect_tasks
        assert old_conn.reconnect is False

    @pytest.mark.asyncio
    async def test_resubscribe_user_streams(self, mock_connection, mock_user_registry):
        ws_common = WebSocketCommon(MagicMock())
        ws_common.user_data_endpoints = MagicMock()
        ws_common.user_data_endpoints.user_data_stream_subscribe = (
            "userDataStream.subscribe"
        )

        old_conn = mock_connection
        old_conn.id = "abc"
        old_conn.stream_callback_map = {"user_stream": ["cb1"]}
        old_conn.response_types = {"user_stream": "rtype1"}

        new_conn = MagicMock()
        new_conn.stream_callback_map = {}
        new_conn.response_types = {}

        mock_user_registry.stream_connections_map = {"user_stream": old_conn}

        with patch.object(
            WebSocketCommon, "send_message", new_callable=AsyncMock
        ) as mock_send:
            await ws_common._resubscribe_user_streams(old_conn, new_conn)

            mock_send.assert_awaited_once()
            assert new_conn.stream_callback_map["user_stream"] == ["cb1"]
            assert new_conn.response_types["user_stream"] == "rtype1"
            assert mock_user_registry.stream_connections_map["user_stream"] == new_conn

    @pytest.mark.asyncio
    async def test_resubscribe_global_streams(self, mock_connection, mock_registry):
        ws_common = WebSocketCommon(MagicMock())

        old_conn = mock_connection
        old_conn.id = "abc"
        old_conn.stream_callback_map = {"trade": ["cb2"]}
        old_conn.response_types = {"trade": "rtype2"}

        new_conn = MagicMock()
        new_conn.id = "abc"
        new_conn.stream_callback_map = {}
        new_conn.response_types = {}

        mock_registry.stream_connections_map = {"trade": old_conn}

        with patch.object(
            WebSocketCommon, "send_message", new_callable=AsyncMock
        ) as mock_send:
            await ws_common._resubscribe_global_streams(old_conn, new_conn)

            mock_send.assert_awaited_once()
            assert new_conn.stream_callback_map["trade"] == ["cb2"]
            assert new_conn.response_types["trade"] == "rtype2"
            assert mock_registry.stream_connections_map["trade"] == new_conn

    @pytest.mark.asyncio
    async def test_initiates_renewal_on_server_shutdown(self):
        payload = {"event": {"e": "serverShutdown", "E": int(time.time() * 1000)}}

        msg = MagicMock()
        msg.type = aiohttp.WSMsgType.TEXT
        msg.data = json.dumps(payload)

        ws_mock = AsyncMock()
        ws_mock.__aiter__.return_value = [msg]

        conn = WebSocketConnection(ws_mock, "test_id", "ConfigurationWebSocketStreams")

        ws_common = WebSocketCommon(MagicMock())
        ws_common.connections = [conn]
        ws_common.reconnect = AsyncMock()

        await ws_common.receive_loop(conn)

        ws_common.reconnect.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_no_renewal_when_already_pending(self):
        payload = {"event": {"e": "serverShutdown", "E": int(time.time() * 1000)}}

        msg = MagicMock()
        msg.type = aiohttp.WSMsgType.TEXT
        msg.data = json.dumps(payload)

        ws_mock = AsyncMock()
        ws_mock.__aiter__.return_value = [msg]

        conn = WebSocketConnection(ws_mock, "test_id", "ConfigurationWebSocketStreams")

        ws_common = WebSocketCommon(MagicMock())
        ws_common.reconnect = AsyncMock()

        ws_common.reconnect_tasks.append(conn.id)

        await ws_common.receive_loop(conn)

        ws_common.reconnect.assert_not_called()

    @pytest.mark.asyncio
    async def test_no_renewal_when_close_initiated(self):
        payload = {"event": {"e": "serverShutdown", "E": int(time.time() * 1000)}}

        msg = MagicMock()
        msg.type = aiohttp.WSMsgType.TEXT
        msg.data = json.dumps(payload)

        ws_mock = AsyncMock()
        ws_mock.__aiter__.return_value = [msg]

        conn = WebSocketConnection(ws_mock, "test_id", "ConfigurationWebSocketStreams")

        ws_common = WebSocketCommon(MagicMock())
        ws_common.reconnect = AsyncMock()
        ws_common.close_initiated = True

        await ws_common.receive_loop(conn)

        ws_common.reconnect.assert_not_called()

    @pytest.mark.asyncio
    async def test_no_renewal_for_non_server_shutdown_event(self):
        payload = {"event": {"e": "somethingElse", "E": int(time.time() * 1000)}}

        msg = MagicMock()
        msg.type = aiohttp.WSMsgType.TEXT
        msg.data = json.dumps(payload)

        ws_mock = AsyncMock()
        ws_mock.__aiter__.return_value = [msg]

        conn = WebSocketConnection(ws_mock, "test_id", "ConfigurationWebSocketStreams")

        ws_common = WebSocketCommon(MagicMock())
        ws_common.reconnect = AsyncMock()

        await ws_common.receive_loop(conn)

        ws_common.reconnect.assert_not_called()

    @pytest.mark.asyncio
    async def test_no_renewal_for_malformed_payload(self):
        payload = {"foo": "bar"}

        msg = MagicMock()
        msg.type = aiohttp.WSMsgType.TEXT
        msg.data = json.dumps(payload)

        ws_mock = AsyncMock()
        ws_mock.__aiter__.return_value = [msg]

        conn = WebSocketConnection(ws_mock, "test_id", "ConfigurationWebSocketStreams")

        ws_common = WebSocketCommon(MagicMock())
        ws_common.reconnect = AsyncMock()

        await ws_common.receive_loop(conn)

        ws_common.reconnect.assert_not_called()

    def test_emit_connection_event_calls_sync_callback(self):
        ws_common = WebSocketCommon(MagicMock())
        callback = MagicMock()
        connection = MagicMock()
        connection.connection_callback_map = {
            "connected": [callback]
        }

        ws_common._emit_connection_event(connection, "connected", connection)

        callback.assert_called_once_with(connection)

    def test_emit_connection_event_calls_multiple_callbacks(self):
        ws_common = WebSocketCommon(MagicMock())
        cb1 = MagicMock()
        cb2 = MagicMock()
        connection = MagicMock()
        connection.connection_callback_map = {
            "connected": [cb1, cb2]
        }

        ws_common._emit_connection_event(connection, "connected", connection)

        cb1.assert_called_once_with(connection)
        cb2.assert_called_once_with(connection)

    def test_emit_connection_event_no_callbacks_does_nothing(self):
        ws_common = WebSocketCommon(MagicMock())
        connection = MagicMock()
        connection.connection_callback_map = {}

        ws_common._emit_connection_event(connection, "connected", connection)

    def test_emit_connection_event_logs_callback_error(self, caplog):
        ws_common = WebSocketCommon(MagicMock())
        failing = MagicMock(side_effect=Exception("connection callback failed"))
        surviving = MagicMock()
        connection = MagicMock()
        connection.id = "test_id"
        connection.connection_callback_map = {"close": [failing, surviving]}

        with caplog.at_level(logging.ERROR):
            ws_common._emit_connection_event(connection, "close")

        assert "connection callback failed" in caplog.text
        surviving.assert_called_once_with()

    def test_emit_connection_event_schedules_async_callback(self):
        ws_common = WebSocketCommon(MagicMock())
        calls = []

        async def callback():
            calls.append("called")

        connection = MagicMock()
        connection.id = "test_id"
        connection.connection_callback_map = {"close": [callback]}

        async def run():
            ws_common._emit_connection_event(connection, "close")
            await asyncio.sleep(0)

        asyncio.run(run())

        assert calls == ["called"]

    def test_emit_connection_event_accepts_zero_arg_callback(self):
        """A payload-carrying event must still accept a no-parameter callback."""

        ws_common = WebSocketCommon(MagicMock())
        calls = []
        connection = MagicMock()
        connection.id = "test_id"
        connection.connection_callback_map = {"ping": [lambda: calls.append("no-args")]}

        ws_common._emit_connection_event(connection, "ping", b"payload")

        assert calls == ["no-args"]

    def test_emit_connection_event_passes_payload_when_accepted(self):
        ws_common = WebSocketCommon(MagicMock())
        received = []
        connection = MagicMock()
        connection.id = "test_id"
        connection.connection_callback_map = {"ping": [lambda data: received.append(data)]}

        ws_common._emit_connection_event(connection, "ping", b"payload")

        assert received == [b"payload"]

    def test_emit_connection_event_passes_payload_to_var_positional(self):
        ws_common = WebSocketCommon(MagicMock())
        received = []
        connection = MagicMock()
        connection.id = "test_id"
        connection.connection_callback_map = {
            "ping": [lambda *args: received.append(args)]
        }

        ws_common._emit_connection_event(connection, "ping", b"payload")

        assert received == [(b"payload",)]

    def test_emit_trims_payload_to_accepted_arity(self):
        """A callback declared without parameters may ignore the payload."""

        ws_common = WebSocketCommon(MagicMock())
        connection = WebSocketConnection(
            AsyncMock(), "test_id", "ConfigurationWebSocketStreams"
        )
        received = []

        connection.connection_callback_map["ping"] = [
            lambda: received.append("no-args"),
            lambda d: received.append(("one-arg", d)),
            lambda *a: received.append(("var-args", a)),
        ]

        ws_common._emit_connection_event(connection, "ping", b"x")

        assert received == [
            "no-args",
            ("one-arg", b"x"),
            ("var-args", (b"x",)),
        ]

    def test_emit_passes_payload_to_unintrospectable_callback(self):
        """Builtins without a signature must still receive the payload."""

        ws_common = WebSocketCommon(MagicMock())
        connection = WebSocketConnection(
            AsyncMock(), "test_id", "ConfigurationWebSocketStreams"
        )
        callback = MagicMock(spec=print)
        connection.connection_callback_map["ping"] = [callback]

        ws_common._emit_connection_event(connection, "ping", b"x")

        callback.assert_called_once_with(b"x")

    def test_validate_connection_event_rejects_unknown(self):
        with pytest.raises(ValueError, match="Unsupported connection event: message"):
            WebSocketCommon._validate_connection_event("message")

    def test_on_connection_invokes_open_immediately(self):
        ws_common = WebSocketCommon(MagicMock())
        connection = WebSocketConnection(
            AsyncMock(), "test_id", "ConfigurationWebSocketStreams"
        )
        ws_common.connections = [connection]
        callback = MagicMock()

        ws_common.on_connection("open", callback)

        callback.assert_called_once_with()
        assert connection.connection_callback_map["open"] == [callback]

    def test_on_connection_deduplicates_bound_method(self):
        """A bound method is a new object per access but must register once."""

        class Handler:
            def on_close(self):
                pass

        handler = Handler()
        ws_common = WebSocketCommon(MagicMock())
        connection = WebSocketConnection(
            AsyncMock(), "test_id", "ConfigurationWebSocketStreams"
        )
        ws_common.connections = [connection]

        ws_common.on_connection("close", handler.on_close)
        ws_common.on_connection("close", handler.on_close)

        assert connection.connection_callback_map["close"] == [handler.on_close]

    def test_off_connection_accepts_rebound_method(self):
        """A freshly bound method still removes the registered one."""

        class Handler:
            def on_close(self):
                pass

        handler = Handler()
        ws_common = WebSocketCommon(MagicMock())
        connection = WebSocketConnection(
            AsyncMock(), "test_id", "ConfigurationWebSocketStreams"
        )
        ws_common.connections = [connection]

        ws_common.on_connection("close", handler.on_close)
        ws_common.off_connection("close", handler.on_close)

        assert connection.connection_callback_map["close"] == []

    def test_on_connection_reports_open_once(self):
        """A duplicate registration neither re-fires `open` nor doubles up."""

        ws_common = WebSocketCommon(MagicMock())
        connection = WebSocketConnection(
            AsyncMock(), "test_id", "ConfigurationWebSocketStreams"
        )
        ws_common.connections = [connection]
        callback = MagicMock()

        ws_common.on_connection("open", callback)
        ws_common.on_connection("open", callback)

        callback.assert_called_once_with()
        assert connection.connection_callback_map["open"] == [callback]

    def test_on_connection_skips_open_when_closed(self):
        ws_common = WebSocketCommon(MagicMock())
        connection = WebSocketConnection(
            AsyncMock(), "test_id", "ConfigurationWebSocketStreams"
        )
        connection.is_open = False
        ws_common.connections = [connection]
        callback = MagicMock()

        ws_common.on_connection("open", callback)

        callback.assert_not_called()

    def test_on_connection_does_not_invoke_other_events(self):
        ws_common = WebSocketCommon(MagicMock())
        connection = WebSocketConnection(
            AsyncMock(), "test_id", "ConfigurationWebSocketStreams"
        )
        ws_common.connections = [connection]
        callback = MagicMock()

        ws_common.on_connection("close", callback)

        callback.assert_not_called()
        assert connection.connection_callback_map["close"] == [callback]

    def test_on_connection_registers_by_connection_id(self):
        ws_common = WebSocketCommon(MagicMock())
        connection = WebSocketConnection(
            AsyncMock(), "test_id", "ConfigurationWebSocketStreams"
        )
        ws_common.connections = [connection]
        callback = MagicMock()

        ws_common.on_connection("close", callback, "test_id")

        assert connection.connection_callback_map["close"] == [callback]

    def test_on_connection_warns_when_not_connected(self, caplog):
        ws_common = WebSocketCommon(MagicMock())
        ws_common.connections = []

        with caplog.at_level(logging.WARNING):
            ws_common.on_connection("close", MagicMock(), "missing")

        assert "Connection missing not connected." in caplog.text

    def test_on_connection_accepts_connection_object(self):
        ws_common = WebSocketCommon(MagicMock())
        connection = WebSocketConnection(
            AsyncMock(), "test_id", "ConfigurationWebSocketStreams"
        )
        ws_common.connections = [connection]
        callback = MagicMock()

        ws_common.on_connection("ping", callback, connection)

        assert connection.connection_callback_map["ping"] == [callback]

    def test_on_connection_registers_on_every_connection(self):
        """Omitting the selector observes the whole pool."""

        ws_common = WebSocketCommon(MagicMock())
        first = WebSocketConnection(AsyncMock(), "a", "ConfigurationWebSocketStreams")
        second = WebSocketConnection(AsyncMock(), "b", "ConfigurationWebSocketStreams")
        ws_common.connections = [first, second]
        callback = MagicMock()

        ws_common.on_connection("ping", callback)

        assert first.connection_callback_map["ping"] == [callback]
        assert second.connection_callback_map["ping"] == [callback]

    def test_on_connection_fires_once_per_connection_event(self):
        """A ping on the connection reaches a connection-scoped callback once."""

        ws_common = WebSocketCommon(MagicMock())
        connection = WebSocketConnection(
            AsyncMock(), "test_id", "ConfigurationWebSocketStreams"
        )
        ws_common.connections = [connection]
        callback = MagicMock()

        ws_common.on_connection("ping", callback, "test_id")
        ws_common._emit_connection_event(connection, "ping", b"payload")

        callback.assert_called_once_with(b"payload")


    def test_off_connection_removes_from_every_connection(self):
        ws_common = WebSocketCommon(MagicMock())
        first = WebSocketConnection(AsyncMock(), "a", "ConfigurationWebSocketStreams")
        second = WebSocketConnection(AsyncMock(), "b", "ConfigurationWebSocketStreams")
        ws_common.connections = [first, second]
        callback = MagicMock()

        ws_common.on_connection("ping", callback)
        ws_common.off_connection("ping", callback)

        assert first.connection_callback_map["ping"] == []
        assert second.connection_callback_map["ping"] == []

    def test_off_connection_scoped_to_one_connection(self):
        ws_common = WebSocketCommon(MagicMock())
        first = WebSocketConnection(AsyncMock(), "a", "ConfigurationWebSocketStreams")
        second = WebSocketConnection(AsyncMock(), "b", "ConfigurationWebSocketStreams")
        ws_common.connections = [first, second]
        callback = MagicMock()

        ws_common.on_connection("ping", callback)
        ws_common.off_connection("ping", callback, "a")

        assert first.connection_callback_map["ping"] == []
        assert second.connection_callback_map["ping"] == [callback]

    def test_on_connection_rejects_unknown_event(self):
        ws_common = WebSocketCommon(MagicMock())

        with pytest.raises(ValueError, match="Unsupported connection event: message"):
            ws_common.on_connection("message", MagicMock())

    def test_on_connection_warns_when_pool_empty(self, caplog):
        ws_common = WebSocketCommon(MagicMock())
        ws_common.connections = []

        with caplog.at_level(logging.WARNING):
            ws_common.on_connection("ping", MagicMock())

        assert "No WebSocket connections available" in caplog.text

    def test_on_connection_warns_for_unknown_id(self, caplog):
        ws_common = WebSocketCommon(MagicMock())
        ws_common.connections = []

        with caplog.at_level(logging.WARNING):
            ws_common.on_connection("ping", MagicMock(), "missing")

        assert "Connection missing not connected." in caplog.text

    def test_off_connection_removes_specific_callback(self):
        ws_common = WebSocketCommon(MagicMock())
        connection = WebSocketConnection(
            AsyncMock(), "test_id", "ConfigurationWebSocketStreams"
        )
        ws_common.connections = [connection]
        keep, drop = MagicMock(), MagicMock()

        ws_common.on_connection("close", keep, "test_id")
        ws_common.on_connection("close", drop, "test_id")
        ws_common.off_connection("close", drop, "test_id")

        assert connection.connection_callback_map["close"] == [keep]

    def test_off_connection_removes_all_callbacks_for_event(self):
        ws_common = WebSocketCommon(MagicMock())
        connection = WebSocketConnection(
            AsyncMock(), "test_id", "ConfigurationWebSocketStreams"
        )
        ws_common.connections = [connection]

        ws_common.on_connection("close", MagicMock(), "test_id")
        ws_common.on_connection("close", MagicMock(), "test_id")
        ws_common.on_connection("error", MagicMock(), "test_id")
        ws_common.off_connection("close")

        assert connection.connection_callback_map["close"] == []
        assert len(connection.connection_callback_map["error"]) == 1

    def test_off_connection_rejects_unknown_event(self):
        ws_common = WebSocketCommon(MagicMock())

        with pytest.raises(ValueError, match="Unsupported connection event: message"):
            ws_common.off_connection("message")

    def test_off_connection_leaves_other_connections_untouched(self):
        ws_common = WebSocketCommon(MagicMock())
        first = WebSocketConnection(AsyncMock(), "a", "ConfigurationWebSocketStreams")
        second = WebSocketConnection(AsyncMock(), "b", "ConfigurationWebSocketStreams")
        ws_common.connections = [first, second]
        callback = MagicMock()

        ws_common.on_connection("close", callback, "a")
        ws_common.on_connection("close", callback, "b")
        ws_common.off_connection("close", callback, "a")

        assert first.connection_callback_map["close"] == []
        assert second.connection_callback_map["close"] == [callback]

    def test_emit_close_event_silent_while_being_replaced(self):
        """A planned replacement must not read as the connection being lost."""

        ws_common = WebSocketCommon(MagicMock())
        connection = WebSocketConnection(
            AsyncMock(), "test_id", "ConfigurationWebSocketStreams"
        )
        callback = MagicMock()
        connection.connection_callback_map["close"].append(callback)
        connection.is_being_replaced = True

        ws_common._emit_close_event(connection)

        callback.assert_not_called()
        assert connection.close_emitted is False
        assert connection.is_open is False

    def test_emit_reconnect_event_fires_once(self):
        """The socket being replaced reports `reconnect`, and only once."""

        ws_common = WebSocketCommon(MagicMock())
        connection = WebSocketConnection(
            AsyncMock(), "test_id", "ConfigurationWebSocketStreams"
        )
        callback = MagicMock()
        connection.connection_callback_map["reconnect"].append(callback)

        ws_common._emit_reconnect_event(connection)
        ws_common._emit_reconnect_event(connection)

        callback.assert_called_once_with()
        assert connection.reconnect_emitted is True
        assert connection.is_open is False

    def test_emit_close_event_reports_close_once(self):
        """The stale receive loop must not report a second close."""

        ws_common = WebSocketCommon(MagicMock())
        connection = WebSocketConnection(
            AsyncMock(), "test_id", "ConfigurationWebSocketStreams"
        )
        callback = MagicMock()
        connection.connection_callback_map["close"].append(callback)

        ws_common._emit_close_event(connection)
        ws_common._emit_close_event(connection)

        callback.assert_called_once_with()
        assert connection.close_emitted is True

    def test_emit_close_event_fires_when_not_reconnecting(self):
        ws_common = WebSocketCommon(MagicMock())
        connection = WebSocketConnection(
            AsyncMock(), "test_id", "ConfigurationWebSocketStreams"
        )
        callback = MagicMock()
        connection.connection_callback_map["close"].append(callback)

        ws_common._emit_close_event(connection)

        callback.assert_called_once_with()
        assert connection.is_open is False

    @pytest.mark.asyncio
    async def test_receive_loop_error_closes_and_drops_connection(self, caplog):
        """A failed connection is logged, closed, and removed from the pool."""

        error_msg = MagicMock()
        error_msg.type = aiohttp.WSMsgType.ERROR

        ws_mock = AsyncMock()
        ws_mock.__aiter__.return_value = [error_msg]
        ws_mock.closed = False
        exc = Exception("transport blew up")
        ws_mock.exception = MagicMock(return_value=exc)

        conn = WebSocketConnection(ws_mock, "test_id", "ConfigurationWebSocketStreams")
        ws_common = WebSocketCommon(None)
        ws_common.connections = [conn]

        with caplog.at_level(logging.ERROR):
            await ws_common.receive_loop(conn)

        assert "transport blew up" in caplog.text
        ws_mock.close.assert_awaited_once()
        assert ws_common.connections == []
        assert conn.is_open is False

    @pytest.mark.asyncio
    async def test_receive_loop_close_drops_connection(self):
        ws_mock = AsyncMock()
        ws_mock.__aiter__.return_value = []
        ws_mock.closed = True

        conn = WebSocketConnection(ws_mock, "test_id", "ConfigurationWebSocketStreams")
        ws_common = WebSocketCommon(None)
        ws_common.connections = [conn]

        await ws_common.receive_loop(conn)

        ws_mock.close.assert_not_awaited()
        assert ws_common.connections == []

    @pytest.mark.asyncio
    async def test_discard_connection_skipped_during_reconnect(self):
        """A reconnecting connection is managed by reconnect(), not discarded."""

        ws_mock = AsyncMock()
        ws_mock.closed = False
        conn = WebSocketConnection(ws_mock, "test_id", "ConfigurationWebSocketStreams")
        conn.is_being_replaced = True

        ws_common = WebSocketCommon(None)
        ws_common.connections = [conn]

        await ws_common._discard_connection(conn)

        ws_mock.close.assert_not_awaited()
        assert ws_common.connections == [conn]

    @pytest.mark.asyncio
    async def test_reconnect_reports_failure_when_init_raises(self):
        ws_common = WebSocketCommon(MagicMock())
        ws_common.configuration = MagicMock(session_re_logon=False)

        conn = WebSocketConnection(
            AsyncMock(), "conn-1", "ConfigurationWebSocketStreams"
        )
        conn.session_logon_request = None
        events = []
        conn.connection_callback_map["error"].append(
            lambda e: events.append(("error", e))
        )
        conn.connection_callback_map["close"].append(lambda: events.append("close"))

        boom = OSError("dns failure")
        ws_common.init_connection = AsyncMock(side_effect=boom)
        ws_common.close_connection = AsyncMock()
        ws_common.connections = [conn]
        ws_common.reconnect_tasks = ["conn-1"]

        config = MagicMock(
            reconnect_delay=0,
            reconnect_attempts=1,
            stream_url="wss://test.com/ws",
        )
        await ws_common.reconnect(conn, config)

        assert events == [("error", boom), "close"]
        assert ws_common.reconnect_tasks == []
        assert conn.reconnect is False
        assert conn.is_open is False
        assert ws_common.connections == []

    @pytest.mark.asyncio
    async def test_reconnect_reports_failure_when_no_new_connection(self):
        ws_common = WebSocketCommon(MagicMock())
        ws_common.configuration = MagicMock(session_re_logon=False)

        conn = WebSocketConnection(
            AsyncMock(), "conn-1", "ConfigurationWebSocketStreams"
        )
        conn.session_logon_request = None
        errors = []
        conn.connection_callback_map["error"].append(lambda e: errors.append(e))
        closed = []
        conn.connection_callback_map["close"].append(lambda: closed.append(1))

        ws_common.init_connection = AsyncMock()
        ws_common.close_connection = AsyncMock()
        ws_common.connections = []
        ws_common.reconnect_tasks = ["conn-1"]

        config = MagicMock(
            reconnect_delay=0,
            reconnect_attempts=1,
            stream_url="wss://test.com/ws",
        )
        await ws_common.reconnect(conn, config)

        assert len(errors) == 1
        assert isinstance(errors[0], ConnectionError)
        assert closed == [1]
        assert ws_common.reconnect_tasks == []

    @pytest.mark.asyncio
    async def test_reconnect_closes_old_then_emits_open_last(
        self, mock_connection, mock_registry, mock_user_registry
    ):
        """A rotation reads as `reconnect` then `open`, the `open` last of all."""

        ws_common = WebSocketCommon(MagicMock())
        ws_common.configuration = MagicMock(session_re_logon=False)

        old_conn = WebSocketConnection(
            AsyncMock(), "conn-1", "ConfigurationWebSocketStreams"
        )
        old_conn.session_logon_request = None
        events = []
        old_conn.connection_callback_map["open"].append(lambda: events.append("open"))
        old_conn.connection_callback_map["close"].append(lambda: events.append("close"))
        old_conn.connection_callback_map["reconnect"].append(
            lambda: events.append("reconnect")
        )

        new_conn = WebSocketConnection(
            AsyncMock(), "conn-1", "ConfigurationWebSocketStreams"
        )

        async def fake_init(*args, **kwargs):
            ws_common.connections.append(new_conn)

        resubscribed = []

        async def fake_resubscribe(old, new):
            resubscribed.append(("order", list(events)))

        ws_common.init_connection = fake_init
        ws_common.close_connection = AsyncMock()
        ws_common._resubscribe_global_streams = fake_resubscribe
        ws_common.reconnect_tasks = ["conn-1"]

        config = MagicMock(
            reconnect_delay=0,
            reconnect_attempts=1,
            stream_url="wss://test.com/ws",
        )
        await ws_common.reconnect(old_conn, config)

        assert old_conn.is_being_replaced is True
        assert resubscribed == [("order", ["reconnect"])]
        assert events == ["reconnect", "open"]

    @pytest.mark.asyncio
    async def test_reconnect_carries_over_connection_callbacks(
        self, mock_registry, mock_user_registry
    ):
        ws_common = WebSocketCommon(MagicMock())
        ws_common.configuration = MagicMock(session_re_logon=False)

        old_conn = WebSocketConnection(
            AsyncMock(), "conn-1", "ConfigurationWebSocketStreams"
        )
        old_conn.session_logon_request = None
        callback = MagicMock()
        old_conn.connection_callback_map["close"].append(callback)

        new_conn = WebSocketConnection(
            AsyncMock(), "conn-1", "ConfigurationWebSocketStreams"
        )

        async def fake_init(*args, **kwargs):
            ws_common.connections.append(new_conn)

        ws_common.init_connection = fake_init
        ws_common.close_connection = AsyncMock()
        ws_common._resubscribe_global_streams = AsyncMock()
        ws_common.reconnect_tasks = ["conn-1"]

        config = MagicMock(
            reconnect_delay=0,
            reconnect_attempts=1,
            stream_url="wss://test.com/ws",
        )
        await ws_common.reconnect(old_conn, config)

        assert new_conn.connection_callback_map["close"] == [callback]

    @pytest.mark.asyncio
    async def test_reconnect_cancels_the_scheduled_rotation(self):
        """A manual reconnect must not leave the automatic rotation pending."""

        ws_common = WebSocketCommon(MagicMock())
        ws_common.configuration = MagicMock(session_re_logon=False)

        old_conn = WebSocketConnection(
            AsyncMock(), "conn-1", "ConfigurationWebSocketStreams"
        )
        old_conn.session_logon_request = None

        new_conn = WebSocketConnection(
            AsyncMock(), "conn-1", "ConfigurationWebSocketStreams"
        )

        async def sleep_forever():
            await asyncio.sleep(3600)

        scheduled = asyncio.ensure_future(sleep_forever())
        old_conn.scheduled_reconnect_task = scheduled

        async def fake_init(*args, **kwargs):
            ws_common.connections.append(new_conn)

        ws_common.init_connection = fake_init
        ws_common.close_connection = AsyncMock()
        ws_common._resubscribe_global_streams = AsyncMock()
        ws_common.connections = [old_conn]

        config = MagicMock(
            reconnect_delay=0,
            reconnect_attempts=1,
            stream_url="wss://test.com/ws",
        )
        await ws_common.reconnect(old_conn, config)

        await asyncio.sleep(0)

        assert scheduled.cancelled()
        assert old_conn.scheduled_reconnect_task is None

    @pytest.mark.asyncio
    async def test_scheduled_rotation_does_not_cancel_itself(self):
        """The rotation task must survive running its own reconnect.

        When the automatic rotation fires, the task calling `reconnect()` *is*
        the connection's `scheduled_reconnect_task`, so cancelling it would kill
        the reconnect midway: the old socket is already closed but the
        replacement is never established.
        """

        ws_common = WebSocketCommon(MagicMock())
        ws_common.configuration = MagicMock(session_re_logon=False)

        old_conn = WebSocketConnection(
            AsyncMock(), "conn-1", "ConfigurationWebSocketStreams"
        )
        old_conn.session_logon_request = None

        new_conn = WebSocketConnection(
            AsyncMock(), "conn-1", "ConfigurationWebSocketStreams"
        )

        async def fake_init(*args, **kwargs):
            await asyncio.sleep(0)
            ws_common.connections.append(new_conn)

        ws_common.init_connection = fake_init
        ws_common.close_connection = AsyncMock()
        ws_common._resubscribe_global_streams = AsyncMock()
        ws_common.connections = [old_conn]

        config = MagicMock(
            reconnect_delay=0,
            reconnect_attempts=1,
            stream_url="wss://test.com/ws",
        )

        task = asyncio.ensure_future(
            ws_common.schedule_reconnect(old_conn, config, 0)
        )
        old_conn.scheduled_reconnect_task = task

        await task

        assert not task.cancelled()
        assert new_conn in ws_common.connections
        assert old_conn.scheduled_reconnect_task is None

    @pytest.mark.asyncio
    async def test_schedule_reconnect_skips_a_replaced_connection(self):
        """A stray timer must not reconnect a connection already dropped."""

        ws_common = WebSocketCommon(MagicMock())
        ws_common.reconnect = AsyncMock()

        conn = WebSocketConnection(
            AsyncMock(), "conn-1", "ConfigurationWebSocketStreams"
        )
        ws_common.connections = []

        await ws_common.schedule_reconnect(conn, MagicMock(), 0)

        ws_common.reconnect.assert_not_awaited()

    @pytest.mark.asyncio
    async def test_schedule_reconnect_skips_a_user_closed_connection(self):
        ws_common = WebSocketCommon(MagicMock())
        ws_common.reconnect = AsyncMock()

        conn = WebSocketConnection(
            AsyncMock(), "conn-1", "ConfigurationWebSocketStreams"
        )
        conn.close_initiated = True
        ws_common.connections = [conn]

        await ws_common.schedule_reconnect(conn, MagicMock(), 0)

        ws_common.reconnect.assert_not_awaited()

    @pytest.mark.asyncio
    async def test_reconnect_clears_the_marker_after_a_failure(self):
        """A failed reconnect must not block the next attempt."""

        ws_common = WebSocketCommon(MagicMock())
        ws_common.configuration = MagicMock(session_re_logon=False)

        conn = WebSocketConnection(
            AsyncMock(), "conn-1", "ConfigurationWebSocketStreams"
        )
        conn.session_logon_request = None

        ws_common.init_connection = AsyncMock(side_effect=OSError("down"))
        ws_common.close_connection = AsyncMock()
        ws_common.connections = [conn]

        config = MagicMock(
            reconnect_delay=0,
            reconnect_attempts=1,
            stream_url="wss://test.com/ws",
        )
        await ws_common.reconnect(conn, config)

        assert ws_common.reconnect_tasks == []
        assert conn.reconnect is False

    @pytest.mark.asyncio
    async def test_reconnect_abandoned_by_the_user_reports_close(self):
        """Giving up because the user closed the connection is a real close.

        The `reconnect` event has already fired by then, so the connection would
        otherwise be left reported as reconnecting forever.
        """

        ws_common = WebSocketCommon(MagicMock())
        ws_common.configuration = MagicMock(session_re_logon=False)

        conn = WebSocketConnection(
            AsyncMock(), "conn-1", "ConfigurationWebSocketStreams"
        )
        conn.session_logon_request = None
        events = []
        conn.connection_callback_map["reconnect"].append(
            lambda: events.append("reconnect")
        )
        conn.connection_callback_map["close"].append(lambda: events.append("close"))

        async def close_then_init(*args, **kwargs):
            raise AssertionError("the reconnect must be abandoned before connecting")

        async def mark_closed(*args, **kwargs):
            conn.close_initiated = True

        ws_common.init_connection = close_then_init
        ws_common.close_connection = mark_closed
        ws_common.connections = [conn]

        config = MagicMock(
            reconnect_delay=0,
            reconnect_attempts=3,
            stream_url="wss://test.com/ws",
        )
        result = await ws_common.reconnect(conn, config)

        assert result is None
        assert events == ["reconnect", "close"]
        assert conn.reconnect is False
        assert conn.is_being_replaced is False
        assert ws_common.reconnect_tasks == []

    @pytest.mark.asyncio
    async def test_reconnect_carries_over_reconnect_callbacks(
        self, mock_registry, mock_user_registry
    ):
        """A `reconnect` listener keeps firing across successive rotations."""

        ws_common = WebSocketCommon(MagicMock())
        ws_common.configuration = MagicMock(session_re_logon=False)

        old_conn = WebSocketConnection(
            AsyncMock(), "conn-1", "ConfigurationWebSocketStreams"
        )
        old_conn.session_logon_request = None
        callback = MagicMock()
        old_conn.connection_callback_map["reconnect"].append(callback)

        new_conn = WebSocketConnection(
            AsyncMock(), "conn-1", "ConfigurationWebSocketStreams"
        )

        async def fake_init(*args, **kwargs):
            ws_common.connections.append(new_conn)

        ws_common.init_connection = fake_init
        ws_common.close_connection = AsyncMock()
        ws_common._resubscribe_global_streams = AsyncMock()
        ws_common.connections = [old_conn]

        config = MagicMock(
            reconnect_delay=0,
            reconnect_attempts=1,
            stream_url="wss://test.com/ws",
        )
        await ws_common.reconnect(old_conn, config)

        callback.assert_called_once_with()
        assert new_conn.connection_callback_map["reconnect"] == [callback]
        assert new_conn.reconnect_emitted is False

    @pytest.mark.asyncio
    async def test_reconnect_retries_until_it_succeeds(self):
        ws_common = WebSocketCommon(MagicMock())
        ws_common.configuration = MagicMock(session_re_logon=False)

        conn = WebSocketConnection(
            AsyncMock(), "conn-1", "ConfigurationWebSocketStreams"
        )
        conn.session_logon_request = None

        new_conn = WebSocketConnection(
            AsyncMock(), "conn-1", "ConfigurationWebSocketStreams"
        )
        attempts = []

        async def flaky_init(*args, **kwargs):
            attempts.append(1)
            if len(attempts) < 3:
                raise OSError("still down")
            ws_common.connections.append(new_conn)

        ws_common.init_connection = flaky_init
        ws_common.close_connection = AsyncMock()
        ws_common._resubscribe_global_streams = AsyncMock()
        ws_common.connections = [conn]

        config = MagicMock(
            reconnect_delay=0,
            reconnect_attempts=3,
            stream_url="wss://test.com/ws",
        )
        result = await ws_common.reconnect(conn, config)

        assert len(attempts) == 3
        assert result is new_conn
        assert ws_common.reconnect_tasks == []

    @pytest.mark.asyncio
    async def test_reconnect_gives_up_after_the_configured_attempts(
        self, mock_registry
    ):
        ws_common = WebSocketCommon(MagicMock())
        ws_common.configuration = MagicMock(session_re_logon=False)

        conn = WebSocketConnection(
            AsyncMock(), "conn-1", "ConfigurationWebSocketStreams"
        )
        conn.session_logon_request = None
        errors = []
        conn.connection_callback_map["error"].append(lambda e: errors.append(e))

        mock_registry.stream_connections_map = {"btcusdt@trade": conn}

        ws_common.init_connection = AsyncMock(side_effect=OSError("down"))
        ws_common.close_connection = AsyncMock()
        ws_common.connections = [conn]

        config = MagicMock(
            reconnect_delay=0,
            reconnect_attempts=3,
            stream_url="wss://test.com/ws",
        )
        await ws_common.reconnect(conn, config)

        assert ws_common.init_connection.await_count == 3
        assert len(errors) == 1
        assert ws_common.connections == []
        assert mock_registry.stream_connections_map == {}

    @pytest.mark.asyncio
    async def test_reconnect_never_exceeds_the_maximum_attempts(self):
        """Retrying is capped even if a caller sets the attempts higher.

        The configuration rejects out-of-range values, so this covers a
        configuration object built another way, e.g. a stub or an older client.
        """

        ws_common = WebSocketCommon(MagicMock())
        ws_common.configuration = MagicMock(session_re_logon=False)

        conn = WebSocketConnection(
            AsyncMock(), "conn-1", "ConfigurationWebSocketStreams"
        )
        conn.session_logon_request = None

        ws_common.init_connection = AsyncMock(side_effect=OSError("down"))
        ws_common.close_connection = AsyncMock()
        ws_common.connections = [conn]

        config = MagicMock(
            reconnect_delay=0,
            reconnect_attempts=99,
            stream_url="wss://test.com/ws",
        )
        await ws_common.reconnect(conn, config)

        assert ws_common.init_connection.await_count == MAX_RECONNECT_ATTEMPTS


class TestReconnectAttemptsConfiguration:
    @pytest.mark.parametrize("attempts", [1, 2, 3, 5, MAX_RECONNECT_ATTEMPTS])
    def test_accepts_the_supported_range(self, attempts):
        assert (
            ConfigurationWebSocketStreams(reconnect_attempts=attempts).reconnect_attempts
            == attempts
        )
        assert (
            ConfigurationWebSocketAPI(reconnect_attempts=attempts).reconnect_attempts
            == attempts
        )

    @pytest.mark.parametrize("attempts", [0, -1, MAX_RECONNECT_ATTEMPTS + 1, 99])
    def test_rejects_values_outside_the_range(self, attempts):
        for config_cls in (ConfigurationWebSocketStreams, ConfigurationWebSocketAPI):
            with pytest.raises(ValueError, match="reconnect_attempts must be between"):
                config_cls(reconnect_attempts=attempts)

    def test_defaults_to_the_default_attempts(self):
        assert (
            ConfigurationWebSocketStreams().reconnect_attempts
            == DEFAULT_RECONNECT_ATTEMPTS
        )
        assert (
            ConfigurationWebSocketAPI().reconnect_attempts == DEFAULT_RECONNECT_ATTEMPTS
        )


class TestSignedWebSocketStreams:
    @pytest.fixture
    def signed_config(self):
        config = ConfigurationWebSocketStreams(
            stream_url="wss://test.com/sapi/wss",
            api_key="test-api-key",
            api_secret="test-api-secret",
            reconnect_delay=0,
            reconnect_attempts=1,
        )
        return config

    @pytest.fixture
    def signed_streams(self, signed_config):
        return WebSocketStreamBase(signed_config, signed=True)

    def test_signed_keeps_stream_url(self, signed_config):
        WebSocketStreamBase(signed_config, signed=True)

        assert signed_config.stream_url == "wss://test.com/sapi/wss"

    def test_unsigned_appends_stream_suffix(self):
        config = ConfigurationWebSocketStreams(stream_url="wss://test.com/ws")

        WebSocketStreamBase(config)

        assert config.stream_url == "wss://test.com/ws/stream"

    def test_signed_with_private_key_uses_signer(self, signed_config):
        signed_config.private_key = "private-key"
        signed_config.private_key_passphrase = "passphrase"
        signer = MagicMock()

        with patch(
            "binance_common.websocket.Signers.get_signer", return_value=signer
        ) as mock_get_signer:
            streams = WebSocketStreamBase(signed_config, signed=True)

        mock_get_signer.assert_called_once_with("private-key", "passphrase")
        assert streams.signer is signer

    def test_sign_stream_url_adds_signed_query(self, signed_streams):
        url = signed_streams.sign_stream_url("wss://test.com/sapi/wss")

        base, query = url.split("?", 1)
        payload, signature = query.split("&signature=")
        params = dict(parse_qsl(payload))
        expected = hmac.new(
            b"test-api-secret", payload.encode("utf-8"), hashlib.sha256
        ).hexdigest()

        assert base == "wss://test.com/sapi/wss"
        assert set(params) == {"random", "recvWindow", "timestamp"}
        assert params["recvWindow"] == "30000"
        assert len(params["random"]) == 32
        assert signature == expected

    def test_sign_stream_url_is_fresh_on_each_call(self, signed_streams):
        first = signed_streams.sign_stream_url("wss://test.com/sapi/wss")
        second = signed_streams.sign_stream_url("wss://test.com/sapi/wss")

        assert first != second

    @pytest.mark.asyncio
    @patch(
        "binance_common.websocket.aiohttp.ClientSession.ws_connect",
        new_callable=AsyncMock,
    )
    async def test_create_connection_signs_url_and_sends_api_key(
        self, mock_ws_connect, signed_streams, mock_websocket
    ):
        mock_ws_connect.return_value = mock_websocket

        await signed_streams.create_connection()

        args, kwargs = mock_ws_connect.call_args
        assert args[0].startswith("wss://test.com/sapi/wss?random=")
        assert "&signature=" in args[0]
        assert kwargs["headers"]["X-MBX-APIKEY"] == "test-api-key"
        await signed_streams.close_connection(close_session=True)

    @pytest.mark.asyncio
    @patch(
        "binance_common.websocket.aiohttp.ClientSession.ws_connect",
        new_callable=AsyncMock,
    )
    async def test_unsigned_connection_sends_no_api_key(
        self, mock_ws_connect, mock_websocket
    ):
        mock_ws_connect.return_value = mock_websocket
        config = ConfigurationWebSocketStreams(
            stream_url="wss://test.com/ws", api_key="test-api-key"
        )
        streams = WebSocketStreamBase(config)

        await streams.create_connection()

        args, kwargs = mock_ws_connect.call_args
        assert args[0] == "wss://test.com/ws/stream"
        assert "X-MBX-APIKEY" not in kwargs["headers"]
        await streams.close_connection(close_session=True)

    @pytest.mark.asyncio
    async def test_init_connection_signs_url_on_reconnect(self, signed_streams):
        with patch.object(
            WebSocketCommon, "init_connection", AsyncMock()
        ) as mock_init_connection:
            await signed_streams.init_connection(
                "wss://test.com/sapi/wss",
                signed_streams.configuration,
                None,
                "conn-1",
            )
            await signed_streams.init_connection(
                "wss://test.com/sapi/wss",
                signed_streams.configuration,
                None,
                "conn-1",
            )

        first_url = mock_init_connection.await_args_list[0].args[0]
        second_url = mock_init_connection.await_args_list[1].args[0]
        assert "&signature=" in first_url
        assert first_url != second_url
        assert mock_init_connection.await_args_list[0].args[3] == "conn-1"

    def test_stream_messages_signed(self, signed_streams):
        assert signed_streams.stream_messages("SUBSCRIBE", ["topic_a", "topic_b"]) == [
            {"command": "SUBSCRIBE", "value": "topic_a"},
            {"command": "SUBSCRIBE", "value": "topic_b"},
        ]

    def test_stream_messages_unsigned(self):
        streams = WebSocketStreamBase(
            ConfigurationWebSocketStreams(stream_url="wss://test.com/ws")
        )

        messages = streams.stream_messages("UNSUBSCRIBE", ["topic_a", "topic_b"])

        assert len(messages) == 1
        assert messages[0]["method"] == "UNSUBSCRIBE"
        assert messages[0]["params"] == ["topic_a", "topic_b"]
        assert "id" in messages[0]

    @pytest.mark.asyncio
    async def test_subscribe_signed_sends_one_command_per_stream(self, signed_streams):
        connection = WebSocketConnection(
            AsyncMock(), "conn-1", "ConfigurationWebSocketStreams"
        )
        signed_streams.connections = [connection]
        signed_streams.send_message = AsyncMock()

        with patch("binance_common.websocket.asyncio.sleep", AsyncMock()):
            await signed_streams.subscribe(["topic_a", "topic_b"])

        assert signed_streams.send_message.await_args_list == [
            call({"command": "SUBSCRIBE", "value": "topic_a"}, connection),
            call({"command": "SUBSCRIBE", "value": "topic_b"}, connection),
        ]
        assert (
            signed_streams.stream_connections.stream_connections_map["topic_a"]
            is connection
        )

    @pytest.mark.asyncio
    async def test_unsubscribe_signed_sends_commands(self, signed_streams):
        websocket = AsyncMock()
        connection = WebSocketConnection(
            websocket, "conn-1", "ConfigurationWebSocketStreams"
        )
        signed_streams.connections = [connection]
        signed_streams.stream_connections.stream_connections_map["topic_a"] = connection
        connection.stream_callback_map["topic_a"] = []

        await signed_streams.unsubscribe(["topic_a"])

        websocket.send_str.assert_awaited_once_with(
            json.dumps({"command": "UNSUBSCRIBE", "value": "topic_a"})
        )
        assert "topic_a" not in signed_streams.stream_connections.stream_connections_map

    @pytest.mark.asyncio
    async def test_resubscribe_signed_streams_after_reconnect(self, signed_streams):
        old_connection = WebSocketConnection(
            AsyncMock(), "conn-1", "ConfigurationWebSocketStreams"
        )
        new_connection = WebSocketConnection(
            AsyncMock(), "conn-1", "ConfigurationWebSocketStreams"
        )
        signed_streams.stream_connections.stream_connections_map["topic_a"] = (
            old_connection
        )
        old_connection.stream_callback_map["topic_a"] = []
        signed_streams.send_message = AsyncMock()

        await signed_streams._resubscribe_global_streams(old_connection, new_connection)

        signed_streams.send_message.assert_awaited_once_with(
            {"command": "SUBSCRIBE", "value": "topic_a"}, new_connection
        )

    def test_parse_signed_stream_message_with_json_string_payload(self):
        data = {
            "type": "DATA",
            "topic": "topic_a",
            "data": json.dumps({"price": "1.0"}),
        }

        assert WebSocketStreamBase.parse_signed_stream_message(data) == {
            "stream": "topic_a",
            "data": {"price": "1.0"},
        }

    def test_parse_signed_stream_message_keeps_non_json_string_payload(self):
        data = {"type": "DATA", "topic": "topic_a", "data": "plain"}

        assert WebSocketStreamBase.parse_signed_stream_message(data) == {
            "stream": "topic_a",
            "data": "plain",
        }

    def test_parse_signed_stream_message_passes_command_replies_through(self):
        reply = {
            "type": "COMMAND",
            "data": "SUCCESS",
            "subType": "REGISTER",
            "code": "00000000",
        }

        assert WebSocketStreamBase.parse_signed_stream_message(reply) is reply

    @pytest.mark.asyncio
    async def test_receive_loop_routes_signed_data_to_stream_callback(
        self, signed_streams
    ):
        websocket = MagicMock()
        websocket.__aiter__.return_value = [
            aiohttp.WSMessage(
                aiohttp.WSMsgType.TEXT,
                json.dumps(
                    {
                        "type": "DATA",
                        "topic": "topic_a",
                        "data": json.dumps({"price": "1.0"}),
                    }
                ),
                None,
            )
        ]
        connection = WebSocketConnection(
            websocket, "conn-1", "ConfigurationWebSocketStreams"
        )
        callback = MagicMock()
        connection.stream_callback_map["topic_a"] = [callback]
        connection.response_types["topic_a"] = None
        signed_streams.connections = [connection]

        with patch.object(signed_streams, "_discard_connection", AsyncMock()):
            await signed_streams.receive_loop(connection)

        callback.assert_called_once_with(
            {"stream": "topic_a", "data": {"price": "1.0"}}
        )


class TestWebSocketStreamBase:

    @pytest.mark.asyncio
    @patch(
        "binance_common.websocket.aiohttp.ClientSession.ws_connect",
        new_callable=AsyncMock,
    )
    async def test_create_connection_with_url_paths(
        self, mock_ws_connect, mock_config, mock_websocket
    ):
        mock_config.stream_url = "wss://test.com/ws"
        mock_config.mode = WebsocketMode.SINGLE
        mock_ws_connect.return_value = mock_websocket

        websocket_stream = WebSocketStreamBase(mock_config, url_paths=["test_path"])
        await websocket_stream.create_connection()

        assert len(websocket_stream.connections) == 1
        connection = websocket_stream.connections[0]
        assert connection.url_path == "test_path"

    @pytest.mark.asyncio
    @patch(
        "binance_common.websocket.aiohttp.ClientSession.ws_connect",
        new_callable=AsyncMock,
    )
    async def test_create_connection_without_url_paths(
        self, mock_ws_connect, mock_config, mock_websocket
    ):
        mock_config.stream_url = "wss://test.com/ws"
        mock_config.mode = WebsocketMode.SINGLE
        mock_ws_connect.return_value = mock_websocket

        websocket_stream = WebSocketStreamBase(mock_config)
        await websocket_stream.create_connection()

        assert len(websocket_stream.connections) == 1
        connection = websocket_stream.connections[0]
        assert connection.url_path is None

    @pytest.mark.asyncio
    async def test_subscribe_adds_stream_and_callback(
        self, websocket_stream, mock_connection, mock_registry
    ):
        await websocket_stream.subscribe(["test_stream"])

        assert "test_stream" in mock_registry.stream_connections_map
        assert mock_registry.stream_connections_map["test_stream"] == mock_connection

        assert "test_stream" in mock_connection.stream_callback_map
        mock_connection.websocket.send_str.assert_called_once()

    @pytest.mark.asyncio
    async def test_subscribe_with_stream_url(
        self, websocket_stream, mock_connection, mock_registry
    ):
        mock_connection.url_path = "test_path"
        websocket_stream.connections = [mock_connection]

        await websocket_stream.subscribe(["test_stream"], stream_url="test_path")

        assert "test_stream" in mock_registry.stream_connections_map
        assert mock_registry.stream_connections_map["test_stream"] == mock_connection
        mock_connection.websocket.send_str.assert_called_once()

    @pytest.mark.asyncio
    async def test_subscribe_with_stream_url_not_found(
        self, websocket_stream, mock_connection, mock_registry, caplog
    ):
        mock_connection.url_path = "different_path"
        websocket_stream.connections = [mock_connection]

        with caplog.at_level(logging.WARNING):
            await websocket_stream.subscribe(["test_stream"], stream_url="test_path")

        assert (
            "No matching connection found for streams: ['test_stream']" in caplog.text
        )
        assert "test_stream" not in mock_registry.stream_connections_map

    @pytest.mark.asyncio
    async def test_on_sets_callback_for_websocket_stream(
        self, websocket_stream, mock_connection
    ):
        await websocket_stream.subscribe(["test_stream"])

        def callback(x):
            return x

        websocket_stream.on("message", callback, "test_stream")

        assert mock_connection.stream_callback_map["test_stream"] == [callback]

    @pytest.mark.asyncio
    async def test_subscribe_with_empty_streams(self, websocket_stream, caplog):
        await websocket_stream.subscribe([])
        assert "No streams to subscribe to." in caplog.text

    @pytest.mark.asyncio
    async def test_subscribe_no_connections_and_reconnects(self, websocket_stream):
        websocket_stream.connections = []
        websocket_stream.reconnect_tasks = []

        with pytest.raises(ValueError, match="No WebSocket connections available."):
            await websocket_stream.subscribe(["btcusdt@aggTrade"])

    @pytest.mark.asyncio
    async def test_subscribe_all_connections_reconnecting(
        self, websocket_stream, caplog
    ):
        websocket_stream.connections = [
            SimpleNamespace(reconnect=True, stream_callback_map={}, id=1)
        ]
        websocket_stream.reconnect_tasks = ["dummy_task"]

        await websocket_stream.subscribe(["btcusdt@aggTrade"])

        assert "No available WebSocket connections for subscription." in caplog.text

    @pytest.mark.asyncio
    async def test_on_unsupported_event_raises(self, websocket_stream):
        with pytest.raises(ValueError):
            websocket_stream.on("open", lambda x: x, "test_stream")

    @pytest.mark.asyncio
    async def test_unsubscribe_removes_stream(
        self, websocket_stream, mock_connection, mock_registry
    ):
        await websocket_stream.subscribe(["test_stream"])
        await websocket_stream.unsubscribe(["test_stream"])

        assert "test_stream" not in mock_registry.stream_connections_map
        assert "test_stream" not in mock_connection.stream_callback_map
        mock_connection.websocket.send_str.assert_called()

    @pytest.mark.asyncio
    async def test_subscribe_batches_streams_into_one_message(
        self, websocket_stream, mock_connection, mock_registry
    ):
        """Streams sharing a connection travel in a single SUBSCRIBE."""

        streams = [f"stream{i}" for i in range(10)]
        await websocket_stream.subscribe(streams)

        assert mock_connection.websocket.send_str.call_count == 1
        payload = json.loads(mock_connection.websocket.send_str.call_args[0][0])
        assert payload["method"] == "SUBSCRIBE"
        assert payload["params"] == streams
        assert set(mock_registry.stream_connections_map) == set(streams)

    @pytest.mark.asyncio
    async def test_subscribe_batches_per_connection_in_pool_mode(
        self, mock_config, mock_registry
    ):
        """Each pooled connection gets one message with only its own streams."""

        mock_config.mode = WebsocketMode.POOL
        first = WebSocketConnection(
            AsyncMock(), "conn-1", "ConfigurationWebSocketStreams"
        )
        second = WebSocketConnection(
            AsyncMock(), "conn-2", "ConfigurationWebSocketStreams"
        )

        websocket_stream = WebSocketStreamBase(mock_config)
        websocket_stream.connections = [first, second]

        await websocket_stream.subscribe(["a", "b", "c", "d"])

        first_payload = json.loads(first.websocket.send_str.call_args[0][0])
        second_payload = json.loads(second.websocket.send_str.call_args[0][0])

        assert first.websocket.send_str.call_count == 1
        assert second.websocket.send_str.call_count == 1
        assert first_payload["params"] == ["a", "c"]
        assert second_payload["params"] == ["b", "d"]

    @pytest.mark.asyncio
    async def test_unsubscribe_batches_streams_into_one_message(
        self, websocket_stream, mock_connection, mock_registry
    ):
        """UNSUBSCRIBE carries each connection's streams exactly once."""

        streams = [f"stream{i}" for i in range(10)]
        await websocket_stream.subscribe(streams)
        mock_connection.websocket.send_str.reset_mock()

        await websocket_stream.unsubscribe(streams)

        assert mock_connection.websocket.send_str.call_count == 1
        payload = json.loads(mock_connection.websocket.send_str.call_args[0][0])
        assert payload["method"] == "UNSUBSCRIBE"
        assert payload["params"] == streams
        assert mock_registry.stream_connections_map == {}

    @pytest.mark.asyncio
    async def test_unsubscribe_only_lists_streams_of_each_connection(
        self, mock_config, mock_registry
    ):
        """A connection must not be told to unsubscribe another's streams."""

        mock_config.mode = WebsocketMode.POOL
        first = WebSocketConnection(
            AsyncMock(), "conn-1", "ConfigurationWebSocketStreams"
        )
        second = WebSocketConnection(
            AsyncMock(), "conn-2", "ConfigurationWebSocketStreams"
        )

        websocket_stream = WebSocketStreamBase(mock_config)
        websocket_stream.connections = [first, second]

        await websocket_stream.subscribe(["a", "b", "c", "d"])
        first.websocket.send_str.reset_mock()
        second.websocket.send_str.reset_mock()

        await websocket_stream.unsubscribe(["a", "b", "c", "d"])

        assert json.loads(first.websocket.send_str.call_args[0][0])["params"] == [
            "a",
            "c",
        ]
        assert json.loads(second.websocket.send_str.call_args[0][0])["params"] == [
            "b",
            "d",
        ]

    @pytest.mark.asyncio
    async def test_resubscribe_global_streams_sends_one_message(
        self, mock_config, mock_registry
    ):
        """A reconnect restores every stream with a single SUBSCRIBE."""

        old_conn = WebSocketConnection(
            AsyncMock(), "conn-1", "ConfigurationWebSocketStreams"
        )
        new_conn = WebSocketConnection(
            AsyncMock(), "conn-1", "ConfigurationWebSocketStreams"
        )
        streams = ["a", "b", "c"]
        old_conn.stream_callback_map = {s: [f"cb-{s}"] for s in streams}
        old_conn.response_types = {s: None for s in streams}
        mock_registry.stream_connections_map = {s: old_conn for s in streams}

        websocket_stream = WebSocketStreamBase(mock_config)
        websocket_stream.connections = [new_conn]

        await websocket_stream._resubscribe_global_streams(old_conn, new_conn)

        assert new_conn.websocket.send_str.call_count == 1
        payload = json.loads(new_conn.websocket.send_str.call_args[0][0])
        assert payload["params"] == streams
        assert all(
            mock_registry.stream_connections_map[s] is new_conn for s in streams
        )

    @pytest.mark.asyncio
    async def test_resubscribe_global_streams_uses_an_int_id_when_required(
        self, mock_config, mock_registry
    ):
        """A connector needing integer ids must not get the UUID connection id."""

        old_conn = WebSocketConnection(
            AsyncMock(), "conn-1", "ConfigurationWebSocketStreams"
        )
        new_conn = WebSocketConnection(
            AsyncMock(), "conn-1", "ConfigurationWebSocketStreams"
        )
        old_conn.stream_callback_map = {"a": ["cb"]}
        old_conn.response_types = {"a": None}
        mock_registry.stream_connections_map = {"a": old_conn}

        websocket_stream = WebSocketStreamBase(mock_config, id_strict_int=True)
        websocket_stream.connections = [new_conn]

        await websocket_stream._resubscribe_global_streams(old_conn, new_conn)

        payload = json.loads(new_conn.websocket.send_str.call_args[0][0])
        assert isinstance(payload["id"], int)

    @pytest.mark.asyncio
    async def test_unsubscribe_with_empty_streams(self, websocket_stream, caplog):
        await websocket_stream.unsubscribe([])

        assert "No streams to unsubscribe to." in caplog.text

    @pytest.mark.asyncio
    async def test_unsubscribe_no_connections(self, websocket_stream, caplog):
        websocket_stream.connections = []
        await websocket_stream.unsubscribe(["btcusdt@aggTrade"])

        assert "No WebSocket connections available for unsubscription." in caplog.text

    @pytest.mark.asyncio
    async def test_unsubscribe_stream_not_connected_warns(
        self, websocket_stream, caplog
    ):
        await websocket_stream.unsubscribe(["non_existent_stream"])
        assert "Stream ['non_existent_stream'] is not subscribed." in caplog.text

    def test_on_connection_fires_once_for_streams_sharing_connection(
        self, websocket_stream, mock_registry
    ):
        """Two streams on one connection still see a single connection event."""

        connection = WebSocketConnection(
            AsyncMock(), "conn-1", "ConfigurationWebSocketStreams"
        )
        mock_registry.stream_connections_map = {
            "btcusdt@trade": connection,
            "ethusdt@trade": connection,
        }
        websocket_stream.connections = [connection]
        callback = MagicMock()

        websocket_stream.on_connection("close", callback)

        assert connection.connection_callback_map["close"] == [callback]

        websocket_stream._emit_connection_event(connection, "close")
        callback.assert_called_once_with()

    @pytest.mark.asyncio
    async def test_unsubscribe_keeps_connection_callbacks(
        self, websocket_stream, mock_registry
    ):
        """Connection callbacks outlive the streams flowing over the connection."""

        connection = WebSocketConnection(
            AsyncMock(), "conn-1", "ConfigurationWebSocketStreams"
        )
        connection.stream_callback_map["btcusdt@trade"] = []
        mock_registry.stream_connections_map = {"btcusdt@trade": connection}
        websocket_stream.connections = [connection]
        callback = MagicMock()

        websocket_stream.on_connection("close", callback)
        await websocket_stream.unsubscribe(["btcusdt@trade"])

        assert connection.connection_callback_map["close"] == [callback]

        websocket_stream._emit_connection_event(connection, "close")
        callback.assert_called_once_with()

    def test_off_connection_for_stream_base(self, websocket_stream, mock_registry):
        connection = WebSocketConnection(
            AsyncMock(), "conn-1", "ConfigurationWebSocketStreams"
        )
        websocket_stream.connections = [connection]
        callback = MagicMock()

        websocket_stream.on_connection("ping", callback, "conn-1")
        websocket_stream.off_connection("ping", callback, "conn-1")

        assert connection.connection_callback_map["ping"] == []

    def test_on_connection_unknown_connection_warns(
        self, websocket_stream, mock_registry, caplog
    ):
        websocket_stream.connections = []

        with caplog.at_level(logging.WARNING):
            websocket_stream.on_connection("ping", MagicMock(), "missing")

        assert "Connection missing not connected." in caplog.text

    def test_handle_has_no_connection_event_methods(self, websocket_stream):
        """Connection events are not reachable from a stream handle."""

        handle = RequestStreamHandle(websocket_stream, "test_stream")

        assert not hasattr(handle, "on_connection")
        assert not hasattr(handle, "off_connection")

    @pytest.mark.asyncio
    async def test_request_stream_returns_correct_interface(self, websocket_stream):
        result = await RequestStream(websocket_stream, "test_stream")
        assert isinstance(result, RequestStreamHandle)
        assert hasattr(result, "on")
        assert hasattr(result, "unsubscribe")

    def test_handle_on_rejects_connection_events(self, websocket_stream):
        handle = RequestStreamHandle(websocket_stream, "test_stream")

        with pytest.raises(ValueError, match="Unsupported stream event: error"):
            handle.on("error", lambda data: data)

    def test_handle_on_points_connection_events_at_the_client(self, websocket_stream):
        """Rejecting a connection event tells the user where it belongs."""

        handle = RequestStreamHandle(websocket_stream, "test_stream")

        with pytest.raises(ValueError, match="client.on_connection"):
            handle.on("ping", lambda data: data)

    @pytest.mark.asyncio
    async def test_request_stream_with_stream_url(
        self, websocket_stream, mock_connection
    ):
        mock_connection.url_path = "test_path"
        websocket_stream.connections = [mock_connection]

        with patch.object(
            websocket_stream, "subscribe", new_callable=AsyncMock
        ) as mock_subscribe:
            result = await RequestStream(
                websocket_stream, "test_stream", stream_url="test_path"
            )

            assert isinstance(result, RequestStreamHandle)
            assert hasattr(result, "on")
            assert hasattr(result, "unsubscribe")

            mock_subscribe.assert_awaited_once_with(
                streams=["test_stream"], response_model=None, stream_url="test_path"
            )

    @pytest.mark.asyncio
    async def test_request_stream_without_stream_url(self, websocket_stream):
        with patch.object(
            websocket_stream, "subscribe", new_callable=AsyncMock
        ) as mock_subscribe:
            result = await RequestStream(websocket_stream, "test_stream")

            assert isinstance(result, RequestStreamHandle)
            assert hasattr(result, "on")
            assert hasattr(result, "unsubscribe")

            mock_subscribe.assert_awaited_once_with(
                streams=["test_stream"], response_model=None, stream_url=None
            )

    @pytest.mark.asyncio
    async def test_ping_ws_stream(self, websocket_stream, mock_connection):
        with patch.object(WebSocketCommon, "ping", new_callable=AsyncMock) as mock_ping:
            await websocket_stream.ping_ws_stream(mock_connection)
            mock_ping.assert_awaited_once_with(mock_connection)

    @pytest.mark.asyncio
    async def test_list_subscribe(self, websocket_stream, mock_connection):
        mock_response = {"id": "some-id", "streams": ["stream1", "stream2"]}
        future = asyncio.Future()
        future.set_result(mock_response)

        websocket_stream.send_message = AsyncMock(return_value=future)
        result = await websocket_stream.list_subscribe()

        assert isinstance(result, dict)
        assert "streams" in result
        assert "id" in result

        sent_message = websocket_stream.send_message.call_args[0][0]
        assert isinstance(sent_message, dict)
        assert sent_message["method"] == "LIST_SUBSCRIPTIONS"
        assert "id" in sent_message

    @pytest.mark.asyncio
    async def test_subscribe_same_stream_on_two_clients_keeps_them_apart(self):
        def client(name):
            config = ConfigurationWebSocketStreams(
                stream_url=f"wss://{name}.example.com/stream"
            )
            conn = MagicMock()
            conn.id = name
            conn.reconnect = False
            conn.websocket = AsyncMock()
            conn.stream_callback_map = {}
            conn.response_types = {}
            conn.pending_request = {}
            instance = WebSocketStreamBase(config)
            instance.connections = [conn]
            return instance, conn

        spot, spot_conn = client("spot")
        futures, futures_conn = client("futures")

        with patch("asyncio.sleep", new_callable=AsyncMock):
            await spot.subscribe(["btcusdt@aggTrade"])
            await futures.subscribe(["btcusdt@aggTrade"])

        spot_conn.websocket.send_str.assert_called_once()
        futures_conn.websocket.send_str.assert_called_once()
        sent = json.loads(futures_conn.websocket.send_str.call_args[0][0])
        assert sent["method"] == "SUBSCRIBE"
        assert sent["params"] == ["btcusdt@aggTrade"]

        spot_cb, futures_cb = MagicMock(), MagicMock()
        spot.on("message", spot_cb, "btcusdt@aggTrade")
        futures.on("message", futures_cb, "btcusdt@aggTrade")
        assert spot_conn.stream_callback_map["btcusdt@aggTrade"] == [spot_cb]
        assert futures_conn.stream_callback_map["btcusdt@aggTrade"] == [futures_cb]

        await spot.unsubscribe(["btcusdt@aggTrade"])
        assert "btcusdt@aggTrade" not in spot.stream_connections.stream_connections_map
        assert (
            futures.stream_connections.stream_connections_map["btcusdt@aggTrade"]
            is futures_conn
        )

    @staticmethod
    def _dropping_connection(conn_id):
        ws_mock = AsyncMock()
        ws_mock.__aiter__.return_value = []
        ws_mock.closed = False
        return WebSocketConnection(ws_mock, conn_id, "ConfigurationWebSocketStreams")

    @pytest.mark.asyncio
    async def test_resubscribe_after_connection_drop_sends_subscribe(self):
        stream = "bnbusdt@depth"
        client = WebSocketStreamBase(
            ConfigurationWebSocketStreams(stream_url="wss://test.com/stream")
        )
        old_conn = self._dropping_connection("conn-1")
        client.connections = [old_conn]

        with patch("asyncio.sleep", new_callable=AsyncMock):
            await client.subscribe([stream])
            # The server drops the connection; the receive loop ends.
            await client.receive_loop(old_conn)

            assert client.connections == []
            assert stream not in client.stream_connections.stream_connections_map

            new_conn = self._dropping_connection("conn-2")
            client.connections = [new_conn]
            await client.subscribe([stream])

        new_conn.websocket.send_str.assert_called_once()
        sent = json.loads(new_conn.websocket.send_str.call_args[0][0])
        assert sent["method"] == "SUBSCRIBE"
        assert sent["params"] == [stream]
        assert client.stream_connections.stream_connections_map[stream] is new_conn

        callback = MagicMock()
        client.on("message", callback, stream)
        assert new_conn.stream_callback_map[stream] == [callback]

    @pytest.mark.asyncio
    async def test_connection_drop_keeps_streams_of_other_connections(self):
        client = WebSocketStreamBase(
            ConfigurationWebSocketStreams(
                stream_url="wss://test.com/stream",
                mode=WebsocketMode.POOL,
                pool_size=2,
            )
        )
        dropped = self._dropping_connection("conn-1")
        alive = self._dropping_connection("conn-2")
        client.connections = [dropped, alive]

        with patch("asyncio.sleep", new_callable=AsyncMock):
            await client.subscribe(["a@trade", "b@trade"])
            await client.receive_loop(dropped)

        assert client.connections == [alive]
        assert client.stream_connections.stream_connections_map == {"b@trade": alive}

    @pytest.mark.asyncio
    async def test_connection_drop_during_reconnect_keeps_streams(self):
        client = WebSocketStreamBase(
            ConfigurationWebSocketStreams(stream_url="wss://test.com/stream")
        )
        conn = self._dropping_connection("conn-1")
        client.connections = [conn]

        with patch("asyncio.sleep", new_callable=AsyncMock):
            await client.subscribe(["a@trade"])

        conn.is_being_replaced = True
        await client._discard_connection(conn)

        assert client.stream_connections.stream_connections_map == {"a@trade": conn}


# ========== WebSocketAPIBase Tests ==========


class TestWebSocketAPIBase:

    @pytest.mark.asyncio
    async def test_send_message_single_connection(self, ws_api, mock_connection):
        ws_api.connections = [mock_connection]
        ws_api.reconnect_tasks = []

        payload = {"params": {"symbol": "BTCUSDT"}, "method": "exchangeInfo"}

        with patch.object(
            WebSocketCommon, "send_message", new_callable=AsyncMock
        ) as mock_send:

            mock_future = asyncio.Future()
            mock_future.set_result({"result": {"foo": "bar"}, "rateLimits": []})
            mock_send.return_value = mock_future

            result = await ws_api.send_message(payload)

            mock_send.assert_awaited_once()
            sent_payload = mock_send.await_args.args[0]
            assert "id" in sent_payload
            assert "method" in sent_payload
            assert "params" in sent_payload

            assert isinstance(result, WebsocketApiResponse)
            assert callable(result._data_function)
            assert result._data_function() == {
                "result": {"foo": "bar"},
                "rateLimits": [],
            }
            assert result.rate_limits == []

    @pytest.mark.asyncio
    async def test_send_signed_message_single_connection(self, ws_api, mock_connection):
        ws_api.connections = [mock_connection]
        ws_api.reconnect_tasks = []

        payload = {"params": {"symbol": "BTCUSDT"}, "method": "exchangeInfo"}

        with patch.object(
            WebSocketCommon, "send_message", new_callable=AsyncMock
        ) as mock_send, patch(
            "binance_common.utils.websocket_api_signature", return_value="signature"
        ) as mock_signature:

            mock_future = asyncio.Future()
            mock_future.set_result({"result": {"foo": "bar"}, "rateLimits": []})
            mock_send.return_value = mock_future

            result = await ws_api.send_signed_message(payload)

            mock_send.assert_awaited_once()
            mock_signature.assert_called_once_with(
                ws_api.configuration, {"symbol": "BTCUSDT"}, None
            )
            sent_payload = mock_send.await_args.args[0]
            assert "id" in sent_payload
            assert "method" in sent_payload
            assert "params" in sent_payload
            assert sent_payload["params"] == "signature"

            assert isinstance(result, WebsocketApiResponse)
            assert callable(result._data_function)
            assert result._data_function() == {
                "result": {"foo": "bar"},
                "rateLimits": [],
            }
            assert result.rate_limits == []

    @pytest.mark.asyncio
    async def test_send_signed_message_no_connections_and_no_reconnect_tasks(
        self, ws_api
    ):
        ws_api.connections = []
        ws_api.reconnect_tasks = []

        payload = {"params": {"symbol": "BTCUSDT"}, "method": "exchangeInfo"}

        with patch.object(
            ws_api, "close_connection", new_callable=AsyncMock
        ) as mock_close:
            with pytest.raises(ValueError, match="No WebSocket connections available."):
                await ws_api.send_signed_message(payload)

            mock_close.assert_awaited_once_with(close_session=True)

    @pytest.mark.asyncio
    async def test_send_signed_message_all_connections_in_reconnect(
        self, ws_api, mock_connection
    ):
        mock_connection.reconnect = True
        ws_api.connections = [mock_connection]
        ws_api.reconnect_tasks = []

        payload = {"params": {"symbol": "BTCUSDT"}, "method": "exchangeInfo"}

        result = await ws_api.send_signed_message(payload)

        assert result._data_function() == "Websocket Reconnect"
        assert result.rate_limits == []

    @pytest.mark.asyncio
    async def test_send_signed_message_single_connection_with_timeout_error(
        self, ws_api, mock_connection
    ):
        ws_api.connections = [mock_connection]
        ws_api.reconnect_tasks = []

        payload = {"params": {"symbol": "BTCUSDT"}, "method": "exchangeInfo"}

        with patch.object(
            WebSocketCommon, "send_message", new_callable=AsyncMock
        ) as mock_send, patch(
            "binance_common.utils.websocket_api_signature", return_value="signature"
        ) as mock_signature:

            hanging_future = asyncio.Future()
            mock_send.return_value = hanging_future

            result = await ws_api.send_signed_message(payload)

            mock_send.assert_awaited_once()
            mock_signature.assert_called_once_with(
                ws_api.configuration, {"symbol": "BTCUSDT"}, None
            )
            sent_payload = mock_send.await_args.args[0]
            assert "id" in sent_payload
            assert "method" in sent_payload
            assert "params" in sent_payload
            assert sent_payload["params"] == "signature"

            assert isinstance(result, WebsocketApiResponse)
            assert callable(result._data_function)
            assert result._data_function() == {"error": "timeout"}
            assert result.rate_limits == []

    @pytest.mark.asyncio
    async def test_send_signed_message_generic_exception_warning(
        self, ws_api, mock_connection, caplog
    ):
        ws_api.connections = [mock_connection]
        ws_api.reconnect_tasks = []

        payload = {"params": {"symbol": "BTCUSDT"}, "method": "exchangeInfo"}

        class ExplodingFuture:
            def __await__(self):
                raise RuntimeError("Something went wrong")

        with caplog.at_level(logging.WARNING), patch.object(
            WebSocketCommon,
            "send_message",
            new=AsyncMock(return_value=ExplodingFuture()),
        ), patch(
            "binance_common.utils.websocket_api_signature", return_value="signature"
        ):

            result = await ws_api.send_signed_message(payload)

            assert "error" in result._data_function()
            assert result._data_function()["error"] == "Something went wrong"
            assert any(
                "Connection with user closed" in message for message in caplog.messages
            )

    @pytest.mark.asyncio
    async def test_send_signed_message_round_robin(self, ws_api, mock_config):
        mock_config.mode = "pool"
        ws_api.configuration = mock_config

        conn1 = MagicMock(reconnect=False)
        conn2 = MagicMock(reconnect=False)

        ws_api.connections = [conn1, conn2]
        ws_api.reconnect_tasks = []
        ws_api.send_message = AsyncMock(return_value="success")

        payload1 = {"params": {"symbol": "BTCUSDT"}}
        payload2 = {"params": {"symbol": "ETHUSDT"}}

        with patch.object(
            WebSocketCommon, "send_message", new_callable=AsyncMock
        ) as mock_send:
            mock_send.return_value = "mocked-response"
            await ws_api.send_signed_message(payload1)
            await ws_api.send_signed_message(payload2)

            assert mock_send.call_count == 2
            called_conn1 = mock_send.call_args_list[0][0][1]
            called_conn2 = mock_send.call_args_list[1][0][1]
            assert called_conn1 == conn1
            assert called_conn2 == conn2

    @pytest.mark.asyncio
    async def test_send_message_no_connections(self, ws_api):
        ws_api.connections = []
        ws_api.reconnect_tasks = []

        with pytest.raises(ValueError):
            await ws_api.send_signed_message({"params": {}})

    @pytest.mark.asyncio
    async def test_send_message_all_reconnect(self, ws_api):
        conn = MagicMock(reconnect=True)
        ws_api.connections = [conn]
        ws_api.reconnect_tasks = []

        result = await ws_api.send_signed_message({"params": {}})
        assert isinstance(result, WebsocketApiResponse)
        assert result.data() == "Websocket Reconnect"

    @pytest.mark.asyncio
    async def test_send_message_return_rate_limits_false_updates_payload(
        self, ws_api, mock_connection
    ):
        ws_api.connections = [mock_connection]
        ws_api.reconnect_tasks = []
        ws_api.configuration.return_rate_limits = False

        payload = {"params": {"symbol": "BTCUSDT"}, "method": "exchangeInfo"}

        with patch.object(
            WebSocketCommon, "send_message", new_callable=AsyncMock
        ) as mock_send:
            mock_future = asyncio.Future()
            mock_future.set_result({"result": {"foo": "bar"}, "rateLimits": []})
            mock_send.return_value = mock_future

            result = await ws_api.send_message(payload)

            assert "params" in payload
            assert payload["params"].get("returnRateLimits") is False

            sent_payload = mock_send.await_args.args[0]
            assert "params" in sent_payload
            assert sent_payload["params"].get("returnRateLimits") in (False, "false")

            assert isinstance(result, WebsocketApiResponse)
            assert callable(result._data_function)
            assert result._data_function() == {
                "result": {"foo": "bar"},
                "rateLimits": [],
            }
            assert result.rate_limits == []

    @pytest.mark.asyncio
    async def test_send_message_return_rate_limits_true_does_not_modify_payload(
        self, ws_api, mock_connection
    ):
        ws_api.connections = [mock_connection]
        ws_api.reconnect_tasks = []
        ws_api.configuration.return_rate_limits = True

        payload = {"params": {"symbol": "BTCUSDT"}, "method": "exchangeInfo"}

        with patch.object(
            WebSocketCommon, "send_message", new_callable=AsyncMock
        ) as mock_send:
            mock_future = asyncio.Future()
            mock_future.set_result(
                {
                    "result": {"foo": "bar"},
                    "rateLimits": [
                        {
                            "rateLimitType": "REQUEST_WEIGHT",
                            "interval": "MINUTE",
                            "intervalNum": 1,
                            "limit": 10,
                            "count": 0,
                        }
                    ],
                }
            )
            mock_send.return_value = mock_future

            result = await ws_api.send_message(payload)

            assert "returnRateLimits" not in payload["params"]
            assert result.rate_limits == [
                WebsocketApiRateLimit(
                    rateLimitType="REQUEST_WEIGHT",
                    interval="MINUTE",
                    intervalNum=1,
                    limit=10,
                    count=0,
                )
            ]

    @pytest.mark.asyncio
    async def test_send_message_session_logon_sets_connection_flags(
        self, ws_api, mock_connection
    ):
        ws_api.connections = [mock_connection]
        ws_api.reconnect_tasks = []
        ws_api.configuration.return_rate_limits = True

        payload = {"params": {"symbol": "BTCUSDT"}, "method": "exchangeInfo"}

        with patch.object(
            WebSocketCommon, "send_message", new_callable=AsyncMock
        ) as mock_send:
            mock_future = asyncio.Future()
            mock_future.set_result({"result": {"foo": "bar"}, "rateLimits": []})
            mock_send.return_value = mock_future

            result = await ws_api.send_message(payload, session_logon=True)

            assert mock_connection.is_session_log_on is True
            assert mock_connection.session_logon_request == payload
            assert "id" in payload
            assert isinstance(result, WebsocketApiResponse)

    @pytest.mark.asyncio
    @pytest.mark.parametrize("signed", [False, True])
    async def test_session_logout_clears_connection_flags(
        self, ws_api, mock_connection, signed
    ):
        ws_api.connections = [mock_connection]
        ws_api.reconnect_tasks = []
        ws_api.configuration.return_rate_limits = True
        mock_connection.is_session_log_on = True
        mock_connection.session_logon_request = {"method": "session.logon"}

        payload = {"method": "session.logout", "params": {}}

        with patch.object(
            WebSocketCommon, "send_message", new_callable=AsyncMock
        ) as mock_send:
            mock_future = asyncio.Future()
            mock_future.set_result({"status": 200, "result": {}, "rateLimits": []})
            mock_send.return_value = mock_future

            if signed:
                await ws_api.send_signed_message(
                    payload, signer=MagicMock(), session_logout=True
                )
            else:
                await ws_api.send_message(payload, session_logout=True)

        assert mock_connection.is_session_log_on is False
        assert mock_connection.session_logon_request is None

    @staticmethod
    def _re_logon_connection():
        conn = MagicMock()
        conn.id = "new"
        conn.is_session_log_on = False
        conn.session_logon_request = None
        conn.pending_request = {}
        conn.connection_callback_map = defaultdict(list)
        return conn

    @pytest.mark.asyncio
    async def test_session_re_log_on_signs_request_and_waits_for_success(self, ws_api):
        conn = self._re_logon_connection()
        request = {
            "method": "session.logon",
            "params": {"returnRateLimits": False},
            "id": "1",
        }

        with patch("binance_common.websocket.Signers.get_signer"), patch(
            "binance_common.utils.get_signature", return_value="sig"
        ), patch.object(
            WebSocketCommon, "send_message", new_callable=AsyncMock
        ) as mock_send:
            mock_future = asyncio.Future()
            mock_future.set_result({"status": 200, "result": {}})
            mock_send.return_value = mock_future

            assert await ws_api.session_re_log_on(request, conn) is True

        sent = mock_send.call_args[0][1]
        assert sent["method"] == "session.logon"
        assert sent["params"]["apiKey"] == "test-api-key"
        assert sent["params"]["signature"] == "sig"
        assert "timestamp" in sent["params"]
        assert request["params"] == {"returnRateLimits": False}
        assert conn.is_session_log_on is True
        assert conn.session_logon_request is request

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "outcome",
        [
            ValueError({"code": -1102, "msg": "Mandatory parameter 'apiKey'"}),
            {"status": 401, "result": {}},
            asyncio.TimeoutError(),
        ],
    )
    async def test_session_re_log_on_failure_keeps_session_logged_off(
        self, ws_api, outcome
    ):
        conn = self._re_logon_connection()
        request = {"method": "session.logon", "params": {}, "id": "1"}
        ws_api._emit_connection_event = MagicMock()

        with patch("binance_common.websocket.Signers.get_signer"), patch(
            "binance_common.utils.get_signature", return_value="sig"
        ), patch.object(
            WebSocketCommon, "send_message", new_callable=AsyncMock
        ) as mock_send, patch(
            "binance_common.websocket.asyncio.wait_for", new_callable=AsyncMock
        ) as mock_wait:
            mock_send.return_value = asyncio.Future()
            if isinstance(outcome, dict):
                mock_wait.return_value = outcome
            else:
                mock_wait.side_effect = outcome

            assert await ws_api.session_re_log_on(request, conn) is False

        assert conn.is_session_log_on is False
        assert conn.session_logon_request is request
        assert conn.pending_request == {}
        ws_api._emit_connection_event.assert_called_once()
        assert ws_api._emit_connection_event.call_args[0][:2] == (conn, "error")

    @pytest.mark.asyncio
    async def test_reconnect_drops_user_streams_when_re_logon_fails(
        self, mock_connection, mock_registry, mock_user_registry
    ):
        ws_common = WebSocketCommon(MagicMock())

        old_conn = mock_connection
        old_conn.id = "abc"
        old_conn.url_path = None
        old_conn.pending_request = {}
        old_conn.session_logon_request = {
            "method": "session.logon",
            "params": {},
            "id": "1",
        }
        old_conn.stream_callback_map = {"user_stream": ["cb1"]}
        mock_user_registry.stream_connections_map = {"user_stream": old_conn}

        new_conn = MagicMock()
        new_conn.id = "abc"
        ws_common.connections = [new_conn]

        ws_common.close_connection = AsyncMock()
        ws_common.init_connection = AsyncMock()
        ws_common.session_re_log_on = AsyncMock(return_value=False)
        ws_common._resubscribe_user_streams = AsyncMock()
        ws_common._resubscribe_global_streams = AsyncMock()

        config = MagicMock()
        config.stream_url = "wss://test.com/ws"
        config.reconnect_delay = 0
        config.reconnect_attempts = 1

        assert await ws_common.reconnect(old_conn, config) is new_conn

        ws_common._resubscribe_user_streams.assert_not_awaited()
        assert mock_user_registry.stream_connections_map == {}
        ws_common._resubscribe_global_streams.assert_awaited_once_with(
            old_conn, new_conn
        )

    @pytest.mark.asyncio
    async def test_send_message_response_model_is_one_of_model(
        self, ws_api, mock_connection
    ):
        ws_api.connections = [mock_connection]
        ws_api.reconnect_tasks = []
        ws_api.configuration.return_rate_limits = True

        class DummyResponseModel:
            @classmethod
            def from_dict(cls, data):
                return {"from_dict": data}

        payload = {"params": {"symbol": "BTCUSDT"}, "method": "exchangeInfo"}

        with patch.object(ws_api, "is_one_of_model", return_value=True), patch.object(
            WebSocketCommon, "send_message", new_callable=AsyncMock
        ) as mock_send:

            mock_future = asyncio.Future()
            mock_future.set_result({"result": {"foo": "bar"}, "rateLimits": []})
            mock_send.return_value = mock_future

            result = await ws_api.send_message(
                payload, response_model=DummyResponseModel
            )

            data = result._data_function()
            assert data == {"from_dict": {"result": {"foo": "bar"}, "rateLimits": []}}

    @pytest.mark.asyncio
    async def test_send_message_response_model_model_validate(
        self, ws_api, mock_connection
    ):
        ws_api.connections = [mock_connection]
        ws_api.reconnect_tasks = []
        ws_api.configuration.return_rate_limits = True

        class DummyResponseModel:
            @classmethod
            def model_validate(cls, data):
                return {"validated": data}

        payload = {"params": {"symbol": "BTCUSDT"}, "method": "exchangeInfo"}

        with patch.object(ws_api, "is_one_of_model", return_value=False), patch.object(
            WebSocketCommon, "send_message", new_callable=AsyncMock
        ) as mock_send:

            mock_future = asyncio.Future()
            mock_future.set_result({"result": {"foo": "bar"}, "rateLimits": []})
            mock_send.return_value = mock_future

            result = await ws_api.send_message(
                payload, response_model=DummyResponseModel
            )

            data = result._data_function()
            assert data == {"validated": {"result": {"foo": "bar"}, "rateLimits": []}}

    @pytest.mark.asyncio
    async def test_send_message_prefers_from_dict(self, ws_api, mock_connection):
        ws_api.connections = [mock_connection]
        ws_api.reconnect_tasks = []
        ws_api.configuration.return_rate_limits = True

        class DummyResponseModel:
            @classmethod
            def from_dict(cls, data):
                return {"from_dict": data}

            @classmethod
            def model_validate(cls, data):
                raise AssertionError("model_validate is only the fallback")

        payload = {"params": {"symbol": "BTCUSDT"}, "method": "exchangeInfo"}
        ws_response = {"result": {"timezone": "UTC"}, "rateLimits": []}

        with patch.object(
            WebSocketCommon, "send_message", new_callable=AsyncMock
        ) as mock_send:

            mock_future = asyncio.Future()
            mock_future.set_result(ws_response)
            mock_send.return_value = mock_future

            result = await ws_api.send_message(
                payload, response_model=DummyResponseModel
            )

            assert result._data_function() == {"from_dict": ws_response}

    @pytest.mark.asyncio
    async def test_send_message_falls_back_to_model_validate(
        self, ws_api, mock_connection
    ):
        ws_api.connections = [mock_connection]
        ws_api.reconnect_tasks = []
        ws_api.configuration.return_rate_limits = True

        class DummyResponseModel:
            @classmethod
            def from_dict(cls, data):
                raise AttributeError("type object 'int' has no attribute 'is_array'")

            @classmethod
            def model_validate(cls, data):
                return {"validated": data}

        payload = {"params": {"symbol": "BTCUSDT"}, "method": "klines"}
        ws_response = {"result": [[1, "2"]], "rateLimits": []}

        with patch.object(
            WebSocketCommon, "send_message", new_callable=AsyncMock
        ) as mock_send:

            mock_future = asyncio.Future()
            mock_future.set_result(ws_response)
            mock_send.return_value = mock_future

            result = await ws_api.send_message(
                payload, response_model=DummyResponseModel
            )

            assert result._data_function() == {"validated": ws_response}

    @pytest.mark.asyncio
    async def test_send_message_one_of_model_error_is_not_swallowed(
        self, ws_api, mock_connection
    ):
        ws_api.connections = [mock_connection]
        ws_api.reconnect_tasks = []
        ws_api.configuration.return_rate_limits = True

        class DummyOneOfModel:
            @classmethod
            def is_oneof_model(cls):
                return True

            @classmethod
            def from_dict(cls, data):
                raise ValueError("Multiple matches found when deserializing")

            @classmethod
            def model_validate(cls, data):
                return {"actual_instance": None}

        payload = {"params": {"symbol": "BTCUSDT"}, "method": "ticker"}

        with patch.object(
            WebSocketCommon, "send_message", new_callable=AsyncMock
        ) as mock_send:

            mock_future = asyncio.Future()
            mock_future.set_result({"result": {}, "rateLimits": []})
            mock_send.return_value = mock_future

            result = await ws_api.send_message(payload, response_model=DummyOneOfModel)

            with pytest.raises(ValueError, match="Multiple matches found"):
                result._data_function()

    @pytest.mark.asyncio
    async def test_send_message_no_response_model_returns_raw(
        self, ws_api, mock_connection
    ):
        ws_api.connections = [mock_connection]
        ws_api.reconnect_tasks = []
        ws_api.configuration.return_rate_limits = True

        payload = {"params": {"symbol": "BTCUSDT"}, "method": "exchangeInfo"}

        with patch.object(ws_api, "is_one_of_model", return_value=False), patch.object(
            WebSocketCommon, "send_message", new_callable=AsyncMock
        ) as mock_send:

            mock_future = asyncio.Future()
            mock_future.set_result({"result": {"foo": "bar"}, "rateLimits": []})
            mock_send.return_value = mock_future

            result = await ws_api.send_message(payload)

            data = result._data_function()
            assert data == {"result": {"foo": "bar"}, "rateLimits": []}

    @pytest.mark.asyncio
    async def test_send_message_timeout_error_returns_error(
        self, ws_api, mock_connection
    ):
        ws_api.connections = [mock_connection]
        ws_api.reconnect_tasks = []
        ws_api.configuration.return_rate_limits = True

        payload = {"params": {"symbol": "BTCUSDT"}, "method": "exchangeInfo"}

        with patch.object(
            WebSocketCommon, "send_message", new_callable=AsyncMock
        ) as mock_send:
            hanging_future = asyncio.Future()
            mock_send.return_value = hanging_future

            result = await ws_api.send_message(payload)

            assert callable(result._data_function)
            assert result._data_function() == {"error": "timeout"}
            assert result.rate_limits == []

    @pytest.mark.asyncio
    async def test_send_message_generic_exception_returns_error(
        self, ws_api, mock_connection, caplog
    ):
        ws_api.connections = [mock_connection]
        ws_api.reconnect_tasks = []
        ws_api.configuration.return_rate_limits = True

        payload = {"params": {"symbol": "BTCUSDT"}, "method": "exchangeInfo"}

        class ExplodingFuture:
            def __await__(self):
                raise RuntimeError("Something went wrong")

        with caplog.at_level(logging.WARNING), patch.object(
            WebSocketCommon,
            "send_message",
            new=AsyncMock(return_value=ExplodingFuture()),
        ):

            result = await ws_api.send_message(payload)

            assert "error" in result._data_function()
            assert result._data_function()["error"] == "Something went wrong"
            assert any("Connection with user closed" in m for m in caplog.messages)

    @pytest.mark.asyncio
    async def test_send_message_skip_auth_logic(self, ws_api, mock_connection):
        mock_connection.is_session_log_on = True
        ws_api.connections = [mock_connection]
        ws_api.reconnect_tasks = []
        ws_api.configuration.return_rate_limits = True

        payload = {"params": {"symbol": "BTCUSDT"}, "method": "exchangeInfo"}

        with patch.object(
            WebSocketCommon, "send_message", new_callable=AsyncMock
        ) as mock_send:
            mock_future = asyncio.Future()
            mock_future.set_result({"result": {"foo": "bar"}, "rateLimits": []})
            mock_send.return_value = mock_future

            await ws_api.send_message(payload, session_logon=None)
            mock_send.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_send_message_no_connections_raises(self, ws_api):
        ws_api.connections = []
        ws_api.reconnect_tasks = []

        with pytest.raises(ValueError, match="No WebSocket connections available."):
            await ws_api.send_message({"params": {}})

    @pytest.mark.asyncio
    async def test_send_message_all_connections_reconnecting_returns_reconnect_response(
        self, ws_api, mock_connection
    ):
        mock_connection.reconnect = True
        ws_api.connections = [mock_connection]
        ws_api.reconnect_tasks = []

        result = await ws_api.send_message({"params": {}})

        assert result._data_function() == "Websocket Reconnect"
        assert result.rate_limits == []

    @pytest.mark.asyncio
    async def test_ping_ws_api(self, ws_api, mock_connection):
        with patch.object(WebSocketCommon, "ping", new_callable=AsyncMock) as mock_ping:
            await ws_api.ping_ws_api(mock_connection)
            mock_ping.assert_awaited_once_with(mock_connection)

    @pytest.mark.asyncio
    async def test_request_stream_returns_correct_interface(
        self, ws_api, mock_connection
    ):
        ws_api.connections = [mock_connection]
        result = await RequestStream(ws_api, "0")
        assert isinstance(result, RequestStreamHandle)
        assert hasattr(result, "on")
        assert hasattr(result, "unsubscribe")

    @pytest.mark.asyncio
    async def test_subscribe_adds_stream_and_callback(
        self, ws_api, mock_connection, mock_user_registry
    ):
        ws_api.connections = [mock_connection]
        await ws_api.subscribe_user_data(id="0", response_model=dict)

        assert "0" in mock_user_registry.stream_connections_map
        assert mock_user_registry.stream_connections_map["0"] == mock_connection
        assert "0" in mock_connection.stream_callback_map
        assert "0" in mock_connection.response_types
        assert mock_connection.response_types["0"] is dict
        await ws_api.unsubscribe(id="0")

    @pytest.mark.asyncio
    async def test_on_sets_callback_for_websocket_api(self, ws_api, mock_connection):
        ws_api.connections = [mock_connection]
        await ws_api.subscribe_user_data(id="0", response_model=dict)

        def callback(x):
            return x

        ws_api.on("message", callback, "0")

        assert mock_connection.stream_callback_map["0"] == [callback]
        assert mock_connection.response_types["0"] is dict
        await ws_api.unsubscribe(id="0")

    @pytest.mark.asyncio
    async def test_on_unsupported_event_raises(self, ws_api):
        with pytest.raises(ValueError):
            ws_api.on("open", lambda x: x, "0")

    @pytest.mark.asyncio
    async def test_unsubscribe_removes_stream(
        self, ws_api, mock_connection, mock_user_registry
    ):
        ws_api.connections = [mock_connection]
        await ws_api.subscribe_user_data(id="0")
        await ws_api.unsubscribe(id="0")

        assert "test_stream" not in mock_user_registry.stream_connections_map

    @pytest.mark.asyncio
    async def test_unsubscribe_with_empty_streams(self, ws_api, caplog):
        await ws_api.unsubscribe(id="0")

        assert "No user data connections available for unsubscription" in caplog.text

    @pytest.mark.asyncio
    async def test_unsubscribe_no_connections(self, ws_api, caplog):
        ws_api.connections = []
        await ws_api.unsubscribe(id="0")

        assert "No user data connections available for unsubscription." in caplog.text

    @pytest.mark.asyncio
    async def test_unsubscribe_stream_not_connected_warns(
        self, ws_api, mock_connection, caplog
    ):
        ws_api.connections = [mock_connection]
        await ws_api.unsubscribe(id="0")
        assert "Stream 0 is not subscribed." in caplog.text

    @pytest.mark.asyncio
    async def test_unsubscribe_keeps_connection_callbacks(
        self, ws_api, mock_user_registry
    ):
        """Unsubscribing a user data id leaves the connection callbacks alone."""

        connection = WebSocketConnection(
            AsyncMock(), "conn-1", "ConfigurationWebSocketAPI"
        )
        ws_api.connections = [connection]
        await ws_api.subscribe_user_data(id="0")
        callback = MagicMock()
        ws_api.on_connection("close", callback, "conn-1")

        await ws_api.unsubscribe(id="0")

        assert connection.connection_callback_map["close"] == [callback]
        assert "0" not in connection.stream_callback_map

    def test_off_connection_for_user_connection(self, ws_api, mock_user_registry):
        connection = WebSocketConnection(
            AsyncMock(), "conn-1", "ConfigurationWebSocketAPI"
        )
        ws_api.connections = [connection]
        callback = MagicMock()

        ws_api.on_connection("pong", callback, "conn-1")
        ws_api.off_connection("pong", callback, "conn-1")

        assert connection.connection_callback_map["pong"] == []

    def test_on_connection_unknown_id_warns(self, ws_api, mock_user_registry, caplog):
        ws_api.connections = []

        with caplog.at_level(logging.WARNING):
            ws_api.on_connection("pong", MagicMock(), "missing")

        assert "Connection missing not connected." in caplog.text


class TestSessionReLogOn:
    """Issue #569: the logon re-sent after a reconnect must be signed."""

    @staticmethod
    def _api():
        config = SimpleNamespace(
            api_key="test-api-key", private_key="key", private_key_passphrase=None
        )
        api = WebSocketAPIBase.__new__(WebSocketAPIBase)
        api.configuration = config
        return api

    @staticmethod
    def _connection(name="conn-1", is_session_log_on=False):
        return SimpleNamespace(
            id=name, is_session_log_on=is_session_log_on, pending_request={}
        )

    @staticmethod
    def _ok_response(*_args, **_kwargs):
        future = asyncio.get_running_loop().create_future()
        future.set_result({"status": 200})
        return future

    @pytest.mark.asyncio
    async def test_re_logon_is_signed_with_api_key_timestamp_and_signature(self):
        api = self._api()
        connection = self._connection()
        request = {"method": "session.logon", "params": {}, "id": "logon-id"}

        with patch(
            "binance_common.websocket.Signers.get_signer", return_value=MagicMock()
        ), patch(
            "binance_common.utils.get_signature", return_value="signed"
        ) as mock_signature, patch.object(
            WebSocketCommon,
            "send_message",
            new_callable=AsyncMock,
            side_effect=self._ok_response,
        ) as mock_send:
            await api.session_re_log_on(request, connection)

        mock_send.assert_awaited_once()
        sent = mock_send.await_args.args[1]
        assert sent["method"] == "session.logon"
        assert sent["params"]["apiKey"] == "test-api-key"
        assert sent["params"]["signature"] == "signed"
        assert "timestamp" in sent["params"]
        mock_signature.assert_called_once()
        assert connection.is_session_log_on is True

    @pytest.mark.asyncio
    async def test_re_logon_leaves_the_stored_request_untouched(self):
        api = self._api()
        request = {"method": "session.logon", "params": {}, "id": "logon-id"}

        with patch(
            "binance_common.websocket.Signers.get_signer", return_value=MagicMock()
        ), patch(
            "binance_common.utils.get_signature", return_value="signed"
        ), patch.object(
            WebSocketCommon,
            "send_message",
            new_callable=AsyncMock,
            side_effect=self._ok_response,
        ) as mock_send:
            for name in ("conn-1", "conn-2"):
                connection = self._connection(name)
                await api.session_re_log_on(request, connection)

        # Nothing from one re-logon leaks into the next: each one is signed afresh.
        assert request == {"method": "session.logon", "params": {}, "id": "logon-id"}
        assert mock_send.await_count == 2

    @pytest.mark.asyncio
    async def test_no_re_logon_when_the_session_is_already_logged_on(self):
        api = self._api()
        connection = self._connection(is_session_log_on=True)

        with patch.object(
            WebSocketCommon, "send_message", new_callable=AsyncMock
        ) as mock_send:
            await api.session_re_log_on(
                {"method": "session.logon", "params": {}, "id": "x"}, connection
            )

        mock_send.assert_not_awaited()


class TestSignatureUserDataResubscribe:
    """Issue #578: a signature user data subscription must survive a reconnect."""

    SUBSCRIBE = "userDataStream.subscribe.signature"

    @staticmethod
    def _api():
        config = MagicMock(
            api_key="test-api-key",
            mode=WebsocketMode.SINGLE,
            return_rate_limits=False,
            session_re_logon=True,
            stream_url="wss://test.com/ws",
            reconnect_delay=0,
            reconnect_attempts=1,
        )
        endpoints = WebsocketApiUserDataEndpoints(
            user_data_stream_subscribe="userDataStream.subscribe",
            user_data_stream_logout="session.logout",
        )
        api = WebSocketAPIBase(config, endpoints)
        api.close_connection = AsyncMock()
        return api

    @staticmethod
    def _server(subscription_ids=None, fail=False):
        """Fake server: answers each request and records what was sent where."""

        sent = []
        ids = defaultdict(int)

        async def send(self, payload, connection):
            sent.append((connection, payload))
            future = asyncio.get_running_loop().create_future()
            if fail and connection.id == "conn-1" and len(sent) > 1:
                future.set_exception(ValueError({"code": -1022, "msg": "bad"}))
                return future
            result = {}
            if payload["method"].startswith("userDataStream.subscribe"):
                key = id(connection)
                if subscription_ids is not None and key in subscription_ids:
                    result = {"subscriptionId": subscription_ids[key].pop(0)}
                else:
                    result = {"subscriptionId": ids[key]}
                    ids[key] += 1
            future.set_result({"id": payload["id"], "status": 200, "result": result})
            return future

        return sent, send

    @classmethod
    def _replays(cls, sent, connection):
        return [p for c, p in sent if c is connection and p["method"] == cls.SUBSCRIBE]

    @staticmethod
    def _connection():
        websocket = AsyncMock()
        websocket.__aiter__.return_value = []
        return WebSocketConnection(websocket, "conn-1", "ConfigurationWebSocketAPI")

    async def _subscribe(self, api):
        response = await api.send_signed_message(
            payload={"method": self.SUBSCRIBE, "params": {"recv_window": 5000}},
            signer=None,
        )
        subscription_id = response.data()["result"]["subscriptionId"]
        handle = await RequestStream(api, subscription_id)
        return subscription_id, handle

    async def _reconnect(self, api, old_conn):
        new_conn = self._connection()

        async def fake_init(*args, **kwargs):
            api.connections.append(new_conn)

        api.init_connection = fake_init
        await api.reconnect(old_conn, api.configuration)
        return new_conn

    @staticmethod
    async def _deliver(api, connection, subscription_id, event):
        message = SimpleNamespace(
            type=aiohttp.WSMsgType.TEXT,
            data=json.dumps({"subscriptionId": subscription_id, "event": event}),
        )
        connection.websocket.__aiter__.return_value = [message]
        await api.receive_loop(connection)

    @pytest.mark.asyncio
    async def test_subscription_is_signed_again_on_the_new_connection(self):
        api = self._api()
        old_conn = self._connection()
        api.connections = [old_conn]
        sent, send = self._server()
        callback = MagicMock()

        with patch.object(WebSocketCommon, "send_message", new=send), patch(
            "binance_common.utils.get_signature", return_value="signed"
        ), patch("binance_common.utils.get_timestamp", side_effect=[1, 2]):
            subscription_id, handle = await self._subscribe(api)
            handle.on("message", callback)
            new_conn = await self._reconnect(api, old_conn)

        replays = self._replays(sent, new_conn)
        assert len(replays) == 1
        params = replays[0]["params"]
        assert params["signature"] == "signed"
        assert params["apiKey"] == "test-api-key"
        assert params["recvWindow"] == "5000"
        assert params["timestamp"] == 2

        await self._deliver(api, new_conn, subscription_id, {"e": "executionReport"})
        callback.assert_called_once_with({"e": "executionReport"})

    @pytest.mark.asyncio
    async def test_callbacks_follow_the_new_subscription_id(self):
        api = self._api()
        old_conn = self._connection()
        api.connections = [old_conn]
        sent, send = self._server()
        first, second = MagicMock(), MagicMock()

        with patch.object(WebSocketCommon, "send_message", new=send), patch(
            "binance_common.utils.get_signature", return_value="signed"
        ):
            id_0, handle_0 = await self._subscribe(api)
            id_1, handle_1 = await self._subscribe(api)
            handle_0.on("message", first)
            handle_1.on("message", second)
            await handle_0.unsubscribe()
            new_conn = await self._reconnect(api, old_conn)

        assert (id_0, id_1) == (0, 1)
        replays = self._replays(sent, new_conn)
        # The unsubscribed stream is not restored; the other one gets id 0 now.
        assert len(replays) == 1
        assert handle_1._stream == 0
        assert api.user_stream_connections.stream_connections_map == {0: new_conn}

        late = MagicMock()
        handle_1.on("message", late)
        await self._deliver(api, new_conn, 0, {"e": "outboundAccountPosition"})
        second.assert_called_once_with({"e": "outboundAccountPosition"})
        late.assert_called_once()
        first.assert_not_called()

        await handle_1.unsubscribe()
        assert api.user_stream_connections.stream_connections_map == {}
        assert new_conn.user_data_subscribe_requests == {}

    @pytest.mark.asyncio
    async def test_server_side_unsubscribe_is_not_restored(self):
        api = self._api()
        old_conn = self._connection()
        api.connections = [old_conn]
        sent, send = self._server()

        with patch.object(WebSocketCommon, "send_message", new=send), patch(
            "binance_common.utils.get_signature", return_value="signed"
        ):
            await self._subscribe(api)
            await self._subscribe(api)
            await api.send_message(
                payload={
                    "method": "userDataStream.unsubscribe",
                    "params": {"subscription_id": 1},
                }
            )
            new_conn = await self._reconnect(api, old_conn)

        replays = self._replays(sent, new_conn)
        assert len(replays) == 1
        assert list(new_conn.user_data_subscribe_requests) == [0]

    @pytest.mark.asyncio
    async def test_unsubscribe_all_is_not_restored(self):
        api = self._api()
        old_conn = self._connection()
        api.connections = [old_conn]
        sent, send = self._server()

        with patch.object(WebSocketCommon, "send_message", new=send), patch(
            "binance_common.utils.get_signature", return_value="signed"
        ):
            await self._subscribe(api)
            await api.send_message(
                payload={"method": "userDataStream.unsubscribe", "params": {}}
            )
            new_conn = await self._reconnect(api, old_conn)

        assert not [p for c, p in sent if c is new_conn]

    @pytest.mark.asyncio
    async def test_failed_resubscribe_emits_error_and_drops_the_stream(self):
        api = self._api()
        old_conn = self._connection()
        api.connections = [old_conn]
        sent, send = self._server(fail=True)
        errors = []
        api.on_connection("error", errors.append)

        with patch.object(WebSocketCommon, "send_message", new=send), patch(
            "binance_common.utils.get_signature", return_value="signed"
        ):
            await self._subscribe(api)
            new_conn = await self._reconnect(api, old_conn)

        assert len(errors) == 1
        assert isinstance(errors[0], ValueError)
        assert api.user_stream_connections.stream_connections_map == {}
        assert new_conn.user_data_subscribe_requests == {}
        assert new_conn.pending_request == {}

    @pytest.mark.asyncio
    async def test_session_logon_subscription_is_not_replayed_as_signature(self):
        api = self._api()
        old_conn = self._connection()
        api.connections = [old_conn]
        sent, send = self._server()

        with patch.object(WebSocketCommon, "send_message", new=send), patch(
            "binance_common.utils.get_signature", return_value="signed"
        ):
            signature_id, _ = await self._subscribe(api)
            old_conn.session_logon_request = {
                "method": "session.logon",
                "params": {},
                "id": "logon",
            }
            old_conn.is_session_log_on = False
            await api.subscribe_user_data(id="logon-stream")
            api.session_re_log_on = AsyncMock(return_value=True)
            new_conn = await self._reconnect(api, old_conn)

        methods = [p["method"] for c, p in sent if c is new_conn]
        assert methods.count(self.SUBSCRIBE) == 1
        assert methods.count("userDataStream.subscribe") == 1

    @pytest.mark.asyncio
    async def test_closed_connection_forgets_its_signature_subscriptions(self):
        api = self._api()
        conn = self._connection()
        api.connections = [conn]
        _, send = self._server()

        with patch.object(WebSocketCommon, "send_message", new=send), patch(
            "binance_common.utils.get_signature", return_value="signed"
        ):
            await self._subscribe(api)

        assert list(conn.user_data_subscribe_requests) == [0]
        await WebSocketCommon.close_connection(api, conn, close_session=False)

        assert conn.user_data_subscribe_requests == {}
        assert api.user_stream_connections.stream_connections_map == {}
