# Changelog

## 3.0.0 - 2025-09-12

### Added (4)

- `get_soft_staking_product_list()` (`GET /sapi/v1/soft-staking/list`)
- `get_soft_staking_rewards_history()` (`GET /sapi/v1/soft-staking/history/rewardsRecord`)
- `set_soft_staking()` (`GET /sapi/v1/soft-staking/set`)
- Updated `binance-common` library to version `3.1.0`

## 2.1.0 - 2025-09-05

### Changed (1)

- Updated `binance-common` library to version `3.0.0`

## 2.0.0 - 2025-08-22

### Changed (2)

- Standardized type hints for required parameters by replacing `default = None` annotations with `Union[..., None]`

- Modified response for `get_on_chain_yields_locked_product_list()` method (`GET /sapi/v1/onchain-yields/locked/list`):
  - `rows`.`detail`.`subscriptionStartTime`: type `string` → `integer`

## 1.2.0 - 2025-08-07

### Changed (1)

- Updated `binance-common` library to version `1.2.0`

## 1.1.0 - 2025-08-06

### Changed (2)

- Updated `binance-common` library to version `1.1.0`
- Added python version `3.13`

## 1.0.0 - 2025-07-17

- Initial release
