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
    from binance.spot.margin import margin_borrow
    from binance.spot.margin import margin_repay
    from binance.spot.margin import margin_asset
    from binance.spot.margin import margin_pair
    from binance.spot.margin import margin_all_assets
    from binance.spot.margin import margin_all_pairs
    from binance.spot.margin import margin_pair_index
    from binance.spot.margin import new_margin_order
    from binance.spot.margin import cancel_margin_order
    from binance.spot.margin import margin_transfer_history
    from binance.spot.margin import margin_load_record
    from binance.spot.margin import margin_repay_record
    from binance.spot.margin import margin_interest_history
    from binance.spot.margin import margin_force_liquidation_record
    from binance.spot.margin import margin_account
    from binance.spot.margin import margin_order
    from binance.spot.margin import margin_open_orders
    from binance.spot.margin import margin_all_orders
    from binance.spot.margin import margin_my_trades
    from binance.spot.margin import margin_max_borrowable
    from binance.spot.margin import margin_max_transferable
