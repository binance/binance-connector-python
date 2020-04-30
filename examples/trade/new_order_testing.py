#!/usr/bin/env python

import logging
import binance
from binance.lib.utils import config_logging
from binance.error import APIException, BinanceException

config_logging(logging, logging.DEBUG)

key = ''
secret = ''

params = {
    'symbol': 'BTCUSDT',
    'side': 'SELL',
    'type': 'LIMIT',
    'timeInForce': 'GTC',
    'quantity': 0.002,
    'price': 9500
}

client = binance.Trade(key, secret, base_url='https://testnet.binance.vision')

try:
    response = client.test_new_order(**params)
    logging.info(response)
except APIException as error:
    logging.error('error happens, status: {}, code: {}, message: {}'.format(error.status_code, error.code, error.message))
