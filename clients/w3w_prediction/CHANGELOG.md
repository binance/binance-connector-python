# Changelog

## 1.8.0 - 2026-10-23

### Changed (6)

- Updated `binance-common` library to version `4.7.0`
- Updated Dependencies

#### WebSocket Streams

- Deleted parameter `id`
  - affected methods:
    - `batch_claim_partially_succeeded()` (`web3_prediction_pm_claim_partial_success` stream)
    - `fund_transfer_failed()` (`web3_prediction_pm_transfer_fail` stream)
    - `fund_transfer_succeeded()` (`web3_prediction_pm_transfer_success` stream)
    - `limit_order_fully_filled()` (`web3_prediction_pm_limit_order_filled` stream)
    - `limit_order_partially_filled()` (`web3_prediction_pm_limit_order_partial_fill` stream)
    - `limit_order_submission_failed()` (`web3_prediction_pm_limit_submit_fail` stream)
    - `limit_order_submitted_successfully()` (`web3_prediction_pm_limit_submit_success` stream)
    - `market_buy_order_failed()` (`web3_prediction_pm_market_buy_fail` stream)
    - `market_buy_order_fully_filled()` (`web3_prediction_pm_market_buy_success` stream)
    - `market_resolution_notification()` (`web3_prediction_pm_market_close` stream)
    - `market_sell_order_failed_expired()` (`web3_prediction_pm_market_sell_fail` stream)
    - `market_sell_order_fully_filled()` (`web3_prediction_pm_market_sell_success` stream)
    - `prediction_order_book_by_market_id()` (`web3_prediction_orderbook_<marketId>` stream)
    - `reward_claim_failed()` (`web3_prediction_pm_claim_fail` stream)
    - `reward_claim_succeeded()` (`web3_prediction_pm_claim_success` stream)
- Modified response for `prediction_order_book_by_market_id()` (`web3_prediction_orderbook_<marketId>` stream):
  - `asks`.items.items: type `string` → `number`
  - `bids`.items.items: type `string` → `number`

- Removed response schema `predictionOrderBookAllResponse`
- Updated stream and response field descriptions

### Removed (1)

#### WebSocket Streams

- `prediction_order_book_all()` (`web3_prediction_orderbook_data` stream)

## 1.7.0 - 2026-10-15

### Added (16)

#### WebSocket Streams

- `batch_claim_partially_succeeded()` (`web3_prediction_pm_claim_partial_success` stream)
- `fund_transfer_failed()` (`web3_prediction_pm_transfer_fail` stream)
- `fund_transfer_succeeded()` (`web3_prediction_pm_transfer_success` stream)
- `limit_order_fully_filled()` (`web3_prediction_pm_limit_order_filled` stream)
- `limit_order_partially_filled()` (`web3_prediction_pm_limit_order_partial_fill` stream)
- `limit_order_submission_failed()` (`web3_prediction_pm_limit_submit_fail` stream)
- `limit_order_submitted_successfully()` (`web3_prediction_pm_limit_submit_success` stream)
- `market_buy_order_failed()` (`web3_prediction_pm_market_buy_fail` stream)
- `market_buy_order_fully_filled()` (`web3_prediction_pm_market_buy_success` stream)
- `market_resolution_notification()` (`web3_prediction_pm_market_close` stream)
- `market_sell_order_failed_expired()` (`web3_prediction_pm_market_sell_fail` stream)
- `market_sell_order_fully_filled()` (`web3_prediction_pm_market_sell_success` stream)
- `prediction_order_book_all()` (`web3_prediction_orderbook_data` stream)
- `prediction_order_book_by_market_id()` (`web3_prediction_orderbook_<marketId>` stream)
- `reward_claim_failed()` (`web3_prediction_pm_claim_fail` stream)
- `reward_claim_succeeded()` (`web3_prediction_pm_claim_success` stream)

### Changed (2)

- Updated `binance-common` library to version `4.6.0`
- Updated Dependencies

## 1.6.1 - 2026-10-09

### Changed (2)

- Modified response for `get_market_detail()` (`GET /sapi/v1/w3w/wallet/prediction/market/detail`):
  - `markets`.items.`outcomes`.items: property `winner` added
  - `markets`.items.`outcomes`.items: item property `winner` added
  - `markets`.items.`outcomes`.items: property `winner` added
  - `markets`.items.`outcomes`.items: item property `winner` added

- Modified response field `markets`:
  - items.`outcomes`.items: property `winner` added
  - items.`outcomes`.items: item property `winner` added
  - items.`outcomes`.items: property `winner` added
  - items.`outcomes`.items: item property `winner` added
  - affected events:
    - `getMarketDetailResponse`

## 1.6.0 - 2026-10-06

### Changed (1)

- Updated `binance-common` library to version `4.5.1`

## 1.5.0 - 2026-09-23

### Changed (1)

- Updated `binance-common` library to version `4.5.0`

## 1.4.0 - 2026-09-02

### Changed (2)

- Updated `binance-common` library to version `4.4.0`
- Updated code generation templates.

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
