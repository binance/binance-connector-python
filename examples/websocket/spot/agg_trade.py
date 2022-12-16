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

# Subscribe to a single symbol stream
my_client.agg_trade(
    symbol="btcusdt",
    id=1,
    callback=message_handler,
)

time.sleep(2)

# Subscribe to a new stream for each symbol in the list
my_client.agg_trade(
    symbol=["bnbusdt", "ethusdt", "ltcusdt"],
    id=2,
    callback=message_handler,
)

time.sleep(5)

logging.debug("closing ws connection")
my_client.stop()
