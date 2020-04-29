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
    client.cancel_order('BTCUSDT', orderId='12345')
except APIException as error:
    logging.error('error happens, code: {}, message: {}'.format(error.code, error.message))
