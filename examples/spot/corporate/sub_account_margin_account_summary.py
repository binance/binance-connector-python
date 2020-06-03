#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

key = ''
secret = ''

spot_client = Client(key, secret)
logging.info(spot_client.sub_account_margin_account_summary())
