import aiohttp
import asyncio
import json
import logging
import platform

from pydantic import BaseModel
from typing import Callable, Optional, Dict, Generic, Union, TypeVar, Type
from types import SimpleNamespace
from urllib.parse import urlencode

from binance_common.configuration import (
    ConfigurationWebSocketAPI,
    ConfigurationWebSocketStreams,
)
from binance_common.constants import WebsocketMode
from binance_common.models import WebsocketApiResponse, WebsocketApiOptions, WebsocketApiUserDataEndpoints
from binance_common.signature import Signers
from binance_common.utils import (
    get_signature,
    get_timestamp,
    get_uuid,
    make_serializable,
    parse_proxies,
    parse_user_event,
    parse_ws_rate_limit_headers,
    snake_to_camel,
    ws_api_payload,
)

T = TypeVar("T", bound=BaseModel)


class StreamConnectionsMap:
    def __init__(self):
        self.stream_connections_map: dict[Union[str, int], WebSocketConnection] = {}


global_stream_connections = StreamConnectionsMap()
global_user_stream_connections = StreamConnectionsMap()


class WebSocketConnection:
    """Represents a WebSocket connection.

    Attributes:
        id (str): Unique identifier for the WebSocket connection.
        pending_request (dict): Dictionary to hold pending requests.
        stream_callback_map (dict): Map of stream names to their callback functions.
        response_types (dict): Map of stream names to their response types.
        ws_type (str): Type of WebSocket connection (API or Stream).
        websocket (aiohttp.ClientWebSocketResponse): The WebSocket response object.
    """

    def __init__(
        self, websocket: aiohttp.ClientWebSocketResponse, id: str, ws_type: str
    ):
        self.id = id
        self.pending_request = {}
        self.stream_callback_map = {}
        self.response_types = {}
        self.ws_type = ws_type
        self.websocket = websocket
        self.reconnect = False
        self.is_session_log_on = False
        self.session_logon_request = None


class WebSocketCommon:
    def __init__(
        self,
        configuration: Union[ConfigurationWebSocketAPI, ConfigurationWebSocketStreams],
        user_data_endpoints: Optional[WebsocketApiUserDataEndpoints] = None
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
        ws_id: str = None,
    ):
        """Connect to the Binance WebSocket server.

        Args:
            url (str): WebSocket URL.
            configuration (Union[ConfigurationWebSocketAPI, ConfigurationWebSocketStreams]): Configuration object.
            ws_id (str): Optional WebSocket ID for the connection.
        """

        try:
            if self.session is None:
                self.session = aiohttp.ClientSession()
            if configuration.mode == WebsocketMode.POOL:
                for i in range(configuration.pool_size):
                    await self.init_connection(url, configuration, ws_id)
            else:
                await self.init_connection(url, configuration, ws_id)
            return self
        except Exception as e:
            logging.error(f"WebSocket failed to connect: {e}")

    async def init_connection(
        self,
        url,
        configuration: Union[ConfigurationWebSocketAPI, ConfigurationWebSocketStreams],
        ws_id: str = None,
    ):
        """Initialize a WebSocket connection.

        Args:
            url (str): WebSocket URL.
            configuration (Union[ConfigurationWebSocketAPI, ConfigurationWebSocketStreams]): Configuration object.
            ws_id (str): Optional WebSocket ID for the connection.
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

        if type(configuration).__name__ == "ConfigurationWebSocketAPI":
            websocket = await self.session.ws_connect(
                url,
                compress=configuration.compression,
                headers={"User-Agent": user_agent},
                max_msg_size=20 * 1024 * 1024,
                proxy=proxy,
                ssl=configuration.https_agent,
                timeout=configuration.timeout,
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
            )
            id = ws_id if ws_id else get_uuid()

        logging.info(f"Establishing Websocket connection with id {id} to: {url}")
        connection = WebSocketConnection(websocket, id, type(configuration).__name__)

        self.connections.append(connection)

        asyncio.create_task(self.schedule_reconnect(connection, configuration, 23 * 3600))
        asyncio.create_task(self.receive_loop(connection))

    async def receive_loop(self, connection: WebSocketConnection):
        """Continuously receive messages from the WebSocket server.

        Args:
            connection (WebSocketConnection): WebSocket connection object.
        """

        async for msg in connection.websocket:
            if msg.type == aiohttp.WSMsgType.TEXT:
                data = json.loads(msg.data)

                request_id = data.get("id")
                if request_id and request_id in connection.pending_request:
                    future = connection.pending_request.pop(request_id)
                    if data.get("error"):
                        future.set_exception(
                            ValueError(f"Error received from server: {data['error']}")
                        )
                    else:
                        future.set_result(data)
                else:
                    if data.get("error"):
                        raise ValueError(f"Error received from server: {data['error']}")

                    stream = data.get("stream")
                    subscription_id = data.get("subscriptionId")

                    key = stream or subscription_id
                    callbacks = connection.stream_callback_map.get(key) if key is not None else None

                    if callbacks:
                        try:
                            if stream:
                                response_model = connection.response_types.get(stream)
                                payload = data["data"] if response_model else data

                                for callback in callbacks:
                                    if response_model:
                                        if response_model.__pydantic_fields__.get("one_of_schemas"):
                                            parsed = payload
                                        elif isinstance(payload, list):
                                            parsed = [
                                                response_model.model_validate_json(json.dumps(item))
                                                for item in payload
                                            ]
                                        else:
                                            parsed = response_model.model_validate_json(json.dumps(payload))
                                        callback(parsed)
                                    else:
                                        callback(payload)
                            else:
                                response_model = connection.response_types.get(subscription_id)
                                payload = data["event"]

                                for callback in callbacks:
                                    if response_model:
                                        if isinstance(payload, list):
                                            parsed = [parse_user_event(item, response_model) for item in payload]
                                        else:
                                            parsed = parse_user_event(payload, response_model)
                                        callback(parsed)
                                    else:
                                        callback(payload)
                        except Exception as e:
                            raise ValueError(f"Error in callback for key {key}: {e}")
                    else:
                        logging.info(f"Received message: {data}")
            elif msg.type == aiohttp.WSMsgType.PING:
                logging.info("Received PING from server")
                await connection.websocket.pong()
            elif msg.type == aiohttp.WSMsgType.PONG:
                logging.info("Received PONG from server")
            elif msg.type == aiohttp.WSMsgType.ERROR:
                logging.error("Received error from server")
                logging.error(connection.websocket.exception())
                break
            elif msg.type == aiohttp.WSMsgType.CLOSE:
                logging.info("WebSocket closed")
                break

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

        logging.info(f"Sending message to WebSocket {connection.id}: {payload}")
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

    async def schedule_reconnect(
        self,
        connection: WebSocketConnection,
        configuration: Union[ConfigurationWebSocketAPI, ConfigurationWebSocketStreams],
        delay: int,
    ):
        """Schedule a reconnect attempt after a delay.

        Args:
            connection (WebSocketConnection): WebSocket connection object.
            configuration (Union[ConfigurationWebSocketAPI, ConfigurationWebSocketStreams]): Configuration object.
            delay (int): Delay in seconds.
        """

        await asyncio.sleep(delay)
        connection.reconnect = True
        if connection.is_session_log_on:
            await WebSocketCommon.send_message(
                self,
                {
                    'method': self.user_data_endpoints.user_data_stream_logout,
                    'params': {},
                    'id': get_uuid()
                },
                connection
            )
            await asyncio.sleep(1)
            connection.is_session_log_on = False
        self.reconnect_tasks.append(connection.id)
        await self.reconnect(connection, configuration)

    async def reconnect(
        self,
        connection: WebSocketConnection,
        configuration: Union[ConfigurationWebSocketAPI, ConfigurationWebSocketStreams],
    ):
        """Reconnect to the WebSocket server.

        Args:
            connection (WebSocketConnection): WebSocket connection object.
            configuration (Union[ConfigurationWebSocketAPI, ConfigurationWebSocketStreams]): Configuration object.
        """

        if len(connection.pending_request) > 0:
            connection.pending_request.clear()

        await self.close_connection(connection, False)
        if configuration.reconnect_delay:
            await asyncio.sleep(configuration.reconnect_delay)

        await self.connect(configuration.stream_url, configuration, connection.id)

        new_connection = next((c for c in self.connections if c.id == connection.id), None)
        if not new_connection:
            return

        if connection.session_logon_request and self.configuration.session_re_logon:
            await self.session_re_log_on(connection.session_logon_request, new_connection)
            await asyncio.sleep(1)
            await self._resubscribe_user_streams(connection, new_connection)

        await self._resubscribe_global_streams(connection, new_connection)

        self.reconnect_tasks.remove(connection.id)
        connection.reconnect = False


    async def _resubscribe_user_streams(self, old_connection: WebSocketConnection, new_connection: WebSocketConnection):
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

            global_user_stream_connections.stream_connections_map[stream] = new_connection
            new_connection.stream_callback_map[stream] = old_target
            new_connection.response_types[stream] = old_connection.response_types.get(stream)


    async def _resubscribe_global_streams(self, old_connection: WebSocketConnection, new_connection: WebSocketConnection):
        """Resubscribe all global streams from old_connection to new_connection.

        Args:
            old_connection (WebSocketConnection): The old WebSocket connection.
            new_connection (WebSocketConnection): The new WebSocket connection.
        """
        for stream, conn in list(global_stream_connections.stream_connections_map.items()):
            if conn != old_connection or not isinstance(stream, str):
                continue

            json_msg = {
                "method": "SUBSCRIBE",
                "params": [stream],
                "id": old_connection.id,
            }
            await self.send_message(json_msg, new_connection)
            global_stream_connections.stream_connections_map[stream] = new_connection

            new_connection.stream_callback_map[stream] = old_connection.stream_callback_map.get(stream)
            new_connection.response_types[stream] = old_connection.response_types.get(stream)


    async def session_re_log_on(self, request, connection: WebSocketConnection):
        """Re-logon the session.
        Args:
            connection (WebSocketConnection): WebSocket connection object.
        """

        if request and connection.is_session_log_on == False:
            data = {
                "method": request["method"],
                "params": request["params"],
                "id": request["id"],
            }
            signer = Signers.get_signer(
                self.configuration.private_key, self.configuration.private_key_passphrase
            )
            websocket_options = WebsocketApiOptions(
                signer=signer,
                api_key=False,
                is_signed=True,
                skip_auth=True
            )
            payload = ws_api_payload(
                self.configuration,
                data,
                websocket_options
            )

            try:
                await WebSocketCommon.send_message(self, payload, connection)
                connection.is_session_log_on = True
            except Exception as e:
                logging.error(f"Session re-logon failed for connection {connection.id}: {e}")

    async def close_connection(
        self, connection: WebSocketConnection = None, close_session: bool = True
    ):
        """Close the WebSocket connection.

        Args:
            connection (WebSocketConnection): WebSocket connection object to close.
            close_session (bool): Whether to close the aiohttp session.
        """

        if len(self.connections) == 0:
            logging.warning("No WebSocket connections to close.")
        elif connection:
            try:
                await connection.websocket.close()
                logging.info(f"WebSocket {connection.id} closed.")
                self.connections.remove(connection)
            except Exception as e:
                logging.error(f"Error closing WebSocket {connection.id}: {e}")
        else:
            for connection in self.connections[:]:
                try:
                    await connection.websocket.close()
                    logging.info(f"WebSocket {connection.id} closed.")
                    self.connections.remove(connection)
                except Exception as e:
                    logging.error(f"Error closing WebSocket {connection.id}: {e}")

        if close_session and self.session is not None:
            await self.session.close()
            self.session = None


class WebSocketStreamBase(WebSocketCommon):
    def __init__(self, configuration: ConfigurationWebSocketStreams):
        if not configuration.stream_url.endswith("stream"):
            configuration.stream_url = configuration.stream_url + "/stream"
        super().__init__(configuration)
        self.configuration = configuration

    async def create_connection(self):
        """Create a WebSocket connection.

        Returns:
            WebSocketConnection: The created WebSocket connection.
        """
        return await self.connect(self.configuration.stream_url, self.configuration)

    async def subscribe(self, streams: list[str], response_model: Type[T] = None):
        """Subscribe to a list of streams.

        Args:
            streams (list[str]): List of streams to subscribe to.
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

        for stream in streams:
            if self.configuration.mode == WebsocketMode.SINGLE:
                connection = self.connections[0]
            else:
                connection = self.connections[
                    self.round_robin_index % len(self.connections)
                ]
                self.round_robin_index = (self.round_robin_index + 1) % len(
                    self.connections
                )

            logging.info(f"Subscribing to streams: {streams}")
            json_msg = {"method": "SUBSCRIBE", "params": streams, "id": get_uuid()}
            await self.send_message(json_msg, connection)
            global_stream_connections.stream_connections_map[stream] = connection
            connection.stream_callback_map.update({stream: []})
            connection.response_types.update({stream: response_model})

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

        for stream in streams:
            connection = (
                global_stream_connections.stream_connections_map[stream]
                if stream in global_stream_connections.stream_connections_map
                else None
            )
            if connection:
                json_msg = json.dumps(
                    {"method": "UNSUBSCRIBE", "params": streams, "id": get_uuid()}
                )
                await connection.websocket.send_str(json_msg)

                logging.info(f"Unsubscribed from stream: {stream}")
                global_stream_connections.stream_connections_map.pop(stream, None)
                connection.stream_callback_map.pop(stream, None)
                connection.response_types.pop(stream, None)
            else:
                raise ValueError(f"Stream {stream} not connected.")

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
    def __init__(self, configuration: ConfigurationWebSocketAPI, user_data_endpoints: Optional[WebsocketApiUserDataEndpoints] = None):
        super().__init__(configuration, user_data_endpoints)
        self.configuration = configuration

    async def create_connection(self):
        return await self.connect(self.configuration.stream_url, self.configuration)

    async def send_signed_message(
        self,
        payload: Dict,
        signer: Optional[Signers] = None,
        promised: bool = True,
        response_model: Type[T] = None,
        api_key: Optional[bool] = False,
        session_logon: Optional[bool] = False,
        session_logout: Optional[bool] = False
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
            signer=signer,
            api_key=api_key,
            is_signed=True,
            skip_auth=skip_auth
        )
        _payload = ws_api_payload(
            self.configuration,
            payload,
            websocket_options
        )

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
                    rate_limits=parse_ws_rate_limit_headers(ws_response["rateLimits"]),
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
                error_message = str(e)

                return WebsocketApiResponse[T](
                    data_function=lambda: {"error": error_message},
                    rate_limits=[],
                )

    async def send_message(
        self,
        payload: Dict,
        promised: bool = True,
        response_model: Type[T] = None,
        api_key: Optional[bool] = False,
        session_logon: Optional[bool] = None,
        session_logout: Optional[bool] = None
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
            api_key=api_key,
            is_signed=False,
            skip_auth=skip_auth
        )
        _payload = ws_api_payload(
            self.configuration,
            payload,
            websocket_options
        )

        future = await super().send_message(_payload, connection)
        if promised:
            try:
                ws_response = await asyncio.wait_for(future, timeout=20)

                if session_logon:
                    payload["id"] = _payload["id"]
                    connection.is_session_log_on = True
                    connection.session_logon_request = payload

                is_oneof = self.is_one_of_model(response_model)
                if is_oneof:
                    data_function = lambda: response_model.from_dict(ws_response)
                elif response_model:
                    data_function = lambda: response_model.model_validate(ws_response)
                else:
                    data_function = lambda: ws_response

                return WebsocketApiResponse[T](
                    data_function=data_function,
                    rate_limits=parse_ws_rate_limit_headers(ws_response["rateLimits"]),
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
                error_message = str(e)

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

        return (hasattr(model_cls, "is_oneof_model") and model_cls.is_oneof_model())

    async def ping_ws_api(self, connection: WebSocketConnection):
        """Send a ping message to the WebSocket server.

        Args:
            connection (WebSocketConnection): WebSocket connection object.
        """

        await super().ping(connection)

    async def subscribe_user_data(self, id: str, response_model: Type[T] = None):
        """Subscribe to user data updates for a specific user.

        Args:
            id (str): User Data ID.
            response_model (Type[T]): Pydantic model to validate the response data.
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
        websocket_base: WebSocketStreamBase | WebSocketAPIBase,
        stream: str,
        response_model: Type[T] = None,
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
        self._websocket_base.on(event, callback, self._stream)


async def RequestStream(
    websocket_base: WebSocketStreamBase | WebSocketAPIBase, stream: str, response_model: Type[T] = None
) -> RequestStreamHandle[T]:
    """Decorator to create a request stream for a specific stream.

    Args:
        websocket_base (WebSocketStreamBase | WebSocketAPIBase): WebSocket base.
        stream (str): Stream name.
        response_model (Type[T], optional): Response model for the stream.
    """

    if isinstance(websocket_base, WebSocketStreamBase):
        await websocket_base.subscribe(streams=[stream], response_model=response_model)
    else:
        await websocket_base.subscribe_user_data(id=stream, response_model=response_model)

    return RequestStreamHandle(websocket_base, stream, response_model)
