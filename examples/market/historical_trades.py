#!/usr/bin/env python

import logging
import binance
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

key = ''

# historical_trades requires api key in request header
market_client= binance.Market(key=key, base_url='https://testnet.binance.vision')

logging.info(market_client.historical_trades('BTCUSDT'))
logging.info(market_client.historical_trades('BTCUSDT', limit=10, fromId=''))
