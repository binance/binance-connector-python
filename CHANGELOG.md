# Changelog
## 3.13.0 - 2025-01-31
### Added
- Staking
  - `GET /sapi/v1/sol-staking/account`
  - `GET /sapi/v1/sol-staking/sol/quota`
  - `POST /sapi/v1/sol-staking/sol/stake`
  - `POST /sapi/v1/sol-staking/sol/redeem`
  - `POST /sapi/v1/sol-staking/sol/claim`
  - `GET /sapi/v1/sol-staking/sol/history/stakingHistory`
  - `GET /sapi/v1/sol-staking/sol/history/redemptionHistory`
  - `GET /sapi/v1/sol-staking/sol/history/bnsolRewardsHistory`
  - `GET /sapi/v1/sol-staking/sol/history/rateHistory`
  - `GET /sapi/v1/sol-staking/sol/history/boostRewardsHistory`
  - `GET /sapi/v1/sol-staking/sol/history/unclaimedRewards`

## 3.12.0 - 2025-01-13
### Changed
- Updated documentation links.

### Removed
- Crypto-loans
  - `GET /sapi/v1/loan/repay/collateral/rate`

## 3.11.0 - 2024-12-19
### Added
- A new optional parameter `time_unit` can be used to select the time unit.

## 3.10.0 - 2024-11-29
### Added
- Margin
  - `POST /sapi/v1/margin/order/oto`
  - `POST /sapi/v1/margin/order/otoco`

- Portfolio
  - `GET /sapi/v2/portfolio/account`
  - `GET /sapi/v1/portfolio/balance`
  - `GET /sapi/v2/portfolio/collateralRate`

- Simple Earn
  - `POST /sapi/v1/simple-earn/locked/setRedeemOption`

- Staking
  - `GET /sapi/v2/eth-staking/account`
  - `GET /sapi/v1/eth-staking/eth/quota`
  - `POST /sapi/v2/eth-staking/eth/stake`
  - `POST /sapi/v1/eth-staking/eth/redeem`
  - `POST /sapi/v1/eth-staking/wbeth/wrap`
  - `GET /sapi/v1/eth-staking/eth/history/stakingHistory`
  - `GET /sapi/v1/eth-staking/eth/history/redemptionHistory`
  - `GET /sapi/v1/eth-staking/eth/history/rewardsHistory`
  - `GET /sapi/v1/eth-staking/eth/history/wbethRewardsHistory`
  - `GET /sapi/v1/eth-staking/eth/history/rateHistory`
  - `GET /sapi/v1/eth-staking/wbeth/history/wrapHistory`
  - `GET /sapi/v1/eth-staking/wbeth/history/unwrapHistory`

- Wallet
  - `POST /sapi/v1/localentity/withdraw/apply`
  - `GET /sapi/v1/localentity/withdraw/history`
  - `PUT /sapi/v1/localentity/deposit/provide-info`
  - `GET /sapi/v1/localentity/deposit/history`

- Websocket Stream
  - `<symbol>kline_<interval>+08:00`

### Updated
- Add parameters showPermissionSets and symbolStatus to `GET /api/v3/exchangeInfo`
- Add parameter timeZone to `GET /api/v3/klines`, `GET /api/v3/uiKlines`, `klines` and `uiKlines`
- Add parameter redeemTo to `POST /sapi/v1/simple-earn/locked/subscribe`
- Add parameters `txId` and `includeSource` to `GET /sapi/v1/capital/deposit/hisrec`
- Add parameter `idList` to `GET /sapi/v1/capital/withdraw/history` and `GET /sapi/v1/capital/deposit/subHisrec`
- Update Documentation
- Update `JSONDecodeError` error response

### Removed
- Crypto-loans
  - `GET /sapi/v1/loan/collateral/data`
  - `POST /sapi/v1/loan/borrow`
  - `POST /sapi/v1/loan/repay`
  - `POST /sapi/v1/loan/adjust/ltv`
  - `POST /sapi/v1/loan/customize/margin_call`
  - `GET /sapi/v1/loan/ongoing/orders`


## 3.9.0 - 2024-10-02

### Removed
- Futures
  - `POST /sapi/v1/futures/transfer`
  - `GET /sapi/v1/futures/transfer`

- BLVT
  - `GET /sapi/v1/blvt/tokenInfo`
  - `POST /sapi/v1/blvt/subscribe`
  - `GET /sapi/v1/blvt/subscribe/record`
  - `POST /sapi/v1/blvt/redeem`
  - `GET /sapi/v1/blvt/redeem/record`
  - `GET /sapi/v1/blvt/userLimit`

- Wallet
  - `POST /sapi/v1/asset/convert-transfer`
  - `GET /sapi/v1/asset/convert-transfer/queryByPage`
  - `GET /sapi/v1/capital/contract/convertible-coins`
  - `POST /sapi/v1/capital/contract/convertible-coins`

## 3.8.1 - 2024-07-25
### Added
- `.readthedocs.yml` to resolve documentation issue

### Changed
- `GET /api/v3/account` has a new optional parameter `omitZeroBalances`, which if enabled hides all zero balances.
- `POST /api/v3/order/cancelReplace` has a new optional parameter `orderRateLimitExceededMode`.

## 3.8.0 - 2024-07-04
### Added
- Trade
  - Spot
    - `POST /api/v3/orderList/oto`
    - `POST /api/v3/orderList/otoco`
  - Websocket API
    - `orderList.place.oto`
    - `orderList.place.otoco`

### Updated
- Updated and Resolved documentation issue
- Updated `Restful` OCO trade deprecated endpoint `POST /api/v3/order/oco` to `POST /api/v3/orderList/oco`
- Updated `Websocket API` OCO trade deprecated endpoint `orderList.place` to `orderList.place.oco`

## 3.7.0 - 2024-05-03
### Added
- Convert
  - `POST /sapi/v1/convert/limit/placeOrder`
  - `POST /sapi/v1/convert/limit/cancelOrder`
  - `GET /sapi/v1/convert/limit/queryOpenOrders`

- Margin
  - `GET /sapi/v1/margin/available-inventory`
  - `POST /sapi/v1/margin/manual-liquidation`
  - `GET /sapi/v1/margin/leverageBracket`

- Market
  - `GET /api/v3/ticker/tradingDay`

- Trade
  - `GET /api/v3/myAllocations`
  - `GET /api/v3/account/commission`

- Wallet
  - `GET /sapi/v1/capital/deposit/address/list`
  - `GET /sapi/v1/spot/delist-schedule`

### Updated
- `POST /sapi/v1/asset/dust-btc` add parameter `accountType`
- `POST /sapi/v1/asset/dust` add parameter `accountType`
- `GET /sapi/v1/asset/dribblet` add parameter `accountType`
- `POST /sapi/v1/margin/order/oco`: New enumerate value `AUTO_BORROW_REPAY` for the field of `sideEffectType`
- `POST /sapi/v1/margin/order`: New enumerate value `AUTO_BORROW_REPAY` for the field of `sideEffectType`
- Update documentation
- Add new handle exception in websocket read_data

### Removed
- Bswap
  - `GET /sapi/v1/bswap/pools`
  - `GET /sapi/v1/bswap/liquidity`
  - `POST /sapi/v1/bswap/liquidityAdd`
  - `POST /sapi/v1/bswap/liquidityRemove`
  - `GET /sapi/v1/bswap/liquidityOps`
  - `GET /sapi/v1/bswap/quote`
  - `POST /sapi/v1/bswap/swap`
  - `GET /sapi/v1/bswap/swap`
  - `GET /sapi/v1/bswap/poolConfigure`
  - `GET /sapi/v1/bswap/addLiquidityPreview`
  - `GET /sapi/v1/bswap/removeLiquidityPreview`
  - `GET /sapi/v1/bswap/unclaimedRewards`
  - `POST /sapi/v1/bswap/claimRewards`
  - `GET /sapi/v1/bswap/claimedHistory`

- Loan
  - `POST /sapi/v1/loan/flexible/borrow`
  - `GET /sapi/v1/loan/flexible/ongoing/orders`
  - `GET /sapi/v1/loan/flexible/borrow/history`
  - `POST /sapi/v1/loan/flexible/repay`
  - `GET /sapi/v1/loan/flexible/repay/history`
  - `POST /sapi/v1/loan/flexible/adjust/ltv`
  - `GET /sapi/v1/loan/flexible/ltv/adjustment/history`
  - `GET /sapi/v1/loan/flexible/loanable/data`
  - `GET /sapi/v1/loan/flexible/collateral/data`

- Staking
  - `GET /sapi/v1/staking/productList`
  - `POST /sapi/v1/staking/purchase`
  - `POST /sapi/v1/staking/redeem`
  - `GET /sapi/v1/staking/position`
  - `GET /sapi/v1/staking/stakingRecord`
  - `POST /sapi/v1/staking/setAutoStaking`
  - `GET /sapi/v1/staking/personalLeftQuota`

## 3.6.0 - 2024-03-07
### Removed
- `POST /sapi/v1/margin/transfer`
- `POST /sapi/v1/margin/isolated/transfer`
- `POST /sapi/v1/margin/loan`
- `POST /sapi/v1/margin/repay`
- `GET /sapi/v1/margin/isolated/transfer`
- `GET /sapi/v1/margin/asset`
- `GET /sapi/v1/margin/pair`
- `GET /sapi/v1/margin/isolated/pair`
- `GET /sapi/v1/margin/loan`
- `GET /sapi/v1/margin/repay`
- `GET /sapi/v1/margin/dribblet`
- `GET /sapi/v1/margin/dust`
- `POST /sapi/v1/margin/dust`

### Added
- `POST /sapi/v1/margin/borrow-repay`
- `GET /sapi/v1/margin/borrow-repay`

### Updated
- `GET /sapi/v1/margin/transfer` add parameter `isolatedSymbol`
- `GET /sapi/v1/margin/allAssets` add parameter `asset`
- `GET /sapi/v1/margin/allPairs` add parameter `symbol`
- `GET /sapi/v1/margin/isolated/allPairs` add parameter `symbol`

## 3.5.1 - 2023-11-17
### Fixed
- Set the default timeout value to None in WebSocket clients

## 3.5.0 - 2023-10-26
### Changed
- Add timeout parameter to Websocket clients
- Add method for `GET /sapi/v1/asset/wallet/balance`

## 3.4.0 - 2023-10-07
### Added
- Portfolio endpoints:
  - `POST /sapi/v1/portfolio/interest-history`
  - `POST /sapi/v1/portfolio/asset-index-price`
  - `POST /sapi/v1/portfolio/auto-collection`
  - `POST /sapi/v1/portfolio/bnb-transfer`
  - `POST /sapi/v1/portfolio/repay-futures-switch`
  - `GET /sapi/v1/portfolio/repay-futures-switch`
  - `POST /sapi/v1/portfolio/repay-futures-negative-balance`
  - `POST /sapi/v1/portfolio/asset-collection`
- Convert
  - `GET /sapi/v1/convert/exchangeInfo`
  - `GET /sapi/v1/convert/assetInfo`
  - `POST /sapi/v1/convert/getQuote`
  - `POST /sapi/v1/convert/acceptQuote`
  - `GET /sapi/v1/convert/orderStatus`
- Crypto Loan
  - `POST /sapi/v1/loan/flexible/borrow`
  - `GET /sapi/v1/loan/flexible/ongoing/order`
  - `GET /sapi/v1/loan/flexible/borrow/history`
  - `POST /sapi/v1/loan/flexible/repay`
  - `GET /sapi/v1/loan/flexible/repay/history`
  - `POST /sapi/v1/loan/flexible/adjust/ltv`
  - `GET /sapi/v1/loan/flexible/ltv/adjustment/history`
  - `GET /sapi/v1/loan/flexible/loanable/data`
  - `GET /sapi/v1/loan/flexible/collateral/data`
- Margin
  - `GET /sapi/v1/margin/crossMarginCollateralRatio`
  - `GET /sapi/v1/margin/exchange-small-liability`
  - `GET /sapi/v1/margin/exchange-small-liability-history`
  - `GET /sapi/v1/margin/next-hourly-interest-rate`
  - `GET /sapi/v1/margin/dust`
  - `POST /sapi/v1/margin/dust`
  - `GET /sapi/v1/margin/max-leverage`
- SubAccount
 - `POST /sapi/v4/sub-account/assets`
 - `POST /sapi/v1/sub-account/eoptions/enable`
 - `GET /sapi/v1/sub-account/transaction-statistics`
 - `GET /sapi/v1/managed-subaccount/query-trans-log`
 - `GET /sapi/v1/managed-subaccount/info`
 - `GET /sapi/v1/managed-subaccount/marginAsset`
 - `GET /sapi/v1/managed-subaccount/fetch-future-asset`
 - `GET /sapi/v1/sub-account/futures/positionRisk`
 - `GET /sapi/v1/sub-account/futures/accountSummary`
 - `GET /sapi/v1/sub-account/futures/account`
- Trade
  - `GET /api/v3/myPreventedMatches`
- Wallet
  - `POST /sapi/v1/capital/deposit/credit-apply`
- Simple Earn
  - `GET /sapi/v1/simple-earn/flexible/list`
  - `GET /sapi/v1/simple-earn/locked/list`
  - `POST /sapi/v1/simple-earn/flexible/subscribe`
  - `POST /sapi/v1/simple-earn/locked/subscribe`
  - `POST /sapi/v1/simple-earn/flexible/redeem`
  - `POST /sapi/v1/simple-earn/locked/redeem`
  - `GET /sapi/v1/simple-earn/flexible/position`
  - `GET /sapi/v1/simple-earn/locked/position`
  - `GET /sapi/v1/simple-earn/account`
  - `GET /sapi/v1/simple-earn/flexible/history/subscriptionRecord`
  - `GET /sapi/v1/simple-earn/locked/history/subscriptionRecord`
  - `GET /sapi/v1/simple-earn/flexible/history/redemptionRecord`
  - `GET /sapi/v1/simple-earn/locked/history/redemptionRecord`
  - `GET /sapi/v1/simple-earn/flexible/history/rewardsRecord`
  - `GET /sapi/v1/simple-earn/locked/history/rewardsRecord`
  - `POST /sapi/v1/simple-earn/flexible/setAutoSubscribe`
  - `POST /sapi/v1/simple-earn/locked/setAutoSubscribe`
  - `GET /sapi/v1/simple-earn/flexible/personalLeftQuota`
  - `GET /sapi/v1/simple-earn/locked/personalLeftQuota`
  - `GET /sapi/v1/simple-earn/flexible/subscriptionPreview`
  - `GET /sapi/v1/simple-earn/locked/subscriptionPreview`
  - `GET /sapi/v1/simple-earn/flexible/history/rateHistory`
  - `GET /sapi/v1/simple-earn/flexible/history/collateralRecord`
- All Auto-Invest endpoints

### Deleted
- `GET /sapi/v1/lending/daily/product/list`
- `GET /sapi/v1/lending/daily/userLeftQuota`
- `POST /sapi/v1/lending/daily/purchase`
- `GET /sapi/v1/lending/daily/userRedemptionQuota`
- `POST /sapi/v1/lending/daily/redeem`
- `GET /sapi/v1/lending/daily/token/position`
- `GET /sapi/v1/lending/union/account`
- `GET /sapi/v1/lending/union/purchaseRecord`
- `GET /sapi/v1/lending/union/redemptionRecord`
- `GET /sapi/v1/lending/union/interestHistory`
- `GET /sapi/v1/lending/project/list`
- `POST /sapi/v1/lending/customizedFixed/purchase`
- `GET /sapi/v1/lending/project/position/list`
- `POST /sapi/v1/lending/positionChanged`
- `GET /sapi/v1/futures/loan/borrow/history`
- `GET /sapi/v1/futures/loan/repay/history`
- `GET /sapi/v2/futures/loan/wallet`
- `GET /sapi/v1/futures/loan/adjustCollateral/history`
- `GET /sapi/v1/futures/loan/liquidationHistory`
- `GET /sapi/v1/futures/loan/interestHistory`

### Changed
- Change `Loan` module name to `Crypto Loan`
- Pump dependencies

## 3.3.1 - 2023-08-23

### Changed
- Add missing enum values in the `User Universal Transfer` endpoint

## 3.3.0 - 2023-08-07

### Changed
- Add support for proxy in Websocket clients
- Remove support for python 3.7


## 3.2.0 - 2023-08-01

### Changed
- Changes to `GET /api/v3/historicalTrades`: api key is not required.


## 3.1.1 - 2023-07-03

### Changed
- Change `User-Agent`

## 3.1.0 - 2023-06-01

### Added
- Add support for use of ED25519 Key to generate signatures

## 3.0.0 - 2023-05-23

### Changed
- Modified format of combined streams in Websocket Market Streams. Please refer to `examples/websocket/websocket_stream/combined_streams.py` for example implementation.

### Removed
- Discontinued official support for Python 3.6

## 3.0.0rc2 - 2023-04-21

### Removed
- Removed endpoint `POST /sapi/v1/sub-account/subAccountApi/ipRestriction/ipList`
- Removed endpoint `POST /sapi/v1/sub-account/subAccountApi/ipRestriction`

### Added
- `POST /sapi/v2/sub-account/subAccountApi/ipRestriction`
- `GET /sapi/v1/managed-subaccount/deposit/address`

## 3.0.0rc1 - 2023-02-10

### Changed
- Redesign of Websocket part. Please consult `README.md` for details on its new usage.

### Added
- Add Websocket API

## 2.0.0 - 2023-01-18
### Added
- New endpoints for wallet
  - `GET /sapi/v1/capital/contract/convertible-coins` Get a user's auto-conversion settings in deposit/withdrawal
  - `POST /sapi/v1/capital/contract/convertible-coins` User can use it to turn on or turn off the BUSD auto-conversion from/to a specific stable coin.
- New endpoints for Sub-Account
  - `GET /v1/managed-subaccount/queryTransLogForInvestor` Investor can use this api to query managed sub account transfer log
  - `GET /v1/managed-subaccount/queryTransLogForTradeParent` Trading team can use this api to query managed sub account transfer log
- New endpoints for Loan
  - `GET /sapi/v1/loan/vip/ongoing/orders` Get VIP Loan Ongoing Orders
  - `POST /sapi/v1/loan/vip/repay` VIP Loan Repay
  - `GET /sapi/v1/loan/vip/repay/history` Get VIP Loan Repayment History
  - `GET /sapi/v1/loan/vip/collateral/account` Check Locked Value of VIP Collateral Account
  - `GET /sapi/v1/loan/loanable/data` Get Loanable Assets Data
  - `GET /sapi/v1/loan/collateral/data` Get Collateral Assets Data
  - `GET /sapi/v1/loan/repay/collateral/rate` Check Collateral Repay Rate
  - `POST /sapi/v1/loan/customize/margin_call` Customize margin call for ongoing orders only.
- New endpoints for Wallet
  - `GET /sapi/v1/asset/ledger-transfer/cloud-mining/queryByPage` Get Cloud-Mining payment and refund history
  - `POST /sapi/v1/asset/convert-transfer` BUSD Convert
  - `GET /sapi/v1/asset/convert-transfer/queryByPage` BUSD Convert History
- New endpoint for gift card
  - `POST /sapi/v1/giftcard/buyCode` Create a dual-token gift card
  - `GET /sapi/v1/giftcard/buyCode/token-limit` Fetch Token Limit

### Changed
- Remove `!bookTicker` Websocket


## 2.0.0rc4 - 2023-01-17

### Change
- Rewrite reading API key in example files.

## 2.0.0rc3 - 2022-12-16

### Removed
- Python 3.6 Support Removed
- Futures Loan Endpoints:
  - `POST /sapi/v1/futures/loan/borrow` - spot.futures_loan_borrow
  - `POST /sapi/v1/futures/loan/repay` - spot.futures_loan_repay
  - `GET /sapi/v2/futures/loan/configs` - spot.futures_loan_configs
  - `GET /sapi/v2/futures/loan/calcAdjustLevel` - spot.futures_loan_calc_adjust_level
  - `GET /sapi/v2/futures/loan/calcMaxAdjustAmount` - spot.futures_loan_calc_max_adjust_amount
  - `POST /sapi/v2/futures/loan/adjustCollateral` - spot.futures_loan_adjust_collateral
  - `GET /sapi/v1/futures/loan/collateralRepayLimit` - spot.futures_loan_collateral_repay_limit
  - `GET /sapi/v1/futures/loan/collateralRepay` - spot.futures_loan_collateral_repay_quote
  - `POST /sapi/v1/futures/loan/collateralRepay` - spot.futures_loan_repay
  - `GET /sapi/v1/futures/loan/collateralRepayResult` - spot.futures_loan_collateral_repay_result

### Added
- New Margin Endpoint:
  - `GET /sapi/v1/margin/tradeCoeff` - Get Summary of Margin Account
- Re: https://github.com/binance/binance-connector-python/issues/184 - Exception handling now returns Raw Data instead of just Error Codes and Error Messages.
- Websocket Enhancements
  - Added support for passing list of symbols on all relevant Websocket endpoints to support subscription to multiple streams.
  - Stream Identification for when multiple streams are subscribed to at once. Allows users to easily identify which data belongs to which stream.
- `examples/config.ini` to globally set API and Secret Keys to apply in all example files

### Fixed
- Twisted reactor hanging in some situations due to the main thread not exiting cleanly
## 2.0.0rc2 - 2022-11-29

### Changed
- Update version name as hyphens are not recommended.

## 2.0.0-rc1 - 2022-11-29

### Added
- Add support for use of RSA Key to generate signatures

## 1.18.0 - 2022-09-29

### Added
- New endpoints for Crypto Loan:
  - `POST /sapi/v1/loan/borrow` - Crypto Loan Borrow
  - `GET /sapi/v1/loan/borrow/history` - Get Loan Borrow History
  - `GET/sapi/v1/loan/ongoing/orders` - Get Loan Ongoing Orders
  - `POST/sapi/v1/loan/repay` - Crypto Loan Repay
  - `GET/sapi/v1/loan/repay/history` - Get Loan Repayment History
  - `POST/sapi/v1/loan/adjust/ltv` - Crypto Loan Adjust LTV
  - `GET/sapi/v1/loan/ltv/adjustment/history` - Get Loan LTV Adjustment History

### Changed
- Changes to `GET /api/v3/exchangeInfo`:
  - New optional parameter `permissions` added to display all symbols with the permissions matching the parameter provided. (eg.SPOT, MARGIN, LEVERAGED)
  - If not provided, the default value will be `["SPOT","MARGIN", "LEVERAGED"]`
  - Cannot be combined with symbol or symbols

## 1.17.0 - 2022-09-05

### Added
- New endpoint for Market:
  - `GET /api/v3/uiKlines`
- New kline interval: `1s`

### Changed
- Changes to `GET /api/v3/ticker` and `GET /api/v3/ticker/24hr`
  - New optional parameter type added
  - Supported values for parameter type are `FULL` and `MINI`
    - `FULL` is the default value and the response that is currently being returned from the endpoint
    - `MINI` omits the following fields from the response: `priceChangePercent`, `weightedAvgPrice`, `bidPrice`, `bidQty`, `askPrice`, `askQty`, and `lastQty`

## 1.16.0 - 2022-08-11

### Added
- New endpoint for Portfolio Margin:
  - `GET /sapi/v1/portfolio/pmLoan` to query Portfolio Margin Bankruptcy Loan Record.
  - `POST /sapi/v1/portfolio/repay` to repay Portfolio Margin Bankruptcy Loan.
  - `GET /sapi/v1/portfolio/collateralRate` to get Portfolio Margin Collateral Rate.

### Update
- Changes to `POST /api/v3/order` and `POST /api/v3/order/cancelReplace`
  - New optional field `strategyId` is a parameter used to identify an order as part of a strategy.
  - New optional field `strategyType` is a parameter used to identify what strategy was running. (E.g. If all the orders are part of spot grid strategy, it can be set to strategyType=1000000)
  - Note: `strategyType` cannot be less than 1000000.
- Changes to `POST /api/v3/order/oco`
  - New optional fields `limitStrategyId`, `limitStrategyType`, `stopStrategyId`, `stopStrategyType`
  - These are the strategy metadata parameters for both legs of the OCO orders.
  - `limitStrategyType` and `stopStrategyType` both cannot be less than 1000000.
- `asset` is no longer mandatory in `GET /sapi/v1/lending/project/position/list`

## 1.15.0 - 2022-07-19

### Added
- New endpoint for Margin:
  - `POST /sapi/v3/asset/getUserAsset` to get user assets.

- New endpoint for Wallet:
  - `GET /sapi/v1/margin/dribblet` to query the historical information of user's margin account small-value asset conversion BNB.

## 1.14.0 - 2022-07-04

### Added

- New endpoint `GET /api/v3/ticker`
- New endpoint `POST /api/v3/order/cancelReplace`
- New websocket stream `<symbol>@ticker_<window_size>`
- New websocket stream `!ticker_<window-size>@arr`

### Update

- #146 `savings_flexible_product_position`  `asset` parameter should be optional

## 1.13.0 - 2022-05-23

### Added
- New endpoint for Gift Card:
  - `GET /sapi/v1/giftcard/cryptography/rsa-public-key` to fetch RSA public key.

- New endpoints for Staking:
  - `GET /sapi/v1/staking/productList` to get Staking product list
  - `POST /sapi/v1/staking/purchase` to stake product
  - `POST /sapi/v1/staking/redeem` to redeem product
  - `GET /sapi/v1/staking/position` to get Staking product holding position
  - `GET /sapi/v1/staking/stakingRecord` to inquiry Staking history records
  - `POST /sapi/v1/staking/setAutoStaking` to set Auto Staking function
  - `GET /sapi/v1/staking/personalLeftQuota` to inquiry Staking left quota

### Changed
- Update endpoints for Market:
  - `GET /api/v3/ticker/24hr`, `GET /api/v3/ticker/price` and `GET /api/v3/ticker/bookTicker` new optional parameter symbols.

- Update endpoint for Gift Card:
  - `POST /sapi/v1/giftcard/redeemCode`: new optional parameter externalUid. Each external unique ID represents a unique user on the partner platform. The function helps you to identify the redemption behavior of different users.

## 1.12.0 - 2022-05-03

### Added
- New endpoint `GET /sapi/v1/managed-subaccount/accountSnapshot` to support investor master account query asset snapshot of managed sub-account.
- New endpoint `GET /sapi/v1/portfolio/account` to support query portfolio margin account info
- New endpoint `GET /sapi/v1/margin/rateLimit/order`, which will display the user's current margin order count usage for all intervals.

## 1.11.0 - 2022-02-23

### Added
- New endpoints for Gift Card (Binance Code in the API Documentation):
    - `POST /sapi/v1/giftcard/createCode` to create a Binance Code
    - `POST /sapi/v1/giftcard/redeemCode` to redeem a Binance Code
    - `GET /sapi/v1/giftcard/verify` to verify a Binance Code
- New endpoint for Wallet:
    - `POST /sapi/v1/asset/dust-btc` to get assets that can be converted into BNB

## 1.10.0 - 2022-01-11

### Added
- New endpoint for Mining:
    - `GET /sapi/v1/mining/payment/uid` to get Mining account earning
- New endpoint for BSwap:
    - `GET /sapi/v1/bswap/unclaimedRewards` to get unclaimed rewards record
    - `POST /sapi/v1/bswap/claimRewards` to claim swap rewards or liquidity rewards
    - `GET /sapi/v1/bswap/claimedHistory` to get history of claimed rewards

### Removed
- Transfer types `MAIN_MINING`, `MINING_MAIN`, `MINING_UMFUTURE`, `MARGIN_MINING`, and `MINING_MARGIN` as they are discontinued in Universal Transfer endpoint `POST /sapi/v1/asset/transfer` from January 05, 2022 08:00 AM UTC

## 1.9.0 - 2021-12-22

### Added
- New endpoint for Convert:
    - `GET /sapi/v1/convert/tradeFlow` to support user query convert trade history records
- New endpoint for Rebate:
    - `GET /sapi/v1/rebate/taxQuery` to support user query spot rebate history records
- New endpoints for Margin:
    - `GET /sapi/v1/margin/crossMarginData` to get cross margin fee data collection
    - `GET /sapi/v1/margin/isolatedMarginData` to get isolated margin fee data collection
    - `GET /sapi/v1/margin/isolatedMarginTier` to get isolated margin tier data collection
- New endpoints for NFT:
    - `GET /sapi/v1/nft/history/transactions` to get NFT transaction history
    - `GET /sapi/v1/nft/history/deposit` to get NFT deposit history
    - `GET /sapi/v1/nft/history/withdraw` to get NFT withdraw history
    - `GET /sapi/v1/nft/user/getAsset` to get NFT asset

## 1.8.0 - 2021-11-25

### Added
- New endpoint for Crypto Loans:
    - `GET /sapi/v1/loan/income` to query an asset's loan history
- New endpoints for Sub-Account:
    - `POST /sapi/v1/sub-account/subAccountApi/ipRestriction` to support master account enable and disable IP restriction for a sub-account API Key
    - `POST /sapi/v1/sub-account/subAccountApi/ipRestriction/ipList` to support master account add IP list for a sub-account API Key
    - `GET /sapi/v1/sub-account/subAccountApi/ipRestriction` to support master account query IP restriction for a sub-account API Key
    - `DELETE /sapi/v1/sub-account/subAccountApi/ipRestriction/ipList` to support master account delete IP list for a sub-account API Key
- New endpoint for Pay:
    - `GET /sapi/v1/pay/transactions` to support user query Pay trade history

### Fixed
- Removed epoch time in util method `config_logging` to provide compatibility with Windows OS
- Allow optional parameter for method `isolated_margin_account_limit`

## 1.7.0 - 2021-11-4

### Updated
- Universal transfer types:
    - Added `MAIN_FUNDING`, `FUNDING_MAIN`, `FUNDING_UMFUTURE`, `UMFUTURE_FUNDING`, `MARGIN_FUNDING`, `FUNDING_MARGIN`, `FUNDING_CMFUTURE` and `CMFUTURE_FUNDING` to support transfer assets among funding account and other accounts
    - Deleted `MAIN_C2C`, `C2C_MAIN`, `C2C_UMFUTURE`, `C2C_MINING`, `UMFUTURE_C2C`, `MINING_C2C`, `MARGIN_C2C`, `C2C_MARGIN`, `MAIN_PAY` and `PAY_MAIN` as C2C account, Binance Payment, Binance Card and other business accounts are merged into a Funding account and they'll be discontinued on November 04, 2021 08:00 AM UTC
- Util method `config_logging` can now provide date time in UTC and epoch time

### Added
- New endpoint `GET api/v3/rateLimit/order` to display the user's current order count usage for all intervals

## 1.6.0 - 2021-09-24

### Added
- Universal transfer types `MAIN_PAY`, `PAY_MAIN`, `ISOLATEDMARGIN_MARGIN`，`MARGIN_ISOLATEDMARGIN`，`ISOLATEDMARGIN_ISOLATEDMARGIN`
- New endpoints for Margin OCO orders:
    - `POST /sapi/v1/margin/order/oco` to send new margin OCO order
    - `DELETE /sapi/v1/margin/orderList` to cancel margin OCO order
    - `GET /sapi/v1/margin/orderList` to query a margin OCO order
    - `GET /sapi/v1/margin/allOrderList` to query all margin OCO orders
    - `GET /sapi/v1/margin/openOrderList` to query open margin OCO orders
- New endpoints for Isolated Margin:
    - `DELETE /sapi/v1/margin/isolated/account` to disable isolated margin account for a specific symbol
    - `POST /sapi/v1/margin/isolated/account` to enable isolated margin account for a specific symbol
    - `GET /sapi/v1/margin/isolated/accountLimit` to query num of enabled isolated margin accounts and its max limit
- New endpoints for BSwap:
    - `GET /sapi/v1/bswap/poolConfigure` to get pool configure
    - `GET /sapi/v1/bswap/addLiquidityPreview` to calculate expected share amount for adding liquidity in single or dual token
    - `GET /sapi/v1/bswap/removeLiquidityPreview` to calculate expected asset amount of single token redemption or dual token redemption

## 1.5.0 - 2021-08-17

### Changed
-  `GET api/v3/exchangeInfo` now supports single or multi-symbol query
-  `GET api/v3/myTrades` has a new optional field `orderId`

### Added
- `GET /sapi/v1/c2c/orderMatch/listUserOrderHistory` to query user C2C trade history

## 1.4.0 - 2021-07-30

### Added
- New Fiat endpoints:
    - `GET /sapi/v1/fiat/orders` to query user fiat deposit and withdraw history
    - `GET /sapi/v1/fiat/payments` to query user fiat payments history

### Fixed
 - Typo in `margin_max_transferable`

## 1.3.0 - 2021-07-22
### Added
- New endpoints for Wallet:
    - `POST /sapi/v1/asset/get-funding-asset` to query funding wallet, includes Binance Pay, Binance Card, Binance Gift Card, Stock Token
    - `GET /sapi/v1/account/apiRestrictions` to query user API Key permission

## 1.2.0 - 2021-07-12

### Changed
- Remove default value in the parameters

## 1.1.1 - 2021-06-24

### Changed
- Upgrade the dependency packages

## 1.1.0 - 2021-06-23

### Added
- A link to the document on `README.md`
- Enabled the sub menu on document nav bar.
- `GET /sapi/v1/lending/daily/product/list` includes new parameters, current and size.
- New endpoints for Sub-Account:
    - `POST /sapi/v1/managed-subaccount/deposit` to deposit assets into the managed sub-account (only for investor master account)
    - `GET /sapi/v1/managed-subaccount/asset` to query managed sub-account asset details (only for investor master account)
    - `POST /sapi/v1/managed-subaccount/withdraw` to withdrawal assets from the managed sub-account (only for investor master account)

## 1.0.0 - 2021-06-15

### Added
- First release, please find details from `README.md`
