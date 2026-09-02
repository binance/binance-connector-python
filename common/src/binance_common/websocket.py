import aiohttp
import asyncio
import inspect
import json
import logging

from pydantic import BaseModel
from typing import Callable, Optional, Dict, Generic, Union, TypeVar, Type
from collections import defaultdict

from binance_common.configuration import (
    ConfigurationWebSocketAPI,
    ConfigurationWebSocketStreams,
)
from binance_common.constants import (
    AUTO_RECONNECT_INTERVAL_SECONDS,
    DEFAULT_RECONNECT_ATTEMPTS,
    MAX_RECONNECT_ATTEMPTS,
    SUBSCRIBE_MESSAGE_DELAY_SECONDS,
    SUPPORTED_CONNECTION_EVENTS,
    WebsocketMode,
)
from binance_common.models import (
    WebsocketApiResponse,
    WebsocketApiOptions,
    WebsocketApiUserDataEndpoints,
)
from binance_common.signature import Signers
from binance_common.utils import (
    get_uuid,
    get_random_int,
    parse_proxies,
    parse_user_event,
    parse_ws_rate_limit_headers,
    redact_sensitive_info,
    ws_api_payload,
)

T = TypeVar("T", bound=BaseModel)


class StreamConnectionsMap:
    def __init__(self):
        self.stream_connections_map: dict[Union[str, int], WebSocketConnection] = {}


global_stream_connections = StreamConnectionsMap()
global_user_stream_connections = StreamConnectionsMap()


def _forget_connection_streams(connection: "WebSocketConnection") -> None:
    """Drop every stream mapping that points at a connection.

    A connection that is gone for good must not be left in the global stream
    maps, or a later subscribe would treat its streams as still live and
    silently skip them.

    Args:
        connection (WebSocketConnection): The connection being forgotten.
    """

    for stream_map in (global_stream_connections, global_user_stream_connections):
        for stream in [
            stream
            for stream, mapped in stream_map.stream_connections_map.items()
            if mapped is connection
        ]:
            stream_map.stream_connections_map.pop(stream, None)


class WebSocketConnection:
    """Represents a WebSocket connection.

    Attributes:
        id (Union[str, int]): Unique identifier for the WebSocket connection.
        pending_request (dict): Dictionary to hold pending requests.
        stream_callback_map (dict): Map of stream names to their callback functions.
        connection_callback_map (defaultdict[list]): Map of connection-level event names
            to lists of registered callback functions.
        response_types (dict): Map of stream names to their response types.
        ws_type (str): Type of WebSocket connection (API or Stream).
        websocket (aiohttp.ClientWebSocketResponse): The WebSocket response object.
        reconnect (bool): Flag indicating if the connection should reconnect.
        is_open (bool): Flag indicating if the connection is currently open.
        is_being_replaced (bool): Flag indicating that this connection is being
            replaced by a reconnect, so it must not be discarded or treated as
            closed by the user while its replacement is established.
        close_emitted (bool): Flag indicating that the `close` event has already
            been emitted for this connection, so it is never reported twice.
        reconnect_emitted (bool): Flag indicating that the `reconnect` event has
            already been emitted for this connection, so a planned replacement
            is never reported twice.
        is_session_log_on (bool): Flag indicating if the session is logged on.
        session_logon_request (Optional[dict]): The session logon request data.
        url_path (Optional[str]): The URL path for the WebSocket connection.
        close_initiated (bool): Flag indicating that the user asked for this
            connection to be closed, so it must not be reconnected.
        scheduled_reconnect_task (Optional[asyncio.Task]): The pending automatic
            reconnect task, kept so it can be cancelled when the connection is
            replaced or closed.
    """

    def __init__(
        self,
        websocket: aiohttp.ClientWebSocketResponse,
        id: Union[str, int],
        ws_type: str,
        url_path: Optional[str] = None,
    ):
        self.id = id
        self.pending_request = {}
        self.stream_callback_map = {}
        self.connection_callback_map = defaultdict(list)
        self.response_types = {}
        self.ws_type = ws_type
        self.websocket = websocket
        self.reconnect = False
        self.is_open = True
        self.is_being_replaced = False
        self.close_emitted = False
        self.reconnect_emitted = False
        self.is_session_log_on = False
        self.session_logon_request = None
        self.url_path = url_path
        self.close_initiated = False
        self.scheduled_reconnect_task = None

    def cancel_scheduled_reconnect(self) -> None:
        """Cancel the pending automatic reconnect for this connection.
        """

        if self.scheduled_reconnect_task is None:
            return

        task = self.scheduled_reconnect_task
        self.scheduled_reconnect_task = None
        if task is not asyncio.current_task():
            task.cancel()


class WebSocketCommon:
    def __init__(
        self,
        configuration: Union[ConfigurationWebSocketAPI, ConfigurationWebSocketStreams],
        user_data_endpoints: Optional[WebsocketApiUserDataEndpoints] = None,
    ):
        """Initialize the WebSocketCommon class.

        Args:
            configuration (Union[ConfigurationWebSocketAPI, ConfigurationWebSocketStreams]): Configuration object.
        """

        self.connections = []
        self.reconnect_tasks = []
        self.round_robin_index = 0
        self.configuration = configuration
        self.session = None
        self.user_data_endpoints = user_data_endpoints

    async def connect(
        self,
        url: str,
        configuration: Union[ConfigurationWebSocketAPI, ConfigurationWebSocketStreams],
        ws_id: Optional[Union[str, int]] = None,
        url_paths: Optional[list[str]] = None,
    ):
        """Connect to the Binance WebSocket server.

        Args:
            url (str): WebSocket URL.
            configuration (Union[ConfigurationWebSocketAPI, ConfigurationWebSocketStreams]): Configuration object.
            ws_id (Optional[Union[str, int]]): Optional WebSocket ID for the connection.
            url_paths (Optional[list[str]]): Optional list of URL paths for the connection.
        """

        try:
            if self.session is None:
                self.session = aiohttp.ClientSession()

            pool_size = (
                configuration.pool_size
                if configuration.mode == WebsocketMode.POOL
                else 1
            )
            urls = url_paths if url_paths else [None]

            for url_path in urls:
                for _ in range(pool_size):
                    await self.init_connection(
                        url, configuration, ws_id=ws_id, url_path=url_path
                    )
            return self
        except Exception as e:
            logging.error(f"WebSocket failed to connect: {e}")

    async def init_connection(
        self,
        url,
        configuration: Union[ConfigurationWebSocketAPI, ConfigurationWebSocketStreams],
        url_path: Optional[str] = None,
        ws_id: Optional[Union[str, int]] = None,
    ):
        """Initialize a WebSocket connection.

        Args:
            url (str): WebSocket URL.
            configuration (Union[ConfigurationWebSocketAPI, ConfigurationWebSocketStreams]): Configuration object.
            url_path (Optional[str]): Optional URL path for the connection.
            ws_id (Optional[Union[str, int]]): Optional WebSocket ID for the connection.
        """

        user_agent = configuration.user_agent

        proxy = (
            parse_proxies(self.configuration.proxy)[configuration.proxy["protocol"]]
            if configuration.proxy is not None
            else None
        )

        if configuration.time_unit:
            url = f"{url}?timeUnit={configuration.time_unit.value}"
        logging.info(f"Connecting to {url} with proxy {proxy}")

        if url_path:
            url = url.replace("/stream", f"/{url_path}/stream")

        if type(configuration).__name__ == "ConfigurationWebSocketAPI":
            websocket = await self.session.ws_connect(
                url,
                compress=configuration.compression,
                headers={"User-Agent": user_agent},
                max_msg_size=20 * 1024 * 1024,
                proxy=proxy,
                ssl=configuration.https_agent,
                timeout=configuration.timeout / 1000,
                autoping=False,
            )
            if ws_id:
                id = ws_id
            else:
                id = (
                    websocket._response.headers.get("x-mbx-uuid")
                    if websocket._response.headers.get("x-mbx-uuid")
                    else get_uuid()
                )
        else:
            websocket = await self.session.ws_connect(
                url,
                compress=configuration.compression,
                headers={"User-Agent": user_agent},
                max_msg_size=20 * 1024 * 1024,
                proxy=proxy,
                ssl=configuration.https_agent,
                autoping=False,
            )
            id = ws_id if ws_id else get_uuid()

        logging.info(f"Establishing Websocket connection with id {id} to: {url}")
        connection = WebSocketConnection(
            websocket, id, type(configuration).__name__, url_path
        )

        self.connections.append(connection)

        connection.scheduled_reconnect_task = asyncio.create_task(
            self.schedule_reconnect(
                connection, configuration, AUTO_RECONNECT_INTERVAL_SECONDS
            )
        )
        asyncio.create_task(self.receive_loop(connection))

    async def receive_loop(self, connection: WebSocketConnection):
        """Continuously receive messages from the WebSocket server.

        Args:
            connection (WebSocketConnection): WebSocket connection object.
        """

        loop_reported_close = False
        async for msg in connection.websocket:
            if msg.type == aiohttp.WSMsgType.TEXT:
                data = json.loads(msg.data)

                request_id = data.get("id")
                if request_id and request_id in connection.pending_request:
                    future = connection.pending_request.pop(request_id)
                    if data.get("error"):
                        logging.error(
                            f"Error received from server for request "
                            f"{request_id}: {data['error']}"
                        )
                        future.set_exception(ValueError(data["error"]))
                    else:
                        future.set_result(data)
                elif (
                    data.get("event", {}).get("e") == "serverShutdown"
                    and not connection.reconnect
                    and connection.id not in self.reconnect_tasks
                    and not connection.close_initiated
                ):
                    logging.warning(
                        "Server shutdown event received, scheduling reconnect"
                    )
                    await self.schedule_reconnect(
                        connection, self.configuration, 5, close_old_connection=False
                    )
                    await self.close_connection(connection, False)
                else:
                    if data.get("error"):
                        logging.error(f"Error received from server: {data['error']}")
                        self._emit_connection_event(
                            connection, "error", data["error"]
                        )
                        continue

                    stream = data.get("stream")
                    subscription_id = data.get("subscriptionId")

                    key = stream or subscription_id
                    callbacks = (
                        connection.stream_callback_map.get(key)
                        if key is not None
                        else None
                    )

                    if callbacks:
                        try:
                            if stream:
                                response_model = connection.response_types.get(stream)
                                payload = data["data"] if response_model else data

                                for callback in callbacks:
                                    if response_model:
                                        if response_model.__pydantic_fields__.get(
                                            "one_of_schemas"
                                        ):
                                            parsed = (
                                                [
                                                    parse_user_event(
                                                        item, response_model
                                                    )
                                                    for item in payload
                                                ]
                                                if isinstance(payload, list)
                                                else parse_user_event(
                                                    payload, response_model
                                                )
                                            )
                                        elif isinstance(payload, list):
                                            parsed = [
                                                response_model.model_validate_json(
                                                    json.dumps(item)
                                                )
                                                for item in payload
                                            ]
                                        else:
                                            parsed = response_model.model_validate_json(
                                                json.dumps(payload)
                                            )
                                        callback(parsed)
                                    else:
                                        callback(payload)
                            else:
                                response_model = connection.response_types.get(
                                    subscription_id
                                )
                                payload = data["event"]

                                for callback in callbacks:
                                    if response_model:
                                        if isinstance(payload, list):
                                            parsed = [
                                                parse_user_event(item, response_model)
                                                for item in payload
                                            ]
                                        else:
                                            parsed = parse_user_event(
                                                payload, response_model
                                            )
                                        callback(parsed)
                                    else:
                                        callback(payload)
                        except Exception as e:
                            logging.error(f"Error in callback for key {key}: {e}")
                            self._emit_connection_event(connection, "error", e)
                    else:
                        logging.info(f"Received message: {data}")
            elif msg.type == aiohttp.WSMsgType.PING:
                logging.info(f"Received PING from server for {connection.id}")
                await connection.websocket.pong(msg.data)
                self._emit_connection_event(connection, "ping", msg.data)

            elif msg.type == aiohttp.WSMsgType.PONG:
                logging.info(f"Received PONG from server for {connection.id}")
                self._emit_connection_event(connection, "pong", msg.data)

            elif msg.type == aiohttp.WSMsgType.ERROR:
                err = connection.websocket.exception()
                logging.error(
                    f"Received error from server on WebSocket {connection.id}: {err}"
                )
                self._emit_connection_event(connection, "error", err)
                self._emit_close_event(connection)
                await self._discard_connection(connection)
                loop_reported_close = True
                break

            elif msg.type == aiohttp.WSMsgType.CLOSE:
                logging.info("WebSocket closed")
                self._emit_close_event(connection)
                await self._discard_connection(connection)
                loop_reported_close = True
                break

        if not loop_reported_close:
            logging.info("WebSocket connection closed")
            self._emit_close_event(connection)
            await self._discard_connection(connection)

    def _emit_close_event(self, connection: WebSocketConnection) -> None:
        """Mark a connection closed and emit its `close` event.

        Args:
            connection (WebSocketConnection): The connection that has closed.
        """

        connection.is_open = False

        if connection.is_being_replaced:
            logging.debug(
                f"WebSocket {connection.id} is being replaced by a reconnect; "
                f"not emitting 'close'."
            )
            return

        if connection.close_emitted:
            logging.debug(
                f"WebSocket {connection.id} already reported as closed; "
                f"not emitting 'close' again."
            )
            return

        connection.close_emitted = True
        self._emit_connection_event(connection, "close")

    def _emit_reconnect_event(self, connection: WebSocketConnection) -> None:
        """Mark a connection as replaced and emit its `reconnect` event.

        Args:
            connection (WebSocketConnection): The connection being replaced.
        """

        connection.is_open = False

        if connection.reconnect_emitted:
            logging.debug(
                f"WebSocket {connection.id} already reported as reconnecting; "
                f"not emitting 'reconnect' again."
            )
            return

        connection.reconnect_emitted = True
        self._emit_connection_event(connection, "reconnect")

    async def _discard_connection(self, connection: WebSocketConnection) -> None:
        """Close a dead socket and stop handing it out for new messages.

        Args:
            connection (WebSocketConnection): The connection that has ended.
        """

        if connection.reconnect or connection.is_being_replaced:
            return

        connection.cancel_scheduled_reconnect()

        if not connection.websocket.closed:
            try:
                await connection.websocket.close()
                logging.info(f"WebSocket {connection.id} closed after failure.")
            except Exception as e:
                logging.error(
                    f"Error closing failed WebSocket {connection.id}: {e}"
                )

        if connection in self.connections:
            self.connections.remove(connection)
            logging.info(
                f"WebSocket {connection.id} removed from the connection pool."
            )

    async def send_message(
        self,
        payload: Dict,
        connection: WebSocketConnection,
    ):
        """Send a message to the WebSocket server.

        Args:
            payload (Dict): Payload to send.
            connection (WebSocketConnection): WebSocket connection object.
        """

        websocket = connection.websocket
        if payload.get("id") not in connection.pending_request:
            future = asyncio.get_event_loop().create_future()
            connection.pending_request[payload.get("id")] = future
        else:
            future = connection.pending_request[payload.get("id")]

        logging.info(
            f"Sending message to WebSocket {connection.id}: {redact_sensitive_info(payload)}"
        )
        await websocket.send_str(json.dumps(payload))
        return future

    async def ping(self, connection: WebSocketConnection):
        """Send a ping message to the WebSocket server.

        Args:
            connection (WebSocketConnection): WebSocket connection object.
        """

        websocket = connection.websocket
        try:
            await websocket.ping()
            logging.info(f"Ping sent to WebSocket {connection.id}")
        except Exception as e:
            logging.error(f"Error sending ping to WebSocket {connection.id}: {e}")

    def _resolve_connections(
        self,
        connection: Optional[Union[WebSocketConnection, str, int]] = None,
    ) -> list[WebSocketConnection]:
        """Resolve a connection selector to the connections it designates.

        Args:
            connection (Optional[Union[WebSocketConnection, str, int]]): A
                connection object, a connection id, or `None` to select every
                connection currently in the pool.

        Returns:
            list[WebSocketConnection]: The matching connections, empty when the
                selector matches nothing.
        """

        if connection is None:
            return list(self.connections)

        if isinstance(connection, WebSocketConnection):
            return [connection]

        return [c for c in self.connections if str(c.id) == str(connection)]

    def on_connection(
        self,
        event: str,
        callback: Callable[..., None],
        connection: Optional[Union[WebSocketConnection, str, int]] = None,
    ) -> None:
        """Register a callback for a connection-level event.

        Args:
            event (str): The connection event to listen for. Supported values are
                `open`, `ping`, `pong`, `reconnect`, `close`, and `error`.
            callback (Callable[..., None]): Callback invoked when the event fires.
                `ping` and `pong` pass the frame payload, `error` passes the
                error, and `open`, `reconnect` and `close` pass nothing. The
                callback may also be declared without parameters to ignore the
                payload.
            connection (Optional[Union[WebSocketConnection, str, int]]): The
                connection to observe, given as a connection object or its id.
                When omitted, every connection of the pool is observed.

        Raises:
            ValueError: If the provided event is not supported.
        """

        self._validate_connection_event(event)

        connections = self._resolve_connections(connection)

        if not connections:
            if connection is None:
                logging.warning(
                    f"No WebSocket connections available to register a "
                    f"'{event}' callback on."
                )
            else:
                logging.warning(f"Connection {connection} not connected.")
            return

        for target in connections:
            registered = target.connection_callback_map[event]

            if callback in registered:
                logging.debug(
                    f"Connection callback for '{event}' is already registered on "
                    f"WebSocket {target.id}; ignoring the duplicate."
                )
                continue

            registered.append(callback)

            if event == "open" and target.is_open:
                self._invoke_connection_callback(target, event, callback)

    def off_connection(
        self,
        event: str,
        callback: Optional[Callable[..., None]] = None,
        connection: Optional[Union[WebSocketConnection, str, int]] = None,
    ) -> None:
        """Unregister connection-level callbacks.

        Args:
            event (str): The connection event to stop listening for.
            callback (Optional[Callable[..., None]]): The callback to remove. When
                omitted, every callback registered for the event is removed.
            connection (Optional[Union[WebSocketConnection, str, int]]): The
                connection to detach from, given as a connection object or its id.
                When omitted, every connection of the pool is targeted.

        Raises:
            ValueError: If the provided event is not supported.
        """

        self._validate_connection_event(event)

        connections = self._resolve_connections(connection)

        if not connections and connection is not None:
            logging.warning(f"Connection {connection} not connected.")
            return

        for target in connections:
            registered = target.connection_callback_map.get(event)
            if not registered:
                continue

            if callback is None:
                registered.clear()
                continue

            while callback in registered:
                registered.remove(callback)

    @staticmethod
    def _validate_connection_event(event: str) -> None:
        """Validate that a connection-level event name is supported.

        Args:
            event (str): The connection event name to validate.

        Raises:
            ValueError: If the provided event is not supported.
        """

        if event not in SUPPORTED_CONNECTION_EVENTS:
            raise ValueError(
                f"Unsupported connection event: {event}. "
                f"Supported connection events are: {SUPPORTED_CONNECTION_EVENTS}"
            )

    def _emit_connection_event(
        self,
        connection: WebSocketConnection,
        event: str,
        *args,
    ) -> None:
        """Invoke callbacks registered for a connection-level event.

        Args:
            connection (WebSocketConnection): The target WebSocket connection.
            event (str): The connection event name to emit, such as `open`,
                `close`, `error`, `ping`, or `pong`.
            *args: Positional arguments passed to each registered callback.
        """

        callbacks = connection.connection_callback_map.get(event, [])
        for callback in list(callbacks):
            self._invoke_connection_callback(connection, event, callback, *args)

    def _invoke_connection_callback(
        self,
        connection: WebSocketConnection,
        event: str,
        callback: Callable[..., None],
        *args,
    ) -> None:
        """Invoke a single connection-level callback, isolating its failures.

        Args:
            connection (WebSocketConnection): The target WebSocket connection.
            event (str): The connection event name being emitted.
            callback (Callable[..., None]): Callback to invoke.
            *args: Positional arguments passed to the callback.
        """

        if args:
            try:
                parameters = inspect.signature(callback).parameters.values()
            except (TypeError, ValueError):
                parameters = None

            if parameters is not None:
                accepted = 0
                for parameter in parameters:
                    if parameter.kind is inspect.Parameter.VAR_POSITIONAL:
                        accepted = len(args)
                        break
                    if parameter.kind in (
                        inspect.Parameter.POSITIONAL_ONLY,
                        inspect.Parameter.POSITIONAL_OR_KEYWORD,
                    ):
                        accepted += 1

                args = args[:accepted]

        try:
            result = callback(*args)
            if asyncio.iscoroutine(result):
                asyncio.ensure_future(result)
        except Exception as e:
            logging.error(
                f"Error in '{event}' connection callback for WebSocket "
                f"{connection.id}: {e}"
            )

    async def schedule_reconnect(
        self,
        connection: WebSocketConnection,
        configuration: Union[ConfigurationWebSocketAPI, ConfigurationWebSocketStreams],
        delay: int,
        close_old_connection: bool = True,
    ):
        """Schedule a reconnect attempt after a delay.

        Args:
            connection (WebSocketConnection): WebSocket connection object.
            configuration (Union[ConfigurationWebSocketAPI, ConfigurationWebSocketStreams]): Configuration object.
            delay (int): Delay in seconds. Use `0` to reconnect immediately;
                :meth:`reconnect` may also be called directly for that.
            close_old_connection (bool): Whether to close the old connection before reconnecting.
        """

        if delay:
            await asyncio.sleep(delay)

        if connection.close_initiated:
            logging.debug(
                f"Skipping reconnect for WebSocket {connection.id}: "
                f"closed by the user."
            )
            return

        if connection not in self.connections:
            logging.debug(
                f"Skipping reconnect for WebSocket {connection.id}: "
                f"no longer in the connection pool."
            )
            return

        if connection.id in self.reconnect_tasks:
            logging.debug(
                f"Skipping reconnect for WebSocket {connection.id}: "
                f"a reconnect is already in flight."
            )
            return

        await self.reconnect(connection, configuration, close_old_connection)

    async def reconnect(
        self,
        connection: WebSocketConnection,
        configuration: Union[ConfigurationWebSocketAPI, ConfigurationWebSocketStreams],
        close_old_connection: bool = True,
    ):
        """Reconnect to the WebSocket server, replacing a connection in place.

        Args:
            connection (WebSocketConnection): WebSocket connection object.
            configuration (Union[ConfigurationWebSocketAPI, ConfigurationWebSocketStreams]): Configuration object.
            close_old_connection (bool): Whether to close the old connection before reconnecting.

        Returns:
            Optional[WebSocketConnection]: The replacement connection, or None
                when every attempt failed.
        """

        connection.cancel_scheduled_reconnect()

        if connection.id not in self.reconnect_tasks:
            self.reconnect_tasks.append(connection.id)

        try:
            if close_old_connection:
                connection.reconnect = True

            if connection.is_session_log_on:
                await WebSocketCommon.send_message(
                    self,
                    {
                        "method": self.user_data_endpoints.user_data_stream_logout,
                        "params": {},
                        "id": get_uuid(),
                    },
                    connection,
                )
                await asyncio.sleep(1)
                connection.is_session_log_on = False

            if len(connection.pending_request) > 0:
                connection.pending_request.clear()

            connection.is_being_replaced = True

            if close_old_connection:
                await self.close_connection(connection, False)

            self._emit_reconnect_event(connection)

            max_attempts = min(
                getattr(configuration, "reconnect_attempts", None)
                or DEFAULT_RECONNECT_ATTEMPTS,
                MAX_RECONNECT_ATTEMPTS,
            )
            delay = (configuration.reconnect_delay or 0) / 1000
            attempt = 0
            error = None
            new_connection = None

            while attempt < max_attempts:
                attempt += 1

                if delay:
                    await asyncio.sleep(delay)

                if connection.close_initiated:
                    logging.info(
                        f"Reconnect for WebSocket {connection.id} abandoned: "
                        f"closed by the user."
                    )
                    connection.reconnect = False
                    connection.is_being_replaced = False
                    self._emit_close_event(connection)
                    return None

                error = None
                try:
                    await self.init_connection(
                        configuration.stream_url,
                        configuration,
                        connection.url_path,
                        connection.id,
                    )
                    new_connection = next(
                        (
                            c
                            for c in self.connections
                            if c.id == connection.id and c is not connection
                        ),
                        None,
                    )
                    if new_connection is not None:
                        break
                    error = ConnectionError(
                        f"Reconnect failed: no new connection established for "
                        f"WebSocket {connection.id}"
                    )
                except Exception as e:
                    error = e

                logging.error(
                    f"Reconnect attempt {attempt}/{max_attempts} failed for "
                    f"WebSocket {connection.id}: {error}"
                )

            if new_connection is None:
                if connection.id in self.reconnect_tasks:
                    self.reconnect_tasks.remove(connection.id)

                connection.reconnect = False
                connection.is_being_replaced = False
                connection.cancel_scheduled_reconnect()

                self._emit_connection_event(connection, "error", error)
                self._emit_close_event(connection)

                if connection in self.connections:
                    self.connections.remove(connection)
                    logging.info(
                        f"WebSocket {connection.id} removed from the connection "
                        f"pool after a failed reconnect."
                    )

                _forget_connection_streams(connection)
                return None

            if connection.session_logon_request and self.configuration.session_re_logon:
                await self.session_re_log_on(
                    connection.session_logon_request, new_connection
                )
                await asyncio.sleep(1)
                await self._resubscribe_user_streams(connection, new_connection)

            if connection.connection_callback_map:
                new_connection.connection_callback_map = defaultdict(
                    list,
                    {event: callbacks.copy() for event, callbacks in connection.connection_callback_map.items()}
                )

            await self._resubscribe_global_streams(connection, new_connection)
            self._emit_connection_event(new_connection, "open")
        finally:
            if connection.id in self.reconnect_tasks:
                self.reconnect_tasks.remove(connection.id)

        connection.reconnect = False
        logging.info(f"Reconnected WebSocket {connection.id}")
        return new_connection

    async def _resubscribe_user_streams(
        self, old_connection: WebSocketConnection, new_connection: WebSocketConnection
    ):
        """Resubscribe all user streams from old_connection to new_connection.

        Args:
            old_connection (WebSocketConnection): The old WebSocket connection.
            new_connection (WebSocketConnection): The new WebSocket connection.
        """
        for stream, old_target in old_connection.stream_callback_map.items():
            if stream not in global_user_stream_connections.stream_connections_map:
                continue

            json_msg = {
                "method": self.user_data_endpoints.user_data_stream_subscribe,
                "params": {},
                "id": old_connection.id,
            }
            await WebSocketCommon.send_message(self, json_msg, new_connection)

            global_user_stream_connections.stream_connections_map[stream] = (
                new_connection
            )
            new_connection.stream_callback_map[stream] = old_target
            new_connection.response_types[stream] = old_connection.response_types.get(
                stream
            )

    async def _resubscribe_global_streams(
        self, old_connection: WebSocketConnection, new_connection: WebSocketConnection
    ):
        """Resubscribe all global streams from old_connection to new_connection.

        Args:
            old_connection (WebSocketConnection): The old WebSocket connection.
            new_connection (WebSocketConnection): The new WebSocket connection.
        """

        streams = [
            stream
            for stream, conn in list(
                global_stream_connections.stream_connections_map.items()
            )
            if conn == old_connection and isinstance(stream, str)
        ]

        if not streams:
            return

        json_msg = {
            "method": "SUBSCRIBE",
            "params": streams,
            "id": (
                get_random_int() if getattr(self, "id_strict_int", False) else get_uuid()
            ),
        }
        await self.send_message(json_msg, new_connection)

        for stream in streams:
            global_stream_connections.stream_connections_map[stream] = new_connection
            new_connection.stream_callback_map[stream] = (
                old_connection.stream_callback_map.get(stream)
            )
            new_connection.response_types[stream] = old_connection.response_types.get(
                stream
            )

    async def session_re_log_on(self, request, connection: WebSocketConnection):
        """Re-logon the session.
        Args:
            connection (WebSocketConnection): WebSocket connection object.
        """

        if request and not connection.is_session_log_on:
            data = {
                "method": request["method"],
                "params": request["params"],
                "id": request["id"],
            }
            signer = Signers.get_signer(
                self.configuration.private_key,
                self.configuration.private_key_passphrase,
            )
            websocket_options = WebsocketApiOptions(
                signer=signer, api_key=False, is_signed=True, skip_auth=True
            )
            payload = ws_api_payload(self.configuration, data, websocket_options)

            try:
                await WebSocketCommon.send_message(self, payload, connection)
                connection.is_session_log_on = True
            except Exception as e:
                logging.error(
                    f"Session re-logon failed for connection {connection.id}: {e}"
                )

    async def close_connection(
        self,
        connection: Optional[WebSocketConnection] = None,
        close_session: bool = True,
    ):
        """Close the WebSocket connection.

        Args:
            connection (Optional[WebSocketConnection]): WebSocket connection object to close.
            close_session (bool): Whether to close the aiohttp session.
        """

        if len(self.connections) == 0:
            logging.warning("No WebSocket connections to close.")
        elif connection:
            await self._close_one(connection)
        else:
            for pooled_connection in self.connections[:]:
                await self._close_one(pooled_connection)

        if close_session and self.session is not None:
            await self.session.close()
            self.session = None

    async def _close_one(self, connection: WebSocketConnection) -> None:
        """Close a single connection and stop its background tasks.

        Args:
            connection (WebSocketConnection): The connection to close.
        """

        user_initiated = not (connection.reconnect or connection.is_being_replaced)

        try:
            if user_initiated:
                connection.close_initiated = True
            connection.cancel_scheduled_reconnect()

            await connection.websocket.close()
            logging.info(f"WebSocket {connection.id} closed.")
            if connection in self.connections:
                self.connections.remove(connection)
        except Exception as e:
            logging.error(f"Error closing WebSocket {connection.id}: {e}")

        if user_initiated:
            _forget_connection_streams(connection)


class WebSocketStreamBase(WebSocketCommon):
    def __init__(
        self,
        configuration: ConfigurationWebSocketStreams,
        id_strict_int: Optional[bool] = False,
        url_paths: Optional[str] = None,
    ):
        """Initialize the WebSocketStreamBase class.

        Args:
            configuration (ConfigurationWebSocketStreams): Configuration object.
            id_strict_int (Optional[bool]): Whether to use strict integer IDs.
            url_paths (Optional[str]): URL paths for the WebSocket connection.
        """

        if configuration.stream_url and not configuration.stream_url.endswith("stream"):
            configuration.stream_url = configuration.stream_url + "/stream"
        super().__init__(configuration)
        self.configuration = configuration
        self.id_strict_int = id_strict_int
        self.url_paths = url_paths

    async def create_connection(self):
        """Create a WebSocket connection.

        Returns:
            WebSocketConnection: The created WebSocket connection.
        """

        return await self.connect(
            self.configuration.stream_url, self.configuration, url_paths=self.url_paths
        )

    async def subscribe(
        self,
        streams: list[str],
        response_model: Optional[Type[T]] = None,
        stream_url: Optional[str] = None,
    ):
        """Subscribe to a list of streams.

        Args:
            streams (list[str]): List of streams to subscribe to.
            response_model (Optional[Type[T]]): Model used to parse the payloads.
            stream_url (Optional[str]): URL path for the subscription
        """

        if not streams:
            logging.warning("No streams to subscribe to.")
            return

        if isinstance(streams, str):
            streams = [streams]

        if len(self.connections) == 0 and len(self.reconnect_tasks) == 0:
            await self.close_connection(close_session=True)
            raise ValueError("No WebSocket connections available.")

        if not any(not connection.reconnect for connection in self.connections):
            logging.warning("No available WebSocket connections for subscription.")
            return

        streams = [
            stream
            for stream in streams
            if stream not in global_stream_connections.stream_connections_map
        ]

        grouped = self._group_streams_by_connection(streams, stream_url)

        for connection, connection_streams in grouped:
            logging.info(
                f"Subscribing to streams on WebSocket {connection.id}: "
                f"{connection_streams}"
            )
            json_msg = {
                "method": "SUBSCRIBE",
                "params": connection_streams,
                "id": get_random_int() if self.id_strict_int else get_uuid(),
            }
            await asyncio.sleep(SUBSCRIBE_MESSAGE_DELAY_SECONDS)
            await self.send_message(json_msg, connection)

            for stream in connection_streams:
                global_stream_connections.stream_connections_map[stream] = connection
                connection.stream_callback_map.update({stream: []})
                connection.response_types.update({stream: response_model})

    def _group_streams_by_connection(
        self,
        streams: list[str],
        stream_url: Optional[str] = None,
    ) -> list[tuple[WebSocketConnection, list[str]]]:
        """Assign streams to connections, grouped so each is sent one message.

        Args:
            streams (list[str]): The streams to assign.
            stream_url (Optional[str]): Only consider connections serving this
                URL path.

        Returns:
            list[tuple[WebSocketConnection, list[str]]]: Each target connection
                with the streams assigned to it, in assignment order.
        """

        if stream_url:
            candidates = [c for c in self.connections if c.url_path == stream_url]
        else:
            candidates = list(self.connections)

        if not candidates:
            logging.warning(f"No matching connection found for streams: {streams}")
            return []

        grouped: dict[Union[str, int], tuple[WebSocketConnection, list[str]]] = {}

        for stream in streams:
            if self.configuration.mode == WebsocketMode.SINGLE:
                connection = candidates[0]
            else:
                connection = candidates[self.round_robin_index % len(candidates)]
                self.round_robin_index = (self.round_robin_index + 1) % len(candidates)

            grouped.setdefault(connection.id, (connection, []))[1].append(stream)

        return list(grouped.values())

    def on(self, event: str, callback: Callable[[T], None], stream: str) -> None:
        """Set the callback function for incoming messages on a specific stream.

        Args:
            event (str): Event type.
            callback (Callable): Callback function.
            stream (str): Stream name.
        """

        if event != "message":
            raise ValueError(f"Unsupported event: {event}")
        connection = (
            global_stream_connections.stream_connections_map[stream]
            if stream in global_stream_connections.stream_connections_map
            else None
        )

        if connection:
            connection.stream_callback_map[stream].append(callback)
        else:
            logging.warning(f"Stream {stream} not connected.")

    async def unsubscribe(self, streams: list[str]):
        """Unsubscribe from a list of streams.

        Args:
            streams (list[str]): List of streams to unsubscribe from.
        """

        if not streams:
            logging.warning("No streams to unsubscribe to.")
            return

        if self.connections is None or len(self.connections) == 0:
            logging.warning("No WebSocket connections available for unsubscription.")
            return

        if isinstance(streams, str):
            streams = [streams]

        missing_stream = [
            stream
            for stream in streams
            if stream not in global_stream_connections.stream_connections_map
        ]

        if missing_stream:
            logging.warning(f"Stream {missing_stream} is not subscribed.")
            return

        grouped: dict[Union[str, int], tuple[WebSocketConnection, list[str]]] = {}
        for stream in streams:
            connection = global_stream_connections.stream_connections_map.get(stream)
            if connection is None:
                raise ValueError(f"Stream {stream} not connected.")
            grouped.setdefault(connection.id, (connection, []))[1].append(stream)

        for connection, connection_streams in grouped.values():
            json_msg = json.dumps(
                {
                    "method": "UNSUBSCRIBE",
                    "params": connection_streams,
                    "id": get_random_int() if self.id_strict_int else get_uuid(),
                }
            )
            await connection.websocket.send_str(json_msg)

            logging.info(
                f"Unsubscribed from streams on WebSocket {connection.id}: "
                f"{connection_streams}"
            )
            for stream in connection_streams:
                global_stream_connections.stream_connections_map.pop(stream, None)
                connection.stream_callback_map.pop(stream, None)
                connection.response_types.pop(stream, None)

    async def list_subscribe(self) -> dict:
        """List all subscriptions.

        Returns:
            dict: Current subscriptions.
        """

        for connection in self.connections:
            json_msg = {"method": "LIST_SUBSCRIPTIONS", "id": get_uuid()}
            future = await self.send_message(json_msg, connection)
            try:
                response = await asyncio.wait_for(future, timeout=20)
                logging.info(f"Current subscriptions: {response}")
                return response
            except asyncio.TimeoutError:
                logging.warning(
                    f"Timeout waiting for response to LIST_SUBSCRIPTIONS for connection {connection.id}"
                )

    async def ping_ws_stream(self, connection: WebSocketConnection):
        """Send a ping message to the WebSocket server.

        Args:
            connection (WebSocketConnection): WebSocket connection object.
        """

        await super().ping(connection)


class WebSocketAPIBase(WebSocketCommon):
    def __init__(
        self,
        configuration: ConfigurationWebSocketAPI,
        user_data_endpoints: Optional[WebsocketApiUserDataEndpoints] = None,
    ):
        super().__init__(configuration, user_data_endpoints)
        self.configuration = configuration

    async def create_connection(self):
        return await self.connect(self.configuration.stream_url, self.configuration)

    async def send_signed_message(
        self,
        payload: Dict,
        signer: Optional[Signers] = None,
        promised: bool = True,
        response_model: Optional[Type[T]] = None,
        api_key: Optional[bool] = False,
        session_logon: Optional[bool] = False,
        session_logout: Optional[bool] = False,
    ) -> WebsocketApiResponse[T]:
        """Send a message to the WebSocket server.

        Args:
            payload (Dict): Payload to send.
            promised (bool): Whether the response is promised.
            response_model (Optional[Type[T]]): Response model.
            api_key (Optional[bool]): Whether to include the API key in the request.
            session_logon (Optional[bool]): Whether the message is for session logon.
            session_logout (Optional[bool]): Whether the message is for session logout.
        Returns:
            WebsocketApiResponse[T]: Response from the server.
        """

        if len(self.connections) == 0 and len(self.reconnect_tasks) == 0:
            await self.close_connection(close_session=True)
            raise ValueError("No WebSocket connections available.")

        if not any(not connection.reconnect for connection in self.connections):
            logging.warning("WebSocket Connection Reconnecting")
            return WebsocketApiResponse(
                data_function=lambda: "Websocket Reconnect", rate_limits=[]
            )

        if self.configuration.mode == WebsocketMode.SINGLE:
            connection = self.connections[0]
        else:
            connection = self.connections[
                self.round_robin_index % len(self.connections)
            ]
            self.round_robin_index = (self.round_robin_index + 1) % len(
                self.connections
            )

        skip_auth = False if session_logon else connection.is_session_log_on is True
        websocket_options = WebsocketApiOptions(
            signer=signer, api_key=api_key, is_signed=True, skip_auth=skip_auth
        )

        if not self.configuration.return_rate_limits:
            if "params" in payload:
                payload["params"].update({"returnRateLimits": False})
            else:
                payload["params"] = {"returnRateLimits": False}

        _payload = ws_api_payload(self.configuration, payload, websocket_options)

        future = await super().send_message(_payload, connection)
        if promised:
            try:
                ws_response = await asyncio.wait_for(future, timeout=20)
                if session_logon:
                    payload["id"] = _payload["id"]
                    connection.is_session_log_on = True
                    connection.session_logon_request = payload

                return WebsocketApiResponse[T](
                    data_function=lambda: (
                        response_model.model_validate(ws_response)
                        if response_model
                        else ws_response
                    ),
                    rate_limits=(
                        parse_ws_rate_limit_headers(ws_response["rateLimits"])
                        if self.configuration.return_rate_limits
                        else []
                    ),
                )
            except asyncio.TimeoutError:
                logging.warning(
                    f"Timeout waiting for response to message ID {payload.get('id')}"
                )
                return WebsocketApiResponse[T](
                    data_function=lambda: {"error": "timeout"},
                    rate_limits=[],
                )
            except Exception as e:
                logging.warning(f"Connection with user closed: {e}")
                error_message = e.args[0] if e.args else str(e)

                return WebsocketApiResponse[T](
                    data_function=lambda: {"error": error_message},
                    rate_limits=[],
                )

    async def send_message(
        self,
        payload: Dict,
        promised: bool = True,
        response_model: Optional[Type[T]] = None,
        api_key: Optional[bool] = False,
        session_logon: Optional[bool] = None,
        session_logout: Optional[bool] = None,
    ) -> WebsocketApiResponse[T]:
        """Send a message to the WebSocket server.

        Args:
            payload (Dict): Payload to send.
            promised (bool): Whether the response is promised.
            response_model (Type[T]): Response model.
            api_key (Optional[bool]): Whether to include the API key in the request.
            session_logon (Optional[bool]): Whether the message is for session logon.
            session_logout (Optional[bool]): Whether the message is for session logout.
        Returns:
            WebsocketApiResponse[T]: Response from the server.
        """

        if len(self.connections) == 0 and len(self.reconnect_tasks) == 0:
            await self.close_connection(close_session=True)
            raise ValueError("No WebSocket connections available.")

        if not any(not connection.reconnect for connection in self.connections):
            logging.warning("WebSocket Connection Reconnecting")
            return WebsocketApiResponse(
                data_function=lambda: "Websocket Reconnect", rate_limits=[]
            )

        if self.configuration.mode == WebsocketMode.SINGLE:
            connection = self.connections[0]
        else:
            connection = self.connections[
                self.round_robin_index % len(self.connections)
            ]
            self.round_robin_index = (self.round_robin_index + 1) % len(
                self.connections
            )

        skip_auth = False if session_logon else connection.is_session_log_on is True

        websocket_options = WebsocketApiOptions(
            api_key=api_key, is_signed=False, skip_auth=skip_auth
        )

        if not self.configuration.return_rate_limits:
            if "params" in payload:
                payload["params"].update({"returnRateLimits": False})
            else:
                payload["params"] = {"returnRateLimits": False}

        _payload = ws_api_payload(self.configuration, payload, websocket_options)

        future = await super().send_message(_payload, connection)
        if promised:
            try:
                ws_response = await asyncio.wait_for(future, timeout=20)

                if session_logon:
                    payload["id"] = _payload["id"]
                    connection.is_session_log_on = True
                    connection.session_logon_request = payload

                if response_model and hasattr(response_model, "from_dict"):
                    def data_function():
                        try:
                            return response_model.from_dict(ws_response)
                        except Exception:
                            if self.is_one_of_model(response_model):
                                raise
                            return response_model.model_validate(ws_response)

                elif response_model:

                    def data_function():
                        return response_model.model_validate(ws_response)

                else:

                    def data_function():
                        return ws_response

                return WebsocketApiResponse[T](
                    data_function=data_function,
                    rate_limits=(
                        parse_ws_rate_limit_headers(ws_response["rateLimits"])
                        if self.configuration.return_rate_limits
                        else []
                    ),
                )
            except asyncio.TimeoutError:
                logging.warning(
                    f"Timeout waiting for response to message ID {payload.get('id')}"
                )
                return WebsocketApiResponse[T](
                    data_function=lambda: {"error": "timeout"},
                    rate_limits=[],
                )
            except Exception as e:
                logging.warning(f"Connection with user closed: {e}")
                error_message = e.args[0] if e.args else str(e)

                return WebsocketApiResponse[T](
                    data_function=lambda: {"error": error_message},
                    rate_limits=[],
                )

    def is_one_of_model(self, model_cls: Type[T]) -> bool:
        """Check if the model is a oneof model.

        Args:
            model_cls (Type[T]): Model class to check.
        Returns:
            bool: True if the model is a oneof model, False otherwise.
        """

        return hasattr(model_cls, "is_oneof_model") and model_cls.is_oneof_model()

    async def ping_ws_api(self, connection: WebSocketConnection):
        """Send a ping message to the WebSocket server.

        Args:
            connection (WebSocketConnection): WebSocket connection object.
        """

        await super().ping(connection)

    async def subscribe_user_data(
        self, id: str, response_model: Optional[Type[T]] = None
    ):
        """Subscribe to user data updates for a specific user.

        Args:
            id (str): User Data ID.
            response_model (Optional[Type[T]]): Pydantic model to validate the response data.
        """
        if self.configuration.mode == WebsocketMode.SINGLE:
            connection = self.connections[0]
        else:
            connection = self.connections[
                self.round_robin_index % len(self.connections)
            ]
            self.round_robin_index = (self.round_robin_index + 1) % len(
                self.connections
            )
        global_user_stream_connections.stream_connections_map[id] = connection
        connection.stream_callback_map.update({id: []})
        connection.response_types.update({id: response_model})

    def on(self, event: str, callback: Callable[[T], None], id: str) -> None:
        """Set the callback function for incoming messages on a specific ID.

        Args:
            event (str): Event type.
            callback (Callable): Callback function.
            id (str): User Data ID.
        """

        if event != "message":
            raise ValueError(f"Unsupported event: {event}")

        connection = (
            global_user_stream_connections.stream_connections_map[id]
            if id in global_user_stream_connections.stream_connections_map
            else None
        )

        if connection:
            connection.stream_callback_map[id].append(callback)
        else:
            logging.warning(f"Stream {id} not connected.")

    async def unsubscribe(self, id: str):
        """Unsubscribe from a user data ID.

        Args:
            id (str): user data ID to unsubscribe from.
        """

        if self.connections is None or len(self.connections) == 0:
            logging.warning("No user data connections available for unsubscription.")
            return

        if id not in global_user_stream_connections.stream_connections_map:
            logging.warning(f"Stream {id} is not subscribed.")
            return

        connection = (
            global_user_stream_connections.stream_connections_map[id]
            if id in global_user_stream_connections.stream_connections_map
            else None
        )
        if connection:
            global_user_stream_connections.stream_connections_map.pop(id, None)
            connection.stream_callback_map.pop(id, None)
            connection.response_types.pop(id, None)
            logging.info(f"Unsubscribed from stream: {id}")
        else:
            raise ValueError(f"Subscription id {id} not connected.")


class RequestStreamHandle(Generic[T]):
    """A wrapper for Request Stream Method.

    :param websocket_base: WebSocket base.
    :param stream: Stream name.
    :param response_model: The Pydantic model to validate the response data.
    """

    def __init__(
        self,
        websocket_base: WebSocketStreamBase or WebSocketAPIBase,
        stream: str,
        response_model: Optional[Type[T]] = None,
    ):
        self._websocket_base = websocket_base
        self._stream = stream
        self._response_model = response_model

    async def unsubscribe(self) -> None:
        if isinstance(self._websocket_base, WebSocketStreamBase):
            await self._websocket_base.unsubscribe(streams=self._stream)
        else:
            await self._websocket_base.unsubscribe(id=self._stream)

    def on(self, event: str, callback: Callable[[T], None]) -> None:
        """Register a callback for the stream's response payloads.

        Args:
            event (str): The stream event to listen for. Only `message` is
                supported. Connection events such as `error` are not stream
                events: register them on the client with `on_connection()`.
            callback (Callable[[T], None]): Callback invoked for each message.

        Raises:
            ValueError: If the provided event is not supported.
        """

        supported_events = {"message"}
        if event not in supported_events:
            raise ValueError(
                f"Unsupported stream event: {event}. "
                f"Supported stream events are: {supported_events}. "
                f"Connection events belong to the connection, not to a stream: "
                f"register {SUPPORTED_CONNECTION_EVENTS} with "
                f"client.on_connection()."
            )
        self._websocket_base.on(event, callback, self._stream)


async def RequestStream(
    websocket_base: WebSocketStreamBase or WebSocketAPIBase,
    stream: str,
    response_model: Optional[Type[T]] = None,
    stream_url: Optional[str] = None,
) -> RequestStreamHandle[T]:
    """Decorator to create a request stream for a specific stream.

    Args:
        websocket_base (WebSocketStreamBase or WebSocketAPIBase): WebSocket base.
        stream (str): Stream name.
        response_model (Type[T], optional): Response model for the stream.
    """

    if isinstance(websocket_base, WebSocketStreamBase):
        await websocket_base.subscribe(
            streams=[stream], response_model=response_model, stream_url=stream_url
        )
    else:
        await websocket_base.subscribe_user_data(
            id=stream, response_model=response_model
        )

    return RequestStreamHandle(websocket_base, stream, response_model)
