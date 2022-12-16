#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging
from configparser import ConfigParser

config = ConfigParser()
config.read("../../config.ini")

config_logging(logging, logging.DEBUG)

api_key = config["keys"]["api_key"]
api_secret = config["keys"]["api_secret"]


client = Client(api_key, api_secret)
logging.info(client.bswap_liquidity_remove("2", "SINGLE", ["BUSD"], "12415"))
logging.info(
    client.bswap_liquidity_remove("2", "COMBINATION", ["BUSD", "USDT"], "12415")
)
