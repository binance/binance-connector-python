#!/usr/bin/env python

import logging
from binance.futures import Futures as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

futures_client = Client(base_url="https://testnet.binancefuture.com")

logging.info(futures_client.funding_rate_history())
logging.info(futures_client.funding_rate_history("BTCUSDT"))
logging.info(futures_client.funding_rate_history("BTCUSDT", limit=10))
