#!/usr/bin/env python

import time
import logging
from binance.lib.utils import config_logging
from binance.websocket.spot.websocket_client import SpotWebsocketClient as Client

config_logging(logging, logging.DEBUG)


def message_handler(message):
    print(message)


my_client = Client(stream_url='wss://testnet.binance.vision')
my_client.start()

my_client.user_data(
    listen_key='',
    id=1,
    callback=message_handler,
)

time.sleep(30)

logging.debug("cloing ws connection")
my_client.stop()
