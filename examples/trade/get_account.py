#!/usr/bin/env python

import logging
import binance
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

key = ''
secret = ''

client = binance.Trade(key, secret, base_url='https://testnet.binance.vision')
logging.info(client.account(recvWindow=6000))
