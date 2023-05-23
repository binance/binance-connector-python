import json
import logging
from binance.lib.utils import get_timestamp
from binance.websocket.binance_socket_manager import BinanceSocketManager


class BinanceWebsocketClient:
    ACTION_SUBSCRIBE = "SUBSCRIBE"
    ACTION_UNSUBSCRIBE = "UNSUBSCRIBE"

    def __init__(
        self,
        stream_url,
        on_message=None,
        on_open=None,
        on_close=None,
        on_error=None,
        on_ping=None,
        on_pong=None,
        logger=None,
    ):
        if not logger:
            logger = logging.getLogger(__name__)
        self.logger = logger
        self.socket_manager = self._initialize_socket(
            stream_url,
            on_message,
            on_open,
            on_close,
            on_error,
            on_ping,
            on_pong,
            logger,
        )

        # start the thread
        self.socket_manager.start()
        self.logger.debug("Binance WebSocket Client started.")

    def _initialize_socket(
        self,
        stream_url,
        on_message,
        on_open,
        on_close,
        on_error,
        on_ping,
        on_pong,
        logger,
    ):
        return BinanceSocketManager(
            stream_url,
            on_message=on_message,
            on_open=on_open,
            on_close=on_close,
            on_error=on_error,
            on_ping=on_ping,
            on_pong=on_pong,
            logger=logger,
        )

    def _single_stream(self, stream):
        if isinstance(stream, str):
            return True
        elif isinstance(stream, list):
            return False
        else:
            raise ValueError("Invalid stream name, expect string or array")

    def send(self, message: dict):
        self.socket_manager.send_message(json.dumps(message))

    def send_message_to_server(self, message, action=None, id=None):
        if not id:
            id = get_timestamp()

        if action != self.ACTION_UNSUBSCRIBE:
            return self.subscribe(message, id=id)
        return self.unsubscribe(message, id=id)

    def subscribe(self, stream, id=None):
        if not id:
            id = get_timestamp()
        if self._single_stream(stream):
            stream = [stream]
        json_msg = json.dumps({"method": "SUBSCRIBE", "params": stream, "id": id})
        self.socket_manager.send_message(json_msg)

    def unsubscribe(self, stream, id=None):
        if not id:
            id = get_timestamp()
        if self._single_stream(stream):
            stream = [stream]
        json_msg = json.dumps({"method": "UNSUBSCRIBE", "params": stream, "id": id})
        self.socket_manager.send_message(json_msg)

    def ping(self):
        self.logger.debug("Sending ping to Binance WebSocket Server")
        self.socket_manager.ping()

    def stop(self, id=None):
        self.socket_manager.close()
        self.socket_manager.join()

    def list_subscribe(self, id=None):
        """sending the list subscription message, e.g.

        {"method": "LIST_SUBSCRIPTIONS","id": 100}

        """

        if not id:
            id = get_timestamp()
        self.socket_manager.send_message(
            json.dumps({"method": "LIST_SUBSCRIPTIONS", "id": id})
        )
