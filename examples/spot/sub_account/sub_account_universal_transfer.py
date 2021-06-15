#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

key = ""
secret = ""

spot_client = Client(key, secret)

# From master account to sub-account alice@test.com
logging.info(
    spot_client.sub_account_universal_transfer(
        toEmail="alice@test.com",
        fromAccountType="SPOT",
        toAccountType="USDT_FUTURE",
        asset="USDT",
        amount=1,
    )
)
