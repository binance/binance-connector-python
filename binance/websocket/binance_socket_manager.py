from typing import Optional

import logging
import threading
from websocket import (
    ABNF,
    create_connection,
    WebSocketException,
    WebSocketConnectionClosedException,
    WebSocketTimeoutException,
)
from binance.lib.utils import parse_proxies


class BinanceSocketManager(threading.Thread):
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
        timeout=None,
        time_unit=None,
        proxies: Optional[dict] = None,
    ):
        threading.Thread.__init__(self)
        if not logger:
            logger = logging.getLogger(__name__)
        self.logger = logger
        self.stream_url = (
            stream_url + f"?timeUnit={time_unit}"
            if time_unit == "microsecond"
            or time_unit == "millisecond"
            or time_unit == "MILLISECOND"
            or time_unit == "MICROSECOND"
            else stream_url
        )
        self.on_message = on_message
        self.on_open = on_open
        self.on_close = on_close
        self.on_ping = on_ping
        self.on_pong = on_pong
        self.on_error = on_error
        self.timeout = timeout

        self._proxy_params = parse_proxies(proxies) if proxies else {}

        self.create_ws_connection()

    def create_ws_connection(self):
        self.logger.debug(
            f"Creating connection with WebSocket Server: {self.stream_url}, proxies: {self._proxy_params}",
        )

        self.ws = create_connection(
            self.stream_url, timeout=self.timeout, **self._proxy_params
        )
        self.logger.debug(
            f"WebSocket connection has been established: {self.stream_url}, proxies: {self._proxy_params}",
        )
        self._callback(self.on_open)

    def run(self):
        self.read_data()

    def send_message(self, message):
        self.logger.debug("Sending message to Binance WebSocket Server: %s", message)
        self.ws.send(message)

    def ping(self):
        self.ws.ping()

    def read_data(self):
        data = ""
        while True:
            try:
                op_code, frame = self.ws.recv_data_frame(True)
            except WebSocketException as e:
                if isinstance(e, WebSocketConnectionClosedException):
                    self.logger.error("Lost websocket connection")
                elif isinstance(e, WebSocketTimeoutException):
                    self.logger.error("Websocket connection timeout")
                else:
                    self.logger.error("Websocket exception: {}".format(e))
                self._handle_exception(e)
                break
            except Exception as e:
                self.logger.error("Exception in read_data: {}".format(e))
                self._handle_exception(e)
                break

            self._handle_data(op_code, frame, data)
            self._handle_heartbeat(op_code, frame)

            if op_code == ABNF.OPCODE_CLOSE:
                self.logger.warning(
                    "CLOSE frame received, closing websocket connection"
                )
                self._callback(self.on_close)
                break

    def _handle_heartbeat(self, op_code, frame):
        if op_code == ABNF.OPCODE_PING:
            self._callback(self.on_ping, frame.data)
            self.ws.pong("")
            self.logger.debug("Received Ping; PONG frame sent back")
        elif op_code == ABNF.OPCODE_PONG:
            self.logger.debug("Received PONG frame")
            self._callback(self.on_pong)

    def _handle_data(self, op_code, frame, data):
        if op_code == ABNF.OPCODE_TEXT:
            data = frame.data.decode("utf-8")
            self._callback(self.on_message, data)

    def close(self):
        if not self.ws.connected:
            self.logger.warning("Websocket already closed")
        else:
            self.ws.send_close()

    def _callback(self, callback, *args):
        if callback:
            try:
                callback(self, *args)
            except Exception as e:
                self.logger.error("Error from callback {}: {}".format(callback, e))
                self._handle_exception(e)

    def _handle_exception(self, e):
        if self.on_error:
            self.on_error(self, e)
        else:
            raise e

    def subscribe_to_agg_trades(self, symbol):
        """Subscribe to aggregate trade streams"""
        stream_name = f"{symbol.lower()}@aggTrade"
        self.send_message(json.dumps({"method": "SUBSCRIBE", "params": [stream_name], "id": 1}))

    def subscribe_to_kline(self, symbol, interval):
        """Subscribe to kline/candlestick streams"""
        stream_name = f"{symbol.lower()}@kline_{interval}"
        self.send_message(json.dumps({"method": "SUBSCRIBE", "params": [stream_name], "id": 1}))

    def subscribe_to_order_book(self, symbol, level=5):
        """Subscribe to order book streams"""
        stream_name = f"{symbol.lower()}@depth{level}"
        self.send_message(json.dumps({"method": "SUBSCRIBE", "params": [stream_name], "id": 1}))
