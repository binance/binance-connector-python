#!/usr/bin/env python

import logging
import binance
from binance.lib.utils import config_logging
from binance.error import APIException, BinanceException

config_logging(logging, logging.DEBUG)

key = ''
secret = ''

client = binance.Trade(key, secret, base_url='https://testnet.binance.vision')

try:
    # get oco orders with default parameters
    response = client.get_oco_orders()

    # provide parameters
    response = client.get_oco_orders(fromId=1, limit=10)
    response = client.get_oco_orders(startTime=1588160817647, limit=10)

    logging.info(response)
except APIException as error:
    logging.error('error happens, status: {}, code: {}, message: {}'.format(error.status_code, error.code, error.message))
