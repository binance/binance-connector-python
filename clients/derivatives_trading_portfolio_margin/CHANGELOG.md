# Changelog

## 9.0.0 - 2026-07-15

### Changed (4)

#### REST API

- Modified response for `cancel_cm_order()` (`DELETE /papi/v1/cm/order`):
  - property `cumBase` deleted
  - property `avgPrice` deleted

- Modified response for `new_cm_order()` (`POST /papi/v1/cm/order`):
  - property `avgPrice` deleted
  - property `cumBase` deleted

- Modified response for `cancel_um_order()` (`DELETE /papi/v1/um/order`):
  - property `avgPrice` deleted
  - property `cumQuote` deleted

- Modified response for `new_um_order()` (`POST /papi/v1/um/order`):
  - property `cumQuote` deleted
  - property `avgPrice` deleted

## 8.0.0 - 2026-07-14

### Changed (31)

- Updated `binance-common` library to version `4.0.3`

#### REST API

- Modified parameter `algo_type`:
  - enum added: `CONDITIONAL`
  - affected methods:
    - `new_um_algo_order()` (`POST /papi/v1/um/algo/order`)
- Modified parameter `archived`:
  - enum added: `true`, `false`
  - affected methods:
    - `get_margin_borrow_loan_interest_history()` (`GET /papi/v1/margin/marginInterestHistory`)
    - `query_margin_loan_record()` (`GET /papi/v1/margin/marginLoan`)
    - `query_margin_repay_record()` (`GET /papi/v1/margin/repayLoan`)
- Modified parameter `auto_repay`:
  - enum added: `true`, `false`
  - affected methods:
    - `change_auto_repay_futures_status()` (`POST /papi/v1/repay-futures-switch`)
- Modified parameter `auto_repay_at_cancel`:
  - enum added: `true`, `false`
  - affected methods:
    - `new_margin_order()` (`POST /papi/v1/margin/order`)
- Modified parameter `dual_side_position`:
  - enum added: `true`, `false`
  - affected methods:
    - `change_cm_position_mode()` (`POST /papi/v1/cm/positionSide/dual`)
    - `change_um_position_mode()` (`POST /papi/v1/um/positionSide/dual`)
- Modified parameter `fee_burn`:
  - enum added: `true`, `false`
  - affected methods:
    - `toggle_bnb_burn_on_um_futures_trade()` (`POST /papi/v1/um/feeBurn`)
- Modified parameter `income_type`:
  - enum added: `TRANSFER`, `WELCOME_BONUS`, `FUNDING_FEE`, `REALIZED_PNL`, `COMMISSION`, `INSURANCE_CLEAR`, `DELIVERED_SETTELMENT`
  - affected methods:
    - `get_cm_income_history()` (`GET /papi/v1/cm/income`)
- Modified parameter `income_type`:
  - enum added: `TRANSFER`, `WELCOME_BONUS`, `REALIZED_PNL`, `FUNDING_FEE`, `COMMISSION`, `INSURANCE_CLEAR`, `REFERRAL_KICKBACK`, `COMMISSION_REBATE`, `API_REBATE`, `CONTEST_REWARD`, `CROSS_COLLATERAL_TRANSFER`, `OPTIONS_PREMIUM_FEE`, `OPTIONS_SETTLE_PROFIT`, `INTERNAL_TRANSFER`, `AUTO_EXCHANGE`, `DELIVERED_SETTELMENT`, `COIN_SWAP_DEPOSIT`, `COIN_SWAP_WITHDRAW`, `POSITION_LIMIT_INCREASE_FEE`
  - affected methods:
    - `get_um_income_history()` (`GET /papi/v1/um/income`)
- Modified parameter `new_order_resp_type`:
  - enum added: `FULL`
  - affected methods:
    - `new_margin_order()` (`POST /papi/v1/margin/order`)
- Modified parameter `price_match`:
  - enum removed: `NONE`
  - affected methods:
    - `new_cm_order()` (`POST /papi/v1/cm/order`)
    - `modify_cm_order()` (`PUT /papi/v1/cm/order`)
    - `new_um_conditional_order()` (`POST /papi/v1/um/conditional/order`)
    - `new_um_order()` (`POST /papi/v1/um/order`)
    - `modify_um_order()` (`PUT /papi/v1/um/order`)
- Modified parameter `price_match`:
  - enum removed: `NONE`
  - affected methods:
    - `new_um_algo_order()` (`POST /papi/v1/um/algo/order`)
- Modified parameter `price_protect`:
  - enum added: `true`, `false`
  - affected methods:
    - `new_cm_conditional_order()` (`POST /papi/v1/cm/conditional/order`)
    - `new_um_algo_order()` (`POST /papi/v1/um/algo/order`)
    - `new_um_conditional_order()` (`POST /papi/v1/um/conditional/order`)
- Modified parameter `reduce_only`:
  - enum added: `true`, `false`
  - affected methods:
    - `new_cm_order()` (`POST /papi/v1/cm/order`)
    - `new_um_algo_order()` (`POST /papi/v1/um/algo/order`)
    - `new_um_conditional_order()` (`POST /papi/v1/um/conditional/order`)
    - `new_um_order()` (`POST /papi/v1/um/order`)
- Modified parameter `side_effect_type`:
  - enum added: `AUTO_BORROW_REPAY`
  - affected methods:
    - `new_margin_order()` (`POST /papi/v1/margin/order`)
- Modified parameter `strategy_type`:
  - enum removed: `LIMIT_MAKER`
  - affected methods:
    - `new_cm_conditional_order()` (`POST /papi/v1/cm/conditional/order`)
    - `new_um_conditional_order()` (`POST /papi/v1/um/conditional/order`)
- Modified parameter `symbol`:
  - required: `true` → `false`
  - affected methods:
    - `query_all_cm_orders()` (`GET /papi/v1/cm/allOrders`)
- Modified parameter `time_in_force`:
  - enum removed: `GTX`
  - affected methods:
    - `new_margin_order()` (`POST /papi/v1/margin/order`)
- Modified parameter `time_in_force`:
  - enum added: `GTD`
  - affected methods:
    - `new_um_algo_order()` (`POST /papi/v1/um/algo/order`)
- Modified parameter `time_in_force`:
  - enum added: `GTD`
  - affected methods:
    - `new_um_conditional_order()` (`POST /papi/v1/um/conditional/order`)
    - `new_um_order()` (`POST /papi/v1/um/order`)
- Modified parameter `transfer_side`:
  - enum added: `TO_UM`, `FROM_UM`
  - affected methods:
    - `bnb_transfer()` (`POST /papi/v1/bnb-transfer`)
- Modified parameter `type`:
  - enum added: `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`, `LIMIT_MAKER`
  - affected methods:
    - `new_margin_order()` (`POST /papi/v1/margin/order`)
- Modified parameter `type`:
  - enum removed: `LIMIT`, `MARKET`
  - enum added: `STOP`, `TAKE_PROFIT`, `STOP_MARKET`, `TAKE_PROFIT_MARKET`, `TRAILING_STOP_MARKET`
  - affected methods:
    - `new_um_algo_order()` (`POST /papi/v1/um/algo/order`)
- Modified parameter `workingType`:
  - enum added: `CONTRACT_PRICE`
  - affected methods:
    - `new_cm_conditional_order()` (`POST /papi/v1/cm/conditional/order`)
    - `new_um_conditional_order()` (`POST /papi/v1/um/conditional/order`)
- Modified parameter `working_type`:
  - enum added: `CONTRACT_PRICE`
  - affected methods:
    - `new_um_algo_order()` (`POST /papi/v1/um/algo/order`)
- Modified response for `account_balance()` (`GET /papi/v1/balance`):
  - oneOf modified

- Modified response for `query_current_um_open_algo_order()` (`GET /papi/v1/um/algo/algoOrder`):
  - property `tpOrderType` deleted
  - property `tpTriggerPrice` deleted
  - property `slPrice` deleted
  - property `tpPrice` deleted
  - property `icebergQuantity` deleted
  - property `slTriggerPrice` deleted

- Modified response for `query_um_algo_order_history()` (`GET /papi/v1/um/algo/allAlgoOrders`):
  - items: property `tpTriggerPrice` deleted
  - items: property `icebergQuantity` deleted
  - items: property `slPrice` deleted
  - items: property `tpPrice` deleted
  - items: property `slTriggerPrice` deleted
  - items: property `tpOrderType` deleted
  - items: item property `tpTriggerPrice` deleted
  - items: item property `icebergQuantity` deleted
  - items: item property `slPrice` deleted
  - items: item property `tpPrice` deleted
  - items: item property `slTriggerPrice` deleted
  - items: item property `tpOrderType` deleted

- Modified response for `query_all_current_um_open_algo_orders()` (`GET /papi/v1/um/algo/openAlgoOrders`):
  - items: property `slTriggerPrice` deleted
  - items: property `tpOrderType` deleted
  - items: property `actualOrderId` deleted
  - items: property `slPrice` deleted
  - items: property `tpPrice` deleted
  - items: property `actualPrice` deleted
  - items: property `icebergQuantity` deleted
  - items: property `tpTriggerPrice` deleted
  - items: item property `slTriggerPrice` deleted
  - items: item property `tpOrderType` deleted
  - items: item property `actualOrderId` deleted
  - items: item property `slPrice` deleted
  - items: item property `tpPrice` deleted
  - items: item property `actualPrice` deleted
  - items: item property `icebergQuantity` deleted
  - items: item property `tpTriggerPrice` deleted

- Modified response for `new_um_algo_order()` (`POST /papi/v1/um/algo/order`):
  - property `icebergQuantity` deleted

- Modified response for `get_um_income_history()` (`GET /papi/v1/um/income`):
  - items.`tranId`: type `integer` → `string`
  - items.`tranId`: type `integer` → `string`

## 7.2.0 - 2026-06-09

### Changed (2)

- Updated `binance-common` library to version `4.0.0`
- Updated `pyproject.toml` dependencies

## 7.1.0 - 2026-05-29

### Changed (1)

- Updated `binance-common` library to version `3.10.0`

## 7.0.0 - 2026-05-22

- Updated `binance-common` library to version `3.9.2`
- Updated `pyproject.toml` dependencies

### Changed (4)

#### REST API

- Deleted parameter `closePosition`
  - affected methods:
    - `new_um_algo_order()` (`POST /papi/v1/um/algo/order`)
- Modified parameter `quantity`:
  - required: `false` → `true`
  - affected methods:
    - `new_um_algo_order()` (`POST /papi/v1/um/algo/order`)
- Modified response for `new_um_algo_order()` (`POST /papi/v1/um/algo/order`):
  - property `closePosition` deleted

- Modified response for `cancel_um_algo_order()` (`DELETE /papi/v1/um/algo/order`):
  - property `complete` added
  - property `msg` deleted
  - property `algoId` deleted
  - property `clientAlgoId` deleted
  - property `code` deleted

## 6.2.0 - 2026-04-29

- Updated `binance-common` library to version `3.9.1`
- Updated `pyproject.toml` dependencies

## 6.1.0 - 2026-04-29

### Changed (1)

- Updated `binance-common` library to version `3.9.0`

## 6.0.0 - 2026-04-20

### Added (7)

#### REST API

- `futures_tradfi_perps_contract()` (`POST /papi/v1/um/stock/contract`)
- `cancel_all_um_algo_open_orders()` (`DELETE /papi/v1/um/algo/allOpenOrders`)
- `cancel_um_algo_order()` (`DELETE /papi/v1/um/algo/order`)
- `new_um_algo_order()` (`POST /papi/v1/um/algo/order`)
- `query_all_current_um_open_algo_orders()` (`GET /papi/v1/um/algo/openAlgoOrders`)
- `query_current_um_open_algo_order()` (`GET /papi/v1/um/algo/algoOrder`)
- `query_um_algo_order_history()` (`GET /papi/v1/um/algo/allAlgoOrders`)

### Changed (8)

#### REST API

- Marked `cancel_all_um_open_conditional_orders()` (`DELETE /papi/v1/um/conditional/allOpenOrders`) as deprecated.
- Marked `cancel_um_conditional_order()` (`DELETE /papi/v1/um/conditional/order`) as deprecated.
- Marked `new_um_conditional_order()` (`POST /papi/v1/um/conditional/order`) as deprecated.
- Marked `query_all_current_um_open_conditional_orders()` (`GET /papi/v1/um/conditional/openOrders`) as deprecated.
- Marked `query_all_um_conditional_orders()` (`GET /papi/v1/um/conditional/allOrders`) as deprecated.
- Marked `query_current_um_open_conditional_order()` (`GET /papi/v1/um/conditional/openOrder`) as deprecated.
- Marked `query_um_conditional_order_history()` (`GET /papi/v1/um/conditional/orderHistory`) as deprecated.
- Modified response for `get_um_income_history()` (`GET /papi/v1/um/income`):
  - items.`tranId`: type `string` → `integer`
  - items.`tranId`: type `string` → `integer`

## 5.3.0 - 2026-03-26

### Added (1)

- Added `py.typed` file to indicate that the package supports type hints.

### Changed (2)

- Updated `binance-common` library to version `3.8.0`
- Updated `tox` file

## 5.2.0 - 2026-03-16

### Changed (1)

- Updated `binance-common` library to version `3.7.0`

## 5.1.0 - 2026-02-11

### Changed (2)

- Updated `binance-common` library to version `3.6.0`
- Updated `pyproject.toml` dependencies

## 5.0.0 - 2026-01-29

### Changed (1)

- Updated `binance-common` library to version `3.5.0`

#### REST API

- Modified parameter `strategyType`:
  - enum added: `LIMIT_MAKER`
  - affected methods:
    - `new_cm_conditional_order()` (`POST /papi/v1/cm/conditional/order`)
    - `new_um_conditional_order()` (`POST /papi/v1/um/conditional/order`)

## 4.0.0 - 2026-01-23

### Changed (2)

- Updated `binance-common` library to version `3.4.1`

#### REST API

- Modified response for `query_current_cm_open_order()` (`GET /papi/v1/cm/openOrder`):
  - type `object` → `array`
  - property `pair` deleted
  - property `symbol` deleted
  - property `positionSide` deleted
  - property `executedQty` deleted
  - property `timeInForce` deleted
  - property `origQty` deleted
  - property `reduceOnly` deleted
  - property `time` deleted
  - property `side` deleted
  - property `status` deleted
  - property `type` deleted
  - property `avgPrice` deleted
  - property `clientOrderId` deleted
  - property `cumBase` deleted
  - property `orderId` deleted
  - property `origType` deleted
  - property `price` deleted
  - property `updateTime` deleted

## 3.2.0 - 2026-01-19

### Changed (1)

- Updated `Subscribe` method in `websocket.py` to accept optional `stream_url` parameter.

## 3.1.0 - 2026-01-13

### Changed (1)

- Updated `binance-common` library to version `3.4.0`

## 3.0.0 - 2025-12-22

### Changed (3)

- Updated `binance-common` library to version `3.3.0`
- Add `Body` to Rest API request

#### REST API

- Modified response for `um_position_adl_quantile_estimation()` (`GET /papi/v1/um/adlQuantile`):
  - items.`adlQuantile`: property `HEDGE` deleted
  - items.`adlQuantile`: property `HEDGE` deleted

## 2.0.0 - 2025-11-24

### Changed (1)

- Modified response for `user_data()` method:
  - removed `M` from Executionreport

## 1.8.0 - 2025-10-10

### Changed (2)

- Updated `binance-common` library to version `3.2.0`

#### WebSocket Streams

- Fixed typo for user data stream events response `account_update`, `Openorderloss` and `Outboundaccountposition`

## 1.7.0 - 2025-09-24

### Changed (2)

#### REST API

- Modified response for `margin_max_borrow()` (`GET /papi/v1/margin/maxBorrowable`):
  - `amount`: type `number` → `string`
  - `borrowLimit`: type `integer` → `string`

- Modified response for `new_margin_order()` (`POST /papi/v1/margin/order`):
  - `marginBuyBorrowAmount`: type `integer` → `string`

## 1.6.0 - 2025-09-16

### Changed (1)

- Updated `binance-common` library to version `3.1.1`

## 1.5.0 - 2025-09-12

### Changed (1)

- Updated `binance-common` library to version `3.1.0`

## 1.4.0 - 2025-09-05

### Changed (1)

- Updated `binance-common` library to version `3.0.0`

## 1.3.0 - 2025-08-22

### Changed (2)

- Standardized type hints for required parameters by replacing `default = None` annotations with `Union[..., None]`

#### WebSocket Streams

- Changed `list_subscribe` to return `dict` response

## 1.2.0 - 2025-08-07

### Changed (1)

- Updated `binance-common` library to version `1.2.0`

## 1.1.0 - 2025-08-06

### Changed (4)

- Updated `binance-common` library to version `1.1.0`
- Changed models responses to handle upper and lower case parameters
- Added python version `3.13`

#### WebSocket Streams

- Fixed`user_data`

## 1.0.0 - 2025-07-17

- Initial release
