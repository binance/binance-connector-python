from binance.api import API


class Futures(API):
    def __init__(self, key=None, secret=None, **kwargs):
        if "base_url" not in kwargs:
            kwargs["base_url"] = "https://fapi.binance.com"
        super().__init__(key, secret, **kwargs)

    # MARKETS
    from binance.futures.market import ping
    from binance.futures.market import time
    from binance.futures.market import exchange_info
    from binance.futures.market import depth
    from binance.futures.market import trades
    from binance.futures.market import historical_trades
    from binance.futures.market import agg_trades
    from binance.futures.market import klines
    from binance.futures.market import continuous_klines
    from binance.futures.market import index_price_klines
    from binance.futures.market import mark_price_klines
    from binance.futures.market import mark_price
    from binance.futures.market import funding_rate_history
    from binance.futures.market import ticker_24hr
    from binance.futures.market import ticker_price
    from binance.futures.market import book_ticker
    from binance.futures.market import open_interest
    from binance.futures.market import open_interest_statistics
    from binance.futures.market import top_trader_accounts
    from binance.futures.market import top_trader_positions
    from binance.futures.market import ratio
    from binance.futures.market import taker_volume
    from binance.futures.market import historical_blvt_nav_kline
    from binance.futures.market import composite_index

    # ACCOUNT(including orders and trades)
    from binance.futures.account import change_position_side
    from binance.futures.account import position_side
    from binance.futures.account import change_multi_assets_margin
    from binance.futures.account import get_multi_assets_margin
    from binance.futures.account import new_order
    from binance.futures.account import new_batch_orders
    from binance.futures.account import get_order
    from binance.futures.account import cancel_order
    from binance.futures.account import cancel_all_orders
    from binance.futures.account import cancel_batch_orders
    from binance.futures.account import auto_cancel_all
    from binance.futures.account import get_open_order
    from binance.futures.account import get_open_orders
    from binance.futures.account import get_all_orders
    from binance.futures.account import balance
    from binance.futures.account import account
    from binance.futures.account import change_leverage
    from binance.futures.account import change_margin
    from binance.futures.account import change_position_margin
    from binance.futures.account import margin_position_history
    from binance.futures.account import risk
    from binance.futures.account import trades
    from binance.futures.account import income
    from binance.futures.account import brackets
    from binance.futures.account import adl_quantile
    from binance.futures.account import force_orders
    from binance.futures.account import status
    from binance.futures.account import commission

