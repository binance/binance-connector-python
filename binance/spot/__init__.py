from binance.api import API

class Spot(API):

    # MARKETS
    from binance.spot.apis import ping
    from binance.spot.apis import time
    from binance.spot.apis import exchange_info
    from binance.spot.apis import depth
    from binance.spot.apis import trades
    from binance.spot.apis import historical_trades
    from binance.spot.apis import agg_trades
    from binance.spot.apis import klines
    from binance.spot.apis import avg_price
    from binance.spot.apis import ticker_24hr
    from binance.spot.apis import ticker_price
    from binance.spot.apis import book_ticker

    # USER_DATA or TRADES
    from binance.spot.apis import new_order_test
    from binance.spot.apis import new_order
    from binance.spot.apis import cancel_order
    from binance.spot.apis import cancel_open_orders
    from binance.spot.apis import get_order
    from binance.spot.apis import get_open_orders
    from binance.spot.apis import get_orders
    from binance.spot.apis import new_oco_order
    from binance.spot.apis import cancel_oco_order
    from binance.spot.apis import get_oco_order
    from binance.spot.apis import get_oco_orders
    from binance.spot.apis import get_oco_open_orders
    from binance.spot.apis import account
    from binance.spot.apis import my_trades

    # STREAMS
    from binance.spot.apis import new_listen_key
    from binance.spot.apis import renew_listen_key
    from binance.spot.apis import close_listen_key

    # MARGIN
    from binance.spot.margin import margin_transfer
