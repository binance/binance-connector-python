# Changelog

## 5.1.0 - 2026-01-13

### Changed (1)

- Updated `binance-common` library to version `3.4.0`

## 5.0.0 - 2025-12-22

### Changed (2)

- Updated `binance-common` library to version `3.3.0`
- Add `Body` to Rest API request

## 4.0.0 - 2025-11-24

### Changed (1)

#### REST API

- Renamed `transfer_ldusdt_for_portfolio_margin()` to `transfer_ldusdt_rwusd_for_portfolio_margin()`.


## 3.0.0 - 2025-11-14

### Removed (2)

#### REST API

- `mint_bfusd_for_portfolio_margin()` (`POST /sapi/v1/portfolio/mint`)
- `redeem_bfusd_for_portfolio_margin()` (`POST /sapi/v1/portfolio/redeem`)

## 2.0.0 - 2025-10-10

### Changed (3)

- Updated `binance-common` library to version `3.2.0`

#### REST API

- Modified response for `mint_bfusd_for_portfolio_margin()` (`POST /sapi/v1/portfolio/mint`):
  - property `mintRate` added
  - property `rate` deleted

- Modified response for `redeem_bfusd_for_portfolio_margin()` (`POST /sapi/v1/portfolio/redeem`):
  - property `redeemRate` added
  - property `rate` deleted

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

### Changed (3)

- Standardized type hints for required parameters by replacing `default = None` annotations with `Union[..., None]`

#### WebSocket Streams

- Changed `list_subscribe` to return `dict` response
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

- Fixed`user_data`

## 1.0.0 - 2025-07-17

- Initial release
