Margin Endpoints
================

Margin Account Borrow/Repay (MARGIN)
------------------------------------
.. autofunction:: binance.spot.Spot.borrow_repay

Get All Margin Assets (MARKET_DATA)
-----------------------------------
.. autofunction:: binance.spot.Spot.margin_all_assets

Get All Margin Pairs (MARKET_DATA)
----------------------------------
.. autofunction:: binance.spot.Spot.margin_all_pairs

Query Margin PriceIndex (MARKET_DATA)
-------------------------------------
.. autofunction:: binance.spot.Spot.margin_pair_index

Margin Account New Order (TRADE)
--------------------------------
.. autofunction:: binance.spot.Spot.new_margin_order

Margin Account Cancel Order (TRADE)
-----------------------------------
.. autofunction:: binance.spot.Spot.cancel_margin_order

Get Transfer History (USER_DATA)
--------------------------------
.. autofunction:: binance.spot.Spot.margin_transfer_history

Query borrow/repay records in Margin account (USER_DATA)
--------------------------------------------------------
.. autofunction:: binance.spot.Spot.borrow_repay_record

Get Interest History (USER_DATA)
--------------------------------
.. autofunction:: binance.spot.Spot.margin_interest_history

Get Force Liquidation Record (USER_DATA)
----------------------------------------
.. autofunction:: binance.spot.Spot.margin_force_liquidation_record

Query Cross Margin Account Details (USER_DATA)
----------------------------------------------
.. autofunction:: binance.spot.Spot.margin_account

Query Margin Account's Order (USER_DATA)
----------------------------------------
.. autofunction:: binance.spot.Spot.margin_order

Query Margin Account's Open Order (USER_DATA)
---------------------------------------------
.. autofunction:: binance.spot.Spot.margin_open_orders

Margin Account Cancel all Open Orders on a Symbol (USER_DATA)
-------------------------------------------------------------
.. autofunction:: binance.spot.Spot.margin_open_orders_cancellation

Query Margin Account's All Orders (USER_DATA)
---------------------------------------------
.. autofunction:: binance.spot.Spot.margin_all_orders

Query Margin Account's Trade List (USER_DATA)
---------------------------------------------
.. autofunction:: binance.spot.Spot.margin_my_trades

Query Max Borrow (USER_DATA)
----------------------------
.. autofunction:: binance.spot.Spot.margin_max_borrowable

Query Max Transfer-Out Amount (USER_DATA)
-----------------------------------------
.. autofunction:: binance.spot.Spot.margin_max_transferable

Query Isolated Margin Account Info (USER_DATA)
----------------------------------------------
.. autofunction:: binance.spot.Spot.isolated_margin_account

Get All Isolated Margin Symbol(USER_DATA)
-----------------------------------------
.. autofunction:: binance.spot.Spot.isolated_margin_all_pairs

Toggle BNB Burn On Spot Trade And Margin Interest (USER_DATA)
-------------------------------------------------------------
.. autofunction:: binance.spot.Spot.toggle_bnbBurn

Get BNB Burn Status (USER_DATA)
-------------------------------
.. autofunction:: binance.spot.Spot.bnbBurn_status

Get Margin Interest Rate History (USER_DATA)
--------------------------------------------
.. autofunction:: binance.spot.Spot.margin_interest_rate_history

Margin Account New OCO (TRADE)
------------------------------
.. autofunction:: binance.spot.Spot.new_margin_oco_order

Margin Account Cancel OCO (TRADE)
---------------------------------
.. autofunction:: binance.spot.Spot.cancel_margin_oco_order

Query Margin Account's OCO (USER_DATA)
--------------------------------------
.. autofunction:: binance.spot.Spot.get_margin_oco_order

Query Margin Account's all OCO (USER_DATA)
------------------------------------------
.. autofunction:: binance.spot.Spot.get_margin_oco_orders

Query Margin Account's Open OCO (USER_DATA)
-------------------------------------------
.. autofunction:: binance.spot.Spot.get_margin_open_oco_orders

Disable Isolated Margin Account (TRADE)
---------------------------------------
.. autofunction:: binance.spot.Spot.cancel_isolated_margin_account

Enable Isolated Margin Account (TRADE)
--------------------------------------
.. autofunction:: binance.spot.Spot.enable_isolated_margin_account

Query Enabled Isolated Margin Account Limit (USER_DATA)
-------------------------------------------------------
.. autofunction:: binance.spot.Spot.isolated_margin_account_limit

Query Cross Margin Fee Data (USER_DATA)
---------------------------------------
.. autofunction:: binance.spot.Spot.margin_fee

Query Isolated Margin Fee Data (USER_DATA)
------------------------------------------
.. autofunction:: binance.spot.Spot.isolated_margin_fee

Query Isolated Margin Tier Data (USER_DATA)
-------------------------------------------
.. autofunction:: binance.spot.Spot.isolated_margin_tier

Query Current Margin Order Count Usage (TRADE)
----------------------------------------------
.. autofunction:: binance.spot.Spot.margin_order_usage

Get Summary of Margin account (USER_DATA)
-----------------------------------------
.. autofunction:: binance.spot.Spot.summary_of_margin_account

Cross margin collateral ratio (MARKET_DATA)
--------------------------------------------
.. autofunction:: binance.spot.Spot.cross_margin_collateral_ratio

Get Small Liability Exchange Coin List (USER_DATA)
--------------------------------------------------
.. autofunction:: binance.spot.Spot.get_small_liability_exchange_coin_list

Get Small Liability Exchange History (USER_DATA)
------------------------------------------------
.. autofunction:: binance.spot.Spot.get_small_liability_exchange_history

Get a future hourly interest rate (USER_DATA)
---------------------------------------------
.. autofunction:: binance.spot.Spot.get_a_future_hourly_interest_rate

Adjust cross margin max leverage (USER_DATA)
--------------------------------------------
.. autofunction:: binance.spot.Spot.adjust_cross_margin_max_leverage

Query Margin Available Inventory (USER_DATA)
---------------------------------------------
.. autofunction:: binance.spot.Spot.margin_available_inventory

Margin manual liquidation (MARGIN)
----------------------------------
.. autofunction:: binance.spot.Spot.margin_manual_liquidation

Query Liability Coin Leverage Bracket in Cross Margin Pro Mode(MARKET_DATA)
---------------------------------------------------------------------------
.. autofunction:: binance.spot.Spot.liability_coin_leverage_bracket
