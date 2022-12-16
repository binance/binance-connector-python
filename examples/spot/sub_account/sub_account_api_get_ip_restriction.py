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

spot_client = Client(api_key, api_secret)

logger = logging.getLogger(__name__)

logger.info(
    spot_client.sub_account_api_get_ip_restriction(
        email="alice@test.com",
        subAccountApiKey="sub_account_api_key",
    )
)
