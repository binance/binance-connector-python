# Changelog

## 4.1.0 - 2026-01-13

### Changed (1)

- Updated `binance-common` library to version `3.4.0`

## 4.0.0 - 2025-12-22

### Changed (4)

- Updated `binance-common` library to version `3.3.0`
- Add `Body` to Rest API request

#### REST API

- Modified parameter `orders`:
  - items.`isMmp`: type `boolean` → `string`
  - items.`postOnly`: type `boolean` → `string`
  - items.`price`: type `number` → `string`
  - items.`quantity`: type `number` → `string`
  - items.`reduceOnly`: type `boolean` → `string`
  - items.`isMmp`: type `boolean` → `string`
  - items.`postOnly`: type `boolean` → `string`
  - items.`price`: type `number` → `string`
  - items.`quantity`: type `number` → `string`
  - items.`reduceOnly`: type `boolean` → `string`
  - affected methods:
    - `place_multiple_orders()` (`POST /eapi/v1/batchOrders`)

#### WebSocket Streams

- Modified parameter `id`:
  - type `string` → `integer`
  - affected methods:
    - `partial_book_depth_streams()` (`<symbol>@depth<levels>@<updateSpeed>` stream)
    - `index_price_streams()` (`<symbol>@index` stream)
    - `kline_candlestick_streams()` (`<symbol>@kline_<interval>` stream)
    - `ticker24_hour()` (`<symbol>@ticker` stream)
    - `trade_streams()` (`<symbol>@trade` stream)
    - `mark_price()` (`<underlyingAsset>@markPrice` stream)
    - `open_interest()` (`<underlyingAsset>@openInterest@<expirationDate>` stream)
    - `ticker24_hour_by_underlying_asset_and_expiration_data()` (`<underlyingAsset>@ticker@<expirationDate>` stream)
    - `new_symbol_info()` (`option_pair` stream)

## 3.0.0 - 2025-11-24

### Changed (2)

#### REST API

- Renamed `symbol_price_ticker()` to `index_price_ticker()`.

#### WebSocket Streams

- Modified response for `trade_streams()` (`<symbol>@trade` method):
  - `t`: number -> string

## 2.0.0 - 2025-10-10

### Changed (9)

- Updated `binance-common` library to version `3.2.0`

#### REST API

- Deleted parameter `price`
  - affected methods:
    - `new_block_trade_order()` (`POST /eapi/v1/block/order/create`)
- Deleted parameter `quantity`
  - affected methods:
    - `new_block_trade_order()` (`POST /eapi/v1/block/order/create`)
- Deleted parameter `side`
  - affected methods:
    - `new_block_trade_order()` (`POST /eapi/v1/block/order/create`)
- Deleted parameter `symbol`
  - affected methods:
    - `new_block_trade_order()` (`POST /eapi/v1/block/order/create`)
- Modified parameter `side`:
  - affected methods:
    - `new_order()` (`POST /eapi/v1/order`)
- Deleted parameter `limit`
  - affected methods:
    - `query_current_open_option_orders()` (`GET /eapi/v1/openOrders`)
- Modified parameter `orders`:
  - affected methods:
    - `place_multiple_orders()` (`POST /eapi/v1/batchOrders`)

#### WebSocket Streams

- Fixed typo for user data stream events response `account_update`

## 1.7.0 - 2025-09-24

### Changed (1)

- Modified method for removing slashes (`/`) in endpoints

## 1.6.0 - 2025-09-16

### Changed (1)

- Updated `binance-common` library to version `3.1.1`

## 1.5.0 - 2025-09-12

### Changed (1)

- Updated `binance-common` library to version `3.1.0`

## 1.4.0 - 2025-09-05

### Changed (1)

- Updated `binance-common` library to version `3.0.0`

## 1.3.0 - 2025-08-22

### Changed (2)

- Standardized type hints for required parameters by replacing `default = None` annotations with `Union[..., None]`

#### WebSocket Streams

- Updated Websocket Streams response type to `RequestStreamHandle`

## 1.2.0 - 2025-08-07

### Changed (1)

- Updated `binance-common` library to version `1.2.0`

## 1.1.1 - 2025-08-06

### Changed (1)

#### REST API

- Moved `option_margin_account_information` unit tests from `test_market_maker_endpoints_api` folder to `test_account_api`

## 1.1.0 - 2025-08-06

### Changed (4)

- Updated `binance-common` library to version `1.1.0`
- Changed models responses to handle upper and lower case parameters
- Added python version `3.13`

#### WebSocket Streams

- Changed `list_subscribe` to return `dict` response

## 1.0.0 - 2025-07-17

- Initial release
