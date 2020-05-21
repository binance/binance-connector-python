#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging
from binance.error import APIException

config_logging(logging, logging.DEBUG)

key = ''
secret = ''

params = {
    'symbol': 'BTCUSDT',
    'side': 'SELL',
    'quantity': 0.002,
    'price': 9500,
    'stopPrice': 7500,
    'stopLimitPrice': 7000,
    'stopLimitTimeInForce': 'GTC'
}

client = Client(key, secret, base_url='https://testnet.binance.vision')

try:
    response = client.new_oco_order(**params)
    logging.info(response)
except APIException as error:
    logging.error('error happens, status: {}, code: {}, message: {}'.format(error.status_code, error.code, error.message))
