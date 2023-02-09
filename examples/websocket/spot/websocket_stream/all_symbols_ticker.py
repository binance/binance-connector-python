#!/usr/bin/env python

import time
import logging
from binance.lib.utils import config_logging
from binance.websocket.spot.websocket_stream import SpotWebsocketStreamClient

config_logging(logging, logging.DEBUG)


def message_handler(_, message):
    print(message)


my_client = SpotWebsocketStreamClient(on_message=message_handler)


# subscribe to all symbols ticker stream
my_client.ticker()

time.sleep(5)

# unsubscribe
my_client.ticker(action=SpotWebsocketStreamClient.ACTION_UNSUBSCRIBE)

time.sleep(5)

# subscribe to single symbol ticker stream
my_client.ticker(symbol="bnbusdt")

time.sleep(5)

# unsubscribe
my_client.ticker(symbol="bnbusdt", action=SpotWebsocketStreamClient.ACTION_UNSUBSCRIBE)

time.sleep(5)

logging.debug("closing ws connection")
my_client.stop()
