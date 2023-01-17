#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging
from examples.utils.prepare_env import get_api_key

config_logging(logging, logging.DEBUG)

api_key, _ = get_api_key()

# historical_trades requires api key in request header
spot_client = Client(api_key=api_key, base_url="https://testnet.binance.vision")

logging.info(spot_client.historical_trades("BTCUSDT"))
logging.info(spot_client.historical_trades("BTCUSDT", limit=10, fromId=""))
