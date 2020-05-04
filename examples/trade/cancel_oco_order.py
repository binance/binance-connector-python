#!/usr/bin/env python

import logging
import binance
from binance.lib.utils import config_logging
from binance.error import APIException, BinanceException

config_logging(logging, logging.DEBUG)

key = ''
secret = ''

client = Trade(key, secret, base_url='https://testnet.binance.vision')

try:
    response = client.cancel_oco_order('BTCUSDT', orderListId=1)
    logging.info(response)
except APIException as error:
    logging.error('error happens, status: {}, code: {}, message: {}'.format(error.status_code, error.code, error.message))
