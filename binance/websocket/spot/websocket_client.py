from binance.websocket.websocket_client import BinanceWebsocketClient


class SpotWebsocketClient(BinanceWebsocketClient):
    def __init__(self, stream_url="wss://stream.binance.com:9443"):
        super().__init__(stream_url)

    def agg_trade(self, symbol: str, id: int, callback, **kwargs):
        """Aggregate Trade Streams

        The Aggregate Trade Streams push trade information that is aggregated for a single taker order.

        Stream Name: <symbol>@aggTrade

        Update Speed: Real-time
        """
        self.live_subscribe(
            "{}@aggTrade".format(symbol.lower()), id, callback, **kwargs
        )

    def trade(self, symbol: str, id: int, callback, **kwargs):
        """Trade Streams

        The Trade Streams push raw trade information; each trade has a unique buyer and seller.

        Stream Name: <symbol>@trade

        Update Speed: Real-time
        """
        self.live_subscribe("{}@trade".format(symbol.lower()), id, callback, **kwargs)

    def kline(self, symbol: str, id: int, interval: str, callback, **kwargs):
        """Kline/Candlestick Streams

        The Kline/Candlestick Stream push updates to the current klines/candlestick every second.

        Stream Name: <symbol>@kline_<interval>

        interval:
        m -> minutes; h -> hours; d -> days; w -> weeks; M -> months

        - 1m
        - 3m
        - 5m
        - 15m
        - 30m
        - 1h
        - 2h
        - 4h
        - 6h
        - 8h
        - 12h
        - 1d
        - 3d
        - 1w
        - 1M

        Update Speed: 2000ms
        """

        self.live_subscribe(
            "{}@kline_{}".format(symbol.lower(), interval), id, callback, **kwargs
        )

    def mini_ticker(self, id: int, callback, symbol=None, **kwargs):
        """Individual symbol or all symbols mini ticker

        24hr rolling window mini-ticker statistics.
        These are NOT the statistics of the UTC day, but a 24hr rolling window for the previous 24hrs

        Stream Name: <symbol>@miniTicker or
        Stream Name: !miniTicker@arr

        Update Speed: 1000ms
        """

        if symbol is None:
            self.live_subscribe("!miniTicker@arr", id, callback, **kwargs)
        else:
            self.live_subscribe(
                "{}@miniTicker".format(symbol.lower()), id, callback, **kwargs
            )

    def ticker(self, id: int, callback, symbol=None, **kwargs):
        """Individual symbol or all symbols ticker

        24hr rolling window ticker statistics for a single symbol.
        These are NOT the statistics of the UTC day, but a 24hr rolling window for the previous 24hrs.

        Stream Name: <symbol>@ticker or
        Stream Name: !ticker@arr

        Update Speed: 1000ms
        """

        if symbol is None:
            self.live_subscribe("!ticker@arr", id, callback, **kwargs)
        else:
            self.live_subscribe(
                "{}@ticker".format(symbol.lower()), id, callback, **kwargs
            )

    def book_ticker(self, id: int, callback, symbol=None, **kwargs):
        """Individual symbol or all book ticker

        Pushes any update to the best bid or ask's price or quantity in real-time for a specified symbol.

        Stream Name: <symbol>@bookTicker or
        Stream Name: !bookTicker

        Update Speed: realtime
        """

        if symbol is None:
            self.live_subscribe("!bookTicker", id, callback, **kwargs)
        else:
            self.live_subscribe(
                "{}@bookTicker".format(symbol.lower()), id, callback, **kwargs
            )

    def partial_book_depth(
        self, symbol: str, id: int, level, speed, callback, **kwargs
    ):
        """Partial Book Depth Streams

        Top bids and asks, Valid are 5, 10, or 20.

        Stream Names: <symbol>@depth<levels> OR <symbol>@depth<levels>@100ms.

        Update Speed: 1000ms or 100ms
        """
        self.live_subscribe(
            "{}@depth{}@{}ms".format(symbol.lower(), level, speed),
            id,
            callback,
            **kwargs
        )

    def diff_book_depth(self, symbol: str, id: int, speed, callback, **kwargs):
        """Diff. Depth Stream

        Stream Name: <symbol>@depth OR <symbol>@depth@100ms

        Update Speed: 1000ms or 100ms

        Order book price and quantity depth updates used to locally manage an order book.
        """
        self.live_subscribe(
            "{}@depth@{}ms".format(symbol.lower(), speed), id, callback, **kwargs
        )

    def user_data(self, listen_key: str, id: int, callback, **kwargs):
        """listen to user data by provided listenkey"""
        self.live_subscribe(listen_key, id, callback, **kwargs)
