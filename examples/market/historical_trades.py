#!/usr/bin/env python

import logging
from binance.market import Market
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

key = ''

# historical_trades requires api key in request header
market_client = Market(key=key, base_url='https://testnet.binance.vision')

logging.info(market_client.historical_trades('BTCUSDT'))
logging.info(market_client.historical_trades('BTCUSDT', limit=10, fromId=''))
