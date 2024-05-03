Account / Trade Endpoints
=========================


Test New Order (TRADE)
----------------------
.. autofunction:: binance.spot.Spot.new_order_test

New Order (TRADE)
-----------------
.. autofunction:: binance.spot.Spot.new_order

Cancel Order (TRADE)
--------------------
.. autofunction:: binance.spot.Spot.cancel_order

Cancel all Open Orders on a Symbol (TRADE)
------------------------------------------
.. autofunction:: binance.spot.Spot.cancel_open_orders

Query Order (USER_DATA)
-----------------------
.. autofunction:: binance.spot.Spot.get_order

Cancel an Existing Order and Send a New Order (USER_DATA)
---------------------------------------------------------
.. autofunction:: binance.spot.Spot.cancel_and_replace

Current Open Orders (USER_DATA)
-------------------------------
.. autofunction:: binance.spot.Spot.get_open_orders

All Orders (USER_DATA)
----------------------
.. autofunction:: binance.spot.Spot.get_orders

New OCO (TRADE)
---------------
.. autofunction:: binance.spot.Spot.new_oco_order

Cancel OCO (TRADE)
------------------
.. autofunction:: binance.spot.Spot.cancel_oco_order

Query OCO (USER_DATA)
---------------------
.. autofunction:: binance.spot.Spot.get_oco_order

Query all OCO (USER_DATA)
-------------------------
.. autofunction:: binance.spot.Spot.get_oco_orders

Query Open OCO (USER_DATA)
--------------------------
.. autofunction:: binance.spot.Spot.get_oco_open_orders

Account Information (USER_DATA)
-------------------------------
.. autofunction:: binance.spot.Spot.account

Account Trade List (USER_DATA)
------------------------------
.. autofunction:: binance.spot.Spot.my_trades

Query Current Order Count Usage (TRADE)
---------------------------------------
.. autofunction:: binance.spot.Spot.get_order_rate_limit

Query Prevented Matches (USER_DATA)
-----------------------------------
.. autofunction:: binance.spot.Spot.query_prevented_matches

Query Cross-Collateral Information (USER_DATA)
----------------------------------------------
.. autofunction:: binance.spot.Spot.query_allocations

Query Commission Rates (USER_DATA)
----------------------------------
.. autofunction:: binance.spot.Spot.query_commission_rates
