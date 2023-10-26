import logging
import time

from binance.lib.utils import config_logging
from binance.websocket.spot.websocket_stream import SpotWebsocketStreamClient

config_logging(logging, logging.DEBUG)


def message_handler(_, message):
    logging.info(message)


my_client = SpotWebsocketStreamClient(on_message=message_handler, is_combined=True)


my_client.subscribe(
    stream=["bnbusdt@bookTicker", "ethusdt@kline_1m"],
)

time.sleep(10)
my_client.stop()
