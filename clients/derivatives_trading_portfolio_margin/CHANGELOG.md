# Changelog

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
