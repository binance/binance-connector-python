# Changelog

## 5.1.0 - 2025-01-13

### Changed (1)

- Updated `binance-common` library to version `3.4.0`

## 5.0.0 - 2025-12-22

- Updated `binance-common` library to version `3.3.0`
- Add `Body` to Rest API request

## 4.0.0 - 2025-11-14

### Changed (1)

- Modified response for `get_current_eth_staking_quota()` (`GET /sapi/v1/eth-staking/eth/quota`):
  - property `redeemPeriod` added
  - property `redeemable` added
  - property `calculating` added
  - property `minRedeemAmount` added
  - property `stakeable` added
  - property `commissionFee` added
  - property `minStakeAmount` added

## 3.2.0 - 2025-10-10

### Changed (2)

- Updated `binance-common` library to version `3.2.0`

#### REST API

- Fixed responses typo

## 3.1.0 - 2025-09-16

### Changed (1)

- Updated `binance-common` library to version `3.1.1`

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
