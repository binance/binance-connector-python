#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

key = "<your_api_key>"
secret = "<your_api_secret>"

client = Client(key, secret)

logging.info(client.vip_loan_loanable_data(
    loanCoin="BTC",
    vipLevel=1
))
