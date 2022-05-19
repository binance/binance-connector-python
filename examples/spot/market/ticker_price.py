#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

spot_client = Client(base_url="https://testnet.binance.vision")
symbols = ["BTCUSDT", "BNBUSDT"]
symbol = "BNBUSDT"
logging.info(spot_client.ticker_price())
logging.info(spot_client.ticker_price(symbol=symbol))
logging.info(spot_client.ticker_price(symbols=symbols))