# Binance Public API connector Python

This is a thin library that working as a connector to the Binance public API.

- aiming to support all endpoints
- thin layer, easy to use
- test cases included
- enable to change base url
- display weight usage or whole response header

## RESTful APIs

```python

from binance.spot import Spot

client = Spot()
print(client.time())

client = Spot(key='xxx', secret='xxxxx')

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

from binance.spot import Spot as Client

client = Client(base_url='https://testnet.binance.vision')
print(client.time())

```

Without providing the base url, this connector works on `api.binance.com` by default.<br/>

It's recommended to allow changing the base url even in production.<br/>
In some rare case, Binance may offer a backup base url.

### RecvWindow

From Binance API, `recvWindow` is available for all endpoints require signature. By default, it's 5000ms.
You are allowed to set this parameter to any value less than 60000, number beyond this limit will receive error from Binance server.

```python

from binance.spot import Spot as Client

client = Client(key, secret)
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

### Timeout

`timeout` is supported and recommend to set a proper time as in second. Be sure you know this value as "no bytes have been received on the underlying socket for timeout seconds".
if not set, request do not time out.

```python

from binance.spot import Spot as Client

client= Client(timeout=1)

```

### Proxy

Proxy is supported.

```python

from binance.spot import Spot as Client

proxies = {
    'http': 'http://1.2.3.4:8080',
    'https': 'http://1.2.3.4:8080'
}

client= Client(proxies=proxies)

```


### Display meta info

Binance API server returns weight usage in the header of each response. This is very useful to indentify the current usage.
To reveal this value, simpily intial the client with `show_weight_usage=True` as:

```python
from binance.spot import Spot as Client

client = Client(show_weight_usage=True)
print(client.time())
```

the returns will be like:

```python

{'data': {'serverTime': 1587990847650}, 'weight_usage': {'X-MBX-USED-WEIGHT': '31', 'X-MBX-USED-WEIGHT-1M': '31'}}

```

It's also able to print out all headers, which may be very helpful for debug:

```python
client = Client(show_header=True)
print(client.time())
```

the returns will be like:

```python

{'data': {'serverTime': 1587990847650}, 'header': {'Context-Type': 'application/json;charset=utf-8', ...}}

```

### Display logs
Set log level to `DEBUG`, it will show request url and payload, also the response text will be logged.
Known what parameters and the values sending to server is essential during debug.


## Websocket

```python
from binance.websocket.spot.websocket_client import SpotWebsocketClient as WebsocketClient

def message_handler(message):
    print(message)

ws_client = WebsocketClient()
ws_client.start()

ws_client.mini_ticker(
    symbol='bnbusdt',
    id=1,
    callback=message_handler,
)

# combine selected streams
ws_client.instant_subscribe(
    stream=['bnbusdt@bookTicker', 'ethusdt@bookTicker'],
    callback=message_handler,
)

ws_client.stop()
```

please find `examples` folder for more websocket usages.

### Heartbeat
Server send ping frame every 3 minutes and require to response pong within 10 minutes. This package response automatically.

### Testnet
```python
from binance.websocket.spot.websocket_client import SpotWebsocketClient as WebsocketClient

ws_client = WebsocketClient(stream_url='wss://testnet.binance.vision')

```

## Test case

```python

# if you haven't installed the packages yet
pip install -r requirements-test.txt

pytest
```

## Python version
3.6+

## Limitation
- support `/api/*` only now, but will add more endpoints

## Found :bug:
Please open an issue

## Found API issue
Open a topic at [Binance Developer Community](https://dev.binance.vision)

## Contribution

contribution is welcome, support endpoints from:

https://binance-docs.github.io/apidocs/spot/en

- should pass all test cases
- pass pep8 check, ignore E501

## License
MIT
