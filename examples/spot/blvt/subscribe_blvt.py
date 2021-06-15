#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

key = ""
secret = ""

client = Client(key, secret)
logging.info(client.subscribe_blvt(tokenName="LINKUP", cost="9.99999995"))
