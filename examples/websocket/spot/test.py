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

my_client.agg_trade(
    symbol="btcusdt",
    id=1,
    callback=message_handler,
)

time.sleep(1)

my_client.agg_trade(
    symbol="bnbusdt",
    id=2,
    callback=message_handler,
)

time.sleep(10)

logging.debug("closing ws connection")
my_client.stop()
