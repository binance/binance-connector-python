#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

key = "AqUZiEuzIXKf3c7PIOV2LmDCY4PXOWcAyqpVZrpsXnt5x0BQtgNqDNTGrp0JGFEv"
secret = "5ptDHTvuudtkaQttQ1KDxmQyEiPLt0N1XjYRp7jbf7BV7DbTYTvVv8gx9fYtQjpx"

client = Client(key, secret)
logging.info(client.user_limit_info(tokenName="BTCDOWN"))
