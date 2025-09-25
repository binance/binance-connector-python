# Changelog

## 1.7.0 - 2025-09-24

### Changed (1)

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

## 1.1.1 - 2025-08-06

### Changed (1)

#### REST API

- Moved `option_margin_account_information` unit tests from `test_market_maker_endpoints_api` folder to `test_account_api`

## 1.1.0 - 2025-08-06

### Changed (4)

- Updated `binance-common` library to version `1.1.0`
- Changed models responses to handle upper and lower case parameters
- Added python version `3.13`

#### WebSocket Streams

- Changed `list_subscribe` to return `dict` response

## 1.0.0 - 2025-07-17

- Initial release