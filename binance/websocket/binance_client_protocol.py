import json
import logging
from autobahn.twisted.websocket import WebSocketClientProtocol


class BinanceClientProtocol(WebSocketClientProtocol):
    def __init__(self, factory, payload=None):
        super().__init__()
        self.factory = factory
        self.payload = payload

    def onOpen(self):
        self.factory.protocol_instance = self

    def onConnect(self, response):
        logging.info("Server connected")
        if self.payload:
            logging.info("Sending message to Server: {}".format(self.payload))
            self.sendMessage(self.payload, isBinary=False)
        # reset the delay after reconnecting
        self.factory.resetDelay()

    def onMessage(self, payload, isBinary):
        if not isBinary:
            try:
                payload_obj = json.loads(payload.decode("utf8"))
            except ValueError:
                pass
            else:
                self.factory.callback(payload_obj)

    def onClose(self, wasClean, code, reason):
        logging.warn(
            "WebSocket connection closed: {0}, code: {1}, clean: {2}, reason: {0}".format(
                reason, code, wasClean
            )
        )

    def onPing(self, payload):
        logging.info("Received Ping from server")
        self.sendPong()
        logging.info("Responded Pong to server")

    def onPong(self, payload):
        logging.info("Received Pong from server")
