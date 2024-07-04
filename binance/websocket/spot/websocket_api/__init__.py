from typing import Optional

from binance.websocket.websocket_client import BinanceWebsocketClient


class SpotWebsocketAPIClient(BinanceWebsocketClient):
    def __init__(
        self,
        stream_url="wss://ws-api.binance.com/ws-api/v3",
        api_key=None,
        api_secret=None,
        on_message=None,
        on_open=None,
        on_close=None,
        on_error=None,
        on_ping=None,
        on_pong=None,
        timeout=None,
        logger=None,
        proxies: Optional[dict] = None,
    ):
        self.api_key = api_key
        self.api_secret = api_secret

        super().__init__(
            stream_url,
            on_message=on_message,
            on_open=on_open,
            on_close=on_close,
            on_error=on_error,
            on_ping=on_ping,
            on_pong=on_pong,
            logger=logger,
            timeout=timeout,
            proxies=proxies,
        )

    # Market
    from binance.websocket.spot.websocket_api._market import ping_connectivity
    from binance.websocket.spot.websocket_api._market import server_time
    from binance.websocket.spot.websocket_api._market import exchange_info
    from binance.websocket.spot.websocket_api._market import order_book
    from binance.websocket.spot.websocket_api._market import recent_trades
    from binance.websocket.spot.websocket_api._market import historical_trades
    from binance.websocket.spot.websocket_api._market import aggregate_trades
    from binance.websocket.spot.websocket_api._market import klines
    from binance.websocket.spot.websocket_api._market import ui_klines
    from binance.websocket.spot.websocket_api._market import avg_price
    from binance.websocket.spot.websocket_api._market import ticker_24hr
    from binance.websocket.spot.websocket_api._market import ticker
    from binance.websocket.spot.websocket_api._market import ticker_price
    from binance.websocket.spot.websocket_api._market import ticker_book

    # Account
    from binance.websocket.spot.websocket_api._account import account
    from binance.websocket.spot.websocket_api._account import order_rate_limit
    from binance.websocket.spot.websocket_api._account import order_history
    from binance.websocket.spot.websocket_api._account import oco_history
    from binance.websocket.spot.websocket_api._account import my_trades
    from binance.websocket.spot.websocket_api._account import prevented_matches

    # Trade
    from binance.websocket.spot.websocket_api._trade import new_order
    from binance.websocket.spot.websocket_api._trade import new_order_test
    from binance.websocket.spot.websocket_api._trade import get_order
    from binance.websocket.spot.websocket_api._trade import cancel_order
    from binance.websocket.spot.websocket_api._trade import cancel_replace_order
    from binance.websocket.spot.websocket_api._trade import get_open_orders
    from binance.websocket.spot.websocket_api._trade import cancel_open_orders
    from binance.websocket.spot.websocket_api._trade import new_oco_order
    from binance.websocket.spot.websocket_api._trade import new_oto_order
    from binance.websocket.spot.websocket_api._trade import new_otoco_order
    from binance.websocket.spot.websocket_api._trade import get_oco_order
    from binance.websocket.spot.websocket_api._trade import cancel_oco_order
    from binance.websocket.spot.websocket_api._trade import get_open_oco_orders

    # User Data Stream
    from binance.websocket.spot.websocket_api._user_data import user_data_start
    from binance.websocket.spot.websocket_api._user_data import user_data_ping
    from binance.websocket.spot.websocket_api._user_data import user_data_stop
