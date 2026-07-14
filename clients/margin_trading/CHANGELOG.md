# Changelog

## 7.0.0 - 2026-07-14

### Added (4)

#### REST API

- `exit_special_key_mode()` (`POST /sapi/v1/margin/exit-special-key-mode`)
- `liquidation_loan_repay()` (`POST /sapi/v1/margin/liquidation-loan/repay`)
- `query_liquidation_loan()` (`GET /sapi/v1/margin/liquidation-loan`)
- `query_liquidation_loan_repay_history()` (`GET /sapi/v1/margin/liquidation-loan/repay-history`)

### Changed (30)

- Updated `binance-common` library to version `4.0.3`

#### REST API

- Added parameter `trailing_delta`
  - affected methods:
    - `margin_account_new_order()` (`POST /sapi/v1/margin/order`)
- Modified parameter `asset_names`:
  - type `array` → `string`
  - affected methods:
    - `small_liability_exchange()` (`POST /sapi/v1/margin/exchange-small-liability`)
- Modified parameter `is_isolated`:
  - enum added: `TRUE`, `FALSE`
  - affected methods:
    - `query_margin_accounts_all_oco()` (`GET /sapi/v1/margin/allOrderList`)
    - `query_margin_accounts_all_orders()` (`GET /sapi/v1/margin/allOrders`)
    - `query_prevented_matches()` (`GET /sapi/v1/margin/myPreventedMatches`)
    - `query_margin_accounts_trade_list()` (`GET /sapi/v1/margin/myTrades`)
    - `query_margin_accounts_open_oco()` (`GET /sapi/v1/margin/openOrderList`)
    - `margin_account_cancel_all_open_orders_on_a_symbol()` (`DELETE /sapi/v1/margin/openOrders`)
    - `query_margin_accounts_open_orders()` (`GET /sapi/v1/margin/openOrders`)
    - `margin_account_cancel_order()` (`DELETE /sapi/v1/margin/order`)
    - `query_margin_accounts_order()` (`GET /sapi/v1/margin/order`)
    - `margin_account_new_order()` (`POST /sapi/v1/margin/order`)
    - `margin_account_new_oco()` (`POST /sapi/v1/margin/order/oco`)
    - `margin_account_new_oto()` (`POST /sapi/v1/margin/order/oto`)
    - `margin_account_new_otoco()` (`POST /sapi/v1/margin/order/otoco`)
    - `margin_account_cancel_oco()` (`DELETE /sapi/v1/margin/orderList`)
    - `query_margin_accounts_oco()` (`GET /sapi/v1/margin/orderList`)
    - `query_current_margin_order_count_usage()` (`GET /sapi/v1/margin/rateLimit/order`)
- Modified parameter `is_isolated`:
  - enum added: `TRUE`, `FALSE`
  - affected methods:
    - `margin_account_borrow_repay()` (`POST /sapi/v1/margin/borrow-repay`)
- Modified parameter `is_isolated`:
  - type `boolean` → `string`
  - enum added: `TRUE`, `FALSE`
  - affected methods:
    - `get_future_hourly_interest_rate()` (`GET /sapi/v1/margin/next-hourly-interest-rate`)
- Modified parameter `pendingAboveTimeInForce`:
  - enum added: `GTC`, `IOC`, `FOK`
  - affected methods:
    - `margin_account_new_otoco()` (`POST /sapi/v1/margin/order/otoco`)
- Modified parameter `pendingAboveType`:
  - enum added: `LIMIT_MAKER`, `STOP_LOSS`, `STOP_LOSS_LIMIT`
  - affected methods:
    - `margin_account_new_otoco()` (`POST /sapi/v1/margin/order/otoco`)
- Modified parameter `pendingBelowTimeInForce`:
  - enum added: `GTC`, `IOC`, `FOK`
  - affected methods:
    - `margin_account_new_otoco()` (`POST /sapi/v1/margin/order/otoco`)
- Modified parameter `pendingBelowType`:
  - enum added: `LIMIT_MAKER`, `STOP_LOSS`, `STOP_LOSS_LIMIT`
  - affected methods:
    - `margin_account_new_otoco()` (`POST /sapi/v1/margin/order/otoco`)
- Modified parameter `pendingSide`:
  - enum added: `BUY`, `SELL`
  - affected methods:
    - `margin_account_new_oto()` (`POST /sapi/v1/margin/order/oto`)
    - `margin_account_new_otoco()` (`POST /sapi/v1/margin/order/otoco`)
- Modified parameter `pendingTimeInForce`:
  - enum added: `GTC`, `IOC`, `FOK`
  - affected methods:
    - `margin_account_new_oto()` (`POST /sapi/v1/margin/order/oto`)
- Modified parameter `pendingType`:
  - enum added: `LIMIT`, `MARKET`, `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`, `LIMIT_MAKER`
  - affected methods:
    - `margin_account_new_oto()` (`POST /sapi/v1/margin/order/oto`)
- Modified parameter `permissionMode`:
  - enum added: `TRADE`, `READ`
  - affected methods:
    - `create_special_key()` (`POST /sapi/v1/margin/apiKey`)
- Modified parameter `selfTradePreventionMode`:
  - enum added: `EXPIRE_TAKER`, `EXPIRE_MAKER`, `EXPIRE_BOTH`, `NONE`
  - affected methods:
    - `margin_account_new_order()` (`POST /sapi/v1/margin/order`)
    - `margin_account_new_oco()` (`POST /sapi/v1/margin/order/oco`)
    - `margin_account_new_oto()` (`POST /sapi/v1/margin/order/oto`)
    - `margin_account_new_otoco()` (`POST /sapi/v1/margin/order/otoco`)
- Modified parameter `sideEffectType`:
  - enum added: `NO_SIDE_EFFECT`, `MARGIN_BUY`, `AUTO_REPAY`, `AUTO_BORROW_REPAY`
  - affected methods:
    - `margin_account_new_order()` (`POST /sapi/v1/margin/order`)
    - `margin_account_new_oco()` (`POST /sapi/v1/margin/order/oco`)
- Modified parameter `sideEffectType`:
  - enum added: `NO_SIDE_EFFECT`, `MARGIN_BUY`
  - affected methods:
    - `margin_account_new_oto()` (`POST /sapi/v1/margin/order/oto`)
    - `margin_account_new_otoco()` (`POST /sapi/v1/margin/order/otoco`)
- Modified parameter `stopLimitTimeInForce`:
  - enum added: `GTC`, `FOK`, `IOC`
  - affected methods:
    - `margin_account_new_oco()` (`POST /sapi/v1/margin/order/oco`)
- Modified parameter `symbol`:
  - required: `true` → `false`
  - affected methods:
    - `margin_account_borrow_repay()` (`POST /sapi/v1/margin/borrow-repay`)
- Modified parameter `type`:
  - enum added: `MARGIN`, `ISOLATED`
  - affected methods:
    - `query_margin_available_inventory()` (`GET /sapi/v1/margin/available-inventory`)
    - `margin_manual_liquidation()` (`POST /sapi/v1/margin/manual-liquidation`)
- Modified parameter `type`:
  - enum added: `BORROW`, `REPAY`
  - affected methods:
    - `query_borrow_repay_records_in_margin_account()` (`GET /sapi/v1/margin/borrow-repay`)
    - `margin_account_borrow_repay()` (`POST /sapi/v1/margin/borrow-repay`)
- Modified parameter `type`:
  - enum added: `TRANSFER`, `BORROW`, `REPAY`, `BUY_INCOME`, `BUY_EXPENSE`, `SELL_INCOME`, `SELL_EXPENSE`, `TRADING_COMMISSION`, `BUY_LIQUIDATION`, `SELL_LIQUIDATION`, `REPAY_LIQUIDATION`, `OTHER_LIQUIDATION`, `LIQUIDATION_FEE`, `SMALL_BALANCE_CONVERT`, `COMMISSION_RETURN`, `SMALL_CONVERT`
  - affected methods:
    - `query_cross_isolated_margin_capital_flow()` (`GET /sapi/v1/margin/capital-flow`)
- Modified parameter `type`:
  - enum added: `LIMIT`, `MARKET`, `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`, `LIMIT_MAKER`
  - affected methods:
    - `margin_account_new_order()` (`POST /sapi/v1/margin/order`)
- Modified parameter `type`:
  - enum added: `ROLL_IN`, `ROLL_OUT`
  - affected methods:
    - `get_cross_margin_transfer_history()` (`GET /sapi/v1/margin/transfer`)
- Modified parameter `workingSide`:
  - enum added: `BUY`, `SELL`
  - affected methods:
    - `margin_account_new_oto()` (`POST /sapi/v1/margin/order/oto`)
    - `margin_account_new_otoco()` (`POST /sapi/v1/margin/order/otoco`)
- Modified parameter `workingTimeInForce`:
  - enum added: `GTC`, `IOC`, `FOK`
  - affected methods:
    - `margin_account_new_oto()` (`POST /sapi/v1/margin/order/oto`)
- Modified parameter `workingTimeInForce`:
  - enum added: `GTC`, `IOC`, `FOK`
  - affected methods:
    - `margin_account_new_otoco()` (`POST /sapi/v1/margin/order/otoco`)
- Modified parameter `workingType`:
  - enum added: `LIMIT`, `LIMIT_MAKER`
  - affected methods:
    - `margin_account_new_oto()` (`POST /sapi/v1/margin/order/oto`)
    - `margin_account_new_otoco()` (`POST /sapi/v1/margin/order/otoco`)
- Modified response for `query_margin_available_inventory()` (`GET /sapi/v1/margin/available-inventory`):
  - `assets`: property `MATIC` deleted
  - `assets`: property `SHIB` deleted
  - `assets`: property `STPT` deleted
  - `assets`: property `TVK` deleted

- Modified response for `query_cross_isolated_margin_capital_flow()` (`GET /sapi/v1/margin/capital-flow`):
  - items: property `note` added
  - items: item property `note` added

## 6.7.0 - 2026-06-09

### Changed (2)

- Updated `binance-common` library to version `4.0.0`
- Updated `pyproject.toml` dependencies

## 6.6.0 - 2026-05-29

### Changed (1)

- Updated `binance-common` library to version `3.10.0`

## 6.5.0 - 2026-05-22

- Updated `binance-common` library to version `3.9.2`
- Updated `pyproject.toml` dependencies

## 6.4.0 - 2026-04-29

- Updated `binance-common` library to version `3.9.1`
- Updated `pyproject.toml` dependencies

## 6.3.0 - 2026-04-29

### Changed (1)

- Updated `binance-common` library to version `3.9.0`

## 6.2.0 - 2026-03-26

### Added (1)

- Added `py.typed` file to indicate that the package supports type hints.

### Changed (2)

- Updated `binance-common` library to version `3.8.0`
- Updated `tox` file

## 6.1.0 - 2026-03-16

### Changed (1)

- Updated `binance-common` library to version `3.7.0`

## 6.0.0 - 2026-02-25

### Added (2)

#### REST API

- `get_margin_restricted_assets()` (`GET /sapi/v1/margin/restricted-asset`)
- `query_prevented_matches()` (`GET /sapi/v1/margin/myPreventedMatches`)

## 5.1.0 - 2026-02-11

### Changed (2)

- Updated `binance-common` library to version `3.6.0`
- Updated `pyproject.toml` dependencies

## 5.0.0 - 2026-01-29

### Added (1)

- Updated `binance-common` library to version `3.5.0`

#### REST API

- `get_margin_asset_risk_based_liquidation_ratio()` (`GET /sapi/v1/margin/risk-based-liquidation-ratio`)

## 4.3.0 - 2026-01-23

### Changed (1)

- Updated `binance-common` library to version `3.4.1`

## 4.2.0 - 2026-01-19

### Changed (1)

- Updated `Subscribe` method in `websocket.py` to accept optional `stream_url` parameter.

## 4.1.0 - 2025-01-13

### Changed (1)

- Updated `binance-common` library to version `3.4.0`

## 4.0.0 - 2025-12-22

### Changed (2)

- Updated `binance-common` library to version `3.3.0`
- Add `Body` to Rest API request

## 3.0.0 - 2025-11-14

### Removed (6)

#### REST API

- `close_isolated_margin_user_data_stream()` (`DELETE /sapi/v1/userDataStream/isolated`)
- `close_margin_user_data_stream()` (`DELETE /sapi/v1/userDataStream`)
- `keepalive_isolated_margin_user_data_stream()` (`PUT /sapi/v1/userDataStream/isolated`)
- `keepalive_margin_user_data_stream()` (`PUT /sapi/v1/userDataStream`)
- `start_isolated_margin_user_data_stream()` (`POST /sapi/v1/userDataStream/isolated`)
- `start_margin_user_data_stream()` (`POST /sapi/v1/userDataStream`)

## 2.4.0 - 2025-10-10

### Changed (2)

- Updated `binance-common` library to version `3.2.0`

#### WebSocket Streams

- Fixed typo for user data stream events response `Outboundaccountposition` and `Liststatus`

## 2.3.0 - 2025-09-16

### Changed (1)

- Updated `binance-common` library to version `3.1.1`

## 2.2.0 - 2025-09-12

### Changed (1)

- Updated `binance-common` library to version `3.1.0`

## 2.1.0 - 2025-09-05

### Changed (1)

- Updated `binance-common` library to version `3.0.0`

## 2.0.0 - 2025-08-22

### Added (1)

#### REST API

- `get_limit_price_pairs()` (`GET /sapi/v1/margin/limit-price-pairs`)

### Changed (1)

- Standardized type hints for required parameters by replacing `default = None` annotations with `Union[..., None]`

## 1.2.0 - 2025-08-07

### Changed (1)

- Updated `binance-common` library to version `1.2.0`

## 1.1.0 - 2025-08-06

### Changed (5)

- Updated `binance-common` library to version `1.1.0`
- Changed models responses to handle upper and lower case parameters
- Added python version `3.13`

#### WebSocket Streams

- Fixed`risk_data` and `trade_data`

## 1.0.0 - 2025-07-17

- Initial release
