# Changelog

## 5.0.0 - 2025-12-22

### Added (5)

- Updated `binance-common` library to version `3.3.0`
- Add `Body` to Rest API request

#### REST API

- `futures_tradfi_perps_contract()` (`POST /fapi/v1/stock/contract`)
- `trading_schedule()` (`GET /fapi/v1/tradingSchedule`)
- `rpi_order_book()` (`GET /fapi/v1/rpiDepth`)

#### WebSocket Streams

- `trading_session_stream()` (`tradingSession` stream)
- `rpi_diff_book_depth_streams()` (`<symbol>@rpiDepth@500ms` stream)

### Changed (12)

#### REST API

- Added parameter `activatePrice`
  - affected methods:
    - `new_algo_order()` (`POST /fapi/v1/algoOrder`)
- Deleted parameter `activationPrice`
  - affected methods:
    - `new_algo_order()` (`POST /fapi/v1/algoOrder`)

- Modified parameter `batchOrders`:
  - items: property `stopPrice` deleted
  - items: property `priceProtect` deleted
  - items: property `activationPrice` deleted
  - items: property `callbackRate` deleted
  - items: property `workingType` deleted
  - items: item property `stopPrice` deleted
  - items: item property `priceProtect` deleted
  - items: item property `activationPrice` deleted
  - items: item property `callbackRate` deleted
  - items: item property `workingType` deleted
  - items.`goodTillDate`: type `integer` → `string`
  - items.`price`: type `number` → `string`
  - items.`quantity`: type `number` → `string`
  - items.`goodTillDate`: type `integer` → `string`
  - items.`price`: type `number` → `string`
  - items.`quantity`: type `number` → `string`
  - affected methods:
    - `place_multiple_orders()` (`POST /fapi/v1/batchOrders`)
- Modified parameter `batchOrders`:
  - items.`orderId`: type `integer` → `string`
  - items.`price`: type `number` → `string`
  - items.`quantity`: type `number` → `string`
  - items.`recvWindow`: type `integer` → `string`
  - items.`orderId`: type `integer` → `string`
  - items.`price`: type `number` → `string`
  - items.`quantity`: type `number` → `string`
  - items.`recvWindow`: type `integer` → `string`
  - affected methods:
    - `modify_multiple_orders()` (`PUT /fapi/v1/batchOrders`)

- Deleted parameter `activationPrice`
  - affected methods:
    - `new_order()` (`POST /fapi/v1/order`)
- Deleted parameter `callbackRate`
  - affected methods:
    - `new_order()` (`POST /fapi/v1/order`)
- Deleted parameter `closePosition`
  - affected methods:
    - `new_order()` (`POST /fapi/v1/order`)
- Deleted parameter `priceProtect`
  - affected methods:
    - `new_order()` (`POST /fapi/v1/order`)
- Deleted parameter `stopPrice`
  - affected methods:
    - `new_order()` (`POST /fapi/v1/order`)
- Deleted parameter `workingType`
  - affected methods:
    - `new_order()` (`POST /fapi/v1/order`)
- Modified response for `place_multiple_orders()` (`POST /fapi/v1/batchOrders`):
  - items: property `priceRate` deleted
  - items: property `activatePrice` deleted
  - items: item property `priceRate` deleted
  - items: item property `activatePrice` deleted

- Modified response for `new_order()` (`POST /fapi/v1/order`):
  - property `activatePrice` deleted
  - property `priceRate` deleted

#### WebSocket API

- Modified response for `cancel_algo_order()` (`algoOrder.cancel` method):
  - `result`: property `code` added
  - `result`: property `msg` added
  - `result`: property `positionSide` deleted
  - `result`: property `priceMatch` deleted
  - `result`: property `createTime` deleted
  - `result`: property `price` deleted
  - `result`: property `priceProtect` deleted
  - `result`: property `algoType` deleted
  - `result`: property `selfTradePreventionMode` deleted
  - `result`: property `timeInForce` deleted
  - `result`: property `updateTime` deleted
  - `result`: property `workingType` deleted
  - `result`: property `goodTillDate` deleted
  - `result`: property `symbol` deleted
  - `result`: property `orderType` deleted
  - `result`: property `triggerPrice` deleted
  - `result`: property `algoStatus` deleted
  - `result`: property `triggerTime` deleted
  - `result`: property `icebergQuantity` deleted
  - `result`: property `side` deleted
  - `result`: property `closePosition` deleted
  - `result`: property `reduceOnly` deleted
  - `result`: property `quantity` deleted

## 4.0.0 - 2025-11-24

### Added (1)

#### REST API

- `adl_risk()` (`GET /fapi/v1/symbolAdlRisk`)

### Changed (5)

#### REST API

- Modified parameter `batchOrders`:
  - items.`timeInForce`: enum added: `RPI`
  - items.`timeInForce`: enum added: `RPI`
  - affected methods:
    - `place_multiple_orders()` (`POST /fapi/v1/batchOrders`)
- Modified parameter `timeInForce`:
  - enum added: `RPI`
  - affected methods:
    - `new_algo_order()` (`POST /fapi/v1/algoOrder`)
    - `new_order()` (`POST /fapi/v1/order`)
    - `test_order()` (`POST /fapi/v1/order/test`)
- Modified response for `old_trades_lookup()` (`GET /fapi/v1/historicalTrades`):
  - items: property `isRPITrade` added
  - items: item property `isRPITrade` added

- Modified response for `recent_trades_list()` (`GET /fapi/v1/trades`):
  - items: property `isRPITrade` added
  - items: item property `isRPITrade` added

#### WebSocket API

- Modified parameter `timeInForce`:
  - enum added: `RPI`
  - affected methods:
    - `new_algo_order()` (`algoOrder.place` method)
    - `new_order()` (`order.place` method)

## 3.0.0 - 2025-11-14

### Added (7)

#### REST API

- `cancel_algo_order()` (`DELETE /fapi/v1/algoOrder`)
- `cancel_all_algo_open_orders()` (`DELETE /fapi/v1/algoOpenOrders`)
- `current_all_algo_open_orders()` (`GET /fapi/v1/openAlgoOrders`)
- `new_algo_order()` (`POST /fapi/v1/algoOrder`)
- `query_algo_order()` (`GET /fapi/v1/algoOrder`)
- `query_all_algo_orders()` (`GET /fapi/v1/allAlgoOrders`)
- Marked `symbol_price_ticker` (`GET /fapi/v1/ticker/price`) as deprecated.

## 2.0.0 - 2025-10-27

### Changed (1)

#### WebSocket Streams

- Modified User Data Streams response for `OrderTradeUpdateO`:
  - `er` added 

## 1.8.0 - 2025-10-10

### Changed (4)

- Updated `binance-common` library to version `3.2.0`

#### REST API

- Fixed typo for endpoints response `GET /fapi/v1/depth` and `GET /fapi/v1/aggTrades`

#### WebSocket API

- Fixed typo for endpoint response `depth`

#### WebSocket Streams

- Fixed typo for user data stream events response `account_update`

## 1.7.0 - 2025-09-24

### Changed (2)

- Modified response for `notional_and_leverage_brackets` (`GET /fapi/v1/leverageBracket`)
- Modified method for removing slashes (`/`) in endpoints

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

- Updated Websocket Streams response type to `RequestStreamHandle`

## 1.2.0 - 2025-08-07

### Changed (1)

- Updated `binance-common` library to version `1.2.0`

## 1.1.0 - 2025-08-06

### Changed (5)

- Updated `binance-common` library to version `1.1.0`
- Changed models responses to handle upper and lower case parameters
- Added python version `3.13`

#### WebSocket Streams

- Changed `list_subscribe` to return `dict` response
- Fixed`user_data`

## 1.0.0 - 2025-07-17

- Initial release
