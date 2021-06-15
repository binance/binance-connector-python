#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

key = ""
secret = ""

client = Client(key, secret)
logging.info(
    client.new_margin_order(
        symbol="BNBUSDT",
        side="SELL",
        type="LIMIT",
        quantity=1,
        price="30",
        timeInForce="GTC",
    )
)
