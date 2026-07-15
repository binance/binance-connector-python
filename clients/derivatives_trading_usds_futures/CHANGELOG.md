# Changelog

## 14.0.0 - 2026-07-15

### Changed (9)

#### REST API

- Modified response for `cancel_multiple_orders()` (`DELETE /fapi/v1/batchOrders`):
  - items: property `cumQuote` deleted
  - items: item property `cumQuote` deleted

- Modified response for `place_multiple_orders()` (`POST /fapi/v1/batchOrders`):
  - items: property `cumQuote` deleted
  - items: property `avgPrice` deleted
  - items: item property `cumQuote` deleted
  - items: item property `avgPrice` deleted

- Modified response for `modify_multiple_orders()` (`PUT /fapi/v1/batchOrders`):
  - items: property `avgPrice` deleted
  - items: property `cumBase` deleted
  - items: item property `avgPrice` deleted
  - items: item property `cumBase` deleted

- Modified response for `cancel_order()` (`DELETE /fapi/v1/order`):
  - property `cumQuote` deleted
  - property `avgPrice` deleted

- Modified response for `new_order()` (`POST /fapi/v1/order`):
  - property `avgPrice` deleted
  - property `cumQuote` deleted

- Modified response for `modify_order()` (`PUT /fapi/v1/order`):
  - property `avgPrice` deleted
  - property `cumBase` deleted

#### WebSocket API

- Modified response for `cancel_order()` (`order.cancel` method):
  - `result`: property `cumQuote` deleted

- Modified response for `modify_order()` (`order.modify` method):
  - `result`: property `avgPrice` deleted
  - `result`: property `cumQuote` deleted

- Modified response for `new_order()` (`order.place` method):
  - `result`: property `cumQuote` deleted
  - `result`: property `avgPrice` deleted

## 13.0.0 - 2026-07-14

### Changed (57)

- Updated `binance-common` library to version `4.0.3`

#### REST API

- Modified parameter `algo_type`:
  - enum added: `CONDITIONAL`
  - affected methods:
    - `new_algo_order()` (`POST /fapi/v1/algoOrder`)
- Modified parameter `batch_orders`:
  - items.`goodTillDate`: type `string` → `integer`
  - items.`price`: type `string` → `number`
  - items.`priceMatch`: enum removed: `NONE`
  - items.`quantity`: type `string` → `number`
  - items.`reduceOnly`: enum added: `true`, `false`
  - items.`selfTradePreventionMode`: enum added: `NONE`
  - items.`type`: enum added: `LIMIT`, `MARKET`, `STOP`, `STOP_MARKET`, `TAKE_PROFIT`, `TAKE_PROFIT_MARKET`, `TRAILING_STOP_MARKET`
  - items.`goodTillDate`: type `string` → `integer`
  - items.`price`: type `string` → `number`
  - items.`priceMatch`: enum removed: `NONE`
  - items.`quantity`: type `string` → `number`
  - items.`reduceOnly`: enum added: `true`, `false`
  - items.`selfTradePreventionMode`: enum added: `NONE`
  - items.`type`: enum added: `LIMIT`, `MARKET`, `STOP`, `STOP_MARKET`, `TAKE_PROFIT`, `TAKE_PROFIT_MARKET`, `TRAILING_STOP_MARKET`
  - affected methods:
    - `place_multiple_orders()` (`POST /fapi/v1/batchOrders`)
- Modified parameter `batch_orders`:
  - items: property `timestamp` added
  - items.`orderId`: type `string` → `integer`
  - items.`price`: type `string` → `number`
  - items.`priceMatch`: enum removed: `NONE`
  - items.`quantity`: type `string` → `number`
  - items.`recvWindow`: type `string` → `integer`
  - items.`stopPrice`: type `string` → `number`
  - items: item property `timestamp` added
  - items.`orderId`: type `string` → `integer`
  - items.`price`: type `string` → `number`
  - items.`priceMatch`: enum removed: `NONE`
  - items.`quantity`: type `string` → `number`
  - items.`recvWindow`: type `string` → `integer`
  - items.`stopPrice`: type `string` → `number`
  - affected methods:
    - `modify_multiple_orders()` (`PUT /fapi/v1/batchOrders`)
- Modified parameter `close_position`:
  - enum added: `true`, `false`
  - affected methods:
    - `new_algo_order()` (`POST /fapi/v1/algoOrder`)
    - `test_order()` (`POST /fapi/v1/order/test`)
- Modified parameter `contract_type`:
  - enum removed: `CURRENT_MONTH`, `NEXT_MONTH`, `PERPETUAL_DELIVERING`
  - enum added: `TRADIFI_PERPETUAL`
  - affected methods:
    - `continuous_contract_kline_candlestick_data()` (`GET /fapi/v1/continuousKlines`)
- Modified parameter `contract_type`:
  - enum removed: `CURRENT_MONTH`, `NEXT_MONTH`, `PERPETUAL_DELIVERING`
  - affected methods:
    - `basis()` (`GET /futures/data/basis`)
- Modified parameter `income_type`:
  - enum added: `TRANSFER`, `WELCOME_BONUS`, `REALIZED_PNL`, `FUNDING_FEE`, `COMMISSION`, `INSURANCE_CLEAR`, `REFERRAL_KICKBACK`, `COMMISSION_REBATE`, `API_REBATE`, `CONTEST_REWARD`, `CROSS_COLLATERAL_TRANSFER`, `OPTIONS_PREMIUM_FEE`, `OPTIONS_SETTLE_PROFIT`, `INTERNAL_TRANSFER`, `AUTO_EXCHANGE`, `DELIVERED_SETTELMENT`, `COIN_SWAP_DEPOSIT`, `COIN_SWAP_WITHDRAW`, `POSITION_LIMIT_INCREASE_FEE`, `STRATEGY_UMFUTURES_TRANSFER`, `FEE_RETURN`, `BFUSD_REWARD`
  - affected methods:
    - `get_income_history()` (`GET /fapi/v1/income`)
- Modified parameter `interval`:
  - enum removed: `1s`
  - affected methods:
    - `continuous_contract_kline_candlestick_data()` (`GET /fapi/v1/continuousKlines`)
    - `index_price_kline_candlestick_data()` (`GET /fapi/v1/indexPriceKlines`)
    - `kline_candlestick_data()` (`GET /fapi/v1/klines`)
    - `mark_price_kline_candlestick_data()` (`GET /fapi/v1/markPriceKlines`)
    - `premium_index_kline_data()` (`GET /fapi/v1/premiumIndexKlines`)
- Modified parameter `order_id_list`:
  - maxLength `null` → `10`
  - affected methods:
    - `cancel_multiple_orders()` (`DELETE /fapi/v1/batchOrders`)
- Modified parameter `orig_client_order_id_list`:
  - maxLength `null` → `10`
  - affected methods:
    - `cancel_multiple_orders()` (`DELETE /fapi/v1/batchOrders`)
- Modified parameter `position_side`:
  - enum removed: `BOTH`, `LONG`, `SHORT`
  - affected methods:
    - `new_algo_order()` (`POST /fapi/v1/algoOrder`)
    - `new_order()` (`POST /fapi/v1/order`)
    - `modify_isolated_position_margin()` (`POST /fapi/v1/positionMargin`)
- Modified parameter `price_match`:
  - enum removed: `NONE`
  - affected methods:
    - `new_algo_order()` (`POST /fapi/v1/algoOrder`)
    - `new_order()` (`POST /fapi/v1/order`)
    - `modify_order()` (`PUT /fapi/v1/order`)
    - `test_order()` (`POST /fapi/v1/order/test`)
- Modified parameter `price_protect`:
  - enum added: `true`, `false`
  - affected methods:
    - `new_algo_order()` (`POST /fapi/v1/algoOrder`)
    - `test_order()` (`POST /fapi/v1/order/test`)
- Modified parameter `reduce_only`:
  - enum added: `true`, `false`
  - affected methods:
    - `new_algo_order()` (`POST /fapi/v1/algoOrder`)
    - `new_order()` (`POST /fapi/v1/order`)
    - `test_order()` (`POST /fapi/v1/order/test`)
- Modified parameter `self_trade_prevention_mode`:
  - enum added: `NONE`
  - affected methods:
    - `new_algo_order()` (`POST /fapi/v1/algoOrder`)
    - `test_order()` (`POST /fapi/v1/order/test`)
- Modified parameter `type`:
  - enum added: `LIMIT`, `MARKET`, `STOP`, `STOP_MARKET`, `TAKE_PROFIT`, `TAKE_PROFIT_MARKET`, `TRAILING_STOP_MARKET`
  - affected methods:
    - `new_algo_order()` (`POST /fapi/v1/algoOrder`)
- Modified parameter `type`:
  - enum added: `LIMIT`, `MARKET`, `STOP`, `STOP_MARKET`, `TAKE_PROFIT`, `TAKE_PROFIT_MARKET`, `TRAILING_STOP_MARKET`
  - affected methods:
    - `new_order()` (`POST /fapi/v1/order`)
    - `test_order()` (`POST /fapi/v1/order/test`)
- Modified parameter `type`:
  - type `string` → `integer`
  - affected methods:
    - `modify_isolated_position_margin()` (`POST /fapi/v1/positionMargin`)
- Modified parameter `type`:
  - type `integer` → `string`
  - affected methods:
    - `get_position_margin_change_history()` (`GET /fapi/v1/positionMargin/history`)
- Modified response for `order_book()` (`GET /fapi/v1/depth`):
  - `asks`.items: minItems `0` → `2`
  - `asks`.items: maxItems `null` → `2`
  - `bids`.items: minItems `0` → `2`
  - `bids`.items: maxItems `null` → `2`

- Modified response for `query_insurance_fund_balance_snapshot()` (`GET /fapi/v1/insuranceBalance`):
  - oneOf modified

- Modified response for `notional_and_leverage_brackets()` (`GET /fapi/v1/leverageBracket`):
  - oneOf modified

- Modified response for `query_order()` (`GET /fapi/v1/order`):
  - property `selfTradePreventionMode` added
  - property `goodTillDate` added
  - property `priceMatch` added

- Modified response for `mark_price()` (`GET /fapi/v1/premiumIndex`):
  - oneOf modified

- Modified response for `rpi_order_book()` (`GET /fapi/v1/rpiDepth`):
  - `asks`.items: minItems `0` → `2`
  - `asks`.items: maxItems `null` → `2`
  - `bids`.items: minItems `0` → `2`
  - `bids`.items: maxItems `null` → `2`

- Modified response for `adl_risk()` (`GET /fapi/v1/symbolAdlRisk`):
  - oneOf modified

- Modified response for `ticker24hr_price_change_statistics()` (`GET /fapi/v1/ticker/24hr`):
  - oneOf modified

- Modified response for `symbol_order_book_ticker()` (`GET /fapi/v1/ticker/bookTicker`):
  - oneOf modified

- Modified response for `symbol_price_ticker()` (`GET /fapi/v1/ticker/price`):
  - oneOf modified

- Modified response for `symbol_price_ticker_v2()` (`GET /fapi/v2/ticker/price`):
  - oneOf modified

- Modified response for `long_short_ratio()` (`GET /futures/data/globalLongShortAccountRatio`):
  - items.`timestamp`: type `string` → `integer`
  - items.`timestamp`: type `string` → `integer`

- Modified response for `open_interest_statistics()` (`GET /futures/data/openInterestHist`):
  - items.`timestamp`: type `string` → `integer`
  - items.`timestamp`: type `string` → `integer`

- Modified response for `taker_buy_sell_volume()` (`GET /futures/data/takerlongshortRatio`):
  - items.`timestamp`: type `string` → `integer`
  - items.`timestamp`: type `string` → `integer`

- Modified response for `top_trader_long_short_ratio_accounts()` (`GET /futures/data/topLongShortAccountRatio`):
  - items.`timestamp`: type `string` → `integer`
  - items.`timestamp`: type `string` → `integer`

- Modified response for `top_trader_long_short_ratio_positions()` (`GET /futures/data/topLongShortPositionRatio`):
  - items.`timestamp`: type `string` → `integer`
  - items.`timestamp`: type `string` → `integer`

- Marked `symbol_price_ticker()` (`GET /fapi/v1/ticker/price`) as deprecated.

#### WebSocket API

- Modified parameter `algo_type`:
  - enum added: `CONDITIONAL`
  - affected methods:
    - `new_algo_order()` (`algoOrder.place` method)
- Modified parameter `close_position`:
  - enum added: `true`, `false`
  - affected methods:
    - `new_algo_order()` (`algoOrder.place` method)
- Modified parameter `price_match`:
  - enum removed: `NONE`
  - affected methods:
    - `new_algo_order()` (`algoOrder.place` method)
    - `modify_order()` (`order.modify` method)
    - `new_order()` (`order.place` method)
- Modified parameter `price_protect`:
  - enum added: `true`, `false`
  - affected methods:
    - `new_algo_order()` (`algoOrder.place` method)
- Modified parameter `reduce_only`:
  - enum added: `true`, `false`
  - affected methods:
    - `new_algo_order()` (`algoOrder.place` method)
    - `new_order()` (`order.place` method)
- Modified parameter `self_trade_prevention_mode`:
  - enum added: `NONE`
  - affected methods:
    - `new_algo_order()` (`algoOrder.place` method)
- Modified parameter `self_trade_prevention_mode`:
  - enum added: `NONE`
  - affected methods:
    - `new_order()` (`order.place` method)
- Modified parameter `time_in_force`:
  - enum removed: `GTX`, `GTD`, `RPI`
  - affected methods:
    - `new_algo_order()` (`algoOrder.place` method)
- Modified parameter `type`:
  - enum added: `STOP_MARKET`, `TAKE_PROFIT_MARKET`, `STOP`, `TAKE_PROFIT`, `TRAILING_STOP_MARKET`
  - affected methods:
    - `new_algo_order()` (`algoOrder.place` method)
- Modified parameter `type`:
  - enum added: `LIMIT`, `MARKET`
  - affected methods:
    - `new_order()` (`order.place` method)
- Modified response for `order_book()` (`depth` method):
  - property `asks` added
  - property `bids` added
  - `result`: property `bids` deleted
  - `result`: property `asks` deleted

- Modified response for `query_order()` (`order.status` method):
  - `result`: property `goodTillDate` added
  - `result`: property `selfTradePreventionMode` added
  - `result`: property `priceMatch` added

- Modified response for `symbol_order_book_ticker()` (`ticker.book` method):
  - oneOf modified

- Modified response for `symbol_price_ticker()` (`ticker.price` method):
  - oneOf modified

#### WebSocket Streams

- Modified parameter `contract_type`:
  - enum added: `perpetual`, `current_quarter`, `next_quarter`, `tradifi_perpetual`
  - affected methods:
    - `continuous_contract_kline_candlestick_streams()` (`<pair>_<contractType>@continuousKline_<interval>` stream)
- Modified parameter `interval`:
  - enum added: `1s`, `1m`, `3m`, `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `8h`, `12h`, `1d`, `3d`, `1w`, `1M`
  - affected methods:
    - `continuous_contract_kline_candlestick_streams()` (`<pair>_<contractType>@continuousKline_<interval>` stream)
- Modified parameter `interval`:
  - enum added: `1m`, `3m`, `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `8h`, `12h`, `1d`, `3d`, `1w`, `1M`
  - affected methods:
    - `kline_candlestick_streams()` (`<symbol>@kline_<interval>` stream)
- Modified parameter `levels`:
  - type `integer` → `string`
  - enum added: `5`, `10`, `20`
  - affected methods:
    - `partial_book_depth_streams()` (`<symbol>@depth<levels>@<updateSpeed>` stream)
- Modified parameter `update_speed`:
  - enum added: `1s`
  - affected methods:
    - `mark_price_stream_for_all_market()` (`!markPrice@arr@<updateSpeed>` stream)
    - `mark_price_stream()` (`<symbol>@markPrice@<updateSpeed>` stream)
- Modified parameter `update_speed`:
  - enum added: `100ms`, `500ms`
  - affected methods:
    - `partial_book_depth_streams()` (`<symbol>@depth<levels>@<updateSpeed>` stream)
    - `diff_book_depth_streams()` (`<symbol>@depth@<updateSpeed>` stream)

## 12.0.0 - 2026-06-29

### Changed (15)

#### REST API

- Modified response for `asset_index()` (`GET /fapi/v1/assetIndex`):
  - oneOf added 2 schema(s)
  - oneOf removed 2 schema(s)

#### WebSocket Streams

- Modified response for `all_book_tickers_stream()` (`!bookTicker` stream):
  - property `ps` added
  - property `st` added

- Modified response for `contract_info_stream()` (`!contractInfo` stream):
  - property `st` added
  - property `ps` deleted

- Modified response for `all_market_liquidation_order_streams()` (`!forceOrder@arr` stream):
  - property `st` added
  - property `ps` added

- Modified response for `mark_price_stream_for_all_market()` (`!markPrice@arr@<updateSpeed>` stream):
  - items: property `st` added
  - items: item property `st` added

- Modified response for `all_market_mini_tickers_stream()` (`!miniTicker@arr` stream):
  - items: property `st` added
  - items: property `ps` added
  - items: item property `st` added
  - items: item property `ps` added

- Modified response for `all_market_tickers_streams()` (`!ticker@arr` stream):
  - items: property `ps` added
  - items: property `st` added
  - items: item property `ps` added
  - items: item property `st` added

- Modified response for `aggregate_trade_streams()` (`<symbol>@aggTrade` stream):
  - property `st` added

- Modified response for `individual_symbol_book_ticker_streams()` (`<symbol>@bookTicker` stream):
  - property `st` added
  - property `ps` added

- Modified response for `partial_book_depth_streams()` (`<symbol>@depth<levels>@<updateSpeed>` stream):
  - property `ps` added
  - property `st` added

- Modified response for `diff_book_depth_streams()` (`<symbol>@depth@<updateSpeed>` stream):
  - property `st` added
  - property `ps` added

- Modified response for `mark_price_stream()` (`<symbol>@markPrice@<updateSpeed>` stream):
  - property `st` added

- Modified response for `individual_symbol_mini_ticker_stream()` (`<symbol>@miniTicker` stream):
  - property `ps` added
  - property `st` added

- Modified response for `rpi_diff_book_depth_streams()` (`<symbol>@rpiDepth@500ms` stream):
  - property `st` added
  - property `ps` added

- Modified response for `individual_symbol_ticker_streams()` (`<symbol>@ticker` stream):
  - property `ps` added
  - property `st` added

## 11.0.0 - 2026-06-09

### Changed (11)

- Updated `binance-common` library to version `4.0.0`
- Updated `pyproject.toml` dependencies

#### REST API

- Modified response for `query_algo_order()` (`GET /fapi/v1/algoOrder`):
  - property `actualType` added
  - property `actualQty` added
  - property `slTriggerPrice` deleted
  - property `tpTriggerPrice` deleted
  - property `tpPrice` deleted
  - property `slPrice` deleted

- Modified response for `trading_schedule()` (`GET /fapi/v1/tradingSchedule`):
  - `marketSchedules`: property `KR_EQUITY` added

- Modified response for `compressed_aggregate_trades_list()` (`GET /fapi/v1/aggTrades`):
  - items: property `nq` added
  - items: item property `nq` added

#### WebSocket API

- Deleted parameter `activationPrice`
  - affected methods:
    - `new_order()` (`order.place` method)
- Deleted parameter `callbackRate`
  - affected methods:
    - `new_order()` (`order.place` method)
- Deleted parameter `closePosition`
  - affected methods:
    - `new_order()` (`order.place` method)
- Deleted parameter `priceProtect`
  - affected methods:
    - `new_order()` (`order.place` method)
- Deleted parameter `stopPrice`
  - affected methods:
    - `new_order()` (`order.place` method)
- Deleted parameter `workingType`
  - affected methods:
    - `new_order()` (`order.place` method)

## 10.4.0 - 2026-05-29

### Changed (1)

- Updated `binance-common` library to version `3.10.0`

## 10.3.0 - 2026-05-22

- Updated `binance-common` library to version `3.9.2`
- Updated `pyproject.toml` dependencies

### Changed (1)

#### WebSocket Streams

- Modified response for `Listenkeyexpired`:
  - `E`: type `StrictStr` → `StrictInt`

## 10.2.0 - 2026-04-29

- Updated `binance-common` library to version `3.9.1`
- Updated `pyproject.toml` dependencies

## 10.1.0 - 2026-04-29

### Changed (1)

- Updated `binance-common` library to version `3.9.0`

## 10.0.1 - 2026-04-21

### Changed (2)

#### REST API

- Modified parameter `price` to optional `float` for `modify_order()` (`PUT /fapi/v1/order`)

#### WebSocket API

- Modified parameter `price` to optional `float` for `modify_order()` method (`order.modify`)

## 10.0.0 - 2026-04-20

### Changed (3)

#### REST API

- Deleted parameter `page`
  - affected methods:
    - `query_all_algo_orders()` (`GET /fapi/v1/allAlgoOrders`)
- Modified parameter `interval`:
  - enum added: `1s`
  - affected methods:
    - `continuous_contract_kline_candlestick_data()` (`GET /fapi/v1/continuousKlines`)
    - `index_price_kline_candlestick_data()` (`GET /fapi/v1/indexPriceKlines`)
    - `kline_candlestick_data()` (`GET /fapi/v1/klines`)
    - `mark_price_kline_candlestick_data()` (`GET /fapi/v1/markPriceKlines`)
    - `premium_index_kline_data()` (`GET /fapi/v1/premiumIndexKlines`)
- Modified parameter `limit`:
  - required: `true` → `false`
  - affected methods:
    - `basis()` (`GET /futures/data/basis`)

## 9.1.0 - 2026-03-26

### Changed (4)

- Updated `binance-common` library to version `3.8.0`
- Updated `tox` file

#### WebSocket Streams

- Modified response for `mark_price_stream_for_all_market()` (`!markPrice@arr@<updateSpeed>` stream):
  - items: property `ap` added
  - items: item property `ap` added

- Modified response for `mark_price_stream()` (`<symbol>@markPrice@<updateSpeed>` stream):
  - property `ap` added

## 9.0.0 - 2026-03-16

### Changed (2)

- Updated `binance-common` library to version `3.7.0`

#### REST API

- Modified response for `query_order()` (`GET /fapi/v1/order`):
  - property `priceProtect` added
  - property `type` added
  - property `updateTime` added
  - property `price` added
  - property `avgPrice` added
  - property `closePosition` added
  - property `reduceOnly` added
  - property `timeInForce` added
  - property `time` added
  - property `origType` added
  - property `priceRate` added
  - property `executedQty` added
  - property `origQty` added
  - property `cumQuote` added
  - property `orderId` added
  - property `side` added
  - property `positionSide` added
  - property `symbol` added
  - property `workingType` added
  - property `clientOrderId` added
  - property `stopPrice` added
  - property `activatePrice` added
  - property `id` deleted
  - property `result` deleted
  - `status`: type `integer` → `string`

## 8.0.0 - 2026-03-09

### Changed (2)

#### REST API

- Modified response for `exchange_information()` (`GET /fapi/v1/exchangeInfo`):
  - `symbols`.items: property `orderTypes` added
  - `symbols`.items: property `OrderType` deleted
  - `symbols`.items: item property `orderTypes` added
  - `symbols`.items: item property `OrderType` deleted

- Modified response for `cancel_order()` (`DELETE /fapi/v1/order`):
  - property `avgPrice` removed

## 7.1.1 - 2026-02-25

### Changed (1)

- Updated following response models to remove unused struct:
  - `ContinuousContractKlineCandlestickDataResponse`
  - `IndexPriceKlineCandlestickDataResponse`
  - `KlineCandlestickDataResponse`
  - `MarkPriceKlineCandlestickDataResponse`
  - `PremiumIndexKlineDataResponse`

## 7.1.0 - 2026-02-11

### Changed (3)

- Updated `binance-common` library to version `3.6.0`
- Updated `pyproject.toml` dependencies

#### REST API

- Modified response for `cancel_order()` (`DELETE /fapi/v1/order`):
  - property `avgPrice` deleted

## 7.0.0 - 2026-01-29

### Changed (7)

- Updated `binance-common` library to version `3.5.0`

#### REST API

- Added parameter `newOrderRespType`
  - affected methods:
    - `new_algo_order()` (`POST /fapi/v1/algoOrder`)
- Modified parameter `batchOrders`:
  - items: property `stopPrice` added
  - items: item property `stopPrice` added
  - affected methods:
    - `modify_multiple_orders()` (`PUT /fapi/v1/batchOrders`)
- Modified response for `place_multiple_orders()` (`POST /fapi/v1/batchOrders`):
  - items: property `closePosition` added
  - items: item property `closePosition` added

- Modified response for `query_order()` (`GET /fapi/v1/order`):
  - property `id` added
  - property `result` added
  - property `activatePrice` deleted
  - property `clientOrderId` deleted
  - property `positionSide` deleted
  - property `closePosition` deleted
  - property `updateTime` deleted
  - property `origQty` deleted
  - property `reduceOnly` deleted
  - property `time` deleted
  - property `side` deleted
  - property `priceRate` deleted
  - property `price` deleted
  - property `executedQty` deleted
  - property `priceProtect` deleted
  - property `avgPrice` deleted
  - property `priceMatch` deleted
  - property `stopPrice` deleted
  - property `goodTillDate` deleted
  - property `symbol` deleted
  - property `orderId` deleted
  - property `cumQuote` deleted
  - property `selfTradePreventionMode` deleted
  - property `timeInForce` deleted
  - property `workingType` deleted
  - property `origType` deleted
  - property `type` deleted
  - `status`: type `string` → `integer`

#### WebSocket API

- Added parameter `newOrderRespType`
  - affected methods:
    - `new_algo_order()` (`algoOrder.place` method)
- Modified response for `position_information_v2()` (`v2/account.position` method):
  - `result`.items: property `unRealizedProfit` added
  - `result`.items: property `unrealizedProfit` deleted
  - `result`.items: item property `unRealizedProfit` added
  - `result`.items: item property `unrealizedProfit` deleted

## 6.2.0 - 2026-01-23

### Changed (1)

- Updated `binance-common` library to version `3.4.1`

## 6.1.0 - 2026-01-19

### Changed (10)

#### REST API

- Added parameter `algoId`
  - affected methods:
    - `cancel_algo_order()` (`DELETE /fapi/v1/algoOrder`)
- Added parameter `clientAlgoId`
  - affected methods:
    - `cancel_algo_order()` (`DELETE /fapi/v1/algoOrder`)
- Deleted parameter `algoid`
  - affected methods:
    - `cancel_algo_order()` (`DELETE /fapi/v1/algoOrder`)
- Deleted parameter `clientalgoid`
  - affected methods:
    - `cancel_algo_order()` (`DELETE /fapi/v1/algoOrder`)
- Modified response for `symbol_configuration()` (`GET /fapi/v1/symbolConfig`):
  - items.`isAutoAddMargin`: type `string` → `boolean`
  - items.`isAutoAddMargin`: type `string` → `boolean`

#### WebSocket API

- Updated `Subscribe` method in `websocket.py` to accept optional `stream_url` parameter.

- Added parameter `algoId`
  - affected methods:
    - `cancel_algo_order()` (`algoOrder.cancel` method)
- Added parameter `clientAlgoId`
  - affected methods:
    - `cancel_algo_order()` (`algoOrder.cancel` method)
- Deleted parameter `algoid`
  - affected methods:
    - `cancel_algo_order()` (`algoOrder.cancel` method)
- Deleted parameter `clientalgoid`
  - affected methods:
    - `cancel_algo_order()` (`algoOrder.cancel` method)

## 6.0.0 - 2025-01-13

### Changed (4)

- Updated `binance-common` library to version `3.4.0`

#### WebSocket API

- Added parameter `activatePrice`
  - affected methods:
    - `new_algo_order()` (`algoOrder.place` method)
- Deleted parameter `activationPrice`
  - affected methods:
    - `new_algo_order()` (`algoOrder.place` method)
#### WebSocket Streams

- Modified response for `aggregate_trade_streams()` (`<symbol>@aggTrade` stream):
  - property `nq` added

## 5.0.0 - 2025-12-22

### Added (5)

- Updated `binance-common` library to version `3.3.0`
- Add `Body` to Rest API request

#### REST API

- `futures_tradfi_perps_contract()` (`POST /fapi/v1/stock/contract`)
- `trading_schedule()` (`GET /fapi/v1/tradingSchedule`)
- `rpi_order_book()` (`GET /fapi/v1/rpiDepth`)

#### WebSocket Streams

- `trading_session_stream()` (`tradingSession` stream)
- `rpi_diff_book_depth_streams()` (`<symbol>@rpiDepth@500ms` stream)

### Changed (12)

#### REST API

- Added parameter `activatePrice`
  - affected methods:
    - `new_algo_order()` (`POST /fapi/v1/algoOrder`)
- Deleted parameter `activationPrice`
  - affected methods:
    - `new_algo_order()` (`POST /fapi/v1/algoOrder`)

- Modified parameter `batchOrders`:
  - items: property `stopPrice` deleted
  - items: property `priceProtect` deleted
  - items: property `activationPrice` deleted
  - items: property `callbackRate` deleted
  - items: property `workingType` deleted
  - items: item property `stopPrice` deleted
  - items: item property `priceProtect` deleted
  - items: item property `activationPrice` deleted
  - items: item property `callbackRate` deleted
  - items: item property `workingType` deleted
  - items.`goodTillDate`: type `integer` → `string`
  - items.`price`: type `number` → `string`
  - items.`quantity`: type `number` → `string`
  - items.`goodTillDate`: type `integer` → `string`
  - items.`price`: type `number` → `string`
  - items.`quantity`: type `number` → `string`
  - affected methods:
    - `place_multiple_orders()` (`POST /fapi/v1/batchOrders`)
- Modified parameter `batchOrders`:
  - items.`orderId`: type `integer` → `string`
  - items.`price`: type `number` → `string`
  - items.`quantity`: type `number` → `string`
  - items.`recvWindow`: type `integer` → `string`
  - items.`orderId`: type `integer` → `string`
  - items.`price`: type `number` → `string`
  - items.`quantity`: type `number` → `string`
  - items.`recvWindow`: type `integer` → `string`
  - affected methods:
    - `modify_multiple_orders()` (`PUT /fapi/v1/batchOrders`)

- Deleted parameter `activationPrice`
  - affected methods:
    - `new_order()` (`POST /fapi/v1/order`)
- Deleted parameter `callbackRate`
  - affected methods:
    - `new_order()` (`POST /fapi/v1/order`)
- Deleted parameter `closePosition`
  - affected methods:
    - `new_order()` (`POST /fapi/v1/order`)
- Deleted parameter `priceProtect`
  - affected methods:
    - `new_order()` (`POST /fapi/v1/order`)
- Deleted parameter `stopPrice`
  - affected methods:
    - `new_order()` (`POST /fapi/v1/order`)
- Deleted parameter `workingType`
  - affected methods:
    - `new_order()` (`POST /fapi/v1/order`)
- Modified response for `place_multiple_orders()` (`POST /fapi/v1/batchOrders`):
  - items: property `priceRate` deleted
  - items: property `activatePrice` deleted
  - items: item property `priceRate` deleted
  - items: item property `activatePrice` deleted

- Modified response for `new_order()` (`POST /fapi/v1/order`):
  - property `activatePrice` deleted
  - property `priceRate` deleted

#### WebSocket API

- Modified response for `cancel_algo_order()` (`algoOrder.cancel` method):
  - `result`: property `code` added
  - `result`: property `msg` added
  - `result`: property `positionSide` deleted
  - `result`: property `priceMatch` deleted
  - `result`: property `createTime` deleted
  - `result`: property `price` deleted
  - `result`: property `priceProtect` deleted
  - `result`: property `algoType` deleted
  - `result`: property `selfTradePreventionMode` deleted
  - `result`: property `timeInForce` deleted
  - `result`: property `updateTime` deleted
  - `result`: property `workingType` deleted
  - `result`: property `goodTillDate` deleted
  - `result`: property `symbol` deleted
  - `result`: property `orderType` deleted
  - `result`: property `triggerPrice` deleted
  - `result`: property `algoStatus` deleted
  - `result`: property `triggerTime` deleted
  - `result`: property `icebergQuantity` deleted
  - `result`: property `side` deleted
  - `result`: property `closePosition` deleted
  - `result`: property `reduceOnly` deleted
  - `result`: property `quantity` deleted

## 4.0.0 - 2025-11-24

### Added (1)

#### REST API

- `adl_risk()` (`GET /fapi/v1/symbolAdlRisk`)

### Changed (5)

#### REST API

- Modified parameter `batchOrders`:
  - items.`timeInForce`: enum added: `RPI`
  - items.`timeInForce`: enum added: `RPI`
  - affected methods:
    - `place_multiple_orders()` (`POST /fapi/v1/batchOrders`)
- Modified parameter `timeInForce`:
  - enum added: `RPI`
  - affected methods:
    - `new_algo_order()` (`POST /fapi/v1/algoOrder`)
    - `new_order()` (`POST /fapi/v1/order`)
    - `test_order()` (`POST /fapi/v1/order/test`)
- Modified response for `old_trades_lookup()` (`GET /fapi/v1/historicalTrades`):
  - items: property `isRPITrade` added
  - items: item property `isRPITrade` added

- Modified response for `recent_trades_list()` (`GET /fapi/v1/trades`):
  - items: property `isRPITrade` added
  - items: item property `isRPITrade` added

#### WebSocket API

- Modified parameter `timeInForce`:
  - enum added: `RPI`
  - affected methods:
    - `new_algo_order()` (`algoOrder.place` method)
    - `new_order()` (`order.place` method)

## 3.0.0 - 2025-11-14

### Added (7)

#### REST API

- `cancel_algo_order()` (`DELETE /fapi/v1/algoOrder`)
- `cancel_all_algo_open_orders()` (`DELETE /fapi/v1/algoOpenOrders`)
- `current_all_algo_open_orders()` (`GET /fapi/v1/openAlgoOrders`)
- `new_algo_order()` (`POST /fapi/v1/algoOrder`)
- `query_algo_order()` (`GET /fapi/v1/algoOrder`)
- `query_all_algo_orders()` (`GET /fapi/v1/allAlgoOrders`)
- Marked `symbol_price_ticker` (`GET /fapi/v1/ticker/price`) as deprecated.

## 2.0.0 - 2025-10-27

### Changed (1)

#### WebSocket Streams

- Modified User Data Streams response for `OrderTradeUpdateO`:
  - `er` added 

## 1.8.0 - 2025-10-10

### Changed (4)

- Updated `binance-common` library to version `3.2.0`

#### REST API

- Fixed typo for endpoints response `GET /fapi/v1/depth` and `GET /fapi/v1/aggTrades`

#### WebSocket API

- Fixed typo for endpoint response `depth`

#### WebSocket Streams

- Fixed typo for user data stream events response `account_update`

## 1.7.0 - 2025-09-24

### Changed (2)

- Modified response for `notional_and_leverage_brackets` (`GET /fapi/v1/leverageBracket`)
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

## 1.1.0 - 2025-08-06

### Changed (5)

- Updated `binance-common` library to version `1.1.0`
- Changed models responses to handle upper and lower case parameters
- Added python version `3.13`

#### WebSocket Streams

- Changed `list_subscribe` to return `dict` response
- Fixed`user_data`

## 1.0.0 - 2025-07-17

- Initial release
