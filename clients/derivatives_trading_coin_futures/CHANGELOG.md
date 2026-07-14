# Changelog

## 8.0.0 - 2026-07-14

### Added (1)

#### WebSocket Streams

- `index_price_stream()` (`<pair>@indexPrice@<updateSpeed>` stream)

### Changed (25)

- Updated `binance-common` library to version `4.0.3`

#### REST API

- Modified parameter `batch_orders`:
  - items: required added: `symbol`, `side`, `type`, `quantity`
  - items.`activation_price`: type `string` → `number`
  - items.`callback_rate`: type `string` → `number`
  - items.`price`: type `string` → `number`
  - items.`price_match`: enum removed: `NONE`
  - items.`price_protect`: enum added: `true`, `false`
  - items.`quantity`: type `string` → `number`
  - items.`reduce_only`: enum added: `true`, `false`
  - items.`self_trade_prevention_mode`: enum removed: `NONE`
  - items.`stop_price`: type `string` → `number`
  - items.`activation_price`: type `string` → `number`
  - items.`callback_rate`: type `string` → `number`
  - items.`price`: type `string` → `number`
  - items.`price_match`: enum removed: `NONE`
  - items.`price_protect`: enum added: `true`, `false`
  - items.`quantity`: type `string` → `number`
  - items.`reduce_only`: enum added: `true`, `false`
  - items.`self_trade_prevention_mode`: enum removed: `NONE`
  - items.`stop_price`: type `string` → `number`
  - affected methods:
    - `place_multiple_orders()` (`POST /dapi/v1/batchOrders`)
- Modified parameter `batch_orders`:
  - items: required added: `side`, `timestamp`, `symbol`
  - items: property `timestamp` added
  - items.`orderId`: type `string` → `integer`
  - items.`price`: type `string` → `number`
  - items.`quantity`: type `string` → `number`
  - items.`recv_window`: type `string` → `integer`
  - items: item property `timestamp` added
  - items.`orderId`: type `string` → `integer`
  - items.`price`: type `string` → `number`
  - items.`quantity`: type `string` → `number`
  - items.`recv_window`: type `string` → `integer`
  - affected methods:
    - `modify_multiple_orders()` (`PUT /dapi/v1/batchOrders`)
- Modified parameter `contractType`:
  - enum removed: `CURRENT_QUARTER_DELIVERING`, `NEXT_QUARTER_DELIVERING`, `PERPETUAL_DELIVERING`
  - affected methods:
    - `continuous_contract_kline_candlestick_data()` (`GET /dapi/v1/continuousKlines`)
    - `basis()` (`GET /futures/data/basis`)
- Modified parameter `contract_type`:
  - enum removed: `CURRENT_QUARTER_DELIVERING`, `NEXT_QUARTER_DELIVERING`, `PERPETUAL_DELIVERING`
  - enum added: `ALL`
  - affected methods:
    - `open_interest_statistics()` (`GET /futures/data/openInterestHist`)
    - `taker_buy_sell_volume()` (`GET /futures/data/takerBuySellVol`)
- Modified parameter `income_type`:
  - enum added: `TRANSFER`, `WELCOME_BONUS`, `FUNDING_FEE`, `REALIZED_PNL`, `COMMISSION`, `INSURANCE_CLEAR`, `DELIVERED_SETTELMENT`
  - affected methods:
    - `get_income_history()` (`GET /dapi/v1/income`)
- Modified parameter `order_id_list`:
  - maxItems `null` → `10`
  - affected methods:
    - `cancel_multiple_orders()` (`DELETE /dapi/v1/batchOrders`)
- Modified parameter `orig_client_order_id_list`:
  - maxItems `null` → `10`
  - affected methods:
    - `cancel_multiple_orders()` (`DELETE /dapi/v1/batchOrders`)
- Modified parameter `price_match`:
  - enum removed: `NONE`
  - affected methods:
    - `new_order()` (`POST /dapi/v1/order`)
    - `modify_order()` (`PUT /dapi/v1/order`)
- Modified parameter `price_protect`:
  - enum added: `true`, `false`
  - affected methods:
    - `new_order()` (`POST /dapi/v1/order`)
- Modified parameter `reduce_only`:
  - enum added: `true`, `false`
  - affected methods:
    - `new_order()` (`POST /dapi/v1/order`)
- Modified parameter `type`:
  - type `string` → `integer`
  - enum removed: `LIMIT`, `MARKET`, `STOP`, `STOP_MARKET`, `TAKE_PROFIT`, `TAKE_PROFIT_MARKET`, `TRAILING_STOP_MARKET`
  - affected methods:
    - `modify_isolated_position_margin()` (`POST /dapi/v1/positionMargin`)
- Modified response for `place_multiple_orders()` (`POST /dapi/v1/batchOrders`):
  - items: property `close_position` added
  - items: item property `close_position` added

- Modified response for `order_book()` (`GET /dapi/v1/depth`):
  - `asks`.items: minItems `0` → `2`
  - `asks`.items: maxItems `null` → `2`
  - `bids`.items: minItems `0` → `2`
  - `bids`.items: maxItems `null` → `2`

- Modified response for `mark_price_kline_candlestick_data()` (`GET /dapi/v1/markPriceKlines`):
  - items.items: oneOf added 2 schema(s)
  - items.items: oneOf removed 2 schema(s)

#### WebSocket API

- Modified parameter `close_position`:
  - enum added: `true`, `false`
  - affected methods:
    - `new_order()` (`order.place` method)
- Modified parameter `price_match`:
  - enum removed: `NONE`
  - affected methods:
    - `modify_order()` (`order.modify` method)
    - `new_order()` (`order.place` method)
- Modified parameter `price_protect`:
  - enum added: `true`, `false`
  - affected methods:
    - `new_order()` (`order.place` method)
- Modified parameter `reduce_only`:
  - enum added: `true`, `false`
  - affected methods:
    - `new_order()` (`order.place` method)
- Modified response for `query_order()` (`order.status` method):
  - `result`: property `cumQty` added

#### WebSocket Streams

- Modified parameter `contract_type`:
  - enum added: `perpetual`, `current_quarter`, `next_quarter`
  - affected methods:
    - `continuous_contract_kline_candlestick_streams()` (`<pair>_<contractType>@continuousKline_<interval>` stream)
- Modified parameter `interval`:
  - enum added: `1m`, `3m`, `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `8h`, `12h`, `1d`, `3d`, `1w`, `1M`
  - affected methods:
    - `index_kline_candlestick_streams()` (`<pair>@indexPriceKline_<interval>` stream)
    - `continuous_contract_kline_candlestick_streams()` (`<pair>_<contractType>@continuousKline_<interval>` stream)
    - `kline_candlestick_streams()` (`<symbol>@kline_<interval>` stream)
    - `mark_price_kline_candlestick_streams()` (`<symbol>@markPriceKline_<interval>` stream)
- Modified parameter `levels`:
  - type `integer` → `string`
  - enum added: `5`, `10`, `20`
  - affected methods:
    - `partial_book_depth_streams()` (`<symbol>@depth<levels>@<updateSpeed>` stream)
- Modified parameter `updateSpeed`:
  - enum added: `1s`
  - affected methods:
    - `mark_price_of_all_symbols_of_a_pair()` (`<pair>@markPrice@<updateSpeed>` stream)
    - `mark_price_stream()` (`<symbol>@markPrice@<updateSpeed>` stream)
- Modified parameter `updateSpeed`:
  - enum added: `100ms`, `500ms`
  - affected methods:
    - `partial_book_depth_streams()` (`<symbol>@depth<levels>@<updateSpeed>` stream)
    - `diff_book_depth_streams()` (`<symbol>@depth@<updateSpeed>` stream)

### Removed (1)

#### WebSocket Streams

- `/<pair>@index_price()` (`<pair>@indexPrice` stream)

## 7.0.0 - 2026-06-30

### Changed (1)

#### REST API

- Modified response for `query_index_price_constituents()` (`GET /dapi/v1/constituents`):
  - `constituents`.items: property `price` added
  - `constituents`.items: property `weight` added
  - `constituents`.items: item property `price` added
  - `constituents`.items: item property `weight` added

## 6.0.0 - 2026-06-29

### Changed (13)

#### WebSocket Streams

- Modified response for `all_book_tickers_stream()` (`!bookTicker` stream):
  - property `st` added

- Modified response for `contract_info_stream()` (`!contractInfo` stream):
  - property `st` added

- Modified response for `all_market_liquidation_order_streams()` (`!forceOrder@arr` stream):
  - property `st` added

- Modified response for `all_market_mini_tickers_stream()` (`!miniTicker@arr` stream):
  - items: property `st` added
  - items: item property `st` added

- Modified response for `all_market_tickers_streams()` (`!ticker@arr` stream):
  - items: property `st` added
  - items: item property `st` added

- Modified response for `aggregate_trade_streams()` (`<symbol>@aggTrade` stream):
  - property `st` added

- Modified response for `individual_symbol_book_ticker_streams()` (`<symbol>@bookTicker` stream):
  - property `st` added

- Modified response for `partial_book_depth_streams()` (`<symbol>@depth<levels>@<updateSpeed>` stream):
  - property `st` added

- Modified response for `diff_book_depth_streams()` (`<symbol>@depth@<updateSpeed>` stream):
  - property `st` added

- Modified response for `mark_price_stream()` (`<symbol>@markPrice@<updateSpeed>` stream):
  - property `st` added

- Modified response for `individual_symbol_mini_ticker_stream()` (`<symbol>@miniTicker` stream):
  - property `st` added

- Modified response for `individual_symbol_ticker_streams()` (`<symbol>@ticker` stream):
  - property `st` added

- Modified response for `mark_price_of_all_symbols_of_a_pair()` (`<pair>@markPrice@<updateSpeed>` stream):
  - items: property `st` added
  - items: item property `st` added

## 5.7.0 - 2026-06-09

### Changed (2)

- Updated `binance-common` library to version `4.0.0`
- Updated `pyproject.toml` dependencies

## 5.6.0 - 2026-05-29

### Changed (1)

- Updated `binance-common` library to version `3.10.0`

## 5.5.0 - 2026-05-22

- Updated `binance-common` library to version `3.9.2`
- Updated `pyproject.toml` dependencies

## 5.4.0 - 2026-04-29

- Updated `binance-common` library to version `3.9.1`
- Updated `pyproject.toml` dependencies

## 5.3.0 - 2026-04-29

### Changed (1)

- Updated `binance-common` library to version `3.9.0`

## 5.2.0 - 2026-03-26

### Added (1)

- Added `py.typed` file to indicate that the package supports type hints.

### Changed (2)

- Updated `binance-common` library to version `3.8.0`
- Updated `tox` file

## 5.1.0 - 2026-03-16

### Changed (1)

- Updated `binance-common` library to version `3.7.0`

## 5.0.0 - 2026-03-09

### Changed (1)

#### REST API

- Modified response for `exchange_information()` (`GET /dapi/v1/exchangeInfo`):
  - `symbols`.items: property `orderTypes` added
  - `symbols`.items: property `OrderType` deleted
  - `symbols`.items: item property `orderTypes` added
  - `symbols`.items: item property `OrderType` deleted

## 4.1.1 - 2026-02-25

### Changed (1)

- Updated following response models to remove unused struct:
  - `ContinuousContractKlineCandlestickDataResponse`
  - `IndexPriceKlineCandlestickDataResponse`
  - `KlineCandlestickDataResponseItem`
  - `MarkPriceKlineCandlestickDataResponse`
  - `PremiumIndexKlineDataResponse`

## 4.1.0 - 2026-02-11

### Changed (2)

- Updated `binance-common` library to version `3.6.0`
- Updated `pyproject.toml` dependencies

## 4.0.0 - 2026-01-29

### Changed (3)

- Updated `binance-common` library to version `3.5.0`

#### REST API

- Modified response for `cancel_multiple_orders()` (`DELETE /dapi/v1/batchOrders`):
  - items: property `pair` added
  - items: item property `pair` added

- Modified response for `current_all_open_orders()` (`GET /dapi/v1/openOrders`):
  - items: property `pair` added
  - items: item property `pair` added

## 3.3.0 - 2026-01-23

### Changed (1)

- Updated `binance-common` library to version `3.4.1`

## 3.2.0 - 2026-01-19

### Changed (1)

- Updated `Subscribe` method in `websocket.py` to accept optional `stream_url` parameter.

## 3.1.0 - 2026-01-13

### Changed (1)

- Updated `binance-common` library to version `3.4.0`

## 3.0.0 - 2025-12-22

### Changed (3)

- Updated `binance-common` library to version `3.3.0`
- Add `Body` to Rest API request

#### REST API

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
    - `modify_multiple_orders()` (`PUT /dapi/v1/batchOrders`)

## 2.5.0 - 2025-10-10

### Changed (4)

- Updated `binance-common` library to version `3.2.0`

#### REST API

- Fixed typo for endpoint response `GET /dapi/v1/depth`

- Modified response for `query_order()` (`GET /dapi/v1/order`):
  - property `position_side` added

#### WebSocket Streams

- Fixed typo for user data stream events response `account_update`

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

### Changed (1)

- Updated `binance-common` library to version `3.0.0`

## 2.0.0 - 2025-08-22

### Changed (3)

- Standardized type hints for required parameters by replacing `default = None` annotations with `Union[..., None]`

#### REST API

- Modified response for `exchange_information()` method (`GET /dapi/v1/exchangeInfo`):
  - `symbols`.`filters`.`multiplierDecimal`: type `integer` → `string`

#### WebSocket Streams

- Updated Websocket Streams response type to `RequestStreamHandle`

## 1.2.0 - 2025-08-07

### Changed (1)

- Updated `binance-common` library to version `1.2.0`

## 1.1.0 - 2025-08-06

### Changed (4)

- Updated `binance-common` library to version `1.1.0`
- Changed models responses to handle upper and lower case parameters
- Added python version `3.13`

#### WebSocket Streams

- Changed `list_subscribe` to return `dict` response

## 1.0.0 - 2025-07-17

- Initial release
