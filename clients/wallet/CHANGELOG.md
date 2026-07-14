# Changelog

## 13.0.0 - 2026-07-14

### Changed (14)

- Updated `binance-common` library to version `4.0.3`
- Added parameter `recvWindow`
  - affected methods:
    - `get_country_list()` (`GET /sapi/v1/localentity/country/list`)
    - `get_region_list()` (`GET /sapi/v1/localentity/region/list`)
- Deleted parameter `signature`
  - affected methods:
    - `submit_deposit_questionnaire()` (`PUT /sapi/v1/localentity/broker/deposit/provide-info`)
    - `broker_withdraw()` (`POST /sapi/v1/localentity/broker/withdraw/apply`)
- Modified parameter `accountType`:
  - enum added: `SPOT`, `MARGIN`
  - affected methods:
    - `dustlog()` (`GET /sapi/v1/asset/dribblet`)
    - `dust_transfer()` (`POST /sapi/v1/asset/dust`)
    - `get_assets_that_can_be_converted_into_bnb()` (`POST /sapi/v1/asset/dust-btc`)
- Modified parameter `depositId`:
  - type `string` → `integer`
  - affected methods:
    - `deposit_history_v2()` (`GET /sapi/v2/localentity/deposit/history`)
- Modified parameter `fromSymbol`:
  - enum added: `ISOLATEDMARGIN_MARGIN`, `ISOLATEDMARGIN_ISOLATEDMARGIN`
  - affected methods:
    - `query_user_universal_transfer_history()` (`GET /sapi/v1/asset/transfer`)
    - `user_universal_transfer()` (`POST /sapi/v1/asset/transfer`)
- Modified parameter `needBtcValuation`:
  - type `string` → `boolean`
  - affected methods:
    - `funding_wallet()` (`POST /sapi/v1/asset/get-funding-asset`)
- Modified parameter `status`:
  - enum added: `0`, `1`, `2`, `6`, `7`, `8`
  - affected methods:
    - `deposit_history()` (`GET /sapi/v1/capital/deposit/hisrec`)
- Modified parameter `subAccountId`:
  - type `integer` → `string`
  - affected methods:
    - `one_click_arrival_deposit_apply()` (`POST /sapi/v1/capital/deposit/credit-apply`)
- Modified parameter `toSymbol`:
  - enum added: `MARGIN_ISOLATEDMARGIN`, `ISOLATEDMARGIN_ISOLATEDMARGIN`
  - affected methods:
    - `query_user_universal_transfer_history()` (`GET /sapi/v1/asset/transfer`)
    - `user_universal_transfer()` (`POST /sapi/v1/asset/transfer`)
- Modified parameter `type`:
  - enum added: `SPOT`, `MARGIN`, `FUTURES`
  - affected methods:
    - `daily_account_snapshot()` (`GET /sapi/v1/accountSnapshot`)
- Modified parameter `type`:
  - enum added: `DELEGATE`, `UNDELEGATE`
  - affected methods:
    - `query_user_delegation_history()` (`GET /sapi/v1/asset/custody/transfer-history`)
- Modified parameter `type`:
  - enum added: `MAIN_UMFUTURE`, `MAIN_CMFUTURE`, `MAIN_MARGIN`, `UMFUTURE_MAIN`, `UMFUTURE_MARGIN`, `CMFUTURE_MAIN`, `CMFUTURE_MARGIN`, `MARGIN_MAIN`, `MARGIN_UMFUTURE`, `MARGIN_CMFUTURE`, `ISOLATEDMARGIN_MARGIN`, `MARGIN_ISOLATEDMARGIN`, `ISOLATEDMARGIN_ISOLATEDMARGIN`, `MAIN_FUNDING`, `FUNDING_MAIN`, `FUNDING_UMFUTURE`, `UMFUTURE_FUNDING`, `MARGIN_FUNDING`, `FUNDING_MARGIN`, `FUNDING_CMFUTURE`, `CMFUTURE_FUNDING`, `MAIN_OPTION`, `OPTION_MAIN`, `UMFUTURE_OPTION`, `OPTION_UMFUTURE`, `MARGIN_OPTION`, `OPTION_MARGIN`, `FUNDING_OPTION`, `OPTION_FUNDING`, `MAIN_PORTFOLIO_MARGIN`, `PORTFOLIO_MARGIN_MAIN`
  - affected methods:
    - `user_universal_transfer()` (`POST /sapi/v1/asset/transfer`)
- Modified response for `deposit_history_travel_rule()` (`GET /sapi/v1/localentity/deposit/history`):
  - items: property `completeTime` added
  - items: property `travelRuleStatusV2` added
  - items: property `unlockConfirm` deleted
  - items: property `walletType` deleted
  - items: item property `completeTime` added
  - items: item property `travelRuleStatusV2` added
  - items: item property `unlockConfirm` deleted
  - items: item property `walletType` deleted

## 12.0.0 - 2026-06-30

### Changed (2)

- Modified response for `broker_withdraw()` (`POST /sapi/v1/localentity/broker/withdraw/apply`):
  - property `accepted` added
  - property `accpted` deleted

- Modified response for `withdraw_travel_rule()` (`POST /sapi/v1/localentity/withdraw/apply`):
  - property `accepted` added
  - property `accpted` deleted

## 11.0.0 - 2026-06-09

### Added (2)

- `get_country_list()` (`GET /sapi/v1/localentity/country/list`)
- `get_region_list()` (`GET /sapi/v1/localentity/region/list`)

### Changed (2)

- Updated `binance-common` library to version `4.0.0`
- Updated `pyproject.toml` dependencies

## 10.0.0 - 2026-05-29

### Changed (2)

- Updated `binance-common` library to version `3.10.0`
- Added parameter `accountType`
  - affected methods:
    - `dust_convert()` (`POST /sapi/v1/asset/dust-convert/convert`)
    - `dust_convertible_assets()` (`POST /sapi/v1/asset/dust-convert/query-convertible-assets`)

## 9.5.0 - 2026-05-22

- Updated `binance-common` library to version `3.9.2`
- Updated `pyproject.toml` dependencies

## 9.4.0 - 2026-04-29

- Updated `binance-common` library to version `3.9.1`
- Updated `pyproject.toml` dependencies

## 9.3.0 - 2026-04-29

### Changed (1)

- Updated `binance-common` library to version `3.9.0`

## 9.2.0 - 2026-03-26

### Added (1)

- Added `py.typed` file to indicate that the package supports type hints.

### Changed (2)

- Updated `binance-common` library to version `3.8.0`
- Updated `tox` file

## 9.1.0 - 2026-03-16

### Changed (1)

- Updated `binance-common` library to version `3.7.0`

## 9.0.0 - 2026-03-09

### Changed (1)

- Modified response for `vasp_list()` (`GET /sapi/v1/localentity/vasp`):
  - items: property `identifier` added
  - items: item property `identifier` added

## 8.1.0 - 2026-02-11

### Changed (2)

- Updated `binance-common` library to version `3.6.0`
- Updated `pyproject.toml` dependencies

## 8.0.0 - 2026-01-29

### Changed (2)

- Updated `binance-common` library to version `3.5.0`
- Modified response for `asset_dividend_record()` (`GET /sapi/v1/asset/assetDividend`):
  - `rows`.items: property `direction` added
  - `rows`.items: item property `direction` added

## 7.0.0 - 2026-01-23

### Changed (5)

- Updated `binance-common` library to version `3.4.1`
- Added parameter `accountType`
  - affected methods:
    - `dustlog()` (`GET /sapi/v1/asset/dribblet`)
- Added parameter `asset`
  - affected methods:
    - `asset_detail()` (`GET /sapi/v1/asset/assetDetail`)
- Modified response for `withdraw_history_v1()` (`GET /sapi/v1/localentity/withdraw/history`):
  - items: property `addressTag` deleted
  - items: item property `addressTag` deleted

- Modified response for `withdraw_history_v2()` (`GET /sapi/v2/localentity/withdraw/history`):
  - items: property `addressTag` deleted
  - items: item property `addressTag` deleted

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
