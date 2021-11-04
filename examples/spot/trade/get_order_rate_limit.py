#!/usr/bin/env python

import logging
from binance.lib.utils import config_logging
from binance.spot import Spot as Client

config_logging(logging, logging.DEBUG)

key = ""
secret = ""

client = Client(key=key, secret=secret, base_url="https://testnet.binance.vision")
logger = logging.getLogger(__name__)

logger.info(client.get_order_rate_limit())
