from binance.lib.utils import check_required_parameter
from binance.lib.utils import check_required_parameters


def mining_algo_list(self):
    """ Acquiring Algorithm (MARKET_DATA)

    GET /sapi/v1/mining/pub/algoList

    https://binance-docs.github.io/apidocs/spot/en/#acquiring-algorithm-market_data

    """

    return self.limit_request('GET', '/sapi/v1/mining/pub/algoList')


def mining_coin_list(self):
    """ Acquiring CoinName (MARKET_DATA)

    GET /sapi/v1/mining/pub/coinList

    https://binance-docs.github.io/apidocs/spot/en/#acquiring-coinname-market_data

    """

    return self.limit_request('GET', '/sapi/v1/mining/pub/coinList')


def mining_worker(self, algo: str, userName: str, workerName: str, **kwargs):
    """ Request for Detail Miner List (USER_DATA)

    GET /sapi/v1/mining/worker/detail

    https://binance-docs.github.io/apidocs/spot/en/#request-for-detail-miner-list-user_data

    """
    check_required_parameters([
        [algo, 'algo'],
        [userName, 'userName'],
        [workerName, 'workerName']
    ])

    payload = {'algo': algo, 'userName': userName, 'workerName': workerName, **kwargs}
    return self.sign_request('GET', '/sapi/v1/mining/worker/detail', payload)


def mining_worker_list(self, algo: str, userName: str, **kwargs):
    """ Request for Miner List (USER_DATA)

    GET /sapi/v1/mining/worker/list

    https://binance-docs.github.io/apidocs/spot/en/#request-for-miner-list-user_data

    """
    check_required_parameters([
        [algo, 'algo'],
        [userName, 'userName']
    ])

    payload = {'algo': algo, 'userName': userName, **kwargs}
    return self.sign_request('GET', '/sapi/v1/mining/worker/list', payload)


def mining_revenue_list(self, algo: str, userName: str, **kwargs):
    """ Revenue List (USER_DATA)

    GET /sapi/v1/mining/payment/list

    https://binance-docs.github.io/apidocs/spot/en/#revenue-list-user_data

    """
    check_required_parameters([
        [algo, 'algo'],
        [userName, 'userName']
    ])

    payload = {'algo': algo, 'userName': userName, **kwargs}
    return self.sign_request('GET', '/sapi/v1/mining/payment/list', payload)


def mining_statistics_list(self, algo: str, userName: str, **kwargs):
    """ Statistic List (USER_DATA)

    GET /sapi/v1/mining/statistics/user/status

    https://binance-docs.github.io/apidocs/spot/en/#statistic-list-user_data

    """
    check_required_parameters([
        [algo, 'algo'],
        [userName, 'userName']
    ])

    payload = {'algo': algo, 'userName': userName, **kwargs}
    return self.sign_request('GET', '/sapi/v1/mining/statistics/user/status', payload)


def mining_account_list(self, algo: str, userName: str, **kwargs):
    """ Account List (USER_DATA)

    GET /sapi/v1/mining/statistics/user/list

    https://binance-docs.github.io/apidocs/spot/en/#account-list-user_data

    """
    check_required_parameters([
        [algo, 'algo'],
        [userName, 'userName']
    ])

    payload = {'algo': algo, 'userName': userName, **kwargs}
    return self.sign_request('GET', '/sapi/v1/mining/statistics/user/list', payload)
