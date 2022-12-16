#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging
from configparser import ConfigParser

config = ConfigParser()
config.read("../../../config.ini")

config_logging(logging, logging.DEBUG)

api_key = config["keys"]["api_key"]

client = Client(api_key, base_url="https://testnet.binance.vision")
logging.info(client.new_listen_key())
