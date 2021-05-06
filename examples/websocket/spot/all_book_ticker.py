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


my_client.book_ticker(
    id=1,
    callback=message_handler,
)

time.sleep(30)

logging.debug("closing ws connection")
my_client.stop()
