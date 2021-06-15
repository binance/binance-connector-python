#!/usr/bin/env python

import time
import logging
from binance.lib.utils import config_logging
from binance.websocket.spot.websocket_client import SpotWebsocketClient as Client

config_logging(logging, logging.DEBUG)


def message_handler(message):
    logging.info(message)


my_client = Client()
my_client.start()


# subscribe one stream
my_client.instant_subscribe(
    stream="bnbusdt@bookTicker",
    callback=message_handler,
)

time.sleep(3)

# subscribe multiple streams
my_client.instant_subscribe(
    stream=["bnbusdt@bookTicker", "ethusdt@bookTicker"],
    callback=message_handler,
)

time.sleep(30)

logging.debug("closing ws connection")
my_client.stop()
