from binance.api import API
from binance.lib.utils import check_required_parameter

class Stream(API):

    """ Steam class is used for managing user data stream related restful APIs.

    """

    def __init__(self, key, **kwargs):
        super(Stream, self).__init__(key, **kwargs)

    def new_listen_key(self):
        """ Create a ListenKey (USER_STREAM)

        POST /api/v3/userDataStream

        https://binance-docs.github.io/apidocs/spot/en/#listen-key-spot
        """

        url_path = '/api/v3/userDataStream'
        return self.send_request('POST', url_path)

    def renew_listen_key(self, listenKey: str):
        """ Create a ListenKey (USER_STREAM)

        PUT /api/v3/userDataStream

        https://binance-docs.github.io/apidocs/spot/en/#listen-key-spot
        """
        check_required_parameter(listenKey, 'listenKey')

        url_path = '/api/v3/userDataStream'
        return self.send_request('PUT', url_path, {'listenKey': listenKey})

    def close_listen_key(self, listenKey: str):
        """ Close a ListenKey (USER_STREAM)

        DELETE /api/v3/userDataStream

        https://binance-docs.github.io/apidocs/spot/en/#listen-key-spot
        """
        check_required_parameter(listenKey, 'listenKey')

        url_path = '/api/v3/userDataStream'
        return self.send_request('DELETE', url_path, {'listenKey': listenKey})
