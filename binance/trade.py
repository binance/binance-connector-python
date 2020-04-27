from binance.api import API

class Trade(API):

    def __init__(self, key, secret, **kwargs):
        super(Trade, self).__init__(key, secret, **kwargs)

    def account(self):
        urlPath = '/api/v3/account'
        return self.sign_query(urlPath)
