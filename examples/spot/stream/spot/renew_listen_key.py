#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

key = ""

client = Client(key, base_url="https://testnet.binance.vision")
logging.info(client.renew_listen_key(""))
