#!/usr/bin/env python

"""
    A simple demo for how to:
    - Create a connection to the websocket api
    - Create a connection to the websocket stream
    - Subscribe to the user data stream from websocket stream
    - Create a new order from websocket api
"""

import logging
import time
from binance.lib.utils import config_logging
from binance.websocket.spot.websocket_api import SpotWebsocketAPIClient
from binance.websocket.spot.websocket_stream import SpotWebsocketStreamClient
from binance.spot import Spot as SpotAPIClient
from examples.utils.prepare_env import get_api_key

api_key, api_secret = get_api_key()

config_logging(logging, logging.DEBUG)


def on_close(_):
    logging.info("Do custom stuff when connection is closed")


def websocket_api_message_handler(_, message):
    logging.info("message from websocket API")
    logging.info(message)


def websocket_stream_message_handler(_, message):
    logging.info("message from websocket stream")
    logging.info(message)


# make a connection to the websocket api
ws_api_client = SpotWebsocketAPIClient(
    stream_url="wss://testnet.binance.vision/ws-api/v3",
    api_key=api_key,
    api_secret=api_secret,
    on_message=websocket_api_message_handler,
    on_close=on_close,
)

# make a connection to the websocket stream
ws_stream_client = SpotWebsocketStreamClient(
    stream_url="wss://testnet.binance.vision",
    on_message=websocket_stream_message_handler,
)

# spot api client to call all restful api endpoints
spot_api_client = SpotAPIClient(api_key, base_url="https://testnet.binance.vision")
response = spot_api_client.new_listen_key()

# You can subscribe to the user data stream from websocket stream, it will broadcast all the events
# related to your account, including order updates, balance updates, etc.
ws_stream_client.user_data(listen_key=response["listenKey"])

time.sleep(5)

# You can create a new order from websocket api
ws_api_client.new_order(
    symbol="BNBUSDT",
    side="BUY",
    type="LIMIT",
    timeInForce="GTC",
    quantity=1,
    price=200,
    newOrderRespType="RESULT",
)

time.sleep(10)

logging.info("closing ws connection")
ws_api_client.stop()
ws_stream_client.stop()
