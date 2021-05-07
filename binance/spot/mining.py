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


def mining_earnings_list(self, algo: str, userName: str, **kwargs):
    """ Revenue List (USER_DATA)

    GET /sapi/v1/mining/payment/list

    https://binance-docs.github.io/apidocs/spot/en/#earnings-list-user_data

    Parameters:
    | algo       | mandatory | string | Transfer algorithm(sha256)                                |
    | userName   | mandatory | string | Mining account                                            |
    | coin       | optional  | string | Coin Name                                                 |
    | startDate  | optional  | int    | Search date, millisecond timestamp, while empty query all |
    | endDate    | optional  | int    | Search date, millisecond timestamp, while empty query all |
    | pageIndex  | optional  | int    | Page number, empty default first page, starting from 1    |
    | pageSize   | optional  | int    | Number of pages, minimum 10, maximum 200	              |
    | recvWindow | optional  | int    |                                                           |
    """
    check_required_parameters([
        [algo, 'algo'],
        [userName, 'userName']
    ])

    payload = {'algo': algo, 'userName': userName, **kwargs}
    return self.sign_request('GET', '/sapi/v1/mining/payment/list', payload)


def mining_bonus_list(self, algo: str, userName: str, **kwargs):
    """ Extra Bonus List (USER_DATA)

    GET /sapi/v1/mining/payment/other

    https://binance-docs.github.io/apidocs/spot/en/#extra-bonus-list-user_data

    Parameters:
    | algo       | mandatory | string | Transfer algorithm(sha256)                                |
    | userName   | mandatory | string | Mining account                                            |
    | coin       | optional  | string | Coin Name                                                 |
    | startDate  | optional  | int    | Search date, millisecond timestamp, while empty query all |
    | endDate    | optional  | int    | Search date, millisecond timestamp, while empty query all |
    | pageIndex  | optional  | int    | Page number, empty default first page, starting from 1    |
    | pageSize   | optional  | int    | Number of pages, minimum 10, maximum 200	              |
    | recvWindow | optional  | int    |                                                           |
    """
    check_required_parameters([
        [algo, 'algo'],
        [userName, 'userName']
    ])

    payload = {'algo': algo, 'userName': userName, **kwargs}
    return self.sign_request('GET', '/sapi/v1/mining/payment/other', payload)


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


def mining_hashrate_resale_request(self, algo: str, userName: str, startDate: int, endDate: int,
                                   toPoolUser: str, hashRate: str, **kwargs):
    """ Hashrate Resale Request (USER_DATA)

    POST /sapi/v1/mining/hash-transfer/config

    https://binance-docs.github.io/apidocs/spot/en/#hashrate-resale-request-user_data

    Parameters:
    | algo       | mandatory | string | Transfer algorithm(sha256)               |
    | userName   | mandatory | string | Mining account                           |
    | startDate  | mandatory | int    | Resale Start Time(Millisecond timestamp) |
    | endDate    | mandatory | int    | Resale End Time (Millisecond timestamp)  |
    | toPoolUser | mandatory | string | Mining Account                           |
    | hashRate   | mandatory | string | Resale hashrate h/s must be transferred  |
    | recvWindow | optional  | int    |                                          |
    """

    check_required_parameters([
        [algo, 'algo'],
        [userName, 'userName'],
        [startDate, 'startDate'],
        [endDate, 'endDate'],
        [toPoolUser, 'toPoolUser'],
        [hashRate, 'hashRate']
    ])

    payload = {
        'algo': algo,
        'userName': userName,
        'startDate': startDate,
        'endDate': endDate,
        'toPoolUser': toPoolUser,
        'hashRate': hashRate,
        **kwargs
    }
    return self.sign_request('POST', '/sapi/v1/mining/hash-transfer/config', payload)


def mining_hashrate_resale_cancellation(self, configId: int, userName: str, **kwargs):
    """ Cancel hashrate resale configuration(USER_DATA)

    POST /sapi/v1/mining/hash-transfer/config/cancel

    https://binance-docs.github.io/apidocs/spot/en/#cancel-hashrate-resale-configuration-user_data

    Parameters:
    | configId   | mandatory | int    | Mining ID      |
    | userName   | mandatory | string | Mining account |
    | recvWindow | optional  | int    |                |
    """

    check_required_parameters([
        [configId, 'configId'],
        [userName, 'userName']
    ])

    payload = {
        'configId': configId,
        'userName': userName,
        **kwargs
    }
    return self.sign_request('POST', '/sapi/v1/mining/hash-transfer/config/cancel', payload)


def mining_hashrate_resale_list(self, **kwargs):
    """ Hashrate Resale List (USER_DATA)

    GET /sapi/v1/mining/hash-transfer/config/details/list

    https://binance-docs.github.io/apidocs/spot/en/#hashrate-resale-list-user_data

    Parameters:
    | pageIndex  | optional  | int    | Page number, empty default first page, starting from 1 |
    | pageSize   | optional  | int    | Number of pages, minimum 10, maximum 200	           |
    | recvWindow | optional  | int    |                                                        |
    """

    return self.sign_request('GET', '/sapi/v1/mining/hash-transfer/config/details/list', kwargs)


def mining_hashrate_resale_details(self, configId: int, userName: str, **kwargs):
    """ Hashrate Resale Detail (USER_DATA)

    GET /sapi/v1/mining/hash-transfer/profit/details

    https://binance-docs.github.io/apidocs/spot/en/#hashrate-resale-detail-user_data

    Parameters:
    | configId   | mandatory | int    | Mining ID                                              |
    | userName   | mandatory | string | Mining Account                                         |
    | pageIndex  | optional  | int    | Page number, empty default first page, starting from 1 |
    | pageSize   | optional  | int    | Number of pages, minimum 10, maximum 200	           |
    | recvWindow | optional  | int    |                                                        |
    """
    check_required_parameters([
        [configId, 'configId'],
        [userName, 'userName']
    ])

    payload = {'configId': configId, 'userName': userName, **kwargs}
    return self.sign_request('GET', '/sapi/v1/mining/hash-transfer/profit/details', payload)
