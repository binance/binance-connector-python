from binance.api import API
from binance.lib.utils import check_required_parameter

class Trade(API):

    """ class Trade for Order, Trade, Account endpoints that require signature
    Margin, Lending or sub-account is not included, will be a separate class handling each of them.

    """

    def __init__(self, key, secret, **kwargs):
        super(Trade, self).__init__(key, secret, **kwargs)

    def cancel_order(self, symbol, **kwargs):
        check_required_parameter(symbol, 'symbol')

        url_path = '/api/v3/order'
        payload = {'symbol': symbol, **kwargs}
        return self.sign_request('DELETE', url_path, payload)

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
