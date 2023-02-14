#!/usr/bin/env python

import time
import logging
from binance.lib.utils import config_logging
from binance.spot import Spot as Client
from binance.websocket.spot.websocket_stream import SpotWebsocketStreamClient
from examples.utils.prepare_env import get_api_key

api_key, api_secret = get_api_key()

config_logging(logging, logging.DEBUG)


def message_handler(_, message):
    logging.info(message)


# get listen key from testnet, make sure you are using testnet api key
client = Client(api_key, base_url="https://testnet.binance.vision")
response = client.new_listen_key()

logging.info("Receving listen key : {}".format(response["listenKey"]))

# create the websocket connection to testnet as well
ws_client = SpotWebsocketStreamClient(
    stream_url="wss://testnet.binance.vision", on_message=message_handler
)

ws_client.user_data(listen_key=response["listenKey"])

time.sleep(30)

# You don't have to, but just in case you want to unsubscribe
logging.info("unsubscribe user data")
ws_client.user_data(
    response["listenKey"], action=SpotWebsocketStreamClient.ACTION_UNSUBSCRIBE
)

time.sleep(300)

logging.debug("closing ws connection")
ws_client.stop()
