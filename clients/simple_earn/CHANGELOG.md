# Changelog

## 3.0.0 - 2025-09-12

### Added (8)

- `get_rwusd_account()` (`GET /sapi/v1/rwusd/account`)
- `get_rwusd_quota_details()` (`GET /sapi/v1/rwusd/quota`)
- `get_rwusd_rate_history()` (`GET /sapi/v1/rwusd/history/rateHistory`)
- `get_rwusd_redemption_history()` (`GET /sapi/v1/rwusd/history/redemptionHistory`)
- `get_rwusd_rewards_history()` (`GET /sapi/v1/rwusd/history/rewardsHistory`)
- `get_rwusd_subscription_history()` (`GET /sapi/v1/rwusd/history/subscriptionHistory`)
- `redeem_rwusd()` (`POST /sapi/v1/rwusd/redeem`)
- `subscribe_rwusd()` (`POST /sapi/v1/rwusd/subscribe`)

### Changed (4)

- Modified parameter `amount`:
  - affected methods:
    - `subscribe_flexible_product()` (`POST /sapi/v1/simple-earn/flexible/subscribe`)
    - `get_flexible_subscription_preview()` (`GET /sapi/v1/simple-earn/flexible/subscriptionPreview`)
    - `subscribe_locked_product()` (`POST /sapi/v1/simple-earn/locked/subscribe`)
    - `get_locked_subscription_preview()` (`GET /sapi/v1/simple-earn/locked/subscriptionPreview`)
- Modified parameter `asset`:
  - affected methods:
    - `get_flexible_redemption_record()` (`GET /sapi/v1/simple-earn/flexible/history/redemptionRecord`)
    - `get_flexible_rewards_history()` (`GET /sapi/v1/simple-earn/flexible/history/rewardsRecord`)
    - `get_flexible_subscription_record()` (`GET /sapi/v1/simple-earn/flexible/history/subscriptionRecord`)
    - `get_simple_earn_flexible_product_list()` (`GET /sapi/v1/simple-earn/flexible/list`)
    - `get_flexible_product_position()` (`GET /sapi/v1/simple-earn/flexible/position`)
    - `get_locked_redemption_record()` (`GET /sapi/v1/simple-earn/locked/history/redemptionRecord`)
    - `get_locked_rewards_history()` (`GET /sapi/v1/simple-earn/locked/history/rewardsRecord`)
    - `get_locked_subscription_record()` (`GET /sapi/v1/simple-earn/locked/history/subscriptionRecord`)
    - `get_simple_earn_locked_product_list()` (`GET /sapi/v1/simple-earn/locked/list`)
    - `get_locked_product_position()` (`GET /sapi/v1/simple-earn/locked/position`)
- Modified parameter `type`:
  - affected methods:
    - `get_flexible_rewards_history()` (`GET /sapi/v1/simple-earn/flexible/history/rewardsRecord`)
- Updated `binance-common` library to version `3.1.0`

## 2.1.0 - 2025-09-05

### Changed (2)

- Modified response for `get_simple_earn_locked_product_list()` (`GET /sapi/v1/simple-earn/locked/list`):
  - `rows`.`detail`.`boostEndTime`: type `string` → `integer`
- Updated `binance-common` library to version `3.0.0`

## 2.0.0 - 2025-08-22

### Changed (3)

- Standardized type hints for required parameters by replacing `default = None` annotations with `Union[..., None]`

- Modified response for `get_simple_earn_flexible_product_list()` method (`GET /sapi/v1/simple-earn/flexible/list`):
  - `rows`.`subscriptionStartTime`: type `string` → `integer`

- Modified response for `get_simple_earn_locked_product_list()` method (`GET /sapi/v1/simple-earn/locked/list`):
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
