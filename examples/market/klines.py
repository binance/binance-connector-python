#!/usr/bin/env python

import logging
import binance
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

key = ''

market_client= binance.Market(base_url='https://testnet.binance.vision')

logging.info(market_client.klines('BTCUSDT', '1m'))
logging.info(market_client.klines('BTCUSDT', '1h',  limit=10))
