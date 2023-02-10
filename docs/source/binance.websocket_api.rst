Spot Websocket API
======================

Test connectivity to the WebSocket API
--------------------------------------
.. autofunction:: binance.websocket.spot.websocket_api.SpotWebsocketAPIClient.ping_connectivity

Check server time
-----------------
.. autofunction:: binance.websocket.spot.websocket_api.SpotWebsocketAPIClient.server_time

Get exchange information
------------------------
.. autofunction:: binance.websocket.spot.websocket_api.SpotWebsocketAPIClient.exchange_info

Get order book
--------------
.. autofunction:: binance.websocket.spot.websocket_api.SpotWebsocketAPIClient.order_book

Get historical trades
---------------------
.. autofunction:: binance.websocket.spot.websocket_api.SpotWebsocketAPIClient.historical_trades

Get compressed, aggregate trades
--------------------------------
.. autofunction:: binance.websocket.spot.websocket_api.SpotWebsocketAPIClient.aggregate_trades

klines
------
.. autofunction:: binance.websocket.spot.websocket_api.SpotWebsocketAPIClient.klines

Klines/candlesticks for UI
--------------------------
.. autofunction:: binance.websocket.spot.websocket_api.SpotWebsocketAPIClient.ui_klines

Current average price for a symbol
----------------------------------
.. autofunction:: binance.websocket.spot.websocket_api.SpotWebsocketAPIClient.avg_price

24hr ticker price change statistics
-----------------------------------
.. autofunction:: binance.websocket.spot.websocket_api.SpotWebsocketAPIClient.ticker_24hr

Rolling window price change statistics
--------------------------------------
.. autofunction:: binance.websocket.spot.websocket_api.SpotWebsocketAPIClient.ticker

Symbol price ticker
-------------------
.. autofunction:: binance.websocket.spot.websocket_api.SpotWebsocketAPIClient.ticker_price

Symbol order book ticker
------------------------
.. autofunction:: binance.websocket.spot.websocket_api.SpotWebsocketAPIClient.ticker_book

Account information
-------------------
.. autofunction:: binance.websocket.spot.websocket_api.SpotWebsocketAPIClient.account

Account order rate limits
-------------------------
.. autofunction:: binance.websocket.spot.websocket_api.SpotWebsocketAPIClient.order_rate_limit

Account order history
---------------------
.. autofunction:: binance.websocket.spot.websocket_api.SpotWebsocketAPIClient.order_history

Account OCO history
-------------------
.. autofunction:: binance.websocket.spot.websocket_api.SpotWebsocketAPIClient.oco_history

Account trade history
---------------------
.. autofunction:: binance.websocket.spot.websocket_api.SpotWebsocketAPIClient.my_trades

Account prevented matches
-------------------------
.. autofunction:: binance.websocket.spot.websocket_api.SpotWebsocketAPIClient.prevented_matches

Create a new order
------------------
.. autofunction:: binance.websocket.spot.websocket_api.SpotWebsocketAPIClient.new_order

Test new order
--------------
.. autofunction:: binance.websocket.spot.websocket_api.SpotWebsocketAPIClient.new_order_test

Get order
---------
.. autofunction:: binance.websocket.spot.websocket_api.SpotWebsocketAPIClient.get_order

Cancel order
------------
.. autofunction:: binance.websocket.spot.websocket_api.SpotWebsocketAPIClient.cancel_order

Cancel and replace order
------------------------
.. autofunction:: binance.websocket.spot.websocket_api.SpotWebsocketAPIClient.cancel_replace_order


Current open orders
-------------------
.. autofunction:: binance.websocket.spot.websocket_api.SpotWebsocketAPIClient.get_open_orders

Cancel all open orders on a symbol
----------------------------------
.. autofunction:: binance.websocket.spot.websocket_api.SpotWebsocketAPIClient.cancel_open_orders

Place a new OCO Order
---------------------
.. autofunction:: binance.websocket.spot.websocket_api.SpotWebsocketAPIClient.new_oco_order

Get OCO order
-------------
.. autofunction:: binance.websocket.spot.websocket_api.SpotWebsocketAPIClient.get_oco_order

Cancel OCO order
----------------
.. autofunction:: binance.websocket.spot.websocket_api.SpotWebsocketAPIClient.cancel_oco_order

Get all OCO orders
------------------
.. autofunction:: binance.websocket.spot.websocket_api.SpotWebsocketAPIClient.get_open_oco_orders

Start user data stream
----------------------
.. autofunction:: binance.websocket.spot.websocket_api.SpotWebsocketAPIClient.user_data_start

Ping user data stream
---------------------
.. autofunction:: binance.websocket.spot.websocket_api.SpotWebsocketAPIClient.user_data_ping

Stop user data stream
---------------------
.. autofunction:: binance.websocket.spot.websocket_api.SpotWebsocketAPIClient.user_data_stop
