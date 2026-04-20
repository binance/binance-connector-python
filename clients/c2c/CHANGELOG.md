# Changelog

## 4.0.0 - 2026-04-20

### Changed (1)

- Modified response for `get_c2_c_trade_history()` (`GET /sapi/v1/c2c/orderMatch/listUserOrderHistory`):
  - property `tradeType` added
  - property `totalPrice` added
  - property `orderNumber` added
  - property `takerCommissionRate` added
  - property `amount` added
  - property `asset` added
  - property `fiat` added
  - property `orderStatus` added
  - property `takerAmount` added
  - property `takerCommission` added
  - property `counterPartNickName` added
  - property `commission` added
  - property `payMethodName` added
  - property `fiatSymbol` added
  - property `advNo` added
  - property `unitPrice` added
  - property `createTime` added
  - property `additionalKycVerify` added
  - property `total` deleted
  - property `code` deleted
  - property `data` deleted
  - property `message` deleted
  - property `success` deleted

## 3.6.0 - 2026-03-26

### Added (1)

- Added `py.typed` file to indicate that the package supports type hints.

### Changed (2)

- Updated `binance-common` library to version `3.8.0`
- Updated `tox` file

## 3.5.0 - 2026-03-16

### Changed (1)

- Updated `binance-common` library to version `3.7.0`

## 3.4.0 - 2026-02-11

### Changed (2)

- Updated `binance-common` library to version `3.6.0`
- Updated `pyproject.toml` dependencies

## 3.3.0 - 2026-01-29

### Changed (1)

- Updated `binance-common` library to version `3.5.0`

## 3.2.0 - 2026-01-23

### Changed (1)

- Updated `binance-common` library to version `3.4.1`

## 3.1.0 - 2026-01-13

### Changed (1)

- Updated `binance-common` library to version `3.4.0`

## 3.0.0 - 2025-12-22

### Changed (2)

- Updated `binance-common` library to version `3.3.0`
- Add `Body` to Rest API request

## 2.0.0 - 2025-11-14

### Changed (6)

- Added parameter `endTimestamp`
  - affected methods:
    - `get_c2_c_trade_history()` (`GET /sapi/v1/c2c/orderMatch/listUserOrderHistory`)
- Added parameter `startTimestamp`
  - affected methods:
    - `get_c2_c_trade_history()` (`GET /sapi/v1/c2c/orderMatch/listUserOrderHistory`)
- Added parameter `rows`
  - affected methods:
    - `get_c2_c_trade_history()` (`GET /sapi/v1/c2c/orderMatch/listUserOrderHistory`)
- Added parameter `tradeType`
  - affected methods:
    - `get_c2_c_trade_history()` (`GET /sapi/v1/c2c/orderMatch/listUserOrderHistory`)

## 1.7.0 - 2025-10-10

### Changed (1)

- Updated `binance-common` library to version `3.2.0`

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
