#!/usr/bin/env python

import logging
import binance
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

market_client= binance.Market(base_url='https://testnet.binance.vision')

logging.info(market_client.agg_trades('BTCUSDT'))
logging.info(market_client.agg_trades('BTCUSDT', limit=10, fromId=''))
