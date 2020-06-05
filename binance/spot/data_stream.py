from binance.lib.utils import check_required_parameter


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


# Margin
def new_margin_listen_key(self):
    """ Create a ListenKey (USER_STREAM)

    POST /sapi/v1/userDataStream

    https://binance-docs.github.io/apidocs/spot/en/#listen-key-margin
    """

    url_path = '/sapi/v1/userDataStream'
    return self.send_request('POST', url_path)


def renew_margin_listen_key(self, listenKey: str):
    """ Create a ListenKey (USER_STREAM)

    PUT /sapi/v1/userDataStream

    https://binance-docs.github.io/apidocs/spot/en/#listen-key-margin
    """
    check_required_parameter(listenKey, 'listenKey')

    url_path = '/sapi/v1/userDataStream'
    return self.send_request('PUT', url_path, {'listenKey': listenKey})


def close_margin_listen_key(self, listenKey: str):
    """ Close a ListenKey (USER_STREAM)

    DELETE /sapi/v1/userDataStream

    https://binance-docs.github.io/apidocs/spot/en/#listen-key-margin
    """
    check_required_parameter(listenKey, 'listenKey')

    url_path = '/sapi/v1/userDataStream'
    return self.send_request('DELETE', url_path, {'listenKey': listenKey})
