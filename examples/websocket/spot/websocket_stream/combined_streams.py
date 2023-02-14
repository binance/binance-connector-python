#!/usr/bin/env python

import logging
import time

from binance.lib.utils import config_logging
from binance.websocket.spot.websocket_stream import SpotWebsocketStreamClient

config_logging(logging, logging.DEBUG)
counter = 1


def message_handler(_, message):
    logging.info(message)


my_client = SpotWebsocketStreamClient(on_message=message_handler, is_combined=True)


# subscribe one stream
my_client.kline(symbol="bnbusdt", interval="1m")

time.sleep(4)

# subscribe another
my_client.ticker(symbol="ethusdt")

time.sleep(10)
my_client.stop()
