#!/usr/bin/env python

import logging
from binance.futures import Futures as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

# historical_trades requires api key in request header
futures_client = Client(base_url="https://testnet.binancefuture.com")

logging.info(futures_client.historical_trades(symbol="BTCUSDT"))
logging.info(futures_client.historical_trades(symbol="BTCUSDT", limit=10, formId=""))
