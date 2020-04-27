# Binance Python Library

## How to use


```python

import binance

client = binance.Market()
print(client.time())

```


## How meta info

Binance API server returns weight usage in the header of each response. This is very useful to indentify the current usage.
To reveal this value, simpily intial the client with `show_weight_usage=True` as:

```python
client = binance.Market(show_weight_usage=True)
print(client.time())
```

the returns will be like:

```json

{'data': {'serverTime': 1587990847650}, 'weight_usage': {'X-MBX-USED-WEIGHT': '31', 'X-MBX-USED-WEIGHT-1M': '31'}}

```

It's also able to print out all headers, which may be very helpful for debug:

```python
client = binance.Market(show_header=True)
print(client.time())
```

the returns will be like:

```json

{'data': {'serverTime': 1587990847650}, 'header': {'Context-Type': 'application/json;charset=utf-8', ...}}

```

