#!/usr/bin/env python

import logging
from binance.futures import Futures as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

futures_client = Client(base_url="https://testnet.binancefuture.com")

logging.info(futures_client.agg_trades(symbol="BTCUSDT"))
logging.info(futures_client.agg_trades(symbol="BTCUSDT", limit=10, formId=""))
