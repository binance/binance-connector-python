#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

key = ""
secret = ""

params = {
    "algo": "sha256",
    "userName": "user_name",
    "startDate": 1607659086000,
    "endDate": 1617659086000,
    "toPoolUser": "pool_user_name",
    "hashRate": "100000000",
}

client = Client(key, secret)
logging.info(client.mining_hashrate_resale_request(**params))
