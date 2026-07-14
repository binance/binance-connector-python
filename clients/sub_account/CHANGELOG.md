# Changelog

## 6.0.0 - 2026-07-14

### Added (4)

- `create_sub_account_api_key()` (`POST /sapi/v1/sub-account/subAccountApi`)
- `delete_sub_account_api_key()` (`DELETE /sapi/v1/sub-account/subAccountApi`)
- `modify_sub_account_api_key_permission()` (`POST /sapi/v1/sub-account/subAccountApiPermission`)
- `query_sub_account_api_key()` (`GET /sapi/v1/sub-account/subAccountApi`)

### Changed (7)

- Updated `binance-common` library to version `4.0.3`
- Modified parameter `fromAccountType`:
  - enum added: `SPOT`, `USDT_FUTURE`, `COIN_FUTURE`, `MARGIN`, `ISOLATED_MARGIN`
  - affected methods:
    - `universal_transfer()` (`POST /sapi/v1/sub-account/universalTransfer`)
- Modified parameter `productType`:
  - enum added: `UM`
  - affected methods:
    - `move_position_for_sub_account()` (`POST /sapi/v1/sub-account/futures/move-position`)
- Modified parameter `status`:
  - type `string` → `integer`
  - affected methods:
    - `add_ip_restriction_for_sub_account_api_key()` (`POST /sapi/v2/sub-account/subAccountApi/ipRestriction`)
- Modified parameter `toAccountType`:
  - enum added: `SPOT`, `USDT_FUTURE`, `COIN_FUTURE`, `MARGIN`, `ISOLATED_MARGIN`
  - affected methods:
    - `universal_transfer()` (`POST /sapi/v1/sub-account/universalTransfer`)
- Modified parameter `transferFunctionAccountType`:
  - enum added: `SPOT`, `MARGIN`, `ISOLATED_MARGIN`, `USDT_FUTURE`, `COIN_FUTURE`
  - affected methods:
    - `query_managed_sub_account_transfer_log_sub_account_trading()` (`GET /sapi/v1/managed-subaccount/query-trans-log`)
    - `query_managed_sub_account_transfer_log_master_account_investor()` (`GET /sapi/v1/managed-subaccount/queryTransLogForInvestor`)
    - `query_managed_sub_account_transfer_log_master_account_trading()` (`GET /sapi/v1/managed-subaccount/queryTransLogForTradeParent`)
- Modified parameter `type`:
  - enum added: `SPOT`, `MARGIN`, `FUTURES`
  - affected methods:
    - `query_managed_sub_account_snapshot()` (`GET /sapi/v1/managed-subaccount/accountSnapshot`)

## 5.0.0 - 2026-06-09

### Changed (3)

- Updated `binance-common` library to version `4.0.0`
- Updated `pyproject.toml` dependencies
- Added parameter `includeSource`
  - affected methods:
    - `get_sub_account_deposit_history()` (`GET /sapi/v1/capital/deposit/subHisrec`)

## 4.1.0 - 2026-05-29

### Changed (1)

- Updated `binance-common` library to version `3.10.0`

## 4.0.0 - 2026-05-11

### Changed (2)

- Updated `binance-common` library to version `3.9.2`
- Updated `pyproject.toml` dependencies

- Added parameter `rows`
  - affected methods:
    - `get_move_position_history_for_sub_account()` (`GET /sapi/v1/sub-account/futures/move-position`)
- Deleted parameter `row`
  - affected methods:
    - `get_move_position_history_for_sub_account()` (`GET /sapi/v1/sub-account/futures/move-position`)

## 3.8.0 - 2026-04-29

- Updated `binance-common` library to version `3.9.1`
- Updated `pyproject.toml` dependencies

## 3.7.0 - 2026-04-29

### Changed (1)

- Updated `binance-common` library to version `3.9.0`

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
- Added parameter `limit`
  - affected methods:
    - `get_summary_of_sub_accounts_futures_account()` (`GET /sapi/v1/sub-account/futures/accountSummary`)
- Added parameter `page`
  - affected methods:
    - `get_summary_of_sub_accounts_futures_account()` (`GET /sapi/v1/sub-account/futures/accountSummary`)

## 3.3.0 - 2026-01-29

### Changed (1)

- Updated `binance-common` library to version `3.5.0`

## 3.2.0 - 2026-01-23

### Changed (1)

- Updated `binance-common` library to version `3.4.1`

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
