from binance.api import API

class Trade(API):

    """ class Trade for Order, Trade, Account endpoints that require signature
    Margin, Lending or sub-account is not included, will be a separate class handling each of them.

    """

    def __init__(self, key, secret, **kwargs):
        super(Trade, self).__init__(key, secret, **kwargs)

    def account(self):
        """ Account Information (USER_DATA)

        Get current account information

        GET /api/v3/account

        https://binance-docs.github.io/apidocs/spot/en/#account-information-user_data
        """

        urlPath = '/api/v3/account'
        return self.sign_request('GET', urlPath)

    #  def my_trades(self, symbol: str, **kargs):
