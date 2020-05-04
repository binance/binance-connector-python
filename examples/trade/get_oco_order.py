#!/usr/bin/env python

import logging
from binance.trade import Trade
from binance.lib.utils import config_logging
from binance.error import APIException

config_logging(logging, logging.DEBUG)

key = ''
secret = ''

client = Trade(key, secret, base_url='https://testnet.binance.vision')

try:
    response = client.get_oco_order(orderListId='')
    logging.info(response)
except APIException as error:
    logging.error('error happens, status: {}, code: {}, message: {}'.format(error.status_code, error.code, error.message))
