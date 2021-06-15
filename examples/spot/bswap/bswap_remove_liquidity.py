#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

key = ""
secret = ""


client = Client(key, secret)
logging.info(client.bswap_liquidity_remove("2", "SINGLE", ["BUSD"], "12415"))
logging.info(
    client.bswap_liquidity_remove("2", "COMBINATION", ["BUSD", "USDT"], "12415")
)
