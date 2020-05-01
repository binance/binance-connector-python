#!/usr/bin/env python

import logging
import binance
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

market_client= binance.Market(base_url='https://testnet.binance.vision')

logging.info(market_client.depth('BTCUSDT'))
logging.info(market_client.depth('BTCUSDT', limit=10))
