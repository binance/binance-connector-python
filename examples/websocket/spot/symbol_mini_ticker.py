#!/usr/bin/env python

import time
import logging
from binance.lib.utils import config_logging
from binance.websocket.spot.websocket_client import SpotWebsocketClient as Client

config_logging(logging, logging.DEBUG)


def message_handler(message):
    print(message)


my_client = Client()
my_client.start()

my_client.mini_ticker(
    symbol="bnbusdt",
    id=1,
    callback=message_handler,
)

time.sleep(2)

my_client.mini_ticker(
    symbol="btcusdt",
    id=2,
    callback=message_handler,
)

time.sleep(3000)

logging.debug("closing ws connection")
my_client.stop()
