# Changelog

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