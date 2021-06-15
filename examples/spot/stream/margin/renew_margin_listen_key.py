#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

key = ""
client = Client(key)
logging.info(client.renew_margin_listen_key(listenKey=""))
