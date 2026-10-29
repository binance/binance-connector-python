# Changelog

## 1.2.0 - 2026-10-29

### Changed (3)

- Updated `binance-common` library to version `4.8.0`
- Updated Dependencies
- Added python version `3.15`

### Removed (1)

- Dropped support for Python `3.10` (minimum supported version is now `3.11`)

## 1.1.0 - 2026-10-23

### Changed (5)

- Updated `binance-common` library to version `4.7.0`
- Updated Dependencies

#### WebSocket Streams

- Deleted parameter `id`
  - affected methods:
    - `com_announcement_en()` (`com_announcement_en` stream)
- Signed connections are now handled by `binance-common` (`WebSocketStreamBase(..., signed=True)`)
- Fixed the module description, which was copied from the W3W Prediction connector

## 1.0.0 - 2026-10-15

- Initial release
