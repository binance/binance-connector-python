#!/usr/bin/env python

import logging
import json
import binance

logging.basicConfig(level=logging.INFO)

key = 'uMaiGTgYH1nLEMRAh2OrpznZHDzCEodtK1xyxYZZt9wtrzVulvNILfawkHxrPFwq'
secret = 'dXSB1pLjt20lwex0MwtecEEOqoBUaJd2wkgUokgmIKWybMqtcPMHJNs40hk4PZtu'

base_url='https://testnet.binance.vision'

test_client = binance.Market(base_url=base_url)

response = test_client.exchange_info()

symbols = []
for symbol in response['symbols']:
    s = {}
    s['symbol'] = symbol['symbol']
    symbols.append(s)


client = binance.Market()
for symbol in symbols:
    ticker = client.ticker_price(symbol['symbol'])
    logging.info('getting ticker for {}'.format(symbol['symbol']))
    symbol['price'] = ticker['price']


test_client = binance.Trade(key, secret, base_url=base_url)

logging.info('start to place orders')
for symbol in symbols:


    qty = 100/float(symbol['price'])
    qty = '{0:.3g}'.format(qty)

    print(qty)

    logging.info('placeing buy order for: {}'.format(symbol['symbol']))
    buy_params = {
        'symbol': symbol['symbol'],
        'side': 'BUY',
        'type': 'LIMIT',
        'timeInForce': 'GTC',
        'quantity': qty,
        'price': symbol['price']
    }

    test_client.new_order(**buy_params)

    logging.info('placeing sell order for: {}'.format(symbol['symbol']))
    sell_params = {
        'symbol': symbol['symbol'],
        'side': 'SELL',
        'type': 'LIMIT',
        'timeInForce': 'GTC',
        'quantity': qty,
        'price': symbol['price']
    }
    test_client.new_order(**sell_params)

