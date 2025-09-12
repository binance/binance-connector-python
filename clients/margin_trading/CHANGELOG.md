# Changelog

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
