# Changelog

## 3.1.0 - 2026-01-13

### Changed (1)

- Updated `binance-common` library to version `3.4.0`

## 3.0.0 - 2025-12-22

### Changed (3)

- Updated `binance-common` library to version `3.3.0`
- Add `Body` to Rest API request

#### REST API

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
    - `modify_multiple_orders()` (`PUT /dapi/v1/batchOrders`)

## 2.5.0 - 2025-10-10

### Changed (4)

- Updated `binance-common` library to version `3.2.0`

#### REST API

- Fixed typo for endpoint response `GET /dapi/v1/depth`

- Modified response for `query_order()` (`GET /dapi/v1/order`):
  - property `position_side` added

#### WebSocket Streams

- Fixed typo for user data stream events response `account_update`

## 2.4.0 - 2025-09-24

### Changed (1)

- Modified method for removing slashes (`/`) in endpoints

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

### Changed (3)

- Standardized type hints for required parameters by replacing `default = None` annotations with `Union[..., None]`

#### REST API

- Modified response for `exchange_information()` method (`GET /dapi/v1/exchangeInfo`):
  - `symbols`.`filters`.`multiplierDecimal`: type `integer` → `string`

#### WebSocket Streams

- Updated Websocket Streams response type to `RequestStreamHandle`

## 1.2.0 - 2025-08-07

### Changed (1)

- Updated `binance-common` library to version `1.2.0`

## 1.1.0 - 2025-08-06

### Changed (4)

- Updated `binance-common` library to version `1.1.0`
- Changed models responses to handle upper and lower case parameters
- Added python version `3.13`

#### WebSocket Streams

- Changed `list_subscribe` to return `dict` response

## 1.0.0 - 2025-07-17

- Initial release
