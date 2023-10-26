#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging
from binance.error import ClientError

from examples.utils.prepare_env import get_api_key

config_logging(logging, logging.DEBUG)
logger = logging.getLogger(__name__)

api_key, api_secret = get_api_key()

client = Client(api_key, api_secret)

try:
    response = client.get_simple_earn_locked_product_list(
        asset="BNB", current=1, size=100, recvWindow=5000
    )
    logger.info(response)
except ClientError as error:
    logger.error(
        "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )
