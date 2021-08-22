#!/usr/bin/env python

import logging
from binance.futures import Futures as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

key = '13640e8ceb79ad1782e2afaca8e973dbf419f96cdfa676d8d712f5299716bd67'
secret = '1640294b53dfe5a35a83825ddc82c627bcd5700a43a5bec2760683201aebb0a3'

client = Client(key, secret, base_url="https://testnet.binancefuture.com")


logging.info(client.set_position_side(dual_side_position="true"))
