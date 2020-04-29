from binance.api import API
from binance.lib.utils import check_required_parameter

class Trade(API):

    """ class Trade for Order, Trade, Account endpoints that require signature
    Margin, Lending or sub-account is not included, will be a separate class handling each of them.

    """

    def __init__(self, key, secret, **kwargs):
        super(Trade, self).__init__(key, secret, **kwargs)

    def cancel_order(self, symbol, **kwargs):
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

    def get_orders(self, symbol=None, **kwargs):
        """ All Orders (USER_DATA)

        Get all account orders; active, canceled, or filled.

        GET /api/v3/allOrders

        https://binance-docs.github.io/apidocs/spot/en/#all-orders-user_data
        """
        check_required_parameter(symbol, 'symbol')

        url_path = '/api/v3/allOrders'
        payload = {'symbol': symbol, **kwargs}
        return self.sign_request('GET', url_path, payload)

    def get_oco_order(self, **kwargs):
        """ Query OCO (USER_DATA)

       Retrieves a specific OCO based on provided optional parameters

        GET /api/v3/orderList

        https://binance-docs.github.io/apidocs/spot/en/#query-oco-user_data
        """
        url_path = '/api/v3/orderList'
        payload = {**kwargs}
        return self.sign_request('GET', url_path, payload)

    def account(self):
        """ Account Information (USER_DATA)

        Get current account information

        GET /api/v3/account

        https://binance-docs.github.io/apidocs/spot/en/#account-information-user_data
        """

        url_path = '/api/v3/account'
        return self.sign_request('GET', url_path)

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
