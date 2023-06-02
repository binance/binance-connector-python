#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

api_key = "api_key"
private_key = "./private_key.txt"
private_key_pass = "private key password (if applicable)"

with open(private_key, "rb") as f:
    private_key = f.read()

spot_client = Client(
    api_key=api_key,
    private_key=private_key,
    private_key_pass=private_key_pass,
    key_type="ed25519",
)
logging.info(spot_client.account_status())
