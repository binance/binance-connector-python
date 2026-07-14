# Changelog

## 10.0.0 - 2026-07-14

### Changed (77)

- Updated `binance-common` library to version `4.0.3`

#### REST API

- Modified parameter `cancelRestrictions`:
  - enum removed: `NEW`, `PARTIALLY_FILLED`
  - affected methods:
    - `delete_order()` (`DELETE /api/v3/order`)
    - `order_cancel_replace()` (`POST /api/v3/order/cancelReplace`)
- Modified parameter `newOrderRespType`:
  - enum removed: `MARKET`, `LIMIT`
  - affected methods:
    - `new_order()` (`POST /api/v3/order`)
    - `order_cancel_replace()` (`POST /api/v3/order/cancelReplace`)
    - `order_oco()` (`POST /api/v3/order/oco`)
    - `order_test()` (`POST /api/v3/order/test`)
    - `order_list_oco()` (`POST /api/v3/orderList/oco`)
    - `order_list_opo()` (`POST /api/v3/orderList/opo`)
    - `order_list_opoco()` (`POST /api/v3/orderList/opoco`)
    - `order_list_oto()` (`POST /api/v3/orderList/oto`)
    - `order_list_otoco()` (`POST /api/v3/orderList/otoco`)
    - `sor_order()` (`POST /api/v3/sor/order`)
    - `sor_order_test()` (`POST /api/v3/sor/order/test`)
- Modified parameter `pegOffsetType`:
  - enum removed: `NON_REPRESENTABLE`
  - affected methods:
    - `new_order()` (`POST /api/v3/order`)
    - `order_cancel_replace()` (`POST /api/v3/order/cancelReplace`)
    - `order_test()` (`POST /api/v3/order/test`)
- Modified parameter `pegPriceType`:
  - enum removed: `NON_REPRESENTABLE`
  - affected methods:
    - `new_order()` (`POST /api/v3/order`)
    - `order_cancel_replace()` (`POST /api/v3/order/cancelReplace`)
    - `order_test()` (`POST /api/v3/order/test`)
- Modified parameter `permissions`:
  - items: enum added: `SPOT`, `MARGIN`, `LEVERAGED`, `TRD_GRP_002`, `TRD_GRP_003`, `TRD_GRP_004`, `TRD_GRP_005`, `TRD_GRP_006`, `TRD_GRP_007`, `TRD_GRP_008`, `TRD_GRP_009`, `TRD_GRP_010`, `TRD_GRP_011`, `TRD_GRP_012`, `TRD_GRP_013`, `TRD_GRP_014`, `TRD_GRP_015`, `TRD_GRP_016`, `TRD_GRP_017`, `TRD_GRP_018`, `TRD_GRP_019`, `TRD_GRP_020`, `TRD_GRP_021`, `TRD_GRP_022`, `TRD_GRP_023`, `TRD_GRP_024`, `TRD_GRP_025`
  - affected methods:
    - `exchange_info()` (`GET /api/v3/exchangeInfo`)
- Modified parameter `selfTradePreventionMode`:
  - enum removed: `NON_REPRESENTABLE`
  - affected methods:
    - `new_order()` (`POST /api/v3/order`)
    - `order_cancel_replace()` (`POST /api/v3/order/cancelReplace`)
    - `order_oco()` (`POST /api/v3/order/oco`)
    - `order_test()` (`POST /api/v3/order/test`)
    - `order_list_oco()` (`POST /api/v3/orderList/oco`)
    - `order_list_opo()` (`POST /api/v3/orderList/opo`)
    - `order_list_opoco()` (`POST /api/v3/orderList/opoco`)
    - `order_list_oto()` (`POST /api/v3/orderList/oto`)
    - `order_list_otoco()` (`POST /api/v3/orderList/otoco`)
    - `sor_order()` (`POST /api/v3/sor/order`)
    - `sor_order_test()` (`POST /api/v3/sor/order/test`)
- Modified parameter `symbolStatus`:
  - enum removed: `END_OF_DAY`, `NON_REPRESENTABLE`
  - affected methods:
    - `depth()` (`GET /api/v3/depth`)
    - `exchange_info()` (`GET /api/v3/exchangeInfo`)
    - `execution_rules()` (`GET /api/v3/executionRules`)
    - `reference_price_calculation()` (`GET /api/v3/referencePrice/calculation`)
    - `ticker_book_ticker()` (`GET /api/v3/ticker/bookTicker`)
    - `ticker_price()` (`GET /api/v3/ticker/price`)
    - `ticker_trading_day()` (`GET /api/v3/ticker/tradingDay`)
- Modified parameter `symbolStatus`:
  - enum removed: `END_OF_DAY`, `NON_REPRESENTABLE`
  - affected methods:
    - `ticker()` (`GET /api/v3/ticker`)
    - `ticker24hr()` (`GET /api/v3/ticker/24hr`)
- Modified parameter `timeInForce`:
  - enum removed: `NON_REPRESENTABLE`
  - affected methods:
    - `new_order()` (`POST /api/v3/order`)
    - `order_cancel_replace()` (`POST /api/v3/order/cancelReplace`)
    - `order_test()` (`POST /api/v3/order/test`)
    - `sor_order()` (`POST /api/v3/sor/order`)
    - `sor_order_test()` (`POST /api/v3/sor/order/test`)
- Modified parameter `type`:
  - enum removed: `NON_REPRESENTABLE`
  - affected methods:
    - `new_order()` (`POST /api/v3/order`)
    - `order_cancel_replace()` (`POST /api/v3/order/cancelReplace`)
    - `order_test()` (`POST /api/v3/order/test`)
- Modified parameter `type`:
  - enum removed: `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`, `LIMIT_MAKER`, `NON_REPRESENTABLE`
  - affected methods:
    - `sor_order()` (`POST /api/v3/sor/order`)
    - `sor_order_test()` (`POST /api/v3/sor/order/test`)
- Modified parameter `windowSize`:
  - enum added: `7d`
  - affected methods:
    - `ticker()` (`GET /api/v3/ticker`)
- Modified response for `all_orders()` (`GET /api/v3/allOrders`):
  - items: property `usedSor` added
  - items: property `workingFloor` added
  - items: property `pegOffsetValue` added
  - items: property `pegOffsetType` added
  - items: property `preventedQuantity` added
  - items: property `strategyType` added
  - items: property `pegPriceType` added
  - items: property `peggedPrice` added
  - items: property `trailingTime` added
  - items: property `trailingDelta` added
  - items: property `strategyId` added
  - items: property `preventedMatchId` added
  - items: property `expiryReason` added
  - items: item property `usedSor` added
  - items: item property `workingFloor` added
  - items: item property `pegOffsetValue` added
  - items: item property `pegOffsetType` added
  - items: item property `preventedQuantity` added
  - items: item property `strategyType` added
  - items: item property `pegPriceType` added
  - items: item property `peggedPrice` added
  - items: item property `trailingTime` added
  - items: item property `trailingDelta` added
  - items: item property `strategyId` added
  - items: item property `preventedMatchId` added
  - items: item property `expiryReason` added

- Modified response for `depth()` (`GET /api/v3/depth`):
  - `asks`.items: minItems `0` → `2`
  - `asks`.items: maxItems `null` → `2`
  - `bids`.items: minItems `0` → `2`
  - `bids`.items: maxItems `null` → `2`

- Modified response for `exchange_info()` (`GET /api/v3/exchangeInfo`):
  - property `sors` added
  - `exchangeFilters`.items: oneOf modified
  - `symbols`.items.`filters`.items: oneOf modified
  - `symbols`.items.`filters`.items: oneOf modified

- Modified response for `klines()` (`GET /api/v3/klines`):
  - items.items: oneOf added 2 schema(s)
  - items.items: oneOf removed 2 schema(s)

- Modified response for `my_filters()` (`GET /api/v3/myFilters`):
  - `assetFilters`.items: oneOf modified
  - `exchangeFilters`.items: oneOf modified
  - `symbolFilters`.items: oneOf modified

- Modified response for `get_open_orders()` (`GET /api/v3/openOrders`):
  - items: property `strategyId` added
  - items: property `peggedPrice` added
  - items: property `pegOffsetType` added
  - items: property `preventedMatchId` added
  - items: property `expiryReason` added
  - items: property `trailingTime` added
  - items: property `pegOffsetValue` added
  - items: property `preventedQuantity` added
  - items: property `trailingDelta` added
  - items: property `strategyType` added
  - items: property `usedSor` added
  - items: property `workingFloor` added
  - items: property `pegPriceType` added
  - items: item property `strategyId` added
  - items: item property `peggedPrice` added
  - items: item property `pegOffsetType` added
  - items: item property `preventedMatchId` added
  - items: item property `expiryReason` added
  - items: item property `trailingTime` added
  - items: item property `pegOffsetValue` added
  - items: item property `preventedQuantity` added
  - items: item property `trailingDelta` added
  - items: item property `strategyType` added
  - items: item property `usedSor` added
  - items: item property `workingFloor` added
  - items: item property `pegPriceType` added

- Modified response for `delete_order()` (`DELETE /api/v3/order`):
  - property `pegOffsetValue` added
  - property `icebergQty` added
  - property `pegOffsetType` added
  - property `expiryReason` added
  - property `trailingDelta` added
  - property `peggedPrice` added
  - property `trailingTime` added
  - property `strategyId` added
  - property `usedSor` added
  - property `strategyType` added
  - property `preventedMatchId` added
  - property `workingFloor` added
  - property `stopPrice` added
  - property `pegPriceType` added
  - property `preventedQuantity` added

- Modified response for `get_order()` (`GET /api/v3/order`):
  - property `pegOffsetType` added
  - property `peggedPrice` added
  - property `pegPriceType` added
  - property `trailingTime` added
  - property `pegOffsetValue` added
  - property `preventedMatchId` added
  - property `strategyId` added
  - property `strategyType` added
  - property `usedSor` added
  - property `expiryReason` added
  - property `trailingDelta` added
  - property `workingFloor` added
  - property `preventedQuantity` added

- Modified response for `order_amend_keep_priority()` (`PUT /api/v3/order/amend/keepPriority`):
  - `amendedOrder`: property `usedSor` added
  - `amendedOrder`: property `strategyType` added
  - `amendedOrder`: property `pegOffsetValue` added
  - `amendedOrder`: property `expiryReason` added
  - `amendedOrder`: property `pegPriceType` added
  - `amendedOrder`: property `workingFloor` added
  - `amendedOrder`: property `stopPrice` added
  - `amendedOrder`: property `pegOffsetType` added
  - `amendedOrder`: property `peggedPrice` added
  - `amendedOrder`: property `preventedQuantity` added
  - `amendedOrder`: property `strategyId` added
  - `amendedOrder`: property `icebergQty` added
  - `amendedOrder`: property `preventedMatchId` added
  - `amendedOrder`: property `trailingDelta` added
  - `amendedOrder`: property `trailingTime` added

- Modified response for `order_cancel_replace()` (`POST /api/v3/order/cancelReplace`):
  - property `msg` deleted
  - property `code` deleted
  - property `data` deleted
  - `cancelResponse`: property `preventedMatchId` added
  - `cancelResponse`: property `strategyType` added
  - `cancelResponse`: property `preventedQuantity` added
  - `cancelResponse`: property `pegOffsetType` added
  - `cancelResponse`: property `trailingDelta` added
  - `cancelResponse`: property `strategyId` added
  - `cancelResponse`: property `icebergQty` added
  - `cancelResponse`: property `pegOffsetValue` added
  - `cancelResponse`: property `pegPriceType` added
  - `cancelResponse`: property `workingFloor` added
  - `cancelResponse`: property `expiryReason` added
  - `cancelResponse`: property `peggedPrice` added
  - `cancelResponse`: property `stopPrice` added
  - `cancelResponse`: property `trailingTime` added
  - `cancelResponse`: property `usedSor` added
  - `newOrderResponse`: property `icebergQty` added
  - `newOrderResponse`: property `strategyType` added
  - `newOrderResponse`: property `preventedMatchId` added
  - `newOrderResponse`: property `pegOffsetType` added
  - `newOrderResponse`: property `trailingDelta` added
  - `newOrderResponse`: property `stopPrice` added
  - `newOrderResponse`: property `preventedQuantity` added
  - `newOrderResponse`: property `pegOffsetValue` added
  - `newOrderResponse`: property `pegPriceType` added
  - `newOrderResponse`: property `peggedPrice` added
  - `newOrderResponse`: property `workingFloor` added
  - `newOrderResponse`: property `strategyId` added
  - `newOrderResponse`: property `trailingTime` added
  - `newOrderResponse`: property `expiryReason` added
  - `newOrderResponse`: property `usedSor` added
  - `newOrderResponse`.`fills`.items: type `string` → `object`
  - `newOrderResponse`.`fills`.items: property `qty` added
  - `newOrderResponse`.`fills`.items: property `tradeId` added
  - `newOrderResponse`.`fills`.items: property `commission` added
  - `newOrderResponse`.`fills`.items: property `commissionAsset` added
  - `newOrderResponse`.`fills`.items: property `price` added
  - `newOrderResponse`.`fills`.items: item property `qty` added
  - `newOrderResponse`.`fills`.items: item property `tradeId` added
  - `newOrderResponse`.`fills`.items: item property `commission` added
  - `newOrderResponse`.`fills`.items: item property `commissionAsset` added
  - `newOrderResponse`.`fills`.items: item property `price` added

- Modified response for `delete_order_list()` (`DELETE /api/v3/orderList`):
  - `orderReports`.items: property `pegOffsetValue` added
  - `orderReports`.items: property `peggedPrice` added
  - `orderReports`.items: property `pegPriceType` added
  - `orderReports`.items: property `strategyId` added
  - `orderReports`.items: property `strategyType` added
  - `orderReports`.items: property `workingFloor` added
  - `orderReports`.items: property `trailingDelta` added
  - `orderReports`.items: property `preventedQuantity` added
  - `orderReports`.items: property `preventedMatchId` added
  - `orderReports`.items: property `pegOffsetType` added
  - `orderReports`.items: property `usedSor` added
  - `orderReports`.items: property `trailingTime` added
  - `orderReports`.items: property `expiryReason` added
  - `orderReports`.items: property `icebergQty` added
  - `orderReports`.items: property `selfTradePreventionMode` deleted
  - `orderReports`.items: item property `pegOffsetValue` added
  - `orderReports`.items: item property `peggedPrice` added
  - `orderReports`.items: item property `pegPriceType` added
  - `orderReports`.items: item property `strategyId` added
  - `orderReports`.items: item property `strategyType` added
  - `orderReports`.items: item property `workingFloor` added
  - `orderReports`.items: item property `trailingDelta` added
  - `orderReports`.items: item property `preventedQuantity` added
  - `orderReports`.items: item property `preventedMatchId` added
  - `orderReports`.items: item property `pegOffsetType` added
  - `orderReports`.items: item property `usedSor` added
  - `orderReports`.items: item property `trailingTime` added
  - `orderReports`.items: item property `expiryReason` added
  - `orderReports`.items: item property `icebergQty` added
  - `orderReports`.items: item property `selfTradePreventionMode` deleted

- Modified response for `order_list_opo()` (`POST /api/v3/orderList/opo`):
  - `orderReports`.items: property `strategyId` added
  - `orderReports`.items: property `workingFloor` added
  - `orderReports`.items: property `strategyType` added
  - `orderReports`.items: property `pegPriceType` added
  - `orderReports`.items: property `pegOffsetType` added
  - `orderReports`.items: property `icebergQty` added
  - `orderReports`.items: property `stopPrice` added
  - `orderReports`.items: property `usedSor` added
  - `orderReports`.items: property `preventedQuantity` added
  - `orderReports`.items: property `preventedMatchId` added
  - `orderReports`.items: property `trailingTime` added
  - `orderReports`.items: property `expiryReason` added
  - `orderReports`.items: property `pegOffsetValue` added
  - `orderReports`.items: property `peggedPrice` added
  - `orderReports`.items: property `trailingDelta` added
  - `orderReports`.items: item property `strategyId` added
  - `orderReports`.items: item property `workingFloor` added
  - `orderReports`.items: item property `strategyType` added
  - `orderReports`.items: item property `pegPriceType` added
  - `orderReports`.items: item property `pegOffsetType` added
  - `orderReports`.items: item property `icebergQty` added
  - `orderReports`.items: item property `stopPrice` added
  - `orderReports`.items: item property `usedSor` added
  - `orderReports`.items: item property `preventedQuantity` added
  - `orderReports`.items: item property `preventedMatchId` added
  - `orderReports`.items: item property `trailingTime` added
  - `orderReports`.items: item property `expiryReason` added
  - `orderReports`.items: item property `pegOffsetValue` added
  - `orderReports`.items: item property `peggedPrice` added
  - `orderReports`.items: item property `trailingDelta` added

- Modified response for `order_list_opoco()` (`POST /api/v3/orderList/opoco`):
  - `orderReports`.items: property `usedSor` added
  - `orderReports`.items: property `pegPriceType` added
  - `orderReports`.items: property `peggedPrice` added
  - `orderReports`.items: property `trailingTime` added
  - `orderReports`.items: property `strategyId` added
  - `orderReports`.items: property `trailingDelta` added
  - `orderReports`.items: property `workingFloor` added
  - `orderReports`.items: property `pegOffsetValue` added
  - `orderReports`.items: property `preventedQuantity` added
  - `orderReports`.items: property `strategyType` added
  - `orderReports`.items: property `pegOffsetType` added
  - `orderReports`.items: property `expiryReason` added
  - `orderReports`.items: property `icebergQty` added
  - `orderReports`.items: property `preventedMatchId` added
  - `orderReports`.items: item property `usedSor` added
  - `orderReports`.items: item property `pegPriceType` added
  - `orderReports`.items: item property `peggedPrice` added
  - `orderReports`.items: item property `trailingTime` added
  - `orderReports`.items: item property `strategyId` added
  - `orderReports`.items: item property `trailingDelta` added
  - `orderReports`.items: item property `workingFloor` added
  - `orderReports`.items: item property `pegOffsetValue` added
  - `orderReports`.items: item property `preventedQuantity` added
  - `orderReports`.items: item property `strategyType` added
  - `orderReports`.items: item property `pegOffsetType` added
  - `orderReports`.items: item property `expiryReason` added
  - `orderReports`.items: item property `icebergQty` added
  - `orderReports`.items: item property `preventedMatchId` added

- Modified response for `order_list_oto()` (`POST /api/v3/orderList/oto`):
  - `orderReports`.items: property `pegOffsetValue` added
  - `orderReports`.items: property `peggedPrice` added
  - `orderReports`.items: property `expiryReason` added
  - `orderReports`.items: property `usedSor` added
  - `orderReports`.items: property `preventedQuantity` added
  - `orderReports`.items: property `icebergQty` added
  - `orderReports`.items: property `pegPriceType` added
  - `orderReports`.items: property `pegOffsetType` added
  - `orderReports`.items: property `workingFloor` added
  - `orderReports`.items: property `strategyId` added
  - `orderReports`.items: property `trailingTime` added
  - `orderReports`.items: property `strategyType` added
  - `orderReports`.items: property `trailingDelta` added
  - `orderReports`.items: property `preventedMatchId` added
  - `orderReports`.items: property `stopPrice` added
  - `orderReports`.items: item property `pegOffsetValue` added
  - `orderReports`.items: item property `peggedPrice` added
  - `orderReports`.items: item property `expiryReason` added
  - `orderReports`.items: item property `usedSor` added
  - `orderReports`.items: item property `preventedQuantity` added
  - `orderReports`.items: item property `icebergQty` added
  - `orderReports`.items: item property `pegPriceType` added
  - `orderReports`.items: item property `pegOffsetType` added
  - `orderReports`.items: item property `workingFloor` added
  - `orderReports`.items: item property `strategyId` added
  - `orderReports`.items: item property `trailingTime` added
  - `orderReports`.items: item property `strategyType` added
  - `orderReports`.items: item property `trailingDelta` added
  - `orderReports`.items: item property `preventedMatchId` added
  - `orderReports`.items: item property `stopPrice` added

- Modified response for `order_list_otoco()` (`POST /api/v3/orderList/otoco`):
  - `orderReports`.items: property `trailingTime` added
  - `orderReports`.items: property `expiryReason` added
  - `orderReports`.items: property `pegOffsetValue` added
  - `orderReports`.items: property `pegOffsetType` added
  - `orderReports`.items: property `trailingDelta` added
  - `orderReports`.items: property `usedSor` added
  - `orderReports`.items: property `workingFloor` added
  - `orderReports`.items: property `strategyType` added
  - `orderReports`.items: property `peggedPrice` added
  - `orderReports`.items: property `icebergQty` added
  - `orderReports`.items: property `preventedMatchId` added
  - `orderReports`.items: property `preventedQuantity` added
  - `orderReports`.items: property `strategyId` added
  - `orderReports`.items: property `pegPriceType` added
  - `orderReports`.items: item property `trailingTime` added
  - `orderReports`.items: item property `expiryReason` added
  - `orderReports`.items: item property `pegOffsetValue` added
  - `orderReports`.items: item property `pegOffsetType` added
  - `orderReports`.items: item property `trailingDelta` added
  - `orderReports`.items: item property `usedSor` added
  - `orderReports`.items: item property `workingFloor` added
  - `orderReports`.items: item property `strategyType` added
  - `orderReports`.items: item property `peggedPrice` added
  - `orderReports`.items: item property `icebergQty` added
  - `orderReports`.items: item property `preventedMatchId` added
  - `orderReports`.items: item property `preventedQuantity` added
  - `orderReports`.items: item property `strategyId` added
  - `orderReports`.items: item property `pegPriceType` added

- Modified response for `ticker()` (`GET /api/v3/ticker`):
  - oneOf modified

- Modified response for `ticker24hr()` (`GET /api/v3/ticker/24hr`):
  - oneOf modified

- Modified response for `ticker_book_ticker()` (`GET /api/v3/ticker/bookTicker`):
  - oneOf modified

- Modified response for `ticker_price()` (`GET /api/v3/ticker/price`):
  - oneOf modified

- Modified response for `ticker_trading_day()` (`GET /api/v3/ticker/tradingDay`):
  - oneOf modified

- Modified response for `ui_klines()` (`GET /api/v3/uiKlines`):
  - items.items: oneOf added 2 schema(s)
  - items.items: oneOf removed 2 schema(s)

- Marked `order_oco()` (`POST /api/v3/order/oco`) as deprecated.

#### WebSocket API

- Modified parameter `cancelRestrictions`:
  - enum removed: `NEW`, `PARTIALLY_FILLED`
  - affected methods:
    - `order_cancel()` (`order.cancel` method)
    - `order_cancel_replace()` (`order.cancelReplace` method)
- Modified parameter `newOrderRespType`:
  - enum removed: `MARKET`, `LIMIT`
  - affected methods:
    - `order_cancel_replace()` (`order.cancelReplace` method)
    - `order_place()` (`order.place` method)
    - `order_test()` (`order.test` method)
    - `order_list_place()` (`orderList.place` method)
    - `order_list_place_oco()` (`orderList.place.oco` method)
    - `order_list_place_opo()` (`orderList.place.opo` method)
    - `order_list_place_opoco()` (`orderList.place.opoco` method)
    - `order_list_place_oto()` (`orderList.place.oto` method)
    - `order_list_place_otoco()` (`orderList.place.otoco` method)
    - `sor_order_place()` (`sor.order.place` method)
    - `sor_order_test()` (`sor.order.test` method)
- Modified parameter `pegOffsetType`:
  - enum removed: `NON_REPRESENTABLE`
  - affected methods:
    - `order_cancel_replace()` (`order.cancelReplace` method)
    - `order_place()` (`order.place` method)
    - `order_test()` (`order.test` method)
- Modified parameter `pegPriceType`:
  - enum removed: `NON_REPRESENTABLE`
  - affected methods:
    - `order_cancel_replace()` (`order.cancelReplace` method)
    - `order_place()` (`order.place` method)
    - `order_test()` (`order.test` method)
- Modified parameter `selfTradePreventionMode`:
  - enum removed: `NON_REPRESENTABLE`
  - affected methods:
    - `order_cancel_replace()` (`order.cancelReplace` method)
    - `order_place()` (`order.place` method)
    - `order_test()` (`order.test` method)
    - `order_list_place()` (`orderList.place` method)
    - `order_list_place_oco()` (`orderList.place.oco` method)
    - `order_list_place_opo()` (`orderList.place.opo` method)
    - `order_list_place_opoco()` (`orderList.place.opoco` method)
    - `order_list_place_oto()` (`orderList.place.oto` method)
    - `order_list_place_otoco()` (`orderList.place.otoco` method)
    - `sor_order_place()` (`sor.order.place` method)
    - `sor_order_test()` (`sor.order.test` method)
- Modified parameter `symbolStatus`:
  - enum removed: `END_OF_DAY`, `NON_REPRESENTABLE`
  - affected methods:
    - `depth()` (`depth` method)
    - `exchange_info()` (`exchangeInfo` method)
    - `execution_rules()` (`executionRules` method)
    - `ticker()` (`ticker` method)
    - `ticker24hr()` (`ticker.24hr` method)
    - `ticker_book()` (`ticker.book` method)
    - `ticker_price()` (`ticker.price` method)
    - `ticker_trading_day()` (`ticker.tradingDay` method)
- Modified parameter `symbolStatus`:
  - enum removed: `END_OF_DAY`, `NON_REPRESENTABLE`
  - affected methods:
    - `reference_price_calculation()` (`referencePrice.calculation` method)
- Modified parameter `timeInForce`:
  - enum removed: `NON_REPRESENTABLE`
  - affected methods:
    - `order_cancel_replace()` (`order.cancelReplace` method)
    - `order_place()` (`order.place` method)
    - `order_test()` (`order.test` method)
    - `sor_order_place()` (`sor.order.place` method)
    - `sor_order_test()` (`sor.order.test` method)
- Modified parameter `type`:
  - enum removed: `NON_REPRESENTABLE`
  - affected methods:
    - `order_cancel_replace()` (`order.cancelReplace` method)
    - `order_place()` (`order.place` method)
    - `order_test()` (`order.test` method)
- Modified parameter `type`:
  - enum removed: `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`, `LIMIT_MAKER`, `NON_REPRESENTABLE`
  - affected methods:
    - `sor_order_place()` (`sor.order.place` method)
    - `sor_order_test()` (`sor.order.test` method)
- Modified parameter `windowSize`:
  - enum added: `7d`
  - affected methods:
    - `ticker()` (`ticker` method)
- Modified response for `all_orders()` (`allOrders` method):
  - `result`.items: property `pegOffsetValue` added
  - `result`.items: property `trailingDelta` added
  - `result`.items: property `strategyId` added
  - `result`.items: property `expiryReason` added
  - `result`.items: property `trailingTime` added
  - `result`.items: property `peggedPrice` added
  - `result`.items: property `strategyType` added
  - `result`.items: property `pegOffsetType` added
  - `result`.items: property `pegPriceType` added
  - `result`.items: property `usedSor` added
  - `result`.items: property `workingFloor` added
  - `result`.items: item property `pegOffsetValue` added
  - `result`.items: item property `trailingDelta` added
  - `result`.items: item property `strategyId` added
  - `result`.items: item property `expiryReason` added
  - `result`.items: item property `trailingTime` added
  - `result`.items: item property `peggedPrice` added
  - `result`.items: item property `strategyType` added
  - `result`.items: item property `pegOffsetType` added
  - `result`.items: item property `pegPriceType` added
  - `result`.items: item property `usedSor` added
  - `result`.items: item property `workingFloor` added

- Modified response for `depth()` (`depth` method):
  - `result`.`asks`.items: minItems `0` → `2`
  - `result`.`asks`.items: maxItems `null` → `2`
  - `result`.`bids`.items: minItems `0` → `2`
  - `result`.`bids`.items: maxItems `null` → `2`

- Modified response for `exchange_info()` (`exchangeInfo` method):
  - property `exchangeFilters` added
  - property `serverTime` added
  - property `sors` added
  - property `symbols` added
  - property `timezone` added
  - property `result` deleted
  - property `status` deleted
  - property `id` deleted

- Modified response for `klines()` (`klines` method):
  - `result`.items: minItems `0` → `12`
  - `result`.items: maxItems `null` → `12`
  - `result`.items.items: oneOf added 2 schema(s)
  - `result`.items.items: oneOf removed 2 schema(s)

- Modified response for `my_filters()` (`myFilters` method):
  - property `symbolFilters` added
  - property `assetFilters` added
  - property `exchangeFilters` added
  - property `id` deleted
  - property `result` deleted
  - property `status` deleted

- Modified response for `open_orders_cancel_all()` (`openOrders.cancelAll` method):
  - `result`.items: property `pegPriceType` added
  - `result`.items: property `preventedQuantity` added
  - `result`.items: property `peggedPrice` added
  - `result`.items: property `preventedMatchId` added
  - `result`.items: property `usedSor` added
  - `result`.items: property `pegOffsetType` added
  - `result`.items: property `pegOffsetValue` added
  - `result`.items: property `expiryReason` added
  - `result`.items: property `workingFloor` added
  - `result`.items.`orderReports`.items: property `trailingDelta` added
  - `result`.items.`orderReports`.items: property `icebergQty` added
  - `result`.items.`orderReports`.items: property `peggedPrice` added
  - `result`.items.`orderReports`.items: property `pegOffsetType` added
  - `result`.items.`orderReports`.items: property `strategyId` added
  - `result`.items.`orderReports`.items: property `pegOffsetValue` added
  - `result`.items.`orderReports`.items: property `usedSor` added
  - `result`.items.`orderReports`.items: property `trailingTime` added
  - `result`.items.`orderReports`.items: property `preventedQuantity` added
  - `result`.items.`orderReports`.items: property `workingFloor` added
  - `result`.items.`orderReports`.items: property `pegPriceType` added
  - `result`.items.`orderReports`.items: property `expiryReason` added
  - `result`.items.`orderReports`.items: property `strategyType` added
  - `result`.items.`orderReports`.items: property `preventedMatchId` added
  - `result`.items.`orderReports`.items: item property `trailingDelta` added
  - `result`.items.`orderReports`.items: item property `icebergQty` added
  - `result`.items.`orderReports`.items: item property `peggedPrice` added
  - `result`.items.`orderReports`.items: item property `pegOffsetType` added
  - `result`.items.`orderReports`.items: item property `strategyId` added
  - `result`.items.`orderReports`.items: item property `pegOffsetValue` added
  - `result`.items.`orderReports`.items: item property `usedSor` added
  - `result`.items.`orderReports`.items: item property `trailingTime` added
  - `result`.items.`orderReports`.items: item property `preventedQuantity` added
  - `result`.items.`orderReports`.items: item property `workingFloor` added
  - `result`.items.`orderReports`.items: item property `pegPriceType` added
  - `result`.items.`orderReports`.items: item property `expiryReason` added
  - `result`.items.`orderReports`.items: item property `strategyType` added
  - `result`.items.`orderReports`.items: item property `preventedMatchId` added
  - `result`.items: item property `pegPriceType` added
  - `result`.items: item property `preventedQuantity` added
  - `result`.items: item property `peggedPrice` added
  - `result`.items: item property `preventedMatchId` added
  - `result`.items: item property `usedSor` added
  - `result`.items: item property `pegOffsetType` added
  - `result`.items: item property `pegOffsetValue` added
  - `result`.items: item property `expiryReason` added
  - `result`.items: item property `workingFloor` added
  - `result`.items.`orderReports`.items: property `trailingDelta` added
  - `result`.items.`orderReports`.items: property `icebergQty` added
  - `result`.items.`orderReports`.items: property `peggedPrice` added
  - `result`.items.`orderReports`.items: property `pegOffsetType` added
  - `result`.items.`orderReports`.items: property `strategyId` added
  - `result`.items.`orderReports`.items: property `pegOffsetValue` added
  - `result`.items.`orderReports`.items: property `usedSor` added
  - `result`.items.`orderReports`.items: property `trailingTime` added
  - `result`.items.`orderReports`.items: property `preventedQuantity` added
  - `result`.items.`orderReports`.items: property `workingFloor` added
  - `result`.items.`orderReports`.items: property `pegPriceType` added
  - `result`.items.`orderReports`.items: property `expiryReason` added
  - `result`.items.`orderReports`.items: property `strategyType` added
  - `result`.items.`orderReports`.items: property `preventedMatchId` added
  - `result`.items.`orderReports`.items: item property `trailingDelta` added
  - `result`.items.`orderReports`.items: item property `icebergQty` added
  - `result`.items.`orderReports`.items: item property `peggedPrice` added
  - `result`.items.`orderReports`.items: item property `pegOffsetType` added
  - `result`.items.`orderReports`.items: item property `strategyId` added
  - `result`.items.`orderReports`.items: item property `pegOffsetValue` added
  - `result`.items.`orderReports`.items: item property `usedSor` added
  - `result`.items.`orderReports`.items: item property `trailingTime` added
  - `result`.items.`orderReports`.items: item property `preventedQuantity` added
  - `result`.items.`orderReports`.items: item property `workingFloor` added
  - `result`.items.`orderReports`.items: item property `pegPriceType` added
  - `result`.items.`orderReports`.items: item property `expiryReason` added
  - `result`.items.`orderReports`.items: item property `strategyType` added
  - `result`.items.`orderReports`.items: item property `preventedMatchId` added

- Modified response for `open_orders_status()` (`openOrders.status` method):
  - `result`.items: property `expiryReason` added
  - `result`.items: property `workingFloor` added
  - `result`.items: property `pegOffsetType` added
  - `result`.items: property `usedSor` added
  - `result`.items: property `strategyId` added
  - `result`.items: property `peggedPrice` added
  - `result`.items: property `strategyType` added
  - `result`.items: property `pegOffsetValue` added
  - `result`.items: property `trailingTime` added
  - `result`.items: property `trailingDelta` added
  - `result`.items: property `preventedMatchId` added
  - `result`.items: property `preventedQuantity` added
  - `result`.items: property `pegPriceType` added
  - `result`.items: item property `expiryReason` added
  - `result`.items: item property `workingFloor` added
  - `result`.items: item property `pegOffsetType` added
  - `result`.items: item property `usedSor` added
  - `result`.items: item property `strategyId` added
  - `result`.items: item property `peggedPrice` added
  - `result`.items: item property `strategyType` added
  - `result`.items: item property `pegOffsetValue` added
  - `result`.items: item property `trailingTime` added
  - `result`.items: item property `trailingDelta` added
  - `result`.items: item property `preventedMatchId` added
  - `result`.items: item property `preventedQuantity` added
  - `result`.items: item property `pegPriceType` added

- Modified response for `order_amend_keep_priority()` (`order.amend.keepPriority` method):
  - `result`.`amendedOrder`: property `icebergQty` added
  - `result`.`amendedOrder`: property `strategyType` added
  - `result`.`amendedOrder`: property `pegOffsetType` added
  - `result`.`amendedOrder`: property `workingFloor` added
  - `result`.`amendedOrder`: property `stopPrice` added
  - `result`.`amendedOrder`: property `expiryReason` added
  - `result`.`amendedOrder`: property `pegPriceType` added
  - `result`.`amendedOrder`: property `pegOffsetValue` added
  - `result`.`amendedOrder`: property `trailingDelta` added
  - `result`.`amendedOrder`: property `strategyId` added
  - `result`.`amendedOrder`: property `usedSor` added
  - `result`.`amendedOrder`: property `preventedQuantity` added
  - `result`.`amendedOrder`: property `trailingTime` added
  - `result`.`amendedOrder`: property `preventedMatchId` added
  - `result`.`amendedOrder`: property `peggedPrice` added

- Modified response for `order_cancel()` (`order.cancel` method):
  - `result`: property `peggedPrice` added
  - `result`: property `pegOffsetType` added
  - `result`: property `pegOffsetValue` added
  - `result`: property `preventedMatchId` added
  - `result`: property `expiryReason` added
  - `result`: property `pegPriceType` added
  - `result`: property `trailingTime` added
  - `result`: property `preventedQuantity` added
  - `result`: property `workingFloor` added
  - `result`: property `usedSor` added
  - `result`.`orderReports`.items: property `preventedQuantity` added
  - `result`.`orderReports`.items: property `usedSor` added
  - `result`.`orderReports`.items: property `pegOffsetType` added
  - `result`.`orderReports`.items: property `strategyType` added
  - `result`.`orderReports`.items: property `trailingDelta` added
  - `result`.`orderReports`.items: property `trailingTime` added
  - `result`.`orderReports`.items: property `preventedMatchId` added
  - `result`.`orderReports`.items: property `peggedPrice` added
  - `result`.`orderReports`.items: property `icebergQty` added
  - `result`.`orderReports`.items: property `pegOffsetValue` added
  - `result`.`orderReports`.items: property `pegPriceType` added
  - `result`.`orderReports`.items: property `strategyId` added
  - `result`.`orderReports`.items: property `expiryReason` added
  - `result`.`orderReports`.items: property `workingFloor` added
  - `result`.`orderReports`.items: item property `preventedQuantity` added
  - `result`.`orderReports`.items: item property `usedSor` added
  - `result`.`orderReports`.items: item property `pegOffsetType` added
  - `result`.`orderReports`.items: item property `strategyType` added
  - `result`.`orderReports`.items: item property `trailingDelta` added
  - `result`.`orderReports`.items: item property `trailingTime` added
  - `result`.`orderReports`.items: item property `preventedMatchId` added
  - `result`.`orderReports`.items: item property `peggedPrice` added
  - `result`.`orderReports`.items: item property `icebergQty` added
  - `result`.`orderReports`.items: item property `pegOffsetValue` added
  - `result`.`orderReports`.items: item property `pegPriceType` added
  - `result`.`orderReports`.items: item property `strategyId` added
  - `result`.`orderReports`.items: item property `expiryReason` added
  - `result`.`orderReports`.items: item property `workingFloor` added

- Modified response for `order_cancel_replace()` (`order.cancelReplace` method):
  - `result`.`cancelResponse`: property `trailingDelta` added
  - `result`.`cancelResponse`: property `pegOffsetType` added
  - `result`.`cancelResponse`: property `expiryReason` added
  - `result`.`cancelResponse`: property `pegOffsetValue` added
  - `result`.`cancelResponse`: property `peggedPrice` added
  - `result`.`cancelResponse`: property `usedSor` added
  - `result`.`cancelResponse`: property `trailingTime` added
  - `result`.`cancelResponse`: property `strategyId` added
  - `result`.`cancelResponse`: property `workingFloor` added
  - `result`.`cancelResponse`: property `strategyType` added
  - `result`.`cancelResponse`: property `preventedMatchId` added
  - `result`.`cancelResponse`: property `preventedQuantity` added
  - `result`.`cancelResponse`: property `icebergQty` added
  - `result`.`cancelResponse`: property `pegPriceType` added
  - `result`.`cancelResponse`: property `stopPrice` added
  - `result`.`newOrderResponse`: property `strategyId` added
  - `result`.`newOrderResponse`: property `icebergQty` added
  - `result`.`newOrderResponse`: property `pegOffsetType` added
  - `result`.`newOrderResponse`: property `expiryReason` added
  - `result`.`newOrderResponse`: property `peggedPrice` added
  - `result`.`newOrderResponse`: property `trailingDelta` added
  - `result`.`newOrderResponse`: property `usedSor` added
  - `result`.`newOrderResponse`: property `stopPrice` added
  - `result`.`newOrderResponse`: property `pegOffsetValue` added
  - `result`.`newOrderResponse`: property `strategyType` added
  - `result`.`newOrderResponse`: property `trailingTime` added
  - `result`.`newOrderResponse`: property `workingFloor` added
  - `result`.`newOrderResponse`: property `pegPriceType` added
  - `result`.`newOrderResponse`: property `preventedQuantity` added
  - `result`.`newOrderResponse`: property `preventedMatchId` added

- Modified response for `order_place()` (`order.place` method):
  - `result`: property `strategyType` added
  - `result`: property `workingFloor` added
  - `result`: property `preventedQuantity` added
  - `result`: property `strategyId` added
  - `result`: property `stopPrice` added
  - `result`: property `expiryReason` added
  - `result`: property `usedSor` added
  - `result`: property `trailingDelta` added
  - `result`: property `pegOffsetType` added
  - `result`: property `preventedMatchId` added
  - `result`: property `pegPriceType` added
  - `result`: property `icebergQty` added
  - `result`: property `pegOffsetValue` added
  - `result`: property `peggedPrice` added
  - `result`: property `trailingTime` added

- Modified response for `order_status()` (`order.status` method):
  - `result`: property `pegPriceType` added
  - `result`: property `workingFloor` added
  - `result`: property `expiryReason` added
  - `result`: property `usedSor` added
  - `result`: property `pegOffsetType` added
  - `result`: property `pegOffsetValue` added
  - `result`: property `peggedPrice` added

- Modified response for `order_list_cancel()` (`orderList.cancel` method):
  - `result`.`orderReports`.items: property `preventedQuantity` added
  - `result`.`orderReports`.items: property `icebergQty` added
  - `result`.`orderReports`.items: property `trailingTime` added
  - `result`.`orderReports`.items: property `pegOffsetValue` added
  - `result`.`orderReports`.items: property `peggedPrice` added
  - `result`.`orderReports`.items: property `usedSor` added
  - `result`.`orderReports`.items: property `pegOffsetType` added
  - `result`.`orderReports`.items: property `expiryReason` added
  - `result`.`orderReports`.items: property `strategyType` added
  - `result`.`orderReports`.items: property `workingFloor` added
  - `result`.`orderReports`.items: property `strategyId` added
  - `result`.`orderReports`.items: property `preventedMatchId` added
  - `result`.`orderReports`.items: property `pegPriceType` added
  - `result`.`orderReports`.items: property `trailingDelta` added
  - `result`.`orderReports`.items: item property `preventedQuantity` added
  - `result`.`orderReports`.items: item property `icebergQty` added
  - `result`.`orderReports`.items: item property `trailingTime` added
  - `result`.`orderReports`.items: item property `pegOffsetValue` added
  - `result`.`orderReports`.items: item property `peggedPrice` added
  - `result`.`orderReports`.items: item property `usedSor` added
  - `result`.`orderReports`.items: item property `pegOffsetType` added
  - `result`.`orderReports`.items: item property `expiryReason` added
  - `result`.`orderReports`.items: item property `strategyType` added
  - `result`.`orderReports`.items: item property `workingFloor` added
  - `result`.`orderReports`.items: item property `strategyId` added
  - `result`.`orderReports`.items: item property `preventedMatchId` added
  - `result`.`orderReports`.items: item property `pegPriceType` added
  - `result`.`orderReports`.items: item property `trailingDelta` added

- Modified response for `order_list_place()` (`orderList.place` method):
  - `result`.`orderReports`.items: property `usedSor` added
  - `result`.`orderReports`.items: property `pegOffsetValue` added
  - `result`.`orderReports`.items: property `peggedPrice` added
  - `result`.`orderReports`.items: property `expiryReason` added
  - `result`.`orderReports`.items: property `icebergQty` added
  - `result`.`orderReports`.items: property `pegOffsetType` added
  - `result`.`orderReports`.items: property `trailingTime` added
  - `result`.`orderReports`.items: property `preventedQuantity` added
  - `result`.`orderReports`.items: property `preventedMatchId` added
  - `result`.`orderReports`.items: property `strategyType` added
  - `result`.`orderReports`.items: property `workingFloor` added
  - `result`.`orderReports`.items: property `strategyId` added
  - `result`.`orderReports`.items: property `pegPriceType` added
  - `result`.`orderReports`.items: property `trailingDelta` added
  - `result`.`orderReports`.items: item property `usedSor` added
  - `result`.`orderReports`.items: item property `pegOffsetValue` added
  - `result`.`orderReports`.items: item property `peggedPrice` added
  - `result`.`orderReports`.items: item property `expiryReason` added
  - `result`.`orderReports`.items: item property `icebergQty` added
  - `result`.`orderReports`.items: item property `pegOffsetType` added
  - `result`.`orderReports`.items: item property `trailingTime` added
  - `result`.`orderReports`.items: item property `preventedQuantity` added
  - `result`.`orderReports`.items: item property `preventedMatchId` added
  - `result`.`orderReports`.items: item property `strategyType` added
  - `result`.`orderReports`.items: item property `workingFloor` added
  - `result`.`orderReports`.items: item property `strategyId` added
  - `result`.`orderReports`.items: item property `pegPriceType` added
  - `result`.`orderReports`.items: item property `trailingDelta` added

- Modified response for `order_list_place_oco()` (`orderList.place.oco` method):
  - `result`.`orderReports`.items: property `pegOffsetType` added
  - `result`.`orderReports`.items: property `peggedPrice` added
  - `result`.`orderReports`.items: property `icebergQty` added
  - `result`.`orderReports`.items: property `pegOffsetValue` added
  - `result`.`orderReports`.items: property `preventedQuantity` added
  - `result`.`orderReports`.items: property `strategyType` added
  - `result`.`orderReports`.items: property `trailingTime` added
  - `result`.`orderReports`.items: property `strategyId` added
  - `result`.`orderReports`.items: property `expiryReason` added
  - `result`.`orderReports`.items: property `preventedMatchId` added
  - `result`.`orderReports`.items: property `pegPriceType` added
  - `result`.`orderReports`.items: property `trailingDelta` added
  - `result`.`orderReports`.items: property `usedSor` added
  - `result`.`orderReports`.items: property `workingFloor` added
  - `result`.`orderReports`.items: item property `pegOffsetType` added
  - `result`.`orderReports`.items: item property `peggedPrice` added
  - `result`.`orderReports`.items: item property `icebergQty` added
  - `result`.`orderReports`.items: item property `pegOffsetValue` added
  - `result`.`orderReports`.items: item property `preventedQuantity` added
  - `result`.`orderReports`.items: item property `strategyType` added
  - `result`.`orderReports`.items: item property `trailingTime` added
  - `result`.`orderReports`.items: item property `strategyId` added
  - `result`.`orderReports`.items: item property `expiryReason` added
  - `result`.`orderReports`.items: item property `preventedMatchId` added
  - `result`.`orderReports`.items: item property `pegPriceType` added
  - `result`.`orderReports`.items: item property `trailingDelta` added
  - `result`.`orderReports`.items: item property `usedSor` added
  - `result`.`orderReports`.items: item property `workingFloor` added

- Modified response for `order_list_place_opo()` (`orderList.place.opo` method):
  - `result`.`orderReports`.items: property `icebergQty` added
  - `result`.`orderReports`.items: property `preventedMatchId` added
  - `result`.`orderReports`.items: property `pegPriceType` added
  - `result`.`orderReports`.items: property `trailingTime` added
  - `result`.`orderReports`.items: property `strategyId` added
  - `result`.`orderReports`.items: property `peggedPrice` added
  - `result`.`orderReports`.items: property `trailingDelta` added
  - `result`.`orderReports`.items: property `usedSor` added
  - `result`.`orderReports`.items: property `workingFloor` added
  - `result`.`orderReports`.items: property `preventedQuantity` added
  - `result`.`orderReports`.items: property `stopPrice` added
  - `result`.`orderReports`.items: property `expiryReason` added
  - `result`.`orderReports`.items: property `strategyType` added
  - `result`.`orderReports`.items: property `pegOffsetValue` added
  - `result`.`orderReports`.items: property `pegOffsetType` added
  - `result`.`orderReports`.items: item property `icebergQty` added
  - `result`.`orderReports`.items: item property `preventedMatchId` added
  - `result`.`orderReports`.items: item property `pegPriceType` added
  - `result`.`orderReports`.items: item property `trailingTime` added
  - `result`.`orderReports`.items: item property `strategyId` added
  - `result`.`orderReports`.items: item property `peggedPrice` added
  - `result`.`orderReports`.items: item property `trailingDelta` added
  - `result`.`orderReports`.items: item property `usedSor` added
  - `result`.`orderReports`.items: item property `workingFloor` added
  - `result`.`orderReports`.items: item property `preventedQuantity` added
  - `result`.`orderReports`.items: item property `stopPrice` added
  - `result`.`orderReports`.items: item property `expiryReason` added
  - `result`.`orderReports`.items: item property `strategyType` added
  - `result`.`orderReports`.items: item property `pegOffsetValue` added
  - `result`.`orderReports`.items: item property `pegOffsetType` added

- Modified response for `order_list_place_opoco()` (`orderList.place.opoco` method):
  - `result`.`orderReports`.items: property `strategyId` added
  - `result`.`orderReports`.items: property `pegOffsetType` added
  - `result`.`orderReports`.items: property `pegOffsetValue` added
  - `result`.`orderReports`.items: property `preventedQuantity` added
  - `result`.`orderReports`.items: property `trailingDelta` added
  - `result`.`orderReports`.items: property `expiryReason` added
  - `result`.`orderReports`.items: property `trailingTime` added
  - `result`.`orderReports`.items: property `pegPriceType` added
  - `result`.`orderReports`.items: property `workingFloor` added
  - `result`.`orderReports`.items: property `icebergQty` added
  - `result`.`orderReports`.items: property `usedSor` added
  - `result`.`orderReports`.items: property `preventedMatchId` added
  - `result`.`orderReports`.items: property `strategyType` added
  - `result`.`orderReports`.items: property `peggedPrice` added
  - `result`.`orderReports`.items: item property `strategyId` added
  - `result`.`orderReports`.items: item property `pegOffsetType` added
  - `result`.`orderReports`.items: item property `pegOffsetValue` added
  - `result`.`orderReports`.items: item property `preventedQuantity` added
  - `result`.`orderReports`.items: item property `trailingDelta` added
  - `result`.`orderReports`.items: item property `expiryReason` added
  - `result`.`orderReports`.items: item property `trailingTime` added
  - `result`.`orderReports`.items: item property `pegPriceType` added
  - `result`.`orderReports`.items: item property `workingFloor` added
  - `result`.`orderReports`.items: item property `icebergQty` added
  - `result`.`orderReports`.items: item property `usedSor` added
  - `result`.`orderReports`.items: item property `preventedMatchId` added
  - `result`.`orderReports`.items: item property `strategyType` added
  - `result`.`orderReports`.items: item property `peggedPrice` added

- Modified response for `order_list_place_oto()` (`orderList.place.oto` method):
  - `result`.`orderReports`.items: property `peggedPrice` added
  - `result`.`orderReports`.items: property `strategyType` added
  - `result`.`orderReports`.items: property `trailingTime` added
  - `result`.`orderReports`.items: property `preventedQuantity` added
  - `result`.`orderReports`.items: property `workingFloor` added
  - `result`.`orderReports`.items: property `preventedMatchId` added
  - `result`.`orderReports`.items: property `strategyId` added
  - `result`.`orderReports`.items: property `pegOffsetType` added
  - `result`.`orderReports`.items: property `trailingDelta` added
  - `result`.`orderReports`.items: property `icebergQty` added
  - `result`.`orderReports`.items: property `pegOffsetValue` added
  - `result`.`orderReports`.items: property `pegPriceType` added
  - `result`.`orderReports`.items: property `stopPrice` added
  - `result`.`orderReports`.items: property `usedSor` added
  - `result`.`orderReports`.items: property `expiryReason` added
  - `result`.`orderReports`.items: item property `peggedPrice` added
  - `result`.`orderReports`.items: item property `strategyType` added
  - `result`.`orderReports`.items: item property `trailingTime` added
  - `result`.`orderReports`.items: item property `preventedQuantity` added
  - `result`.`orderReports`.items: item property `workingFloor` added
  - `result`.`orderReports`.items: item property `preventedMatchId` added
  - `result`.`orderReports`.items: item property `strategyId` added
  - `result`.`orderReports`.items: item property `pegOffsetType` added
  - `result`.`orderReports`.items: item property `trailingDelta` added
  - `result`.`orderReports`.items: item property `icebergQty` added
  - `result`.`orderReports`.items: item property `pegOffsetValue` added
  - `result`.`orderReports`.items: item property `pegPriceType` added
  - `result`.`orderReports`.items: item property `stopPrice` added
  - `result`.`orderReports`.items: item property `usedSor` added
  - `result`.`orderReports`.items: item property `expiryReason` added

- Modified response for `order_list_place_otoco()` (`orderList.place.otoco` method):
  - `result`.`orderReports`.items: property `icebergQty` added
  - `result`.`orderReports`.items: property `trailingDelta` added
  - `result`.`orderReports`.items: property `pegOffsetType` added
  - `result`.`orderReports`.items: property `peggedPrice` added
  - `result`.`orderReports`.items: property `expiryReason` added
  - `result`.`orderReports`.items: property `workingFloor` added
  - `result`.`orderReports`.items: property `pegOffsetValue` added
  - `result`.`orderReports`.items: property `trailingTime` added
  - `result`.`orderReports`.items: property `usedSor` added
  - `result`.`orderReports`.items: property `pegPriceType` added
  - `result`.`orderReports`.items: property `strategyId` added
  - `result`.`orderReports`.items: property `strategyType` added
  - `result`.`orderReports`.items: property `preventedMatchId` added
  - `result`.`orderReports`.items: property `preventedQuantity` added
  - `result`.`orderReports`.items: item property `icebergQty` added
  - `result`.`orderReports`.items: item property `trailingDelta` added
  - `result`.`orderReports`.items: item property `pegOffsetType` added
  - `result`.`orderReports`.items: item property `peggedPrice` added
  - `result`.`orderReports`.items: item property `expiryReason` added
  - `result`.`orderReports`.items: item property `workingFloor` added
  - `result`.`orderReports`.items: item property `pegOffsetValue` added
  - `result`.`orderReports`.items: item property `trailingTime` added
  - `result`.`orderReports`.items: item property `usedSor` added
  - `result`.`orderReports`.items: item property `pegPriceType` added
  - `result`.`orderReports`.items: item property `strategyId` added
  - `result`.`orderReports`.items: item property `strategyType` added
  - `result`.`orderReports`.items: item property `preventedMatchId` added
  - `result`.`orderReports`.items: item property `preventedQuantity` added

- Modified response for `reference_price()` (`referencePrice` method):
  - property `rateLimits` added

- Modified response for `reference_price_calculation()` (`referencePrice.calculation` method):
  - property `rateLimits` added

- Modified response for `sor_order_place()` (`sor.order.place` method):
  - `result`.items: property `pegOffsetType` added
  - `result`.items: property `peggedPrice` added
  - `result`.items: property `stopPrice` added
  - `result`.items: property `strategyType` added
  - `result`.items: property `expiryReason` added
  - `result`.items: property `icebergQty` added
  - `result`.items: property `pegPriceType` added
  - `result`.items: property `preventedMatchId` added
  - `result`.items: property `strategyId` added
  - `result`.items: property `pegOffsetValue` added
  - `result`.items: property `trailingDelta` added
  - `result`.items: property `preventedQuantity` added
  - `result`.items: property `trailingTime` added
  - `result`.items: item property `pegOffsetType` added
  - `result`.items: item property `peggedPrice` added
  - `result`.items: item property `stopPrice` added
  - `result`.items: item property `strategyType` added
  - `result`.items: item property `expiryReason` added
  - `result`.items: item property `icebergQty` added
  - `result`.items: item property `pegPriceType` added
  - `result`.items: item property `preventedMatchId` added
  - `result`.items: item property `strategyId` added
  - `result`.items: item property `pegOffsetValue` added
  - `result`.items: item property `trailingDelta` added
  - `result`.items: item property `preventedQuantity` added
  - `result`.items: item property `trailingTime` added

- Modified response for `ticker()` (`ticker` method):
  - oneOf modified

- Modified response for `ticker24hr()` (`ticker.24hr` method):
  - oneOf modified

- Modified response for `ticker_book()` (`ticker.book` method):
  - oneOf modified

- Modified response for `ticker_price()` (`ticker.price` method):
  - oneOf modified

- Modified response for `ui_klines()` (`uiKlines` method):
  - `result`.items: minItems `0` → `12`
  - `result`.items: maxItems `null` → `12`
  - `result`.items.items: oneOf added 2 schema(s)
  - `result`.items.items: oneOf removed 2 schema(s)

- Marked `order_list_place()` (`orderList.place` method) as deprecated.

#### WebSocket Streams

- Modified parameter `updateSpeed`:
  - enum added: `100ms`
  - affected methods:
    - `partial_book_depth()` (`<symbol>@depth<levels>@<updateSpeed>` stream)
    - `diff_book_depth()` (`<symbol>@depth@<updateSpeed>` stream)
- Modified response for `partial_book_depth()` (`<symbol>@depth<levels>@<updateSpeed>` stream):
  - `asks`.items: minItems `0` → `2`
  - `asks`.items: maxItems `null` → `2`
  - `bids`.items: minItems `0` → `2`
  - `bids`.items: maxItems `null` → `2`

- Modified response for `diff_book_depth()` (`<symbol>@depth@<updateSpeed>` stream):
  - `a`.items: minItems `0` → `2`
  - `a`.items: maxItems `null` → `2`
  - `b`.items: minItems `0` → `2`
  - `b`.items: maxItems `null` → `2`

## 9.2.0 - 2026-06-09

### Changed (2)

- Updated `binance-common` library to version `4.0.0`
- Updated `pyproject.toml` dependencies

## 9.1.0 - 2026-05-29

### Changed (1)

- Updated `binance-common` library to version `3.10.0`

## 9.0.0 - 2026-05-18

### Added (2)

#### REST API

- `historical_block_trades()` (`GET /api/v3/historicalBlockTrades`)

#### WebSocket API

- `block_trades_historical()` (`blockTrades.historical` method)

#### WebSocket Streams

- `block_trade()` (`<symbol>@blockTrade` stream)

### Changed (3)

- Updated `binance-common` library to version `3.9.2`
- Updated `pyproject.toml` dependencies

#### REST API

- Modified parameter `selfTradePreventionMode`:
  - enum added: `TRANSFER`
  - affected methods:
    - `new_order()` (`POST /api/v3/order`)
    - `order_cancel_replace()` (`POST /api/v3/order/cancelReplace`)
    - `order_oco()` (`POST /api/v3/order/oco`)
    - `order_test()` (`POST /api/v3/order/test`)
    - `order_list_oco()` (`POST /api/v3/orderList/oco`)
    - `order_list_opo()` (`POST /api/v3/orderList/opo`)
    - `order_list_opoco()` (`POST /api/v3/orderList/opoco`)
    - `order_list_oto()` (`POST /api/v3/orderList/oto`)
    - `order_list_otoco()` (`POST /api/v3/orderList/otoco`)
    - `sor_order()` (`POST /api/v3/sor/order`)
    - `sor_order_test()` (`POST /api/v3/sor/order/test`)
- Marked `order_oco()` (`POST /api/v3/order/oco`) as deprecated.

#### WebSocket API

- Modified parameter `selfTradePreventionMode`:
  - enum added: `TRANSFER`
  - affected methods:
    - `order_cancel_replace()` (`order.cancelReplace` method)
    - `order_place()` (`order.place` method)
    - `order_test()` (`order.test` method)
    - `order_list_place()` (`orderList.place` method)
    - `order_list_place_oco()` (`orderList.place.oco` method)
    - `order_list_place_opo()` (`orderList.place.opo` method)
    - `order_list_place_opoco()` (`orderList.place.opoco` method)
    - `order_list_place_oto()` (`orderList.place.oto` method)
    - `order_list_place_otoco()` (`orderList.place.otoco` method)
    - `sor_order_place()` (`sor.order.place` method)
    - `sor_order_test()` (`sor.order.test` method)

## 8.4.0 - 2026-04-29

- Updated `binance-common` library to version `3.9.1`
- Updated `pyproject.toml` dependencies

## 8.3.0 - 2026-04-29

### Changed (1)

- Updated `binance-common` library to version `3.9.0`

## 8.2.1 - 2026-04-21

### Changed (1)

- Update `user_data_stream_subscribe_signature()` and `user_data_stream_subscribe()` error checks.

## 8.2.0 - 2026-04-20

### Changed (2)

#### WebSocket API

- Modified response for `reference_price()` (`referencePrice` method):
  - `result`: property `code` added
  - `result`: property `msg` added
- Fix empty user data stream subscription response in `user_data_stream_subscribe_signature()` (`userDataStream.subscribe.signature` method) and `user_data_stream_subscribe()` (`userDataStream.subscribe` method) methods by adding error checks for missing subscription ID and presence of error in the response.

## 8.1.0 - 2026-03-26

### Added (1)

- Added `py.typed` file to indicate that the package supports type hints.

### Changed (2)

- Updated `binance-common` library to version `3.8.0`
- Updated `tox` file

## 8.0.0 - 2026-03-16

### Added (7)

#### REST API

- `execution_rules()` (`GET /api/v3/executionRules`)
- `reference_price()` (`GET /api/v3/referencePrice`)
- `reference_price_calculation()` (`GET /api/v3/referencePrice/calculation`)

#### WebSocket API

- `execution_rules()` (`executionRules` method)
- `reference_price()` (`referencePrice` method)
- `reference_price_calculation()` (`referencePrice.calculation` method)

#### WebSocket Streams

- `reference_price()` (`<symbol>@referencePrice` stream)

### Changed (1)

- Updated `binance-common` library to version `3.7.0`

## 7.2.0 - 2026-02-25

### Changed (2)

#### REST API

- Updated following response models to remove unused struct:
  - `KlinesResponse`
  - `UiKlinesResponse`

#### WebSocket API

- Fixed error in `KlinesResponse` and `UiKlinesResponse` models by removing `KlinesItemInner` struct.

## 7.1.0 - 2026-02-11

### Changed (2)

- Updated `binance-common` library to version `3.6.0`
- Updated `pyproject.toml` dependencies

## 7.0.0 - 2026-01-29

### Changed (2)

- Updated `binance-common` library to version `3.5.0`

#### WebSocket API

- Added parameter `recvWindow`
  - affected methods:
    - `user_data_stream_subscribe_signature()` (`userDataStream.subscribe.signature` method)

## 6.3.0 - 2026-01-23

### Changed (1)

- Updated `binance-common` library to version `3.4.1`

## 6.2.0 - 2026-01-19

### Changed (1)

- Updated `Subscribe` method in `websocket.py` to accept optional `stream_url` parameter.

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
