from binance.api import API
from binance.lib.utils import check_required_parameter


class Trade(API):

    """ class Trade for Order, Trade, Account endpoints that require signature
    Margin, Lending or sub-account is not included, will be a separate class handling each of them.

    """

    def __init__(self, key, secret, **kwargs):
        super(Trade, self).__init__(key, secret, **kwargs)

    def new_order_test(self, **kwargs):
        """ Test New Order (TRADE)

        Test new order creation and signature/recvWindow long. Creates and validates a new order but does not send it into the matching engine.

        POST /api/v3/order/test

        https://binance-docs.github.io/apidocs/spot/en/#test-new-order-trade
        """

        url_path = '/api/v3/order/test'
        return self.sign_request('POST', url_path, {**kwargs})

    def new_order(self, **kwargs):
        """ New OCO (TRADE)

        Post a new order

        POST /api/v3/order

        https://binance-docs.github.io/apidocs/spot/en/#new-order-trade
        """

        url_path = '/api/v3/order'
        return self.sign_request('POST', url_path, {**kwargs})

    def cancel_order(self, symbol: str, **kwargs):
        """ Cancel Order (TRADE)

        Cancel an active order.

        DELETE /api/v3/order

        https://binance-docs.github.io/apidocs/spot/en/#cancel-order-trade
        """
        check_required_parameter(symbol, 'symbol')

        url_path = '/api/v3/order'
        payload = {'symbol': symbol, **kwargs}
        return self.sign_request('DELETE', url_path, payload)

    def cancel_open_orders(self, symbol, **kwargs):
        """ Cancel all Open Orders on a Symbol (TRADE)

        Cancels all active orders on a symbol.
        This includes OCO orders.

        DELETE api/v3/openOrders

        https://binance-docs.github.io/apidocs/spot/en/#cancel-all-open-orders-on-a-symbol-trade
        """
        check_required_parameter(symbol, 'symbol')

        url_path = '/api/v3/openOrders'
        payload = {'symbol': symbol, **kwargs}
        return self.sign_request('DELETE', url_path, payload)

    def get_order(self, symbol, **kwargs):
        """ Query Order (USER_DATA)

        Check an order's status.

        GET /api/v3/order

        https://binance-docs.github.io/apidocs/spot/en/#query-order-user_data
        """
        check_required_parameter(symbol, 'symbol')

        url_path = '/api/v3/order'
        payload = {'symbol': symbol, **kwargs}
        return self.sign_request('GET', url_path, payload)

    def get_open_orders(self, symbol=None, **kwargs):
        """ Current Open Orders (USER_DATA)

        Get all open orders on a symbol.

        GET /api/v3/openOrders

        https://binance-docs.github.io/apidocs/spot/en/#current-open-orders-user_data
        """

        url_path = '/api/v3/openOrders'
        payload = {'symbol': symbol, **kwargs}
        return self.sign_request('GET', url_path, payload)

    def get_orders(self, symbol: str, **kwargs):
        """ All Orders (USER_DATA)

        Get all account orders; active, canceled, or filled.

        GET /api/v3/allOrders

        https://binance-docs.github.io/apidocs/spot/en/#all-orders-user_data
        """
        check_required_parameter(symbol, 'symbol')

        url_path = '/api/v3/allOrders'
        payload = {'symbol': symbol, **kwargs}
        return self.sign_request('GET', url_path, payload)

    def new_oco_order(self, **kwargs):
        """ New OCO (TRADE)

        Post a new oco order

        POST /api/v3/order/oco

        https://binance-docs.github.io/apidocs/spot/en/#new-oco-trade
        """

        url_path = '/api/v3/order/oco'
        return self.sign_request('POST', url_path, {**kwargs})

    def cancel_oco_order(self, symbol, **kwargs):
        """ Cancel OCO (TRADE)

        Cancel an entire Order List

        DELETE /api/v3/orderList

        https://binance-docs.github.io/apidocs/spot/en/#cancel-oco-trade
        """
        check_required_parameter(symbol, 'symbol')

        url_path = '/api/v3/orderList'
        payload = {'symbol': symbol, **kwargs}
        return self.sign_request('DELETE', url_path, payload)

    def get_oco_order(self, **kwargs):
        """ Query OCO (USER_DATA)

       Retrieves a specific OCO based on provided optional parameters

        GET /api/v3/orderList

        https://binance-docs.github.io/apidocs/spot/en/#query-oco-user_data
        """
        url_path = '/api/v3/orderList'
        return self.sign_request('GET', url_path, {**kwargs})

    def get_oco_orders(self, **kwargs):
        """ Query all OCO (USER_DATA)

        Retrieves all OCO based on provided optional parameters

        GET /api/v3/allOrderList

        https://binance-docs.github.io/apidocs/spot/en/#query-all-oco-user_data
        """

        url_path = '/api/v3/allOrderList'
        return self.sign_request('GET', url_path, {**kwargs})

    def get_oco_open_orders(self, **kwargs):
        """ Query Open OCO (USER_DATA)

        GET /api/v3/openOrderList

        https://binance-docs.github.io/apidocs/spot/en/#query-open-oco-user_data
        """

        url_path = '/api/v3/openOrderList'
        return self.sign_request('GET', url_path, {**kwargs})

    def account(self, **kwargs):
        """ Account Information (USER_DATA)

        Get current account information

        GET /api/v3/account

        https://binance-docs.github.io/apidocs/spot/en/#account-information-user_data
        """

        url_path = '/api/v3/account'
        return self.sign_request('GET', url_path, {**kwargs})

    def my_trades(self, symbol: str, **kwargs):
        """ Account Trade List (USER_DATA)

        Get trades for a specific account and symbol.

        GET /api/v3/myTrades

        https://binance-docs.github.io/apidocs/spot/en/#account-trade-list-user_data
        """

        check_required_parameter(symbol, 'symbol')

        url_path = '/api/v3/myTrades'
        payload = {'symbol': symbol, **kwargs}
        return self.sign_request('GET', url_path, payload)
