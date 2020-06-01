#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging
from binance.error import ClientError

config_logging(logging, logging.DEBUG)

key = ''
secret = ''

client = Client(key, secret, base_url='https://testnet.binance.vision')

try:
    response = client.get_order('BTCUSDT', orderId='')
    logging.info(response)
except ClientError as error:
    logging.error('error happens, status: {}, code: {}, message: {}'.format(error.status_code, error.code, error.message))