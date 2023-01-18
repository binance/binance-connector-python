#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging
from examples.utils.prepare_env import get_api_key

config_logging(logging, logging.DEBUG)

api_key, api_secret = get_api_key()


client = Client(api_key, api_secret)
logging.info(client.convert_history(startTime=1603954452000, endTime=1613954452000))
