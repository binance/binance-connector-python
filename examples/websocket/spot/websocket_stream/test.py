#!/usr/bin/env python

import time
import logging
from binance.lib.utils import config_logging
from binance.websocket.spot.websocket_stream import SpotWebsocketStreamClient as Client

config_logging(logging, logging.DEBUG)


def message_handler(socketMangar, message):
    logging.info(message)


def on_ping(socketMangar):
    logging.info("received ping from server")


def on_pong(socketMangar):
    logging.info("received pong from server")


def on_open(socketMangar):
    logging.info("opened connection")


def on_close(socketMangar):
    logging.info("Closing connection received")


my_client = Client(
    on_open=on_open,
    on_message=message_handler,
    on_ping=on_ping,
    on_pong=on_pong,
    on_close=on_close,
    is_combined=True,
)


my_client.kline(symbol="bnbusdt", interval="1m")

time.sleep(5)

my_client.ping()

time.sleep(10)

my_client.list_subscribe()

time.sleep(10)

logging.debug("closing ws connection")
my_client.stop()
