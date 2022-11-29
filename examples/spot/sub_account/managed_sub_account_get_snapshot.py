#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

api_key = ""
api_secret = ""

spot_client = Client(api_key, api_secret)

logging.info(
    spot_client.managed_sub_account_get_snapshot(email="alice@test.com", type="SPOT")
)
