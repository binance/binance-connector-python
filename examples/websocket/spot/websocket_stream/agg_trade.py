#!/usr/bin/env python

import logging
import time
from binance.lib.utils import config_logging
from binance.websocket.spot.websocket_stream import SpotWebsocketStreamClient

config_logging(logging, logging.DEBUG)


def message_handler(_, message):
    logging.info(message)


my_client = SpotWebsocketStreamClient(on_message=message_handler, is_combined=True)

# Subscribe to a single symbol stream
my_client.agg_trade(symbol="bnbusdt")

time.sleep(5)

# Unsubscribe
my_client.agg_trade(
    symbol="bnbusdt", action=SpotWebsocketStreamClient.ACTION_UNSUBSCRIBE
)

time.sleep(5)

logging.info("closing ws connection")
my_client.stop()
