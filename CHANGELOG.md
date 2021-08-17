# Changelog

## Unreleased

## 1.5.0 - 2021-08-17

### Changed
-  `GET api/v3/exchangeInfo` now supports single or multi-symbol query
-  `GET api/v3/myTrades` has a new optional field `orderId`

### Added
- `GET /sapi/v1/c2c/orderMatch/listUserOrderHistory` to query user C2C trade history

## 1.4.0 - 2021-07-30

### Added
- New Fiat endpoints
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
