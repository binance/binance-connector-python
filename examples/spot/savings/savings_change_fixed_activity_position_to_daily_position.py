#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

key = ''
secret = ''

client = Client(key, secret)
logging.info(client.savings_change_fixed_activity_position_to_daily_position(projectId='USDT001', lot=1))
