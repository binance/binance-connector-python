#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging
from examples.utils.prepare_env import get_api_key

config_logging(logging, logging.DEBUG)

api_key, api_secret = get_api_key()

spot_client = Client(api_key, api_secret)

# From master account to sub-account alice@test.com
logging.info(
    spot_client.sub_account_universal_transfer(
        toEmail="alice@test.com",
        fromAccountType="SPOT",
        toAccountType="USDT_FUTURE",
        asset="USDT",
        amount=1,
        clientTranId="test",
    )
)
