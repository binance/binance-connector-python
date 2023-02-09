#!/usr/bin/env python

import logging
import time
from binance.lib.utils import config_logging
from binance.websocket.spot.websocket_api import SpotWebsocketAPIClient

config_logging(logging, logging.DEBUG)


def on_close(_):
    logging.info("Do custom stuff when connection is closed")


def message_handler(_, message):
    logging.info(message)


my_client = SpotWebsocketAPIClient(on_message=message_handler, on_close=on_close)


my_client.ping_connectivity()
time.sleep(2)

my_client.server_time()
time.sleep(2)

my_client.exchange_info()
time.sleep(2)

my_client.order_book(symbol="BNBBUSD", limit=1)
time.sleep(2)

my_client.recent_trades(symbol="BNBBUSD", limit=1)
time.sleep(2)

my_client.historical_trades(
    symbol="BNBBUSD",
    apiKey="HX0gpRCAJHiAZBCaPfkDMXAN2uXj3BrNNwjBRjlFhn3E4jtZthu4SijD31rkLqr2",
    limit=1,
)
time.sleep(2)

my_client.aggregate_trades(symbol="BNBBUSD", limit=1, fromId=0)
time.sleep(2)

my_client.ticker_24hr(symbol="BNBBUSD")
time.sleep(2)

my_client.ticker(symbol="BNBBUSD", type="FULL")
time.sleep(2)

my_client.ticker_price(symbol="BNBBUSD")
time.sleep(2)

my_client.ticker_book(symbol="BNBBUSD")
time.sleep(2)

logging.info("closing ws connection")
my_client.stop()
