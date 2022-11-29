#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

api_key = ""
api_secret = ""

logger = logging.getLogger(__name__)
spot_client = Client(api_key, api_secret, show_header=True)
logging.info(spot_client.bnb_convertible_assets())
