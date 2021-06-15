import json
from twisted.internet import reactor
from binance.websocket.binance_socket_manager import BinanceSocketManager


class BinanceWebsocketClient(BinanceSocketManager):
    def __init__(self, stream_url):
        super().__init__(stream_url)

    def stop(self):
        try:
            self.close()
        finally:
            reactor.stop()

    def _single_stream(self, stream):
        if isinstance(stream, str):
            return True
        elif isinstance(stream, list):
            return False
        else:
            raise ValueError("Invalid stream name, expect string or array")

    def live_subscribe(self, stream, id, callback, **kwargs):
        """live subscribe websocket
        Connect to the server
        - SPOT: wss://stream.binance.com:9443/ws
        - SPOT testnet : wss://testnet.binance.vision/ws

        and sending the subscribe message, e.g.

        {"method": "SUBSCRIBE","params":["btcusdt@miniTicker"],"id": 100}

        """
        combined = False
        if self._single_stream(stream):
            stream = [stream]
        else:
            combined = True

        data = {"method": "SUBSCRIBE", "params": stream, "id": id}

        data.update(**kwargs)
        payload = json.dumps(data, ensure_ascii=False).encode("utf8")
        stream_name = "-".join(stream)
        return self._start_socket(
            stream_name, payload, callback, is_combined=combined, is_live=True
        )

    def instant_subscribe(self, stream, callback, **kwargs):
        """Instant subscribe, e.g.
        wss://stream.binance.com:9443/ws/btcusdt@bookTicker
        wss://stream.binance.com:9443/stream?streams=btcusdt@bookTicker/bnbusdt@bookTicker

        """
        combined = False
        if not self._single_stream(stream):
            combined = True
            stream = "/".join(stream)

        data = {"method": "SUBSCRIBE", "params": stream}

        data.update(**kwargs)
        payload = json.dumps(data, ensure_ascii=False).encode("utf8")
        stream_name = "-".join(stream)
        return self._start_socket(
            stream_name, payload, callback, is_combined=combined, is_live=False
        )
