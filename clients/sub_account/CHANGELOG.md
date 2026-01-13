# Changelog

## 3.1.0 - 2025-01-13

### Changed (1)

- Updated `binance-common` library to version `3.4.0`

## 3.0.0 - 2025-12-22

- Updated `binance-common` library to version `3.3.0`
- Add `Body` to Rest API request

## 2.1.0 - 2025-10-10

### Changed (2)

- Modified parameter `orderArgs`:
  - item property `symbol` added
  - item property `positionSide` added
  - item property `quantity` added
  - affected methods:
    - `move_position_for_sub_account()` (`POST /sapi/v1/sub-account/futures/move-position`)
- Updated `binance-common` library to version `3.2.0`

## 2.0.0 - 2025-09-24

### Changed (2)

- Modified parameter `email`:
  - required: `true` → `false`
  - affected methods:
    - `query_sub_account_transaction_statistics()` (`GET /sapi/v1/sub-account/transaction-statistics`)

- Add missing example field `order_args` to endpoint `POST /sapi/v1/sub-account/futures/move-position`

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

### Changed (1)

- Standardized type hints for required parameters by replacing `default = None` annotations with `Union[..., None]`

## 1.2.0 - 2025-08-07

### Changed (1)

- Updated `binance-common` library to version `1.2.0`

## 1.1.0 - 2025-08-06

### Changed (2)

- Updated `binance-common` library to version `1.1.0`
- Added python version `3.13`

## 1.0.0 - 2025-07-17

- Initial release
