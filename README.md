# Binance Public API connector Python

This is a thin library that working as a connector to the Binance public API. 

## Todo list (for dev only)

- [x] all api endpoints
- [x] better logging
- [x] more examples
- [ ] better readme
- [ ] pipeline, Actions or travis-ci?

## How to use

```python

import binance

client = binance.Market()
print(client.time())

client = binance.Trade(key='xxx', secret='xxxxx')

# get account information
print(client.account())

# post a new order

params = {
    'symbol': 'BTCUSDT',
    'side': 'SELL',
    'type': 'LIMIT',
    'timeInForce': 'GTC',
    'quantity': 0.002,
    'price': 9500
}

response = client.new_order(**params)
print(response)

```

please find `examples` folder for more endpoints

### Testnet

The [spot testnet](https://testnet.binance.vision/) is available. In order to test on testnet:

```python

market_client= binance.Market(base_url='https://testnet.binance.vision')
print(market_client.time())

```

Without providing the base url, this connector works on `api.binance.com`.<br/>

It's recommended to allow changing the base url even in production <br/>
In some rare case, Binance may offer a backup base url.

## Display meta info

Binance API server returns weight usage in the header of each response. This is very useful to indentify the current usage.
To reveal this value, simpily intial the client with `show_weight_usage=True` as:

```python
client = binance.Market(show_weight_usage=True)
print(client.time())
```

the returns will be like:

```python

{'data': {'serverTime': 1587990847650}, 'weight_usage': {'X-MBX-USED-WEIGHT': '31', 'X-MBX-USED-WEIGHT-1M': '31'}}

```

It's also able to print out all headers, which may be very helpful for debug:

```python
client = binance.Market(show_header=True)
print(client.time())
```

the returns will be like:

```python

{'data': {'serverTime': 1587990847650}, 'header': {'Context-Type': 'application/json;charset=utf-8', ...}}

```

## Display logs

Set log level to `DEBUG`, it will show request url and payload, also the response text will be logged.
Known what parameters and the values sending to server is essential during debug.

## Python version
3.5+
