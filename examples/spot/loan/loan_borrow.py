#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

key = ""
secret = ""


client = Client(key, secret)
logging.info(
    client.loan_borrow(
        loanCoin="USDT", collateralCoin="BUSD", loanTerm=7, loanAmount=1.1
    )
)
