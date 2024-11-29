#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging
from examples.utils.prepare_env import get_api_key

config_logging(logging, logging.DEBUG)

api_key, api_secret = get_api_key()

client = Client(api_key, api_secret)
logging.info(
    client.margin_new_otoco_order(
        symbol="BNBUSDT",
        workingType="LIMIT",
        workingSide="BUY",
        workingPrice=600.0,
        workingQuantity=1.0,
        pendingSide="SELL",
        pendingQuantity=1.0,
        pendingAboveType="LIMIT_MAKER",
        workingTimeInForce="GTC",
        pendingAbovePrice=605.0,
        pendingBelowType="LIMIT_MAKER",
        pendingBelowPrice=595.0,
        workingIcebergQty=0.1,
    )
)
