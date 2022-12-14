#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

api_key = ""
api_secret = ""

client = Client(api_key, api_secret)
logging.info(
    client.isolated_margin_transfer(
        asset="USDT",
        symbol="BTCUSDT",
        transFrom="SPOT",
        transTo="ISOLATED_MARGIN",
        amount=1,
    )
)
