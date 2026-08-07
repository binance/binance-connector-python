# Changelog

## 6.0.0 - 2026-08-07

### Added (1)

- `get_latest_block_height()` (`GET /api/v1/dex/pre-transaction/block-height`)

### Changed (3)

- Updated `binance-common` library to version `4.2.0`
- Updated Dependencies
- Added parameter `vendor`
  - affected methods:
    - `get_aggregated_quote()` (`GET /api/v1/dex/aggregator/quote`)

## 5.0.0 - 2026-07-29

### Changed (8)

- Added parameter `fee_percent`
  - affected methods:
    - `get_aggregated_quote()` (`GET /api/v1/dex/aggregator/quote`)
    - `quote_and_build_swap_transaction()` (`GET /api/v1/dex/aggregator/quote-and-swap`)
    - `build_swap_transaction()` (`GET /api/v1/dex/aggregator/swap`)
    - `build_solana_swap_instructions()` (`GET /api/v1/dex/aggregator/swap-instruction`)
- Added parameter `fee_source`
  - affected methods:
    - `get_aggregated_quote()` (`GET /api/v1/dex/aggregator/quote`)
- Added parameter `from_token_referrer_wallet_address`
  - affected methods:
    - `quote_and_build_swap_transaction()` (`GET /api/v1/dex/aggregator/quote-and-swap`)
    - `build_swap_transaction()` (`GET /api/v1/dex/aggregator/swap`)
    - `build_solana_swap_instructions()` (`GET /api/v1/dex/aggregator/swap-instruction`)
- Added parameter `to_token_referrer_wallet_address`
  - affected methods:
    - `quote_and_build_swap_transaction()` (`GET /api/v1/dex/aggregator/quote-and-swap`)
    - `build_swap_transaction()` (`GET /api/v1/dex/aggregator/swap`)
    - `build_solana_swap_instructions()` (`GET /api/v1/dex/aggregator/swap-instruction`)
- Modified response for `get_aggregated_quote()` (`GET /api/v1/dex/aggregator/quote`):
  - `data`.items: property `actual_swap_amount` added
  - `data`.items: property `fee_amount` added
  - `data`.items: property `fee_token` added
  - `data`.items: item property `actual_swap_amount` added
  - `data`.items: item property `fee_amount` added
  - `data`.items: item property `fee_token` added

- Modified response for `quote_and_build_swap_transaction()` (`GET /api/v1/dex/aggregator/quote-and-swap`):
  - `data`.`routerResult`: property `actual_swap_amount` added
  - `data`.`routerResult`: property `fee_amount` added
  - `data`.`routerResult`: property `fee_token` added

- Modified response for `build_swap_transaction()` (`GET /api/v1/dex/aggregator/swap`):
  - `data`.`routerResult`: property `actual_swap_amount` added
  - `data`.`routerResult`: property `fee_amount` added
  - `data`.`routerResult`: property `fee_token` added

- Modified response for `buildSolanaSwapInstructions()` (`GET /api/v1/dex/aggregator/swap-instruction`):
  - `data`.`routerResult`: property `actual_swap_amount` added
  - `data`.`routerResult`: property `fee_amount` added
  - `data`.`routerResult`: property `fee_token` added

## 4.0.0 - 2026-07-28

### Changed (2)

- Added parameter `tron_tx`
  - affected methods:
    - `get_gas_limit()` (`POST /api/v1/dex/pre-transaction/gas-limit`)
    - `simulate_transactions()` (`POST /api/v1/dex/pre-transaction/simulate`)

- Modified response for `getGasLimit()` (`POST /api/v1/dex/pre-transaction/gas-limit`):
  - `data`: property `energyFee` added
  - `data`: property `energyRequired` added
  - `data`: property `freeBandwidth` added
  - `data`: property `freeEnergy` added
  - `data`: property `bandwidthFee` added
  - `data`: property `bandwidthRequired` added

## 3.0.0 - 2026-07-21

### Added (17)

- `get_address_pn_l_for_specific_token()` (`GET /api/v1/dex/market/portfolio/token/latest-pnl`)
- `get_address_portfolio_overview()` (`GET /api/v1/dex/market/portfolio/overview`)
- `get_address_recent_pn_l()` (`GET /api/v1/dex/market/portfolio/recent-pnl`)
- `get_dex_trade_history()` (`GET /api/v1/dex/market/portfolio/dex-history`)
- `get_portfolio_supported_chains()` (`GET /api/v1/dex/market/portfolio/supported/chain`)
- `get_leaderboard()` (`GET /api/v1/dex/market/leaderboard/list`)
- `get_tracked_trades()` (`GET /api/v1/dex/market/address-tracker/trades`)
- `get_rwa_token_issuance_platforms()` (`GET /api/v1/dex/market/rwa/platforms`)
- `get_rwa_token_list()` (`GET /api/v1/dex/market/rwa/tokens`)
- `get_rwa_token_price()` (`GET /api/v1/dex/market/rwa/price`)
- `get_rwa_underlying_info()` (`GET /api/v1/dex/market/rwa/underlying-profile`)
- `get_rwa_underlying_market_data()` (`GET /api/v1/dex/market/rwa/underlying-market`)
- `search_rwa_token()` (`GET /api/v1/dex/market/rwa/search`)
- `build_solana_swap_instructions()` (`GET /api/v1/dex/aggregator/swap-instruction`)
- `get_rfq_order_status()` (`GET /api/v1/dex/aggregator/order/{orderId}`)
- `quote_and_build_swap_transaction()` (`GET /api/v1/dex/aggregator/quote-and-swap`)
- `submit_rfq_order()` (`POST /api/v1/dex/aggregator/order/submit`)

### Changed (6)

- Added parameter `user_wallet_address`
  - affected methods:
    - `get_aggregated_quote()` (`GET /api/v1/dex/aggregator/quote`)
- Added parameter `vendor`
  - affected methods:
    - `get_erc20_approve_transaction()` (`GET /api/v1/dex/aggregator/approve-transaction`)
- Modified response for `get_aggregated_quote()` (`GET /api/v1/dex/aggregator/quote`):
  - `data`.items: property `approve_target` added
  - `data`.items: property `execution_mode` added
  - `data`.items: property `is_best` added
  - `data`.items: item property `approve_target` added
  - `data`.items: item property `execution_mode` added
  - `data`.items: item property `is_best` added
- Modified response for `build_swap_transaction()` (`GET /api/v1/dex/aggregator/swap`):
  - `data`: property `execution_mode` added
  - `data`: property `rfq` added
- Modified parameter `slippage_percent`:
  - required: `true` → `false`
  - affected methods:
    - `build_swap_transaction()` (`GET /api/v1/dex/aggregator/swap`)
- Update dependencies

## 2.0.1 - 2026-06-17

- Updated `binance-common` library to version `4.0.1`

## 2.0.0 - 2026-06-10

### Changed (8)

- Renamed `get_hot_tokens()` to `get_hot_token_list()`
- Renamed `get_price()` to `get_token_price()`
- Renamed `get_price_info()` to `get_token_trading_info()`
- Renamed `search_tokens()` to `search_token()`
- - Modified response for `get_candles()` (`GET /api/v1/dex/market/candles`):
  - `data`.items.items: type `string` → `number`
- Modified response for `get_hot_token_list()` (`GET /api/v1/dex/market/token/hot-token`):
  - `data`.`items`.items: property `riskLevel` deleted
  - `data`.`items`.items: item property `riskLevel` deleted

## 1.0.0 - 2026-06-09

- Initial release
