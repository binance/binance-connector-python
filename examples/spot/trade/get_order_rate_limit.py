#!/usr/bin/env python

import logging
from binance.lib.utils import config_logging
from binance.spot import Spot as Client
from examples.utils.prepare_env import get_api_key

config_logging(logging, logging.DEBUG)

api_key, api_secret = get_api_key()

client = Client(
    api_key=api_key, api_secret=api_secret, base_url="https://testnet.binance.vision"
)
logger = logging.getLogger(__name__)

logger.info(client.get_order_rate_limit())
