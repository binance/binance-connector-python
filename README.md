# Binance Public API connector Python

This is a thin library that working as a connector to the Binance public API.

- aiming to support all endpoints
- thin layer, easy to use
- test cases included
- enable to change base url
- display weight usage or whole response header

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

Without providing the base url, this connector works on `api.binance.com` by default.<br/>

It's recommended to allow changing the base url even in production.<br/>
In some rare case, Binance may offer a backup base url.

### RecvWindow

From Binance API, `recvWindow` is available for all endpoints require signature. By default, it's 5000ms.
You are allowed to set this parameter to any value less than 60000, number beyond this limit will receive error from Binance server.

```python

client = binance.Trade(key, secret)
response = client.get_order('BTCUSDT', orderId='11', recvWindow=10000)

```

### Optional parameters

For the optional parameters in the endpoint, pass exactly the field name from API document into method. e.g

```python

# correct
response = client.cancel_oco_order('BTCUSDT', orderListId=1)

# this is incorrect
response = client.cancel_oco_order('BTCUSDT', order_list_id=1)
```

PEP8 suggest method name as "lowercase with words separated by underscores", but not here. Let's follow the document, copy the name from there.



### Display meta info

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

### Display logs
Set log level to `DEBUG`, it will show request url and payload, also the response text will be logged.
Known what parameters and the values sending to server is essential during debug.

## Test case

```python

# if you haven't installed the packages yet
pip install -r requirements.txt

pytest
```

## Python version
3.5+

## Limitation
- support `/api/*` only now, but will add more endpoints

## Found :bug:
Please open an issue

## Found API issue
Open a topic at [Binance Developer Community](https://dev.binance.vision)

## Contribution

contribution is welcome, support endpoints from:

https://binance-docs.github.io/apidocs/spot/en/#general-info

## License
MIT
