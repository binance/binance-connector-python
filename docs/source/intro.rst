.. role:: raw-html-m2r(raw)
   :format: html


Binance Public API Connector Python
===================================


.. image:: https://img.shields.io/pypi/v/binance-connector.svg
   :target: https://pypi.org/project/binance-connector/
   :alt: PyPI version


.. image:: https://img.shields.io/pypi/pyversions/binance-connector
   :target: https://www.python.org/downloads/
   :alt: Python version


.. image:: https://img.shields.io/badge/docs-latest-blue
   :target: https://binance-connector.readthedocs.io/en/stable/)
   :alt: Documentation


.. image:: https://img.shields.io/badge/code_style-black-black
   :target: https://black.readthedocs.io/en/stable/
   :alt: Code Style


.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :target: https://opensource.org/licenses/MIT
   :alt: License: MIT


This is a lightweight library that works as a connector to `Binance public API <https://github.com/binance/binance-spot-api-docs>`_.
It's designed to be simple, clean, and easy to use with minimal dependencies.

* Source Code: https://github.com/binance/binance-connector-python
* Official API document:

  * https://github.com/binance/binance-spot-api-docs
  * https://binance-docs.github.io/apidocs/spot/en

* Support channels:

  * Binance developer forum: https://dev.binance.vision/
  * Telegram Channel: https://t.me/binance_api_english

* API key setup: https://www.binance.com/en-NG/support/faq/360002502072
* Testnet API key setup: https://dev.binance.vision/t/99

Features
--------

* Supported APIs:

  * ``/api/*``
  * ``/sapi/*``
  * Spot Websocket Market Stream
  * Spot User Data Stream

* Inclusion of test cases and examples
* Customizable base URL, request timeout and HTTP proxy
* Response metadata can be displayed

Quick Start
-----------

Installation
^^^^^^^^^^^^

* Install via package name

  .. code-block:: bash

     pip install binance-connector

* Alternatively, install with git repository path

  .. code-block:: bash

    python -m pip install git+https://github.com/binance/binance-connector-python.git


Usage
-----

RESTful APIs
^^^^^^^^^^^^

.. code-block:: python

   import logging
   from binance.spot import Spot
   from binance.lib.utils import config_logging

   config_logging(logging, logging.DEBUG)

   client = Spot()
   logging.info(client.time())

   client = Spot(api_key='<api_key>', api_secret='<api_secret>')

   # Get account information
   logging.info(client.account())

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
   logging.info(response)

Please find `examples <https://github.com/binance/binance-connector-python/tree/master/examples>`_ folder to check for more endpoints.


Websocket
^^^^^^^^^

.. code-block:: python

   import logging
   from binance.websocket.spot.websocket_api import SpotWebsocketAPIClient

   def on_close(_):
       logging.info("Do custom stuff when connection is closed")

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

More websocket examples are available in the `examples <https://github.com/binance/binance-connector-python/tree/master/examples>`_ folder
