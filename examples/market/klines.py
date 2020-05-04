#!/usr/bin/env python

import logging
from binance.market import Market
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

market_client = Market(base_url='https://testnet.binance.vision')

logging.info(market_client.klines('BTCUSDT', '1m'))
logging.info(market_client.klines('BTCUSDT', '1h', limit=10))
