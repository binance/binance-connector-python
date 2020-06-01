#!/usr/bin/env python

import time
import logging
from binance.lib.utils import config_logging
from binance.websocket.spot.websocket_client import SpotWebsocketClient as Client

config_logging(logging, logging.DEBUG)


def message_handler(message):
    logging.info(message)


my_client = Client(stream_url='wss://testnet.binance.vision')
my_client.start()

my_client.ticker(
    symbol='bnbusdt',
    id=1,
    callback=message_handler,
)

my_client.request(['bnbusdt@ticker', 'ethusdt@ticker'], callback=message_handler)

time.sleep(2000)

logging.debug("cloing ws connection")
my_client.stop()
