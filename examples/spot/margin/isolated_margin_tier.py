#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

key = ""
secret = ""

spot_client = Client(key, secret)

logger = logging.getLogger(__name__)

logger.info(spot_client.isolated_margin_tier(symbol="BNBUSDT"))
