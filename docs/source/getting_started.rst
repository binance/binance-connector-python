.. role:: raw-html-m2r(raw)
   :format: html

Getting Started
===============


Installation
------------

.. code-block:: bash

   pip install binance-connector

How to Generate the API key
---------------------------

One account can have multiple API key and secret key pairs.
Please follow the `step by step tutorial <https://www.binance.com/en-NG/support/faq/360002502072>`_
and create the key on web site or mobile app.

How to Use This Connector
-------------------------

RESTful APIs
^^^^^^^^^^^^

Usage example:

.. code-block:: python

   from binance.spot import Spot

   client = Spot()
   # Get server timestamp
   print(client.time())
   # Get klines of BTCUSDT at 1m interval
   print(client.klines("BTCUSDT", "1m"))
   # Get last 10 klines of BNBUSDT at 1h interval
   print(client.klines("BNBUSDT", "1h", limit=10))

   # api key/secret are required for user data endpoints
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

Please find `examples <https://github.com/binance/binance-connector-python/tree/master/examples>`_ folder to check for more endpoints.

Base URL
""""""""

If ``base_url`` is not provided, it defaults to ``api.binance.com``.\ :raw-html-m2r:`<br/>`

.. code-block:: python

    from binance.spot import Spot as Client

    client = Client(base_url='https://api.binance.com')

It's recommended to pass in the ``base_url`` parameter, even in production as Binance provides alternative URLs
in case of performance issues:


* ``https://api1.binance.com``
* ``https://api2.binance.com``
* ``https://api3.binance.com``

Optional parameters
"""""""""""""""""""

PEP8 suggests *lowercase with words separated by underscores*\ , but for this connector,
the methods' optional parameters should follow their exact naming as in the API documentation, aka camel case.

.. code-block:: python

   # Recognised parameter name
   response = client.cancel_oco_order('BTCUSDT', orderListId=1)

   # Unrecognised parameter name
   response = client.cancel_oco_order('BTCUSDT', order_list_id=1)

RecvWindow parameter
""""""""""""""""""""

An optional parameter ``recvWindow`` is available for endpoints requiring timestamp and signature.\ :raw-html-m2r:`<br/>`
It defaults to ``5000`` (milliseconds) and can be any value lower than ``60000``\ (milliseconds).
Anything beyond the limit will result in an error response from Binance server.

.. code-block:: python

   from binance.spot import Spot as Client

   client = Client(api_key, api_secret)
   response = client.get_order('BTCUSDT', orderId=11, recvWindow=10000)


Websocket
^^^^^^^^^

Usage example:

.. code-block:: python

   import logging
   from binance.websocket.spot.websocket_api import SpotWebsocketAPIClient

   def message_handler(message):
       print(message)

   ws_client = SpotWebsocketAPIClient(on_message=message_handler, on_close=on_close)

   ws_client.ticker(
       symbol='bnbusdt',
       type="FULL",
   )

   # Combine selected streams
   ws_client.ticker(
       symbols=["BNBBUSD", "BTCUSDT"],
       type="MINI",
       windowSize="2h",
   )

   ws_client.stop()

The ``stream_url`` defaults to ``wss://stream.binance.com:9443``.
More websocket examples are available in the `examples <https://github.com/binance/binance-connector-python/tree/master/examples>`_ folder.

Heartbeat
"""""""""

Once connected, the websocket server sends a ping frame every 3 minutes and requires a response pong frame back within
a 10 minutes period. This package handles the pong responses automatically.

Testnet
-------
Testnet is an environment provided for the traders to get familiar with the API usage and behaviour
without the risk of losing funds. It is possible that the price and liquidity are different from the real trading
environment due to the scale difference and the regular data reset.

``/api/*`` endpoints can be tested in Spot Test Network (Spot Testnet).
After creating the API key from `Spot Testnet <https://testnet.binance.vision/>`_, you can access it
by changing the base URL while initiating the API client.

Note: ``/sapi/*`` endpoints don't have testnet environment yet.

API
^^^
.. code-block:: python

   from binance.spot import Spot as Client

   client = Client(base_url='https://testnet.binance.vision')
   print(client.time())


WebSocket
^^^^^^^^^

.. code-block:: python

   from binance.websocket.spot.websocket_api import SpotWebsocketAPIClient

   ws_client = SpotWebsocketAPIClient(stream_url='wss://ws-api.testnet.binance.vision/ws-api/v3')

Errors
------

There are 2 types of error returned from the library with respect to server response:


* ``binance.error.ClientError``

  * This is thrown when server returns ``4XX``\ , it's an issue from client side.
  * It has 4 properties:

    * ``status_code`` - HTTP status code
    * ``error_code`` - Server's error code, e.g. ``-1102``
    * ``error_message`` - Server's error message, e.g. ``Unknown order sent.``
    * ``header`` - Full response header.

* ``binance.error.ServerError``

  * This is thrown when server returns ``5XX``\ , it's an issue from server side.

The library also provides some basic validation towards the required arguments before it sends out the request to the server.
The violation results in any one of the following errors:

* ``binance.error.ParameterRequiredError``

  * This means one (or more) required parameter is missing.

* ``binance.error.ParameterValueError``

  * This means the provided enum value is invalid.

Proxy
-----

Proxy is supported.

.. code-block:: python

   from binance.spot import Spot as Client

   proxies = { 'https': 'http://1.2.3.4:8080' }

   client= Client(proxies=proxies)

Timeout
-------

``timeout`` is available to be assigned with the number of seconds you find most appropriate to wait for a server response.\ :raw-html-m2r:`<br/>`
Please remember the value as it won't be shown in error message *no bytes have been received on the underlying socket for timeout seconds*.\ :raw-html-m2r:`<br/>`
By default, ``timeout`` is None. Hence, requests do not time out.

.. code-block:: python

   from binance.spot import Spot as Client

   client= Client(timeout=1)
