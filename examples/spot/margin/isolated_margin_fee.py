#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

api_key = ""
api_secret = ""

spot_client = Client(api_key, api_secret)

logger = logging.getLogger(__name__)

logger.info(spot_client.isolated_margin_fee(vipLevel=1, symbol="BNBUSDT"))
