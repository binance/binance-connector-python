import asyncio
import aiohttp
import json
import logging
import pytest_asyncio
import pytest

from unittest.mock import AsyncMock, MagicMock, patch
from types import SimpleNamespace
from collections import OrderedDict

from binance_common.configuration import ConfigurationWebSocketAPI
from binance_common.constants import WebsocketMode
from binance_common.websocket import (
    global_stream_connections,
    RequestStream,
    RequestStreamHandle,
    WebSocketStreamBase,
    WebSocketAPIBase,
    WebSocketCommon,
    WebSocketConnection,
)
from binance_common.models import WebsocketApiResponse


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
    return config


@pytest.fixture
def mock_connection():
    conn = MagicMock()
    conn.id = 1
    conn.reconnect = False
    conn.websocket = AsyncMock()
    conn.stream_callback_map = {}
    return conn


@pytest.fixture
def mock_registry(monkeypatch):
    mock = type(global_stream_connections)()
    monkeypatch.setattr("binance_common.websocket.global_stream_connections", mock)
    return mock


@pytest.fixture
def websocket_stream(mock_config, mock_connection):
    instance = WebSocketStreamBase(mock_config)
    instance.connections = [mock_connection]
    instance.reconnect_tasks = []
    return instance


@pytest.fixture
def ws_api(mock_config):
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
    async def test_connect_single_mode(self, mock_ws_connect, config, mock_websocket):
        mock_ws_connect.return_value = mock_websocket

        ws_common = WebSocketCommon(config)
        await ws_common.connect("wss://test.com/ws", config)

        assert len(ws_common.connections) == 1
        connection = ws_common.connections[0]
        assert isinstance(connection, WebSocketConnection)
        assert connection.id == "mock-uuid"

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

        callback = {"foo": lambda x: x, "bar": lambda x: x + 1}

        mock_registry.stream_connections_map = {"foo": connection, "bar": connection}
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

        pong_msg = MagicMock()
        pong_msg.type = aiohttp.WSMsgType.PONG

        close_msg = MagicMock()
        close_msg.type = aiohttp.WSMsgType.CLOSE

        ws_mock = AsyncMock()
        ws_mock.pong = AsyncMock()
        ws_mock.__aiter__.return_value = [ping_msg, pong_msg, close_msg]

        conn = WebSocketConnection(ws_mock, "test_id", "ConfigurationWebSocketStreams")

        ws_common = WebSocketCommon(None)
        await ws_common.receive_loop(conn)

        ws_mock.pong.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_receive_loop_logs_error_and_closes(self):
        error_msg = MagicMock()
        error_msg.type = aiohttp.WSMsgType.ERROR

        ws_mock = AsyncMock()
        ws_mock.__aiter__.return_value = [error_msg]
        ws_mock.exception = MagicMock(return_value=Exception("test error"))

        conn = WebSocketConnection(ws_mock, "test_id", "ConfigurationWebSocketStreams")
        ws_common = WebSocketCommon(None)

        await ws_common.receive_loop(conn)

        ws_mock.exception.assert_called_once()


class TestWebSocketStreamBase:

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
    async def test_on_sets_callback_for_stream(self, websocket_stream, mock_connection):
        await websocket_stream.subscribe(["test_stream"])

        callback = lambda x: x
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

    @pytest.mark.asyncio
    async def test_request_stream_returns_correct_interface(self, websocket_stream):
        result = await RequestStream(websocket_stream, "test_stream")
        assert isinstance(result, RequestStreamHandle)
        assert hasattr(result, "on")
        assert hasattr(result, "unsubscribe")

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
            assert "id" in payload
            assert "method" in payload
            assert "params" in payload

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
        ) as mock_send, patch.object(
            ws_api, "websocket_api_signature", return_value="signature"
        ) as mock_signature:

            mock_future = asyncio.Future()
            mock_future.set_result({"result": {"foo": "bar"}, "rateLimits": []})
            mock_send.return_value = mock_future

            result = await ws_api.send_signed_message(payload)

            mock_send.assert_awaited_once()
            mock_signature.assert_called_once_with({"symbol": "BTCUSDT"}, None)
            assert "id" in payload
            assert "method" in payload
            assert "params" in payload
            assert payload["params"] == "signature"

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
        ) as mock_send, patch.object(
            ws_api, "websocket_api_signature", return_value="signature"
        ) as mock_signature:

            hanging_future = asyncio.Future()
            mock_send.return_value = hanging_future

            result = await ws_api.send_signed_message(payload)

            mock_send.assert_awaited_once()
            mock_signature.assert_called_once_with({"symbol": "BTCUSDT"}, None)
            assert "id" in payload
            assert "method" in payload
            assert "params" in payload
            assert payload["params"] == "signature"

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
        ), patch.object(ws_api, "websocket_api_signature", return_value="signature"):

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

    def test_websocket_api_signature(self, ws_api):
        with patch(
            "binance_common.websocket.get_timestamp", return_value=1234567890
        ), patch(
            "binance_common.websocket.get_signature", return_value="mocked-signature"
        ):

            result = ws_api.websocket_api_signature({"foo": "bar"})

            assert isinstance(result, OrderedDict)
            assert result["apiKey"] == "test-api-key"
            assert result["timestamp"] == 1234567890
            assert result["foo"] == "bar"
            assert result["signature"] == "mocked-signature"

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
        self, ws_api, mock_connection, mock_registry
    ):
        ws_api.connections = [mock_connection]
        await ws_api.subscribe_user_data(id="0")

        assert "0" in mock_registry.stream_connections_map
        assert mock_registry.stream_connections_map["0"] == mock_connection
        assert "0" in mock_connection.stream_callback_map
        await ws_api.unsubscribe(id="0")

    @pytest.mark.asyncio
    async def test_on_sets_callback_for_stream(self, ws_api, mock_connection):
        ws_api.connections = [mock_connection]
        await ws_api.subscribe_user_data(id="0")

        callback = lambda x: x
        ws_api.on("message", callback, "0")

        assert mock_connection.stream_callback_map["0"] == [callback]

        callback = lambda x: x
        ws_api.on("message", callback, "0")

        assert mock_connection.stream_callback_map["0"] == [callback]
        await ws_api.unsubscribe(id="0")

    @pytest.mark.asyncio
    async def test_on_sets_callback_for_stream(self, ws_api, mock_connection):
        ws_api.connections = [mock_connection]
        await ws_api.subscribe_user_data(id="0")

        callback = lambda x: x
        ws_api.on("message", callback, "0")

        assert mock_connection.stream_callback_map["0"] == [callback]
        await ws_api.unsubscribe(id="0")

    @pytest.mark.asyncio
    async def test_on_unsupported_event_raises(self, ws_api):
        with pytest.raises(ValueError):
            ws_api.on("open", lambda x: x, "0")

    @pytest.mark.asyncio
    async def test_unsubscribe_removes_stream(
        self, ws_api, mock_connection, mock_registry
    ):
        ws_api.connections = [mock_connection]
        await ws_api.subscribe_user_data(id="0")
        await ws_api.unsubscribe(id="0")

        assert "test_stream" not in mock_registry.stream_connections_map

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
