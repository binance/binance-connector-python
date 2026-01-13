# Changelog

## 6.1.0 - 2025-01-13

### Changed (1)

- Updated `binance-common` library to version `3.4.0`

## 6.0.0 - 2025-12-22

### Added (5)

#### REST API

- `order_list_opo()` (`POST /api/v3/orderList/opo`)
- `order_list_opoco()` (`POST /api/v3/orderList/opoco`)

#### WebSocket API

- `order_list_place_opo()` (`orderList.place.opo` method)
- `order_list_place_opoco()` (`orderList.place.opoco` method)
- `order_amend_keep_priority()` (`order.amend.keepPriority` method)

### Changed (4)

- Updated `binance-common` library to version `3.3.0`
- Add `Body` to Rest API request

#### REST API

- Modified response for `exchange_info()` (`GET /api/v3/exchangeInfo`):
  - `symbols`.items: property `opoAllowed` added
  - `symbols`.items: item property `opoAllowed` added

#### WebSocket API

- Modified response for `exchange_info()` (`exchangeInfo` method):
  - `result`.`symbols`.items: property `opoAllowed` added
  - `result`.`symbols`.items: item property `opoAllowed` added

### Removed (1)

#### WebSocket Streams

- `/!ticker@arr()` (`!ticker@arr` stream)

## 5.0.0 - 2025-11-24

### Changed (1)

#### WebSocket Streams

- Marked `all_ticker()` (`!ticker@arr` stream) as deprecated.

## 4.0.0 - 2025-11-14

### Changed (2)

#### REST API

- Added parameter `symbolStatus`
  - affected methods:
    - `depth()` (`GET /api/v3/depth`)
    - `ticker()` (`GET /api/v3/ticker`)
    - `ticker24hr()` (`GET /api/v3/ticker/24hr`)
    - `ticker_book_ticker()` (`GET /api/v3/ticker/bookTicker`)
    - `ticker_price()` (`GET /api/v3/ticker/price`)
    - `ticker_trading_day()` (`GET /api/v3/ticker/tradingDay`)

#### WebSocket API

- Added parameter `symbolStatus`
  - affected methods:
    - `depth()` (`depth` method)
    - `ticker()` (`ticker` method)
    - `ticker24hr()` (`ticker.24hr` method)
    - `ticker_book()` (`ticker.book` method)
    - `ticker_price()` (`ticker.price` method)
    - `ticker_trading_day()` (`ticker.tradingDay` method)
- Marked `order_oco` (`POST /api/v3/order/oco`) as deprecated.

- Marked `order_list_place` (`orderList.place` method) as deprecated.

## 3.0.0 - 2025-10-10

### Added (2)

#### REST API

- `myFilters()` (`GET /api/v3/myFilters`)

#### WebSocket API

- `myFilters()` (`myFilters` method)

### Changed (8)

- Updated `binance-common` library to version `3.2.0`
- Updated `recv_window` type from `Optional[int]` to `Optional[float]`
- Modified parameter `OrderListOcoBelowTimeInForceEnum`:
  - enum added: `GTC`, `IOC`, `FOK`
  - affected methods: `order_list_oco()` (`POST /api/v3/orderList/oco`)
- Fixed models typo

#### REST API

- Modified response for `exchange_info()` (`GET /api/v3/exchangeInfo`):
  - `exchangeFilters`: item property `minQty` deleted
  - `exchangeFilters`: item property `minTrailingAboveDelta` deleted
  - `exchangeFilters`: item property `bidMultiplierDown` deleted
  - `exchangeFilters`: item property `applyMinToMarket` deleted
  - `exchangeFilters`: item property `stepSize` deleted
  - `exchangeFilters`: item property `maxNumAlgoOrders` deleted
  - `exchangeFilters`: item property `tickSize` deleted
  - `exchangeFilters`: item property `applyMaxToMarket` deleted
  - `exchangeFilters`: item property `avgPriceMins` deleted
  - `exchangeFilters`: item property `askMultiplierDown` deleted
  - `exchangeFilters`: item property `filterType` deleted
  - `exchangeFilters`: item property `maxTrailingBelowDelta` deleted
  - `exchangeFilters`: item property `maxPrice` deleted
  - `exchangeFilters`: item property `multiplierDown` deleted
  - `exchangeFilters`: item property `askMultiplierUp` deleted
  - `exchangeFilters`: item property `maxNumOrderLists` deleted
  - `exchangeFilters`: item property `asset` deleted
  - `exchangeFilters`: item property `applyToMarket` deleted
  - `exchangeFilters`: item property `maxNumOrderAmends` deleted
  - `exchangeFilters`: item property `multiplierUp` deleted
  - `exchangeFilters`: item property `maxPosition` deleted
  - `exchangeFilters`: item property `maxNumOrders` deleted
  - `exchangeFilters`: item property `maxNotional` deleted
  - `exchangeFilters`: item property `maxTrailingAboveDelta` deleted
  - `exchangeFilters`: item property `bidMultiplierUp` deleted
  - `exchangeFilters`: item property `minTrailingBelowDelta` deleted
  - `exchangeFilters`: item property `minPrice` deleted
  - `exchangeFilters`: item property `maxNumIcebergOrders` deleted
  - `exchangeFilters`: item property `minNotional` deleted
  - `exchangeFilters`: item property `maxQty` deleted
  - `exchangeFilters`: item property `limit` deleted
  - `symbols`.`filters`: item property `maxTrailingAboveDelta` deleted
  - `symbols`.`filters`: item property `maxNumOrderAmends` deleted
  - `symbols`.`filters`: item property `askMultiplierUp` deleted
  - `symbols`.`filters`: item property `maxNumOrderLists` deleted
  - `symbols`.`filters`: item property `maxQty` deleted
  - `symbols`.`filters`: item property `minNotional` deleted
  - `symbols`.`filters`: item property `applyMaxToMarket` deleted
  - `symbols`.`filters`: item property `maxTrailingBelowDelta` deleted
  - `symbols`.`filters`: item property `maxNotional` deleted
  - `symbols`.`filters`: item property `multiplierUp` deleted
  - `symbols`.`filters`: item property `bidMultiplierUp` deleted
  - `symbols`.`filters`: item property `minTrailingBelowDelta` deleted
  - `symbols`.`filters`: item property `limit` deleted
  - `symbols`.`filters`: item property `asset` deleted
  - `symbols`.`filters`: item property `avgPriceMins` deleted
  - `symbols`.`filters`: item property `filterType` deleted
  - `symbols`.`filters`: item property `applyToMarket` deleted
  - `symbols`.`filters`: item property `minQty` deleted
  - `symbols`.`filters`: item property `multiplierDown` deleted
  - `symbols`.`filters`: item property `stepSize` deleted
  - `symbols`.`filters`: item property `maxNumOrders` deleted
  - `symbols`.`filters`: item property `bidMultiplierDown` deleted
  - `symbols`.`filters`: item property `maxNumIcebergOrders` deleted
  - `symbols`.`filters`: item property `maxPrice` deleted
  - `symbols`.`filters`: item property `minTrailingAboveDelta` deleted
  - `symbols`.`filters`: item property `minPrice` deleted
  - `symbols`.`filters`: item property `maxNumAlgoOrders` deleted
  - `symbols`.`filters`: item property `applyMinToMarket` deleted
  - `symbols`.`filters`: item property `tickSize` deleted
  - `symbols`.`filters`: item property `askMultiplierDown` deleted
  - `symbols`.`filters`: item property `maxPosition` deleted

- Modified response for `my_filters()` (`GET /api/v3/myFilters`):
  - `assetFilters`: item property `maxNotional` deleted
  - `assetFilters`: item property `multiplierUp` deleted
  - `assetFilters`: item property `maxTrailingAboveDelta` deleted
  - `assetFilters`: item property `maxNumOrderAmends` deleted
  - `assetFilters`: item property `bidMultiplierDown` deleted
  - `assetFilters`: item property `maxNumOrderLists` deleted
  - `assetFilters`: item property `maxQty` deleted
  - `assetFilters`: item property `maxNumOrders` deleted
  - `assetFilters`: item property `minNotional` deleted
  - `assetFilters`: item property `asset` deleted
  - `assetFilters`: item property `applyMaxToMarket` deleted
  - `assetFilters`: item property `avgPriceMins` deleted
  - `assetFilters`: item property `minTrailingAboveDelta` deleted
  - `assetFilters`: item property `askMultiplierDown` deleted
  - `assetFilters`: item property `minTrailingBelowDelta` deleted
  - `assetFilters`: item property `maxTrailingBelowDelta` deleted
  - `assetFilters`: item property `applyMinToMarket` deleted
  - `assetFilters`: item property `applyToMarket` deleted
  - `assetFilters`: item property `multiplierDown` deleted
  - `assetFilters`: item property `maxPosition` deleted
  - `assetFilters`: item property `askMultiplierUp` deleted
  - `assetFilters`: item property `limit` deleted
  - `assetFilters`: item property `minQty` deleted
  - `assetFilters`: item property `filterType` deleted
  - `assetFilters`: item property `maxNumIcebergOrders` deleted
  - `assetFilters`: item property `maxPrice` deleted
  - `assetFilters`: item property `bidMultiplierUp` deleted
  - `assetFilters`: item property `stepSize` deleted
  - `assetFilters`: item property `maxNumAlgoOrders` deleted
  - `assetFilters`: item property `tickSize` deleted
  - `assetFilters`: item property `minPrice` deleted
  - `exchangeFilters`: item property `avgPriceMins` deleted
  - `exchangeFilters`: item property `minTrailingBelowDelta` deleted
  - `exchangeFilters`: item property `multiplierDown` deleted
  - `exchangeFilters`: item property `maxQty` deleted
  - `exchangeFilters`: item property `maxNumAlgoOrders` deleted
  - `exchangeFilters`: item property `maxTrailingAboveDelta` deleted
  - `exchangeFilters`: item property `maxNumOrderAmends` deleted
  - `exchangeFilters`: item property `maxPosition` deleted
  - `exchangeFilters`: item property `askMultiplierUp` deleted
  - `exchangeFilters`: item property `limit` deleted
  - `exchangeFilters`: item property `minTrailingAboveDelta` deleted
  - `exchangeFilters`: item property `maxNotional` deleted
  - `exchangeFilters`: item property `applyToMarket` deleted
  - `exchangeFilters`: item property `maxNumOrders` deleted
  - `exchangeFilters`: item property `bidMultiplierUp` deleted
  - `exchangeFilters`: item property `applyMinToMarket` deleted
  - `exchangeFilters`: item property `askMultiplierDown` deleted
  - `exchangeFilters`: item property `minQty` deleted
  - `exchangeFilters`: item property `maxTrailingBelowDelta` deleted
  - `exchangeFilters`: item property `bidMultiplierDown` deleted
  - `exchangeFilters`: item property `maxNumIcebergOrders` deleted
  - `exchangeFilters`: item property `maxPrice` deleted
  - `exchangeFilters`: item property `minNotional` deleted
  - `exchangeFilters`: item property `asset` deleted
  - `exchangeFilters`: item property `stepSize` deleted
  - `exchangeFilters`: item property `tickSize` deleted
  - `exchangeFilters`: item property `applyMaxToMarket` deleted
  - `exchangeFilters`: item property `filterType` deleted
  - `exchangeFilters`: item property `multiplierUp` deleted
  - `exchangeFilters`: item property `minPrice` deleted
  - `exchangeFilters`: item property `maxNumOrderLists` deleted
  - `symbolFilters`: item property `minNotional` deleted
  - `symbolFilters`: item property `asset` deleted
  - `symbolFilters`: item property `maxNumOrders` deleted
  - `symbolFilters`: item property `applyMaxToMarket` deleted
  - `symbolFilters`: item property `avgPriceMins` deleted
  - `symbolFilters`: item property `maxNumOrderLists` deleted
  - `symbolFilters`: item property `applyMinToMarket` deleted
  - `symbolFilters`: item property `minTrailingAboveDelta` deleted
  - `symbolFilters`: item property `maxNotional` deleted
  - `symbolFilters`: item property `maxPosition` deleted
  - `symbolFilters`: item property `applyToMarket` deleted
  - `symbolFilters`: item property `tickSize` deleted
  - `symbolFilters`: item property `bidMultiplierUp` deleted
  - `symbolFilters`: item property `askMultiplierDown` deleted
  - `symbolFilters`: item property `maxPrice` deleted
  - `symbolFilters`: item property `maxTrailingBelowDelta` deleted
  - `symbolFilters`: item property `bidMultiplierDown` deleted
  - `symbolFilters`: item property `multiplierDown` deleted
  - `symbolFilters`: item property `limit` deleted
  - `symbolFilters`: item property `maxNumAlgoOrders` deleted
  - `symbolFilters`: item property `stepSize` deleted
  - `symbolFilters`: item property `maxTrailingAboveDelta` deleted
  - `symbolFilters`: item property `maxNumOrderAmends` deleted
  - `symbolFilters`: item property `maxNumIcebergOrders` deleted
  - `symbolFilters`: item property `askMultiplierUp` deleted
  - `symbolFilters`: item property `maxQty` deleted
  - `symbolFilters`: item property `multiplierUp` deleted
  - `symbolFilters`: item property `filterType` deleted
  - `symbolFilters`: item property `minTrailingBelowDelta` deleted
  - `symbolFilters`: item property `minQty` deleted
  - `symbolFilters`: item property `minPrice` deleted

#### WebSocket API

- Modified response for `exchange_info()` (`exchangeInfo` method):
  - `result`.`exchangeFilters`: item property `maxTrailingBelowDelta` deleted
  - `result`.`exchangeFilters`: item property `askMultiplierUp` deleted
  - `result`.`exchangeFilters`: item property `maxNumOrderAmends` deleted
  - `result`.`exchangeFilters`: item property `maxNumAlgoOrders` deleted
  - `result`.`exchangeFilters`: item property `multiplierDown` deleted
  - `result`.`exchangeFilters`: item property `bidMultiplierDown` deleted
  - `result`.`exchangeFilters`: item property `filterType` deleted
  - `result`.`exchangeFilters`: item property `maxPrice` deleted
  - `result`.`exchangeFilters`: item property `stepSize` deleted
  - `result`.`exchangeFilters`: item property `minTrailingAboveDelta` deleted
  - `result`.`exchangeFilters`: item property `askMultiplierDown` deleted
  - `result`.`exchangeFilters`: item property `applyToMarket` deleted
  - `result`.`exchangeFilters`: item property `maxQty` deleted
  - `result`.`exchangeFilters`: item property `avgPriceMins` deleted
  - `result`.`exchangeFilters`: item property `maxNumOrders` deleted
  - `result`.`exchangeFilters`: item property `maxTrailingAboveDelta` deleted
  - `result`.`exchangeFilters`: item property `maxNotional` deleted
  - `result`.`exchangeFilters`: item property `tickSize` deleted
  - `result`.`exchangeFilters`: item property `maxNumOrderLists` deleted
  - `result`.`exchangeFilters`: item property `asset` deleted
  - `result`.`exchangeFilters`: item property `minPrice` deleted
  - `result`.`exchangeFilters`: item property `minQty` deleted
  - `result`.`exchangeFilters`: item property `maxNumIcebergOrders` deleted
  - `result`.`exchangeFilters`: item property `limit` deleted
  - `result`.`exchangeFilters`: item property `minNotional` deleted
  - `result`.`exchangeFilters`: item property `multiplierUp` deleted
  - `result`.`exchangeFilters`: item property `maxPosition` deleted
  - `result`.`exchangeFilters`: item property `applyMinToMarket` deleted
  - `result`.`exchangeFilters`: item property `applyMaxToMarket` deleted
  - `result`.`exchangeFilters`: item property `minTrailingBelowDelta` deleted
  - `result`.`exchangeFilters`: item property `bidMultiplierUp` deleted
  - `result`.`symbols`.`filters`: item property `filterType` deleted
  - `result`.`symbols`.`filters`: item property `stepSize` deleted
  - `result`.`symbols`.`filters`: item property `minPrice` deleted
  - `result`.`symbols`.`filters`: item property `minQty` deleted
  - `result`.`symbols`.`filters`: item property `asset` deleted
  - `result`.`symbols`.`filters`: item property `maxPrice` deleted
  - `result`.`symbols`.`filters`: item property `applyMaxToMarket` deleted
  - `result`.`symbols`.`filters`: item property `maxNumOrders` deleted
  - `result`.`symbols`.`filters`: item property `maxTrailingBelowDelta` deleted
  - `result`.`symbols`.`filters`: item property `bidMultiplierDown` deleted
  - `result`.`symbols`.`filters`: item property `minTrailingBelowDelta` deleted
  - `result`.`symbols`.`filters`: item property `limit` deleted
  - `result`.`symbols`.`filters`: item property `maxTrailingAboveDelta` deleted
  - `result`.`symbols`.`filters`: item property `tickSize` deleted
  - `result`.`symbols`.`filters`: item property `maxNumOrderLists` deleted
  - `result`.`symbols`.`filters`: item property `minNotional` deleted
  - `result`.`symbols`.`filters`: item property `askMultiplierUp` deleted
  - `result`.`symbols`.`filters`: item property `maxQty` deleted
  - `result`.`symbols`.`filters`: item property `avgPriceMins` deleted
  - `result`.`symbols`.`filters`: item property `minTrailingAboveDelta` deleted
  - `result`.`symbols`.`filters`: item property `maxNumOrderAmends` deleted
  - `result`.`symbols`.`filters`: item property `multiplierUp` deleted
  - `result`.`symbols`.`filters`: item property `applyMinToMarket` deleted
  - `result`.`symbols`.`filters`: item property `maxNumAlgoOrders` deleted
  - `result`.`symbols`.`filters`: item property `applyToMarket` deleted
  - `result`.`symbols`.`filters`: item property `maxNumIcebergOrders` deleted
  - `result`.`symbols`.`filters`: item property `bidMultiplierUp` deleted
  - `result`.`symbols`.`filters`: item property `maxNotional` deleted
  - `result`.`symbols`.`filters`: item property `multiplierDown` deleted
  - `result`.`symbols`.`filters`: item property `askMultiplierDown` deleted
  - `result`.`symbols`.`filters`: item property `maxPosition` deleted

- Modified response for `my_filters()` (`myFilters` method):
  - `result`.`assetFilters`: item property `multiplierDown` deleted
  - `result`.`assetFilters`: item property `minQty` deleted
  - `result`.`assetFilters`: item property `avgPriceMins` deleted
  - `result`.`assetFilters`: item property `maxPosition` deleted
  - `result`.`assetFilters`: item property `stepSize` deleted
  - `result`.`assetFilters`: item property `maxNumIcebergOrders` deleted
  - `result`.`assetFilters`: item property `asset` deleted
  - `result`.`assetFilters`: item property `askMultiplierDown` deleted
  - `result`.`assetFilters`: item property `askMultiplierUp` deleted
  - `result`.`assetFilters`: item property `filterType` deleted
  - `result`.`assetFilters`: item property `maxNumAlgoOrders` deleted
  - `result`.`assetFilters`: item property `tickSize` deleted
  - `result`.`assetFilters`: item property `maxNumOrderLists` deleted
  - `result`.`assetFilters`: item property `maxNumOrders` deleted
  - `result`.`assetFilters`: item property `applyMaxToMarket` deleted
  - `result`.`assetFilters`: item property `bidMultiplierDown` deleted
  - `result`.`assetFilters`: item property `bidMultiplierUp` deleted
  - `result`.`assetFilters`: item property `minNotional` deleted
  - `result`.`assetFilters`: item property `maxTrailingAboveDelta` deleted
  - `result`.`assetFilters`: item property `maxNotional` deleted
  - `result`.`assetFilters`: item property `applyMinToMarket` deleted
  - `result`.`assetFilters`: item property `minPrice` deleted
  - `result`.`assetFilters`: item property `minTrailingBelowDelta` deleted
  - `result`.`assetFilters`: item property `maxNumOrderAmends` deleted
  - `result`.`assetFilters`: item property `applyToMarket` deleted
  - `result`.`assetFilters`: item property `limit` deleted
  - `result`.`assetFilters`: item property `multiplierUp` deleted
  - `result`.`assetFilters`: item property `maxTrailingBelowDelta` deleted
  - `result`.`assetFilters`: item property `maxQty` deleted
  - `result`.`assetFilters`: item property `minTrailingAboveDelta` deleted
  - `result`.`assetFilters`: item property `maxPrice` deleted
  - `result`.`exchangeFilters`: item property `limit` deleted
  - `result`.`exchangeFilters`: item property `minPrice` deleted
  - `result`.`exchangeFilters`: item property `askMultiplierUp` deleted
  - `result`.`exchangeFilters`: item property `filterType` deleted
  - `result`.`exchangeFilters`: item property `maxNumOrders` deleted
  - `result`.`exchangeFilters`: item property `applyMaxToMarket` deleted
  - `result`.`exchangeFilters`: item property `bidMultiplierDown` deleted
  - `result`.`exchangeFilters`: item property `avgPriceMins` deleted
  - `result`.`exchangeFilters`: item property `minTrailingAboveDelta` deleted
  - `result`.`exchangeFilters`: item property `askMultiplierDown` deleted
  - `result`.`exchangeFilters`: item property `minQty` deleted
  - `result`.`exchangeFilters`: item property `asset` deleted
  - `result`.`exchangeFilters`: item property `bidMultiplierUp` deleted
  - `result`.`exchangeFilters`: item property `minNotional` deleted
  - `result`.`exchangeFilters`: item property `applyMinToMarket` deleted
  - `result`.`exchangeFilters`: item property `applyToMarket` deleted
  - `result`.`exchangeFilters`: item property `maxNumOrderLists` deleted
  - `result`.`exchangeFilters`: item property `maxNumAlgoOrders` deleted
  - `result`.`exchangeFilters`: item property `maxNumIcebergOrders` deleted
  - `result`.`exchangeFilters`: item property `maxQty` deleted
  - `result`.`exchangeFilters`: item property `maxTrailingAboveDelta` deleted
  - `result`.`exchangeFilters`: item property `maxNotional` deleted
  - `result`.`exchangeFilters`: item property `multiplierUp` deleted
  - `result`.`exchangeFilters`: item property `minTrailingBelowDelta` deleted
  - `result`.`exchangeFilters`: item property `maxPosition` deleted
  - `result`.`exchangeFilters`: item property `maxNumOrderAmends` deleted
  - `result`.`exchangeFilters`: item property `maxPrice` deleted
  - `result`.`exchangeFilters`: item property `tickSize` deleted
  - `result`.`exchangeFilters`: item property `stepSize` deleted
  - `result`.`exchangeFilters`: item property `maxTrailingBelowDelta` deleted
  - `result`.`exchangeFilters`: item property `multiplierDown` deleted
  - `result`.`symbolFilters`: item property `maxQty` deleted
  - `result`.`symbolFilters`: item property `maxPrice` deleted
  - `result`.`symbolFilters`: item property `maxTrailingBelowDelta` deleted
  - `result`.`symbolFilters`: item property `multiplierDown` deleted
  - `result`.`symbolFilters`: item property `maxTrailingAboveDelta` deleted
  - `result`.`symbolFilters`: item property `multiplierUp` deleted
  - `result`.`symbolFilters`: item property `applyMinToMarket` deleted
  - `result`.`symbolFilters`: item property `maxNumAlgoOrders` deleted
  - `result`.`symbolFilters`: item property `applyMaxToMarket` deleted
  - `result`.`symbolFilters`: item property `minPrice` deleted
  - `result`.`symbolFilters`: item property `maxNumIcebergOrders` deleted
  - `result`.`symbolFilters`: item property `bidMultiplierUp` deleted
  - `result`.`symbolFilters`: item property `filterType` deleted
  - `result`.`symbolFilters`: item property `minTrailingBelowDelta` deleted
  - `result`.`symbolFilters`: item property `asset` deleted
  - `result`.`symbolFilters`: item property `minNotional` deleted
  - `result`.`symbolFilters`: item property `tickSize` deleted
  - `result`.`symbolFilters`: item property `applyToMarket` deleted
  - `result`.`symbolFilters`: item property `maxNumOrderLists` deleted
  - `result`.`symbolFilters`: item property `minQty` deleted
  - `result`.`symbolFilters`: item property `minTrailingAboveDelta` deleted
  - `result`.`symbolFilters`: item property `askMultiplierDown` deleted
  - `result`.`symbolFilters`: item property `askMultiplierUp` deleted
  - `result`.`symbolFilters`: item property `maxNotional` deleted
  - `result`.`symbolFilters`: item property `stepSize` deleted
  - `result`.`symbolFilters`: item property `bidMultiplierDown` deleted
  - `result`.`symbolFilters`: item property `avgPriceMins` deleted
  - `result`.`symbolFilters`: item property `limit` deleted
  - `result`.`symbolFilters`: item property `maxPosition` deleted
  - `result`.`symbolFilters`: item property `maxNumOrders` deleted
  - `result`.`symbolFilters`: item property `maxNumOrderAmends` deleted

## 2.4.0 - 2025-09-24

### Changed (1)

- Modified method for removing slashes (`/`) in endpoints

## 2.3.0 - 2025-09-16

### Changed (1)

- Updated `binance-common` library to version `3.1.1`

## 2.2.0 - 2025-09-12

### Changed (1)

- Updated `binance-common` library to version `3.1.0`

## 2.1.0 - 2025-09-05

### Added (1)

- Added user data stream relogin logic.

### Changed (1)

- Updated `binance-common` library to version `3.0.0`

## 2.0.0 - 2025-08-22

### Added (2)

#### WebSocket API

- `session_subscriptions()` (`session.subscriptions` method)
- `user_data_stream_subscribe_signature()` (`userDataStream.subscribe.signature` method)

### Changed (85)

- Standardized type hints for required parameters by replacing `default = None` annotations with `Union[..., None]`

#### REST API

- Added parameter `abovePegOffsetType`
  - affected methods:
    - `order_list_oco()` (`POST /api/v3/orderList/oco`)
- Added parameter `abovePegOffsetValue`
  - affected methods:
    - `order_list_oco()` (`POST /api/v3/orderList/oco`)
- Added parameter `abovePegPriceType`
  - affected methods:
    - `order_list_oco()` (`POST /api/v3/orderList/oco`)
- Added parameter `belowPegOffsetType`
  - affected methods:
    - `order_list_oco()` (`POST /api/v3/orderList/oco`)
- Added parameter `belowPegOffsetValue`
  - affected methods:
    - `order_list_oco()` (`POST /api/v3/orderList/oco`)
- Added parameter `belowPegPriceType`
  - affected methods:
    - `order_list_oco()` (`POST /api/v3/orderList/oco`)
- Added parameter `icebergQty`
  - affected methods:
    - `sor_order_test()` (`POST /api/v3/sor/order/test`)
- Added parameter `newClientOrderId`
  - affected methods:
    - `sor_order_test()` (`POST /api/v3/sor/order/test`)
- Added parameter `newOrderRespType`
  - affected methods:
    - `sor_order_test()` (`POST /api/v3/sor/order/test`)
- Added parameter `pegOffsetType`
  - affected methods:
    - `new_order()` (`POST /api/v3/order`)
    - `order_cancel_replace()` (`POST /api/v3/order/cancelReplace`)
    - `order_test()` (`POST /api/v3/order/test`)
- Added parameter `pegOffsetValue`
  - affected methods:
    - `new_order()` (`POST /api/v3/order`)
    - `order_cancel_replace()` (`POST /api/v3/order/cancelReplace`)
    - `order_test()` (`POST /api/v3/order/test`)
- Added parameter `pegPriceType`
  - affected methods:
    - `new_order()` (`POST /api/v3/order`)
    - `order_cancel_replace()` (`POST /api/v3/order/cancelReplace`)
    - `order_test()` (`POST /api/v3/order/test`)
- Added parameter `pendingAbovePegOffsetType`
  - affected methods:
    - `order_list_otoco()` (`POST /api/v3/orderList/otoco`)
- Added parameter `pendingAbovePegOffsetValue`
  - affected methods:
    - `order_list_otoco()` (`POST /api/v3/orderList/otoco`)
- Added parameter `pendingAbovePegPriceType`
  - affected methods:
    - `order_list_otoco()` (`POST /api/v3/orderList/otoco`)
- Added parameter `pendingBelowPegOffsetType`
  - affected methods:
    - `order_list_otoco()` (`POST /api/v3/orderList/otoco`)
- Added parameter `pendingBelowPegOffsetValue`
  - affected methods:
    - `order_list_otoco()` (`POST /api/v3/orderList/otoco`)
- Added parameter `pendingBelowPegPriceType`
  - affected methods:
    - `order_list_otoco()` (`POST /api/v3/orderList/otoco`)
- Added parameter `pendingPegOffsetType`
  - affected methods:
    - `order_list_oto()` (`POST /api/v3/orderList/oto`)
- Added parameter `pendingPegOffsetValue`
  - affected methods:
    - `order_list_oto()` (`POST /api/v3/orderList/oto`)
- Added parameter `pendingPegPriceType`
  - affected methods:
    - `order_list_oto()` (`POST /api/v3/orderList/oto`)
- Added parameter `price`
  - affected methods:
    - `sor_order_test()` (`POST /api/v3/sor/order/test`)
- Added parameter `quantity`
  - affected methods:
    - `sor_order_test()` (`POST /api/v3/sor/order/test`)
- Added parameter `recvWindow`
  - affected methods:
    - `sor_order_test()` (`POST /api/v3/sor/order/test`)
- Added parameter `selfTradePreventionMode`
  - affected methods:
    - `sor_order_test()` (`POST /api/v3/sor/order/test`)
- Added parameter `side`
  - affected methods:
    - `sor_order_test()` (`POST /api/v3/sor/order/test`)
- Added parameter `strategyId`
  - affected methods:
    - `sor_order_test()` (`POST /api/v3/sor/order/test`)
- Added parameter `strategyType`
  - affected methods:
    - `sor_order_test()` (`POST /api/v3/sor/order/test`)
- Added parameter `symbol`
  - affected methods:
    - `sor_order_test()` (`POST /api/v3/sor/order/test`)
- Added parameter `timeInForce`
  - affected methods:
    - `sor_order_test()` (`POST /api/v3/sor/order/test`)
- Added parameter `type`
  - affected methods:
    - `sor_order_test()` (`POST /api/v3/sor/order/test`)
- Added parameter `workingPegOffsetType`
  - affected methods:
    - `order_list_oto()` (`POST /api/v3/orderList/oto`)
    - `order_list_otoco()` (`POST /api/v3/orderList/otoco`)
- Added parameter `workingPegOffsetValue`
  - affected methods:
    - `order_list_oto()` (`POST /api/v3/orderList/oto`)
    - `order_list_otoco()` (`POST /api/v3/orderList/otoco`)
- Added parameter `workingPegPriceType`
  - affected methods:
    - `order_list_oto()` (`POST /api/v3/orderList/oto`)
    - `order_list_otoco()` (`POST /api/v3/orderList/otoco`)
- Modified parameter `computeCommissionRates`:
  - affected methods:
    - `order_test()` (`POST /api/v3/order/test`)
    - `sor_order_test()` (`POST /api/v3/sor/order/test`)

- Modified response for `account_commission()` method (`GET /api/v3/account/commission`):
  - property `specialCommission` added

- Modified response for `exchange_info()` method (`GET /api/v3/exchangeInfo`):
  - `exchangeFilters`: item property `maxNumOrderAmends` added
  - `exchangeFilters`: item property `maxNumOrderLists` added
  - `symbols`: item property `pegInstructionsAllowed` added
  - `symbols`.`filters`: item property `maxNumOrderLists` added
  - `symbols`.`filters`: item property `maxNumOrderAmends` added

- Modified response for `order_test()` method (`POST /api/v3/order/test`):
  - property `specialCommissionForOrder` added

#### WebSocket API

- Added parameter `abovePegOffsetType`
  - affected methods:
    - `order_list_place_oco()` (`orderList.place.oco` method)
- Added parameter `abovePegOffsetValue`
  - affected methods:
    - `order_list_place_oco()` (`orderList.place.oco` method)
- Added parameter `abovePegPriceType`
  - affected methods:
    - `order_list_place_oco()` (`orderList.place.oco` method)
- Added parameter `belowPegOffsetType`
  - affected methods:
    - `order_list_place_oco()` (`orderList.place.oco` method)
- Added parameter `belowPegOffsetValue`
  - affected methods:
    - `order_list_place_oco()` (`orderList.place.oco` method)
- Added parameter `belowPegPriceType`
  - affected methods:
    - `order_list_place_oco()` (`orderList.place.oco` method)
- Added parameter `icebergQty`
  - affected methods:
    - `order_test()` (`order.test` method)
    - `sor_order_test()` (`sor.order.test` method)
- Added parameter `newClientOrderId`
  - affected methods:
    - `order_test()` (`order.test` method)
    - `sor_order_test()` (`sor.order.test` method)
- Added parameter `newOrderRespType`
  - affected methods:
    - `order_test()` (`order.test` method)
    - `sor_order_test()` (`sor.order.test` method)
- Added parameter `pegOffsetType`
  - affected methods:
    - `order_cancel_replace()` (`order.cancelReplace` method)
    - `order_place()` (`order.place` method)
    - `order_test()` (`order.test` method)
- Added parameter `pegOffsetValue`
  - affected methods:
    - `order_cancel_replace()` (`order.cancelReplace` method)
    - `order_place()` (`order.place` method)
    - `order_test()` (`order.test` method)
- Added parameter `pegPriceType`
  - affected methods:
    - `order_cancel_replace()` (`order.cancelReplace` method)
    - `order_place()` (`order.place` method)
    - `order_test()` (`order.test` method)
- Added parameter `pendingAbovePegOffsetType`
  - affected methods:
    - `order_list_place_otoco()` (`orderList.place.otoco` method)
- Added parameter `pendingAbovePegOffsetValue`
  - affected methods:
    - `order_list_place_otoco()` (`orderList.place.otoco` method)
- Added parameter `pendingAbovePegPriceType`
  - affected methods:
    - `order_list_place_otoco()` (`orderList.place.otoco` method)
- Added parameter `pendingBelowPegOffsetType`
  - affected methods:
    - `order_list_place_otoco()` (`orderList.place.otoco` method)
- Added parameter `pendingBelowPegOffsetValue`
  - affected methods:
    - `order_list_place_otoco()` (`orderList.place.otoco` method)
- Added parameter `pendingBelowPegPriceType`
  - affected methods:
    - `order_list_place_otoco()` (`orderList.place.otoco` method)
- Added parameter `pendingPegOffsetType`
  - affected methods:
    - `order_list_place_oto()` (`orderList.place.oto` method)
- Added parameter `pendingPegOffsetValue`
  - affected methods:
    - `order_list_place_oto()` (`orderList.place.oto` method)
- Added parameter `pendingPegPriceType`
  - affected methods:
    - `order_list_place_oto()` (`orderList.place.oto` method)
- Added parameter `price`
  - affected methods:
    - `order_test()` (`order.test` method)
    - `sor_order_test()` (`sor.order.test` method)
- Added parameter `quantity`
  - affected methods:
    - `order_test()` (`order.test` method)
    - `sor_order_test()` (`sor.order.test` method)
- Added parameter `quoteOrderQty`
  - affected methods:
    - `order_test()` (`order.test` method)
- Added parameter `recvWindow`
  - affected methods:
    - `order_test()` (`order.test` method)
    - `sor_order_test()` (`sor.order.test` method)
- Added parameter `selfTradePreventionMode`
  - affected methods:
    - `order_test()` (`order.test` method)
    - `sor_order_test()` (`sor.order.test` method)
- Added parameter `side`
  - affected methods:
    - `order_test()` (`order.test` method)
    - `sor_order_test()` (`sor.order.test` method)
- Added parameter `stopPrice`
  - affected methods:
    - `order_test()` (`order.test` method)
- Added parameter `strategyId`
  - affected methods:
    - `order_test()` (`order.test` method)
    - `sor_order_test()` (`sor.order.test` method)
- Added parameter `strategyType`
  - affected methods:
    - `order_test()` (`order.test` method)
    - `sor_order_test()` (`sor.order.test` method)
- Added parameter `subscriptionId`
  - affected methods:
    - `user_data_stream_unsubscribe()` (`userDataStream.unsubscribe` method)
- Added parameter `symbol`
  - affected methods:
    - `order_test()` (`order.test` method)
    - `sor_order_test()` (`sor.order.test` method)
- Added parameter `timeInForce`
  - affected methods:
    - `order_test()` (`order.test` method)
    - `sor_order_test()` (`sor.order.test` method)
- Added parameter `trailingDelta`
  - affected methods:
    - `order_test()` (`order.test` method)
- Added parameter `type`
  - affected methods:
    - `order_test()` (`order.test` method)
    - `sor_order_test()` (`sor.order.test` method)
- Added parameter `workingPegOffsetType`
  - affected methods:
    - `order_list_place_oto()` (`orderList.place.oto` method)
    - `order_list_place_otoco()` (`orderList.place.otoco` method)
- Added parameter `workingPegOffsetValue`
  - affected methods:
    - `order_list_place_oto()` (`orderList.place.oto` method)
    - `order_list_place_otoco()` (`orderList.place.otoco` method)
- Added parameter `workingPegPriceType`
  - affected methods:
    - `order_list_place_oto()` (`orderList.place.oto` method)
    - `order_list_place_otoco()` (`orderList.place.otoco` method)
- Modified parameter `cancelOrderId`:
  - format `int32` → `int64`
  - affected methods:
    - `order_cancel_replace()` (`order.cancelReplace` method)
- Modified parameter `computeCommissionRates`:
  - affected methods:
    - `order_test()` (`order.test` method)
    - `sor_order_test()` (`sor.order.test` method)
- Modified parameter `orderId`:
  - format `int32` → `int64`
  - affected methods:
    - `all_orders()` (`allOrders` method)
    - `my_trades()` (`myTrades` method)
    - `order_cancel()` (`order.cancel` method)
    - `order_status()` (`order.status` method)

- Modified response for `account_commission()` method (`POST /account.commission`):
  - `result`: property `specialCommission` added

- Modified response for `user_data_stream_subscribe()` method (`POST /userDataStream.subscribe`):
  - `result`: property `subscriptionId` added

- Modified response for `user_data_stream_unsubscribe()` method (`POST /userDataStream.unsubscribe`):
  - `result`: property `subscriptionId` deleted

- Modified response for `exchange_info()` method (`POST /exchangeInfo`):
  - `result`.`exchangeFilters`: item property `maxNumOrderLists` added
  - `result`.`exchangeFilters`: item property `maxNumOrderAmends` added
  - `result`.`symbols`: item property `pegInstructionsAllowed` added
  - `result`.`symbols`.`filters`: item property `maxNumOrderLists` added
  - `result`.`symbols`.`filters`: item property `maxNumOrderAmends` added

- Modified response for `order_test()` method (`POST /order.test`):
  - `result`: property `specialCommissionForOrder` added

#### WebSocket Streams

### Changed (1)

- Updated Websocket Streams response type to `RequestStreamHandle`

## 1.2.0 - 2025-08-07

### Changed (1)

- Updated `binance-common` library to version `1.2.0`

## 1.1.0 - 2025-08-06

### Changed (5)

- Updated `binance-common` library to version `1.1.0`
- Changed models responses to handle upper and lower case parameters
- Added python version `3.13`

#### REST API

- Added missing parameters to `order_test()` (`POST /api/v3/order/test`)

#### WebSocket Streams

- Changed `list_subscribe` to return `dict` response

## 1.0.0 - 2025-07-17

- Initial release
