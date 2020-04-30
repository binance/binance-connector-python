#!/usr/bin/env python

import logging
import binance
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

key = ''

client = binance.Stream(key, base_url='https://testnet.binance.vision')
logging.info(client.close_listen_key(''))
