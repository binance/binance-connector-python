
Changelog
=========

3.7.0 - 2024-05-03
------------------

Added
^^^^^

* Convert

  * ``POST /sapi/v1/convert/limit/placeOrder``
  * ``POST /sapi/v1/convert/limit/cancelOrder``
  * ``GET /sapi/v1/convert/limit/queryOpenOrders``

* Margin

  * ``GET /sapi/v1/margin/available-inventory``
  * ``POST /sapi/v1/margin/manual-liquidation``
  * ``GET /sapi/v1/margin/leverageBracket``

* Market

  * ``GET /api/v3/ticker/tradingDay``

* Trade

  * ``GET /api/v3/myAllocations``
  * ``GET /api/v3/account/commission``

* Wallet

  * ``GET /sapi/v1/capital/deposit/address/list``
  * ``GET /sapi/v1/spot/delist-schedule``

Updated
^^^^^^^

* ``POST /sapi/v1/asset/dust-btc`` add parameter ``accountType``
* ``POST /sapi/v1/asset/dust`` add parameter ``accountType``
* ``GET /sapi/v1/asset/dribblet`` add parameter ``accountType``
* ``POST /sapi/v1/margin/order/oco``: New enumerate value ``AUTO_BORROW_REPAY`` for the field of ``sideEffectType``
* ``POST /sapi/v1/margin/order``: New enumerate value ``AUTO_BORROW_REPAY`` for the field of ``sideEffectType``
* Update documentation
* Add new handle exception in websocket read_data

Removed
^^^^^^^

* Bswap

  * ``GET /sapi/v1/bswap/pools``
  * ``GET /sapi/v1/bswap/liquidity``
  * ``POST /sapi/v1/bswap/liquidityAdd``
  * ``POST /sapi/v1/bswap/liquidityRemove``
  * ``GET /sapi/v1/bswap/liquidityOps``
  * ``GET /sapi/v1/bswap/quote``
  * ``POST /sapi/v1/bswap/swap``
  * ``GET /sapi/v1/bswap/swap``
  * ``GET /sapi/v1/bswap/poolConfigure``
  * ``GET /sapi/v1/bswap/addLiquidityPreview``
  * ``GET /sapi/v1/bswap/removeLiquidityPreview``
  * ``GET /sapi/v1/bswap/unclaimedRewards``
  * ``POST /sapi/v1/bswap/claimRewards``
  * ``GET /sapi/v1/bswap/claimedHistory``

* Loan

  * ``POST /sapi/v1/loan/flexible/borrow``
  * ``GET /sapi/v1/loan/flexible/ongoing/orders``
  * ``GET /sapi/v1/loan/flexible/borrow/history``
  * ``POST /sapi/v1/loan/flexible/repay``
  * ``GET /sapi/v1/loan/flexible/repay/history``
  * ``POST /sapi/v1/loan/flexible/adjust/ltv``
  * ``GET /sapi/v1/loan/flexible/ltv/adjustment/history``
  * ``GET /sapi/v1/loan/flexible/loanable/data``
  * ``GET /sapi/v1/loan/flexible/collateral/data``

* Staking

  * ``GET /sapi/v1/staking/productList``
  * ``POST /sapi/v1/staking/purchase``
  * ``POST /sapi/v1/staking/redeem``
  * ``GET /sapi/v1/staking/position``
  * ``GET /sapi/v1/staking/stakingRecord``
  * ``POST /sapi/v1/staking/setAutoStaking``
  * ``GET /sapi/v1/staking/personalLeftQuota``

3.6.0 - 2024-03-07
------------------

Removed
^^^^^^^

* ``POST /sapi/v1/margin/transfer``
* ``POST /sapi/v1/margin/isolated/transfer``
* ``POST /sapi/v1/margin/loan``
* ``POST /sapi/v1/margin/repay``
* ``GET /sapi/v1/margin/isolated/transfer``
* ``GET /sapi/v1/margin/asset``
* ``GET /sapi/v1/margin/pair``
* ``GET /sapi/v1/margin/isolated/pair``
* ``GET /sapi/v1/margin/loan``
* ``GET /sapi/v1/margin/repay``
* ``GET /sapi/v1/margin/dribblet``
* ``GET /sapi/v1/margin/dust``
* ``POST /sapi/v1/margin/dust``

Added
^^^^^

* ``POST /sapi/v1/margin/borrow-repay``
* ``GET /sapi/v1/margin/borrow-repay``

Updated
^^^^^^^

* ``GET /sapi/v1/margin/transfer`` add parameter ``isolatedSymbol``
* ``GET /sapi/v1/margin/allAssets`` add parameter ``asset``
* ``GET /sapi/v1/margin/allPairs`` add parameter ``symbol``
* ``GET /sapi/v1/margin/isolated/allPairs`` add parameter ``symbol``


3.5.1 - 2023-11-17
------------------

Fixed
^^^^^

* Set the default timeout value to None in WebSocket clients


3.5.0 - 2023-10-26
------------------

Changed
^^^^^^^

* Add timeout parameter to Websocket clients
* Add method for ``GET /sapi/v1/asset/wallet/balance``


3.4.0 - 2023-10-07
------------------

Added
^^^^^

* Portfolio endpoints:

  * ``POST /sapi/v1/portfolio/interest-history``
  * ``POST /sapi/v1/portfolio/asset-index-price``
  * ``POST /sapi/v1/portfolio/auto-collection``
  * ``POST /sapi/v1/portfolio/bnb-transfer``
  * ``POST /sapi/v1/portfolio/repay-futures-switch``
  * ``GET /sapi/v1/portfolio/repay-futures-switch``
  * ``POST /sapi/v1/portfolio/repay-futures-negative-balance``
  * ``POST /sapi/v1/portfolio/asset-collection``

* Convert

  * ``GET /sapi/v1/convert/exchangeInfo``
  * ``GET /sapi/v1/convert/assetInfo``
  * ``POST /sapi/v1/convert/getQuote``
  * ``POST /sapi/v1/convert/acceptQuote``
  * ``GET /sapi/v1/convert/orderStatus``

* Crypto Loan

  * ``POST /sapi/v1/loan/flexible/borrow``
  * ``GET /sapi/v1/loan/flexible/ongoing/order``
  * ``GET /sapi/v1/loan/flexible/borrow/history``
  * ``POST /sapi/v1/loan/flexible/repay``
  * ``GET /sapi/v1/loan/flexible/repay/history``
  * ``POST /sapi/v1/loan/flexible/adjust/ltv``
  * ``GET /sapi/v1/loan/flexible/ltv/adjustment/history``
  * ``GET /sapi/v1/loan/flexible/loanable/data``
  * ``GET /sapi/v1/loan/flexible/collateral/data``

* Margin

  * ``GET /sapi/v1/margin/crossMarginCollateralRatio``
  * ``GET /sapi/v1/margin/exchange-small-liability``
  * ``GET /sapi/v1/margin/exchange-small-liability-history``
  * ``GET /sapi/v1/margin/next-hourly-interest-rate``
  * ``GET /sapi/v1/margin/dust``
  * ``POST /sapi/v1/margin/dust``
  * ``GET /sapi/v1/margin/max-leverage``

* SubAccount

  * ``POST /sapi/v4/sub-account/assets``
  * ``POST /sapi/v1/sub-account/eoptions/enable``
  * ``GET /sapi/v1/sub-account/transaction-statistics``
  * ``GET /sapi/v1/managed-subaccount/query-trans-log``
  * ``GET /sapi/v1/managed-subaccount/info``
  * ``GET /sapi/v1/managed-subaccount/marginAsset``
  * ``GET /sapi/v1/managed-subaccount/fetch-future-asset``
  * ``GET /sapi/v1/sub-account/futures/positionRisk``
  * ``GET /sapi/v1/sub-account/futures/accountSummary``
  * ``GET /sapi/v1/sub-account/futures/account``

* Trade

  * ``GET /api/v3/myPreventedMatches``

* Wallet

  * ``POST /sapi/v1/capital/deposit/credit-apply``

* Simple Earn

  * ``GET /sapi/v1/simple-earn/flexible/list``
  * ``GET /sapi/v1/simple-earn/locked/list``
  * ``POST /sapi/v1/simple-earn/flexible/subscribe``
  * ``POST /sapi/v1/simple-earn/locked/subscribe``
  * ``POST /sapi/v1/simple-earn/flexible/redeem``
  * ``POST /sapi/v1/simple-earn/locked/redeem``
  * ``GET /sapi/v1/simple-earn/flexible/position``
  * ``GET /sapi/v1/simple-earn/locked/position``
  * ``GET /sapi/v1/simple-earn/account``
  * ``GET /sapi/v1/simple-earn/flexible/history/subscriptionRecord``
  * ``GET /sapi/v1/simple-earn/locked/history/subscriptionRecord``
  * ``GET /sapi/v1/simple-earn/flexible/history/redemptionRecord``
  * ``GET /sapi/v1/simple-earn/locked/history/redemptionRecord``
  * ``GET /sapi/v1/simple-earn/flexible/history/rewardsRecord``
  * ``GET /sapi/v1/simple-earn/locked/history/rewardsRecord``
  * ``POST /sapi/v1/simple-earn/flexible/setAutoSubscribe``
  * ``POST /sapi/v1/simple-earn/locked/setAutoSubscribe``
  * ``GET /sapi/v1/simple-earn/flexible/personalLeftQuota``
  * ``GET /sapi/v1/simple-earn/locked/personalLeftQuota``
  * ``GET /sapi/v1/simple-earn/flexible/subscriptionPreview``
  * ``GET /sapi/v1/simple-earn/locked/subscriptionPreview``
  * ``GET /sapi/v1/simple-earn/flexible/history/rateHistory``
  * ``GET /sapi/v1/simple-earn/flexible/history/collateralRecord``

Deleted
^^^^^^^

* ``GET /sapi/v1/lending/daily/product/list``
* ``GET /sapi/v1/lending/daily/userLeftQuota``
* ``POST /sapi/v1/lending/daily/purchase``
* ``GET /sapi/v1/lending/daily/userRedemptionQuota``
* ``POST /sapi/v1/lending/daily/redeem``
* ``GET /sapi/v1/lending/daily/token/position``
* ``GET /sapi/v1/lending/union/account``
* ``GET /sapi/v1/lending/union/purchaseRecord``
* ``GET /sapi/v1/lending/union/redemptionRecord``
* ``GET /sapi/v1/lending/union/interestHistory``
* ``GET /sapi/v1/lending/project/list``
* ``POST /sapi/v1/lending/customizedFixed/purchase``
* ``GET /sapi/v1/lending/project/position/list``
* ``POST /sapi/v1/lending/positionChanged``
* ``GET /sapi/v1/futures/loan/borrow/history``
* ``GET /sapi/v1/futures/loan/repay/history``
* ``GET /sapi/v2/futures/loan/wallet``
* ``GET /sapi/v1/futures/loan/adjustCollateral/history``
* ``GET /sapi/v1/futures/loan/liquidationHistory``
* ``GET /sapi/v1/futures/loan/interestHistory``


Changed
^^^^^^^

* Change ``Loan`` module name to ``Crypto Loan``
* Pump dependencies


3.3.1 - 2023-08-23
------------------

Changed
^^^^^^^

* Add missing enum values in the ``User Universal Transfer`` endpoint


3.3.0 - 2023-08-07
------------------

Changed
^^^^^^^

* Add support for proxy in Websocket clients
* Remove support for python 3.7


3.2.0 - 2023-08-01
------------------

Changed
^^^^^^^

* Changes to ``GET /api/v3/historicalTrades``: api key is not required.


3.1.1 - 2023-07-03
------------------

Changed
^^^^^^^

* Change ``User-Agent``

3.0.0rc2 - 2023-04-21
---------------------

Removed
^^^^^^^

* Removed endpoint ``POST /sapi/v1/sub-account/subAccountApi/ipRestriction/ipList``
* Removed endpoint ``POST /sapi/v1/sub-account/subAccountApi/ipRestriction``

Added
^^^^^

* ``POST /sapi/v2/sub-account/subAccountApi/ipRestriction``
* ``GET /sapi/v1/managed-subaccount/deposit/address``


3.0.0rc1 - 2023-02-10
---------------------

Changed
^^^^^^^

* Redesign of Websocket part. Please consult ``README.md`` for details on its new usage.

Added
^^^^^

* Add Websocket API

2.0.0 - 2023-01-18
------------------

Added
^^^^^

* New endpoints for wallet

  * ``GET /sapi/v1/capital/contract/convertible-coins``` Get a user's auto-conversion settings in deposit/withdrawal
  * ``POST /sapi/v1/capital/contract/convertible-coins`` User can use it to turn on or turn off the BUSD auto-conversion from/to a specific stable coin.
* New endpoints for Sub-Account

  * ``GET /v1/managed-subaccount/queryTransLogForInvestor`` Investor can use this api to query managed sub account transfer log
  * ``GET /v1/managed-subaccount/queryTransLogForTradeParent`` Trading team can use this api to query managed sub account transfer log
* New endpoints for Loan

  * ``GET /sapi/v1/loan/vip/ongoing/orders`` Get VIP Loan Ongoing Orders
  * ``POST /sapi/v1/loan/vip/repay`` VIP Loan Repay
  * ``GET /sapi/v1/loan/vip/repay/history`` Get VIP Loan Repayment History
  * ``GET /sapi/v1/loan/vip/collateral/account`` Check Locked Value of VIP Collateral Account
  * ``GET /sapi/v1/loan/loanable/data`` Get Loanable Assets Data
  * ``GET /sapi/v1/loan/collateral/data`` Get Collateral Assets Data
  * ``GET /sapi/v1/loan/repay/collateral/rate`` Check Collateral Repay Rate
  * ``POST /sapi/v1/loan/customize/margin_call`` Customize margin call for ongoing orders only.
* New endpoints for Wallet

  * ``GET /sapi/v1/asset/ledger-transfer/cloud-mining/queryByPage`` Get Cloud-Mining payment and refund history
  * ``POST /sapi/v1/asset/convert-transfer`` BUSD Convert
  * ``GET /sapi/v1/asset/convert-transfer/queryByPage`` BUSD Convert History
* New endpoint for gift card

  * ``POST /sapi/v1/giftcard/buyCode`` Create a dual-token gift card
  * ``GET /sapi/v1/giftcard/buyCode/token-limit`` Fetch Token Limit


2.0.0rc2 - 2022-11-29
---------------------

Changed
^^^^^^^
* Update version name as hyphens are not recommended.

2.0.0-rc1 - 2022-11-29
----------------------

Added
^^^^^

* Add support for use of RSA Key to generate signatures

1.18.0 - 2022-09-29
-------------------

Added
^^^^^

* New endpoints for Crypto Loan:

  * ``POST /sapi/v1/loan/borrow`` - Crypto Loan Borrow
  * ``GET /sapi/v1/loan/borrow/history`` - Get Loan Borrow History
  * ``GET/sapi/v1/loan/ongoing/orders`` - Get Loan Ongoing Orders
  * ``POST/sapi/v1/loan/repay`` - Crypto Loan Repay
  * ``GET/sapi/v1/loan/repay/history`` - Get Loan Repayment History
  * ``POST/sapi/v1/loan/adjust/ltv`` - Crypto Loan Adjust LTV
  * ``GET/sapi/v1/loan/ltv/adjustment/history`` - Get Loan LTV Adjustment History

Changed
^^^^^^^

* Changes to ``GET /api/v3/exchangeInfo``:

  * New optional parameter ``permissions`` added to display all symbols with the permissions matching the parameter provided (eg.SPOT, MARGIN, LEVERAGED).
  * If not provided, the default value will be ``["SPOT","MARGIN", "LEVERAGED"]``
  * Cannot be combined with symbol or symbols

1.17.0 - 2022-09-05
-------------------

Added
^^^^^

* New endpoint for Market:
  * ``GET /api/v3/uiKlines``

* New kline interval: ``1s``

Changed
^^^^^^^

* Changes to ``GET /api/v3/ticker`` and ``GET /api/v3/ticker/24hr``

  * New optional parameter type added
  * Supported values for parameter type are ``FULL`` and ``MINI``
      * ``FULL`` is the default value and the response that is currently being returned from the endpoint
      * ``MINI`` omits the following fields from the response: ``priceChangePercent``, ``weightedAvgPrice``, ``bidPrice``, ``bidQty``, ``askPrice``, ``askQty``, and ``lastQty``

1.16.0 - 2022-08-11
-------------------

Added
^^^^^

* New endpoint for Portfolio Margin:

  * ``GET /sapi/v1/portfolio/pmLoan`` to query Portfolio Margin Bankruptcy Loan Record.
  * ``POST /sapi/v1/portfolio/repay`` to repay Portfolio Margin Bankruptcy Loan.
  * ``GET /sapi/v1/portfolio/collateralRate`` to get Portfolio Margin Collateral Rate.

Update
^^^^^^

* Changes to ``POST /api/v3/order`` and ``POST /api/v3/order/cancelReplace``

  * New optional field ``strategyId`` is a parameter used to identify an order as part of a strategy.
  * New optional field ``strategyType`` is a parameter used to identify what strategy was running. (E.g. If all the orders are part of spot grid strategy, it can be set to strategyType=1000000)
  * Note: ``strategyType`` cannot be less than 1000000.

* Changes to ``POST /api/v3/order/oco``

  * New optional fields ``limitStrategyId``, ``limitStrategyType``, ``stopStrategyId``, ``stopStrategyType``
  * These are the strategy metadata parameters for both legs of the OCO orders.
  * ``limitStrategyType`` and ``stopStrategyType`` both cannot be less than 1000000.

* ``asset`` is no longer mandatory in ``GET /sapi/v1/lending/project/position/list``

1.15.0 - 2022-07-19
-------------------

Added
^^^^^

* New endpoint for Margin:

  * ``POST /sapi/v3/asset/getUserAsset`` to get user assets.

* New endpoint for Wallet:

  * ``GET /sapi/v1/margin/dribblet`` to query the historical information of user's margin account small-value asset conversion BNB.

1.14.0 - 2022-07-04
-------------------

Added
^^^^^

* New endpoint ``GET /api/v3/ticker``
* New endpoint ``POST /api/v3/order/cancelReplace``
* New websocket stream ``<symbol>@ticker_<window_size>``
* New websocket stream ``!ticker_<window-size>@arr``

Update
^^^^^^

* #146 ``savings_flexible_product_position``  ``asset`` parameter should be optional


1.13.0 - 2022-05-23
-------------------

Added
^^^^^

* New endpoint for Gift Card:

  * ``GET /sapi/v1/giftcard/cryptography/rsa-public-key`` to fetch RSA public key.

* New endpoints for Staking:

  * ``GET /sapi/v1/staking/productList`` to get Staking product list
  * ``POST /sapi/v1/staking/purchase`` to stake product
  * ``POST /sapi/v1/staking/redeem`` to redeem product
  * ``GET /sapi/v1/staking/position`` to get Staking product holding position
  * ``GET /sapi/v1/staking/stakingRecord`` to inquiry Staking history records
  * ``POST /sapi/v1/staking/setAutoStaking`` to set Auto Staking function
  * ``GET /sapi/v1/staking/personalLeftQuota`` to inquiry Staking left quota

Changed
^^^^^^^

* Update endpoints for Market:

  * ``GET /api/v3/ticker/24hr``, ``GET /api/v3/ticker/price`` and ``GET /api/v3/ticker/bookTicker`` new optional parameter symbols.

* Update endpoint for Gift Card:

  * ``POST /sapi/v1/giftcard/redeemCode``: new optional parameter externalUid. Each external unique ID represents a unique user on the partner platform. The function helps you to identify the redemption behavior of different users.


1.12.0 - 2022-05-03
-------------------

Added
^^^^^

* New endpoint ``GET /sapi/v1/managed-subaccount/accountSnapshot`` to support investor master account query asset snapshot of managed sub-account.
* New endpoint ``GET /sapi/v1/portfolio/account`` to support query portfolio margin account info
* New endpoint ``GET /sapi/v1/margin/rateLimit/order``, which will display the user's current margin order count usage for all intervals.



1.11.0 - 2022-02-23
-------------------

Added
^^^^^


* New endpoints for Gift Card (Binance Code in the API Documentation):

  * ``POST /sapi/v1/giftcard/createCode`` to create a Binance Code
  * ``POST /sapi/v1/giftcard/redeemCode`` to redeem a Binance Code
  * ``GET /sapi/v1/giftcard/verify`` to verify a Binance Code

* New endpoint for Wallet:

  * ``POST /sapi/v1/asset/dust-btc`` to get assets that can be converted into BNB

1.10.0 - 2022-01-11
-------------------

Added
^^^^^


* New endpoint for Mining:

  * ``GET /sapi/v1/mining/payment/uid`` to get Mining account earning

* New endpoint for BSwap:

  * ``GET /sapi/v1/bswap/unclaimedRewards`` to get unclaimed rewards record
  * ``POST /sapi/v1/bswap/claimRewards`` to claim swap rewards or liquidity rewards
  * ``GET /sapi/v1/bswap/claimedHistory`` to get history of claimed rewards

Removed
^^^^^^^


* Transfer types ``MAIN_MINING``\ , ``MINING_MAIN``\ , ``MINING_UMFUTURE``\ , ``MARGIN_MINING``\ , and ``MINING_MARGIN`` as they are discontinued in Universal Transfer endpoint ``POST /sapi/v1/asset/transfer`` from January 05, 2022 08:00 AM UTC

1.9.0 - 2021-12-22
------------------

Added
^^^^^


* New endpoint for Convert:

  * ``GET /sapi/v1/convert/tradeFlow`` to support user query convert trade history records

* New endpoint for Rebate:

  * ``GET /sapi/v1/rebate/taxQuery`` to support user query spot rebate history records

* New endpoints for Margin:

  * ``GET /sapi/v1/margin/crossMarginData`` to get cross margin fee data collection
  * ``GET /sapi/v1/margin/isolatedMarginData`` to get isolated margin fee data collection
  * ``GET /sapi/v1/margin/isolatedMarginTier`` to get isolated margin tier data collection

* New endpoints for NFT:

  * ``GET /sapi/v1/nft/history/transactions`` to get NFT transaction history
  * ``GET /sapi/v1/nft/history/deposit`` to get NFT deposit history
  * ``GET /sapi/v1/nft/history/withdraw`` to get NFT withdraw history
  * ``GET /sapi/v1/nft/user/getAsset`` to get NFT asset

1.8.0 - 2021-11-25
------------------

Added
^^^^^


* New endpoint for Crypto Loans:

  * ``GET /sapi/v1/loan/income`` to query an asset's loan history

* New endpoints for Sub-Account:

  * ``POST /sapi/v1/sub-account/subAccountApi/ipRestriction`` to support master account enable and disable IP restriction for a sub-account API Key
  * ``POST /sapi/v1/sub-account/subAccountApi/ipRestriction/ipList`` to support master account add IP list for a sub-account API Key
  * ``GET /sapi/v1/sub-account/subAccountApi/ipRestriction`` to support master account query IP restriction for a sub-account API Key
  * ``DELETE /sapi/v1/sub-account/subAccountApi/ipRestriction/ipList`` to support master account delete IP list for a sub-account API Key

* New endpoint for Pay:

  * ``GET /sapi/v1/pay/transactions`` to support user query Pay trade history

Fixed
^^^^^


* Removed epoch time in util method ``config_logging`` to provide compatibility with Windows OS
* Allow optional parameter for method ``isolated_margin_account_limit``

1.7.0 - 2021-11-04
------------------

Updated
^^^^^^^


* Universal transfer types:

  * Added ``MAIN_FUNDING``\ , ``FUNDING_MAIN``\ , ``FUNDING_UMFUTURE``\ , ``UMFUTURE_FUNDING``\ , ``MARGIN_FUNDING``\ , ``FUNDING_MARGIN``\ , ``FUNDING_CMFUTURE`` and ``CMFUTURE_FUNDING`` to support transfer assets among funding account and other accounts
  * Deleted ``MAIN_C2C``\ , ``C2C_MAIN``\ , ``C2C_UMFUTURE``\ , ``C2C_MINING``\ , ``UMFUTURE_C2C``\ , ``MINING_C2C``\ , ``MARGIN_C2C``\ , ``C2C_MARGIN``\ , ``MAIN_PAY`` and ``PAY_MAIN`` as C2C account, Binance Payment, Binance Card and other business accounts are merged into a Funding account and they'll be discontinued on November 04, 2021 08:00 AM UTC

* Util method ``config_logging`` can now provide date time in UTC and epoch time

Added
^^^^^


* New endpoint ``GET api/v3/rateLimit/order`` to display the user's current order count usage for all intervals

1.6.0 - 2021-09-24
------------------

Added
^^^^^


* Universal transfer types ``MAIN_PAY``\ , ``PAY_MAIN``\ , ``ISOLATEDMARGIN_MARGIN``\ ，\ ``MARGIN_ISOLATEDMARGIN``\ ，\ ``ISOLATEDMARGIN_ISOLATEDMARGIN``
* New endpoints for Margin OCO orders:

  * ``POST /sapi/v1/margin/order/oco`` to send new margin OCO order
  * ``DELETE /sapi/v1/margin/orderList`` to cancel margin OCO order
  * ``GET /sapi/v1/margin/orderList`` to query a margin OCO order
  * ``GET /sapi/v1/margin/allOrderList`` to query all margin OCO orders
  * ``GET /sapi/v1/margin/openOrderList`` to query open margin OCO orders

* New endpoints for Isolated Margin:

  * ``DELETE /sapi/v1/margin/isolated/account`` to disable isolated margin account for a specific symbol
  * ``POST /sapi/v1/margin/isolated/account`` to enable isolated margin account for a specific symbol
  * ``GET /sapi/v1/margin/isolated/accountLimit`` to query num of enabled isolated margin accounts and its max limit

* New endpoints for BSwap:

  * ``GET /sapi/v1/bswap/poolConfigure`` to get pool configure
  * ``GET /sapi/v1/bswap/addLiquidityPreview`` to calculate expected share amount for adding liquidity in single or dual token
  * ``GET /sapi/v1/bswap/removeLiquidityPreview`` to calculate expected asset amount of single token redemption or dual token redemption

1.5.0 - 2021-08-17
------------------

Changed
^^^^^^^


* ``GET api/v3/exchangeInfo`` now supports single or multi-symbol query
* ``GET api/v3/myTrades`` has a new optional field ``orderId``

Added
^^^^^


* ``GET /sapi/v1/c2c/orderMatch/listUserOrderHistory`` to query user C2C trade history

1.4.0 - 2021-07-30
------------------

Added
^^^^^


* New Fiat endpoints:

  * ``GET /sapi/v1/fiat/orders`` to query user fiat deposit and withdraw history
  * ``GET /sapi/v1/fiat/payments`` to query user fiat payments history

Fixed
^^^^^


* Typo in ``margin_max_transferable``

1.3.0 - 2021-07-22
------------------

Added
^^^^^


* New endpoints for Wallet:

  * ``POST /sapi/v1/asset/get-funding-asset`` to query funding wallet, includes Binance Pay, Binance Card, Binance Gift Card, Stock Token
  * ``GET /sapi/v1/account/apiRestrictions`` to query user API Key permission

1.2.0 - 2021-07-12
------------------

Changed
^^^^^^^


* Remove default value in the parameters

1.1.1 - 2021-06-24
------------------

Changed
^^^^^^^


* Upgrade the dependency packages

1.1.0 - 2021-06-23
------------------

Added
^^^^^


* A link to the document on ``README.md``
* Enabled the sub menu on document nav bar.
* ``GET /sapi/v1/lending/daily/product/list`` includes new parameters, current and size.
* New endpoints for Sub-Account:

  * ``POST /sapi/v1/managed-subaccount/deposit`` to deposit assets into the managed sub-account (only for investor master account)
  * ``GET /sapi/v1/managed-subaccount/asset`` to query managed sub-account asset details (only for investor master account)
  * ``POST /sapi/v1/managed-subaccount/withdraw`` to withdrawal assets from the managed sub-account (only for investor master account)

1.0.0 - 2021-06-15
------------------

Added
^^^^^


* First release, please find details from ``README.md``
