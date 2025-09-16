# Changelog

## 3.1.1 - 2025-09-16

### Changed (1)

- Fixed missing enum check in `clean_none_value`.

## 3.1.0 - 2025-09-12

### Changed (3)

- Updated WebsocketStream user data stream response handler
- Updated Encoded request matrix handler
- Fix decimal type in request parameters

## 3.0.0 - 2025-09-05

### Added (2)

- Support automatic session re-logon on reconncetions/renewals when session is already logged on (`Session re-logon` option on `WebSocketAPIBase`).
- Added the `api_key` parameter to include `apiKey` in WebsocketAPI request parameters.

### Changed (2)

- Fixed return type mismatch by returning the raw value.
- Updated `WebsocketAPI` user data return value to match its type.

## 2.0.0 - 2025-08-22

### Changed (3)

- Added custom REST headers
- Added `subscribe_user_data`, `on` and `unsubscribe` method to `WebSocketAPIBase`
- Updated `RequestStream` response type to `RequestStreamHandle`

## 1.2.0 - 2025-08-07

### Changed (1)

- Fixed empty array response handling in `utils.py`.

## 1.1.0 - 2025-08-06

### Changed (2)

- Updated `list_subscribe` method `json_msg` format and response.
- Added Enum serialization in `utils.py` to handle Enum values.

## 1.0.0 - 2025-01-16

First release
