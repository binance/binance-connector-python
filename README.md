# Binance Public API Connector Python
[![PyPI version](https://img.shields.io/pypi/v/binance-connector)](https://pypi.python.org/pypi/binance-connector)
[![Python version](https://img.shields.io/pypi/pyversions/binance-connector)](https://www.python.org/downloads/)
[![Documentation](https://img.shields.io/badge/docs-latest-blue)](https://binance-connector.readthedocs.io/en/stable/)
[![Code Style](https://img.shields.io/badge/code_style-black-black)](https://black.readthedocs.io/en/stable/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is a lightweight library that works as a connector to [Binance public API](https://github.com/binance/binance-spot-api-docs)

- Supported APIs:
    - `/api/*`
    - `/sapi/*`
    - Spot Websocket Market Stream
    - Spot User Data Stream
    - Spot WebSocket API
- Inclusion of test cases and examples
- Customizable base URL, request timeout and HTTP proxy
- Response metadata can be displayed

## Installation

```bash
pip install binance-connector
```

## Documentation

[https://binance-connector.readthedocs.io](https://binance-connector.readthedocs.io)

## RESTful APIs

Usage examples:
```python
from binance.spot import Spot

client = Spot()

# Get server timestamp
print(client.time())
# Get klines of BTCUSDT at 1m interval
print(client.klines("BTCUSDT", "1m"))
# Get last 10 klines of BNBUSDT at 1h interval
print(client.klines("BNBUSDT", "1h", limit=10))

# API key/secret are required for user data endpoints
client = Spot(api_key='<api_key>', api_secret='<api_secret>')

# Get account and balance information
print(client.account())

# Post a new order
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
Please find `examples` folder to check for more endpoints.
- In order to set your API and Secret Key for use of the examples, create a file `examples/config.ini` with your keys.
- Eg:
    ```ini
    # examples/config.ini
    [keys]
    api_key=abc123456
    api_secret=cba654321
    ```

### Authentication

Binance supports HMAC, RSA and ED25519 API authentication.

```python

# HMAC: pass API key and secret
client = Client(api_key, api_secret)
print(client.account())

# RSA Keys
client = Client(api_key=api_key, private_key=private_key)
print(client.account())

# ED25519 Keys
api_key = ""
private_key = "./private_key.pem"
private_key_pass = "<password_if_applicable>"

with open(private_key, 'rb') as f:
    private_key = f.read()

spot_client = Client(api_key=api_key, private_key=private_key, private_key_pass=private_key_pass)

# Encrypted RSA Key
client = Client(api_key=api_key, private_key=private_key, private_key_pass='password')
print(client.account())
```
Please find `examples/spot/wallet/account_snapshot.py` for more details on ED25519.
Please find `examples/spot/trade/get_account.py` for more details on RSA.

### Testnet

[Spot Testnet](https://testnet.binance.vision/) is available, it can be used to test `/api/*` endpoints.

- `/sapi/*` endpoints are not available.
- No UI.
- Steps to setup testnet API key.  [https://dev.binance.vision/t/99](https://dev.binance.vision/t/99)

To use testnet:
```python
from binance.spot import Spot as Client

client = Client(base_url='https://testnet.binance.vision')
print(client.time())
```

### Base URL

If `base_url` is not provided, it defaults to `api.binance.com`.<br/>
It's recommended to pass in the `base_url` parameter, even in production as Binance provides alternative URLs
in case of performance issues:
- `https://api1.binance.com`
- `https://api2.binance.com`
- `https://api3.binance.com`

### Optional parameters

PEP8 suggests _lowercase with words separated by underscores_, but for this connector,
the methods' optional parameters should follow their exact naming as in the API documentation.

```python
# Recognised parameter name
response = client.cancel_oco_order('BTCUSDT', orderListId=1)

# Unrecognised parameter name
response = client.cancel_oco_order('BTCUSDT', order_list_id=1)
```

### RecvWindow parameter

Additional parameter `recvWindow` is available for endpoints requiring signature.<br/>
It defaults to `5000` (milliseconds) and can be any value lower than `60000`(milliseconds).
Anything beyond the limit will result in an error response from Binance server.

```python
from binance.spot import Spot as Client

client = Client(api_key, api_secret)
response = client.get_order('BTCUSDT', orderId=11, recvWindow=10000)
```

### Timeout

`timeout` is available to be assigned with the number of seconds you find most appropriate to wait for a server response.<br/>
Please remember the value as it won't be shown in error message _no bytes have been received on the underlying socket for timeout seconds_.<br/>
By default, `timeout` is None. Hence, requests do not time out.

```python
from binance.spot import Spot as Client

client= Client(timeout=1)
```

### Proxy

Proxy is supported.

```python
from binance.spot import Spot as Client

proxies = { 'https': 'http://1.2.3.4:8080' }

client= Client(proxies=proxies)
```


### Response Metadata

The Binance API server provides weight usages in the headers of each response.
You can display them by initializing the client with `show_limit_usage=True`:

```python
from binance.spot import Spot as Client

client = Client(show_limit_usage=True)
print(client.time())
```
returns:

```python
{'data': {'serverTime': 1587990847650}, 'limit_usage': {'x-mbx-used-weight': '31', 'x-mbx-used-weight-1m': '31'}}
```
You can also display full response metadata to help in debugging:

```python
client = Client(show_header=True)
print(client.time())
```

returns:

```python
{'data': {'serverTime': 1587990847650}, 'header': {'Context-Type': 'application/json;charset=utf-8', ...}}
```

If `ClientError` is received, it'll display full response meta information.

### Display logs

Setting the log level to `DEBUG` will log the request URL, payload and response text.

### Error

There are 2 types of error returned from the library:
- `binance.error.ClientError`
    - This is thrown when server returns `4XX`, it's an issue from client side.
    - It has 5 properties:
        - `status_code` - HTTP status code
        - `error_code` - Server's error code, e.g. `-1102`
        - `error_message` - Server's error message, e.g. `Unknown order sent.`
        - `header` - Full response header.
        - `error_data`* - Additional detailed data which supplements the `error_message`.
            - **Only applicable on select endpoints, eg. `cancelReplace`*
- `binance.error.ServerError`
    - This is thrown when server returns `5XX`, it's an issue from server side.

## Websocket

### Connector v3

WebSocket can be established through either of the following types of connections:
- WebSocket API (`https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-api.md`)
- WebSocket Stream (`https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md`)

```python

# WebSocket API Client
from binance.websocket.spot.websocket_api import SpotWebsocketAPIClient

def message_handler(_, message):
    logging.info(message)

my_client = SpotWebsocketAPIClient(on_message=message_handler)

my_client.ticker(symbol="BNBBUSD", type="FULL")

time.sleep(5)
logging.info("closing ws connection")
my_client.stop()
```

```python

# WebSocket Stream Client
from binance.websocket.spot.websocket_stream import SpotWebsocketStreamClient

def message_handler(_, message):
    logging.info(message)

my_client = SpotWebsocketStreamClient(on_message=message_handler)

# Subscribe to a single symbol stream
my_client.agg_trade(symbol="bnbusdt")
time.sleep(5)
logging.info("closing ws connection")
my_client.stop()
```

#### Proxy

Proxy is supported for both WebSocket API and WebSocket Stream.

To use it, pass in the `proxies` parameter when initializing the client.

The format of the `proxies` parameter is the same as the one used in the Spot RESTful API.

It consists on a dictionary with the following format, where the key is the type of the proxy and the value is the proxy URL:

For websockets, the proxy type is `http`.

```python
proxies = { 'http': 'http://1.2.3.4:8080' }
```

You can also use authentication for the proxy by adding the `username` and `password` parameters to the proxy URL:

```python
proxies = { 'http': 'http://username:password@host:port' }
```


```python

# WebSocket API Client
from binance.websocket.spot.websocket_api import SpotWebsocketAPIClient

def message_handler(_, message):
    logging.info(message)

proxies = { 'http': 'http://1.2.3.4:8080' }

my_client = SpotWebsocketAPIClient(on_message=message_handler, proxies=proxies, timeout=10)

my_client.ticker(symbol="BNBBUSD", type="FULL")

time.sleep(5)
logging.info("closing ws connection")
my_client.stop()
```

```python

# WebSocket Stream Client
from binance.websocket.spot.websocket_stream import SpotWebsocketStreamClient

def message_handler(_, message):
    logging.info(message)

proxies = { 'http': 'http://1.2.3.4:8080' }

my_client = SpotWebsocketStreamClient(on_message=message_handler, proxies=proxies, timeout=10)

# Subscribe to a single symbol stream
my_client.agg_trade(symbol="bnbusdt")
time.sleep(5)
logging.info("closing ws connection")
my_client.stop()
```

#### Request Id

Client can assign a request id to each request. The request id will be returned in the response message. Not mandatory in the library, it generates a uuid format string if not provided.

```python
# id provided by client
my_client.ping_connectivity(id="my_request_id")

# library will generate a random uuid string
my_client.ping_connectivity()
```

#### Combined Streams
- If you set `is_combined` to `True`, `"/stream/"` will be appended to the `baseURL` to allow for Combining streams.
- `is_combined` defaults to `False` and `"/ws/"` (raw streams) will be appended to the `baseURL`.

More websocket examples are available in the `examples` folder.

Example file "examples/websocket_api/app_demo.py" demonstrates how Websocket API and Websocket Stream can be used together.

### Connector v1 and v2

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

# Combine selected streams
ws_client.instant_subscribe(
    stream=['bnbusdt@bookTicker', 'ethusdt@bookTicker'],
    callback=message_handler,
)

ws_client.stop()
```

### Heartbeat

Once connected, the websocket server sends a ping frame every 3 minutes and requires a response pong frame back within
a 10 minutes period. This package handles the pong responses automatically.

### Testnet

```python
from binance.websocket.spot.websocket_client import SpotWebsocketClient as WebsocketClient

ws_client = WebsocketClient(stream_url='wss://stream.testnet.binance.vision')
```

## Test Case

```python
# In case packages are not installed yet
pip install -r requirements/requirements-test.txt

python -m pytest tests/
```

## Limitation

Futures and Vanilla Options APIs are not supported:
  - `/fapi/*`
  - `/dapi/*`
  - `/vapi/*`
  -  Associated Websocket Market and User Data Streams

## Contributing

Contributions are welcome.<br/>
If you've found a bug within this project, please open an issue to discuss what you would like to change.<br/>
If it's an issue with the API, please open a topic at [Binance Developer Community](https://dev.binance.vision)
