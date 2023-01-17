#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging
from examples.utils.prepare_env import get_api_key

config_logging(logging, logging.DEBUG)

# HMAC authentication with API key and secret
api_key, api_secret = get_api_key()

client = Client(api_key, api_secret, base_url="https://testnet.binance.vision")
logging.info(client.account(recvWindow=6000))


# RSA authentication with RSA key
api_key = ""
with open("/Users/john/ssl/private_key.pem", "r") as f:
    private_key = f.read()

client = Client(
    api_key, base_url="https://testnet.binance.vision", private_key=private_key
)
logging.info(client.account())


api_key = ""
with open("/Users/john/ssl/private_key.pem", "r") as f:
    private_key = f.read()

client = Client(
    api_key=api_key,
    base_url="https://testnet.binance.vision",
    private_key=private_key,
    private_key_pass="password",
)
logging.info(client.account())
