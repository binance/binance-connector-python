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

