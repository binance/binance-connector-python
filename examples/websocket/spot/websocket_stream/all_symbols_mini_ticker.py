#!/usr/bin/env python

import time
import logging
from binance.lib.utils import config_logging
from binance.websocket.spot.websocket_stream import SpotWebsocketStreamClient

config_logging(logging, logging.DEBUG)


def message_handler(_, message):
    logging.info(message)


my_client = SpotWebsocketStreamClient(on_message=message_handler)


# subscribe to all symbols mini ticker stream
my_client.mini_ticker(symbol="bnbusdt")

time.sleep(10)

# unsubscribe
my_client.mini_ticker(
    symbol="bnbusdt", action=SpotWebsocketStreamClient.ACTION_UNSUBSCRIBE
)

time.sleep(10)

logging.info("closing ws connection")
my_client.stop()
