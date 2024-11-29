#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging
from examples.utils.prepare_env import get_api_key

config_logging(logging, logging.DEBUG)

api_key, api_secret = get_api_key()

client = Client(api_key, api_secret)
logging.info(
    client.margin_new_oto_order(
        symbol="BNBUSDT",
        workingType="LIMIT",
        workingSide="SELL",
        workingPrice=600.0,
        workingQuantity=1.0,
        pendingType="LIMIT",
        pendingSide="BUY",
        pendingQuantity=1.0,
        workingTimeInForce="GTC",
        pendingPrice=595.0,
        pendingTimeInForce="GTC",
        workingIcebergQty=0.1,
    )
)
