# Changelog

## 1.3.0 - 2026-08-19

### Changed (1)

- Updated `binance-common` library to version `4.3.0`

## 1.2.0 - 2026-08-18

### Added (10)

- `apply_mm_deposit()` (`POST /sapi/v1/w3w/wallet/prediction/deposit/apply`)
- `apply_mm_withdraw()` (`POST /sapi/v1/w3w/wallet/prediction/withdraw/apply`)
- `create_otc_blocktrade()` (`POST /sapi/v1/w3w/wallet/prediction/otc/blocktrade/create`)
- `fulfil_otc_blocktrade()` (`POST /sapi/v1/w3w/wallet/prediction/otc/blocktrade/fulfil`)
- `get_otc_blocktrade_detail()` (`POST /sapi/v1/w3w/wallet/prediction/otc/blocktrade/detail`)
- `get_otc_blocktrade_events()` (`POST /sapi/v1/w3w/wallet/prediction/otc/blocktrade/events`)
- `get_otc_reserved_balances()` (`POST /sapi/v1/w3w/wallet/prediction/otc/blocktrade/reserved-balances`)
- `list_otc_blocktrades()` (`POST /sapi/v1/w3w/wallet/prediction/otc/blocktrade/list`)
- `preview_otc_blocktrade()` (`POST /sapi/v1/w3w/wallet/prediction/otc/blocktrade/preview`)
- `remove_otc_blocktrades()` (`POST /sapi/v1/w3w/wallet/prediction/otc/blocktrade/remove`)

### Changed (10)

- Added response schema `fulfilOtcBlocktradeResponse`
- Added response schema `listOtcBlocktradesResponse`
- Added response schema `removeOtcBlocktradesResponse`
- Added response schema `getOtcBlocktradeDetailResponse`
- Added response schema `getOtcBlocktradeEventsResponse`
- Added response schema `getOtcReservedBalancesResponse`
- Added response schema `previewOtcBlocktradeResponse`
- Added response schema `applyMmDepositResponse`
- Added response schema `applyMmWithdrawResponse`
- Added response schema `createOtcBlocktradeResponse`

## 1.1.0 - 2026-08-07

### Changed (2)

- Updated `binance-common` library to version `4.2.0`
- Updated Dependencies

## 1.0.1 - 2026-06-30

- Updated `pyproject.toml` dependencies

## 1.0.0 - 2026-06-29

- Initial release
