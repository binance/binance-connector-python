#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

api_key = ""
api_secret = ""

client = Client(api_key, api_secret)
logging.info(
    client.bswap_add_liquidity_preview(
        poolId=2, type="SINGLE", quoteAsset="USDT", quoteQty=0.01
    )
)
