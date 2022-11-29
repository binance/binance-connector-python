#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

api_key = ""
client = Client(api_key)
logging.info(client.close_isolated_margin_listen_key(symbol="BTCUSDT", listenKey=""))
