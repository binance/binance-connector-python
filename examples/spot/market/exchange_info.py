import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

spot_client = Client()

logging.info(spot_client.exchange_info())

logging.info(spot_client.exchange_info(symbol="BNBUSDT"))
logging.info(spot_client.exchange_info(symbols=["BTCUSDT", "BNBUSDT"]))

logging.info(spot_client.exchange_info(permissions=["MARGIN"]))
logging.info(spot_client.exchange_info(permissions=["MARGIN", "LEVERAGED"]))
