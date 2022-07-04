#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging
from binance.error import ClientError

config_logging(logging, logging.DEBUG)

key = ""
secret = ""

client = Client(key, secret, base_url="https://testnet.binance.vision")

try:
    response = client.cancel_and_replace(
        "BNBUSDT",
        "SELL",
        "LIMIT",
        "STOP_ON_FAILURE",
        timeInForce="GTC",
        quantity=10.1,
        price=295.92,
        # The order with this id (cancelOrderId) has to be able to be cancelled.
        # If you wish to test, create an open order first, then copy and paste id to here.
        cancelOrderId=12,
        recvWindow=5000,
    )
    logging.info(response)
except ClientError as error:
    logging.error(
        "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )
