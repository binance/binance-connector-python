#!/usr/bin/env python

import time
import logging
from binance.lib.utils import config_logging
from binance.websocket.spot.websocket_stream import SpotWebsocketStreamClient

config_logging(logging, logging.DEBUG)


def message_handler(_, message):
    print(message)


my_client = SpotWebsocketStreamClient(on_message=message_handler)


my_client.diff_book_depth(symbol="bnbusdt", speed=1000)

time.sleep(30)

logging.debug("closing ws connection")
my_client.stop()
