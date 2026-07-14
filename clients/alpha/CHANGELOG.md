# Changelog

## 2.0.0 - 2026-07-14

### Added (1)

#### REST API

- `full_depth()` (`GET /bapi/defi/v1/public/alpha-trade/fullDepth`)

### Changed (2)

- Updated `binance-common` library to version `4.0.3`

#### REST API

- Modified parameter `interval`:
  - enum added: `1s`, `15s`, `1m`, `3m`, `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `8h`, `12h`, `1d`, `3d`, `1w`, `1M`
  - affected methods:
    - `klines()` (`GET /bapi/defi/v1/public/alpha-trade/klines`)
- Modified parameter `limit`:
  - enum added: `5`, `10`, `20`, `50`, `100`, `500`, `1000`
  - affected methods:
    - `full_depth()` (`GET /bapi/defi/v1/public/alpha-trade/fullDepth`)

## 1.9.0 - 2026-06-09

### Changed (2)

- Updated `binance-common` library to version `4.0.0`
- Updated `pyproject.toml` dependencies

## 1.8.0 - 2026-05-29

### Changed (1)

- Updated `binance-common` library to version `3.10.0`

## 1.7.0 - 2026-05-22

- Updated `binance-common` library to version `3.9.2`
- Updated `pyproject.toml` dependencies

## 1.6.0 - 2026-04-29

- Updated `binance-common` library to version `3.9.1`
- Updated `pyproject.toml` dependencies

## 1.5.0 - 2026-04-29

### Changed (1)

- Updated `binance-common` library to version `3.9.0`

## 1.4.0 - 2026-03-26

### Added (1)

- Added `py.typed` file to indicate that the package supports type hints.

### Changed (2)

- Updated `binance-common` library to version `3.8.0`
- Updated `tox` file

## 1.3.0 - 2026-03-16

### Changed (1)

- Updated `binance-common` library to version `3.7.0`

## 1.2.1 - 2026-02-25

### Changed (1)

- Updated `Klines_response` model to remove unused `KlinesResponseDataItemInner` struct

## 1.2.0 - 2026-02-11

### Changed (2)

- Updated `binance-common` library to version `3.6.0`
- Updated `pyproject.toml` dependencies

## 1.1.0 - 2026-01-29

### Changed (1)

- Updated `binance-common` library to version `3.5.0`

## 1.0.0 - 2026-01-23

- Initial release
