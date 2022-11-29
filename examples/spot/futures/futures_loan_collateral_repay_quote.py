#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

api_key = ""
api_secret = ""

client = Client(api_key, api_secret)
logging.info(
    client.futures_loan_collateral_repay_quote(
        coin="USDT", collateralCoin="BTC", amount=0.00222
    )
)
