# Changelog

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
