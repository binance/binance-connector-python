#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging
from binance.error import ClientError
from examples.utils.prepare_env import get_api_key

config_logging(logging, logging.DEBUG)

api_key, api_secret = get_api_key()

client = Client(api_key, api_secret, base_url="https://testnet.binance.vision")

try:
    # get oco orders with default parameters
    response = client.get_oco_orders()
    logging.info(response)

    # provide parameters
    response = client.get_oco_orders(fromId=1, limit=10)
    logging.info(response)

    response = client.get_oco_orders(startTime=1588160817647, limit=10)
    logging.info(response)
except ClientError as error:
    logging.error(
        "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )
