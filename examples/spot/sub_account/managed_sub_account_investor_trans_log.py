#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging
from examples.utils.prepare_env import get_api_key

config_logging(logging, logging.DEBUG)

api_key, api_secret = get_api_key()

spot_client = Client(api_key, api_secret)
logging.info(
    spot_client.managed_sub_account_investor_trans_log(
        email="alice@test.com",
        startTime=1600000000000,
        endTime=1620000000000,
        page=1,
        limit=10,
    )
)
