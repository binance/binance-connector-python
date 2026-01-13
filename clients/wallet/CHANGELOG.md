# Changelog

## 6.0.0 - 2026-01-13

### Added (1)

- `submit_deposit_questionnaire_v2()` (`PUT /sapi/v2/localentity/deposit/provide-info`)

### Changed (2)

- Updated `binance-common` library to version `3.4.0`
- Modified parameter `depositId`:
  - type `string` → `integer`
  - affected methods:
    - `submit_deposit_questionnaire()` (`PUT /sapi/v1/localentity/broker/deposit/provide-info`)

## 5.0.0 - 2025-12-22

### Changed (3)

- Updated `binance-common` library to version `3.3.0`
- Add `Body` to Rest API request

- Modified parameter `dustQuotaAssetToTargetAssetPrice`:
  - type `BIGDECIMAL` → `number`
  - affected methods:
    - `dust_convert()` (`POST /sapi/v1/asset/dust-convert/convert`)
    - `dust_convertible_assets()` (`POST /sapi/v1/asset/dust-convert/query-convertible-assets`)

## 4.1.0 - 2025-10-10

### Changed (2)

- Updated `binance-common` library to version `3.2.0`

#### REST API

- Fixed responses typo

## 4.0.0 - 2025-09-16

### Changed (2)

- Modified response for `deposit_history()` (`GET /sapi/v1/capital/deposit/hisrec`):
  - item property `travelRuleStatus` added
- Updated `binance-common` library to version `3.1.1`

## 3.0.0 - 2025-09-12

### Changed (2)

- Modified response for `all_coins_information()` (`GET /sapi/v1/capital/config/getall`):
  - `networkList`: item property `withdrawTag` added
- Updated `binance-common` library to version `3.1.0`

## 2.0.0 - 2025-09-05

### Added (1)

- `deposit_history_v2()` (`GET /sapi/v2/localentity/deposit/history`)

### Changed (2)

- Modified response for `deposit_history_travel_rule()` (`GET /sapi/v1/localentity/deposit/history`)
- Updated `binance-common` library to version `3.0.0`

## 1.3.0 - 2025-08-22

### Changed (1)

- Standardized type hints for required parameters by replacing `default = None` annotations with `Union[..., None]`

## 1.2.0 - 2025-08-07

### Changed (1)

- Updated `binance-common` library to version `1.2.0`

## 1.1.0 - 2025-08-06

### Added (1)

- `check_questionnaire_requirements()` (`GET /sapi/v1/localentity/questionnaire-requirements`)

### Changed (4)

- Updated `binance-common` library to version `1.1.0`
- Added python version `3.13`
- Updated name `onboarded_vasp_list()` to `vasp_list()`
- Added parameter `recvWindow`
  - affected methods:
    - `fetch_address_verification_list()` (`GET /sapi/v1/addressVerify/list`)
    - `vasp_list()` (`GET /sapi/v1/localentity/vasp`)

## 1.0.0 - 2025-07-17

- Initial release
