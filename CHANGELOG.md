# Changelog

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
