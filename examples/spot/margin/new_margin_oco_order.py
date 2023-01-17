#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging
from binance.error import ClientError
from examples.utils.prepare_env import get_api_key

config_logging(logging, logging.DEBUG)

api_key, api_secret = get_api_key()

params = {
    "symbol": "BTCUSDT",
    "side": "SELL",
    "quantity": 0.002,
    "price": 9500,
    "stopPrice": 7500,
    "stopLimitPrice": 7000,
    "stopLimitTimeInForce": "GTC",
}

client = Client(api_key, api_secret)

try:
    response = client.new_margin_oco_order(**params)
    logging.info(response)
except ClientError as error:
    logging.error(
        "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )
