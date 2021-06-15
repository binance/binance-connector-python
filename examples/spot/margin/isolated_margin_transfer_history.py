#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

key = ""
secret = ""

client = Client(key, secret)
logging.info(
    client.isolated_margin_transfer_history(
        asset="USDT", symbol="BTCUSDT", transFrom="SPOT", transTo="ISOLATED_MARGIN"
    )
)
