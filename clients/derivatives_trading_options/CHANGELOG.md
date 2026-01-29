# Changelog

## 5.2.0 - 2026-01-29

### Changed (1)

- Updated `binance-common` library to version `3.5.0`

## 5.1.0 - 2026-01-23

### Changed (1)

- Updated `binance-common` library to version `3.4.1`

## 5.0.0 - 2026-01-19

### Added (10)

#### REST API

- `user_commission()` (`GET /eapi/v1/commission`)

#### WebSocket Streams

- `diff_book_depth_streams()` (`<symbol>@depth@<updateSpeed>` stream)
- `index_price_streams()` (`!index@arr` stream)
- `individual_symbol_book_ticker_streams()` (`<symbol>@bookTicker` stream)
- `mark_price()` (`<underlying>@optionMarkPrice` stream)
- `new_symbol_info()` (`!optionSymbol` stream)
- `open_interest()` (`underlying@optionOpenInterest@<expirationDate>` stream)
- `partial_book_depth_streams()` (`<symbol>@depth<level>@<updateSpeed>` stream)
- `ticker24_hour()` (`<symbol>@optionTicker` stream)
- `trade_streams()` (`<symbol>@optionTrade` stream)

### Changed (20)

#### REST API

- Modified parameter `orders`:
  - items.`timeInForce`: enum added: `GTX`
  - items.`timeInForce`: enum added: `GTX`
  - affected methods:
    - `place_multiple_orders()` (`POST /eapi/v1/batchOrders`)
- Modified parameter `timeInForce`:
  - enum added: `GTX`
  - affected methods:
    - `new_order()` (`POST /eapi/v1/order`)
- Modified response for `cancel_all_option_orders_by_underlying()` (`DELETE /eapi/v1/allOpenOrdersByUnderlying`):
  - property `data` deleted

- Modified response for `cancel_multiple_option_orders()` (`DELETE /eapi/v1/batchOrders`):
  - items: property `priceScale` added
  - items: property `optionSide` added
  - items: property `mmp` added
  - items: property `source` added
  - items: property `quoteAsset` added
  - items: property `quantityScale` added
  - items: property `fee` deleted
  - items: item property `priceScale` added
  - items: item property `optionSide` added
  - items: item property `mmp` added
  - items: item property `source` added
  - items: item property `quoteAsset` added
  - items: item property `quantityScale` added
  - items: item property `fee` deleted

- Modified response for `place_multiple_orders()` (`POST /eapi/v1/batchOrders`):
  - items: property `optionSide` added
  - items: property `status` added
  - items: property `timeInForce` added
  - items: property `quantityScale` added
  - items: property `avgPrice` added
  - items: property `createTime` added
  - items: property `priceScale` added
  - items: property `source` added
  - items: property `quoteAsset` added
  - items: property `updateTime` added
  - items: property `executedQty` added
  - items: property `postOnly` deleted
  - items: item property `optionSide` added
  - items: item property `status` added
  - items: item property `timeInForce` added
  - items: item property `quantityScale` added
  - items: item property `avgPrice` added
  - items: item property `createTime` added
  - items: item property `priceScale` added
  - items: item property `source` added
  - items: item property `quoteAsset` added
  - items: item property `updateTime` added
  - items: item property `executedQty` added
  - items: item property `postOnly` deleted

- Modified response for `order_book()` (`GET /eapi/v1/depth`):
  - property `lastUpdateId` added
  - property `u` deleted

- Modified response for `exchange_information()` (`GET /eapi/v1/exchangeInfo`):
  - `optionSymbols`.items: property `status` added
  - `optionSymbols`.items: property `makerFeeRate` deleted
  - `optionSymbols`.items: property `takerFeeRate` deleted
  - `optionSymbols`.items: item property `status` added
  - `optionSymbols`.items: item property `makerFeeRate` deleted
  - `optionSymbols`.items: item property `takerFeeRate` deleted

- Modified response for `user_exercise_record()` (`GET /eapi/v1/exerciseRecord`):
  - items: property `markPrice` deleted
  - items: item property `markPrice` deleted

- Modified response for `query_option_order_history()` (`GET /eapi/v1/historyOrders`):
  - items: property `reason` deleted
  - items: property `postOnly` deleted
  - items: property `source` deleted
  - items: property `fee` deleted
  - items: item property `reason` deleted
  - items: item property `postOnly` deleted
  - items: item property `source` deleted
  - items: item property `fee` deleted

- Modified response for `kline_candlestick_data()` (`GET /eapi/v1/klines`):
  - items: type `object` → `array`
  - items: property `interval` deleted
  - items: property `openTime` deleted
  - items: property `takerVolume` deleted
  - items: property `amount` deleted
  - items: property `close` deleted
  - items: property `low` deleted
  - items: property `takerAmount` deleted
  - items: property `closeTime` deleted
  - items: property `high` deleted
  - items: property `open` deleted
  - items: property `tradeCount` deleted
  - items: property `volume` deleted
  - items: item property `interval` deleted
  - items: item property `openTime` deleted
  - items: item property `takerVolume` deleted
  - items: item property `amount` deleted
  - items: item property `close` deleted
  - items: item property `low` deleted
  - items: item property `takerAmount` deleted
  - items: item property `closeTime` deleted
  - items: item property `high` deleted
  - items: item property `open` deleted
  - items: item property `tradeCount` deleted
  - items: item property `volume` deleted

- Modified response for `start_user_data_stream()` (`POST /eapi/v1/listenKey`):
  - property `expiration` added

- Modified response for `option_margin_account_information()` (`GET /eapi/v1/marginAccount`):
  - property `canDeposit` added
  - property `canTrade` added
  - property `canWithdraw` added
  - property `reduceOnly` added

- Modified response for `query_current_open_option_orders()` (`GET /eapi/v1/openOrders`):
  - items: property `postOnly` deleted
  - items: property `fee` deleted
  - items: item property `postOnly` deleted
  - items: item property `fee` deleted

- Modified response for `cancel_option_order()` (`DELETE /eapi/v1/order`):
  - property `postOnly` deleted
  - property `fee` deleted

- Modified response for `query_single_order()` (`GET /eapi/v1/order`):
  - property `postOnly` deleted
  - property `fee` deleted
  - property `source` deleted

- Modified response for `new_order()` (`POST /eapi/v1/order`):
  - property `source` added
  - property `fee` deleted
  - property `postOnly` deleted
  - property `createDate` deleted

- Modified response for `option_position_information()` (`GET /eapi/v1/position`):
  - items: property `time` added
  - items: property `bidQuantity` added
  - items: property `askQuantity` added
  - items: property `ror` deleted
  - items: property `positionCost` deleted
  - items: property `reducibleQty` deleted
  - items: item property `time` added
  - items: item property `bidQuantity` added
  - items: item property `askQuantity` added
  - items: item property `ror` deleted
  - items: item property `positionCost` deleted
  - items: item property `reducibleQty` deleted

- Modified response for `recent_trades_list()` (`GET /eapi/v1/trades`):
  - items: property `tradeId` added
  - items.`id`: type `string` → `integer`
  - items: item property `tradeId` added
  - items.`id`: type `string` → `integer`

- Modified response for `account_trade_list()` (`GET /eapi/v1/userTrades`):
  - items: property `volatility` deleted
  - items: item property `volatility` deleted

#### WebSocket Streams

- Modified response for `kline_candlestick_streams()` (`<symbol>@kline_<interval>` stream):
  - `k`: property `f` added
  - `k`: property `F` deleted

### Removed (12)

#### REST API

- `get_download_id_for_option_transaction_history()` (`GET /eapi/v1/income/asyn`)
- `get_option_transaction_history_download_link_by_id()` (`GET /eapi/v1/income/asyn/id`)
- `old_trades_lookup()` (`GET /eapi/v1/historicalTrades`)
- `option_account_information()` (`GET /eapi/v1/account`)

#### WebSocket Streams

- `/<symbol>@depth<levels>@<update_speed>()` (`<symbol>@depth<levels>@<updateSpeed>` stream)
- `/<symbol>@index()` (`<symbol>@index` stream)
- `/<symbol>@ticker()` (`<symbol>@ticker` stream)
- `/<symbol>@trade()` (`<symbol>@trade` stream)
- `/<underlying_asset>@mark_price()` (`<underlyingAsset>@markPrice` stream)
- `/<underlying_asset>@open_interest@<expiration_date>()` (`<underlyingAsset>@openInterest@<expirationDate>` stream)
- `/<underlying_asset>@ticker@<expiration_date>()` (`<underlyingAsset>@ticker@<expirationDate>` stream)
- `/option_pair()` (`option_pair` stream)

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
