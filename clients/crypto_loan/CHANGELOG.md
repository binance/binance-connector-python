# Changelog

## 2.1.0 - 2025-09-12

### Changed (1)

- Updated `binance-common` library to version `3.1.0`

## 2.0.0 - 2025-08-25

### Changed (5)

- Added parameter `collateralAmount`
  - affected methods:
    - `flexible_loan_borrow()` (`POST /sapi/v2/loan/flexible/borrow`)
- Added parameter `loanAmount`
  - affected methods:
    - `flexible_loan_borrow()` (`POST /sapi/v2/loan/flexible/borrow`)

- Modified response for `flexible_loan_repay()` method (`POST /sapi/v2/loan/flexible/repay`):

- Modified response for `get_flexible_loan_repayment_history()` method (`GET /sapi/v2/loan/flexible/repay/history`):
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
