# Changelog

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
