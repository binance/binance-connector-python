# Changelog

## 5.6.0 - 2026-03-26

### Changed (8)

- Updated `binance-common` library to version `3.8.0`
- Updated `tox` file
- - Added parameter `purchaseId`
  - affected methods:
    - `get_eth_staking_history()` (`GET /sapi/v1/eth-staking/eth/history/stakingHistory`)
    - `get_sol_staking_history()` (`GET /sapi/v1/sol-staking/sol/history/stakingHistory`)
- Added parameter `redeemId`
  - affected methods:
    - `get_eth_redemption_history()` (`GET /sapi/v1/eth-staking/eth/history/redemptionHistory`)
    - `get_sol_redemption_history()` (`GET /sapi/v1/sol-staking/sol/history/redemptionHistory`)
- Modified response for `redeem_eth()` (`POST /sapi/v1/eth-staking/eth/redeem`):
  - property `redeemId` added

- Modified response for `redeem_sol()` (`POST /sapi/v1/sol-staking/sol/redeem`):
  - property `redeemId` added

- Modified response for `subscribe_sol_staking()` (`POST /sapi/v1/sol-staking/sol/stake`):
  - property `purchaseId` added

- Modified response for `subscribe_eth_staking()` (`POST /sapi/v2/eth-staking/eth/stake`):
  - property `purchaseId` added

## 5.5.0 - 2026-03-16

### Changed (1)

- Updated `binance-common` library to version `3.7.0`

## 5.4.0 - 2026-02-11

### Changed (2)

- Updated `binance-common` library to version `3.6.0`
- Updated `pyproject.toml` dependencies

## 5.3.0 - 2026-01-29

### Changed (1)

- Updated `binance-common` library to version `3.5.0`

## 5.2.0 - 2026-01-23

### Changed (1)

- Updated `binance-common` library to version `3.4.1`

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
