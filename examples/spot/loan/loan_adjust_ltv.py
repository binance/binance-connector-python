#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

api_key = ""
api_secret = ""


client = Client(api_key, api_secret)
logging.info(
    client.loan_adjust_ltv(
        orderId=756783308056935434, amount=5.235, direction="ADDITIONAL"
    )
)