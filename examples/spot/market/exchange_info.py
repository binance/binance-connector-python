import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

spot_client = Client(base_url="https://testnet.binance.vision")
symbols = ["BTCUSDT", "BNBUSDT"]
symbol = "BNBUSDT"
logging.info(spot_client.exchange_info())
logging.info(spot_client.exchange_info(symbol=symbol))
logging.info(spot_client.exchange_info(symbols=symbols))
