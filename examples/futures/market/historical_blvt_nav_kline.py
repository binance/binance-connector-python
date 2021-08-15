#!/usr/bin/env python

import logging
from binance.futures import Futures as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

futures_client = Client(base_url="https://fapi.binance.com")

logging.info(futures_client.historical_blvt_nav_kline("BTCDOWN", "1h"))
logging.info(futures_client.historical_blvt_nav_kline("BTCDOWN", "1h", limit=10))
