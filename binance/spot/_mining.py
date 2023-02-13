from binance.lib.utils import check_required_parameters
from binance.lib.utils import check_required_parameter


def mining_algo_list(self):
    """Acquiring Algorithm (MARKET_DATA)

    GET /sapi/v1/mining/pub/algoList

    https://binance-docs.github.io/apidocs/spot/en/#acquiring-algorithm-market_data

    """

    return self.limit_request("GET", "/sapi/v1/mining/pub/algoList")


def mining_coin_list(self):
    """Acquiring CoinName (MARKET_DATA)

    GET /sapi/v1/mining/pub/coinList

    https://binance-docs.github.io/apidocs/spot/en/#acquiring-coinname-market_data

    """

    return self.limit_request("GET", "/sapi/v1/mining/pub/coinList")


def mining_worker(self, algo: str, userName: str, workerName: str, **kwargs):
    """Request for Detail Miner List (USER_DATA)

    GET /sapi/v1/mining/worker/detail

    https://binance-docs.github.io/apidocs/spot/en/#request-for-detail-miner-list-user_data

    Args:
        algo (str)
        userName (str): Mining account
        workerName (str)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters(
        [[algo, "algo"], [userName, "userName"], [workerName, "workerName"]]
    )

    payload = {"algo": algo, "userName": userName, "workerName": workerName, **kwargs}
    return self.sign_request("GET", "/sapi/v1/mining/worker/detail", payload)


def mining_worker_list(self, algo: str, userName: str, **kwargs):
    """Request for Miner List (USER_DATA)

    GET /sapi/v1/mining/worker/list

    https://binance-docs.github.io/apidocs/spot/en/#request-for-miner-list-user_data

    Args:
        algo (str)
        userName (str): Mining account
    Keyword Args:
        pageIndex (int, optional): Page number，default is first page，start form 1
        sort (int, optional): sort sequence (default=0)0 positive sequence，1 negative sequence
        sortColumn (int, optional): Sort by (default 1):
                1: miner name, 2: real-time computing power, 3: daily average computing power,
                4: real-time rejection rate, 5: last submission time
        workerStatus (int, optional): miners status (default = 0) 0 all, 1 valid, 2 invalid, 3 failure
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters([[algo, "algo"], [userName, "userName"]])

    payload = {"algo": algo, "userName": userName, **kwargs}
    return self.sign_request("GET", "/sapi/v1/mining/worker/list", payload)


def mining_earnings_list(self, algo: str, userName: str, **kwargs):
    """Revenue List (USER_DATA)

    GET /sapi/v1/mining/payment/list

    https://binance-docs.github.io/apidocs/spot/en/#earnings-list-user_data

    Args:
        algo (str)
        userName (str): Mining account
    Keyword Args:
        coin (str, optional): Coin Name
        startDate (int, optional): Search date, millisecond timestamp, while empty query all
        endDate (int, optional): Search date, millisecond timestamp, while empty query all
        pageIndex (int, optional): Page number, empty default first page, starting from 1
        pageSize (int, optional): Number of pages, minimum 10, maximum 200
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters([[algo, "algo"], [userName, "userName"]])

    payload = {"algo": algo, "userName": userName, **kwargs}
    return self.sign_request("GET", "/sapi/v1/mining/payment/list", payload)


def mining_bonus_list(self, algo: str, userName: str, **kwargs):
    """Extra Bonus List (USER_DATA)

    GET /sapi/v1/mining/payment/other

    https://binance-docs.github.io/apidocs/spot/en/#extra-bonus-list-user_data

    Args:
        algo (str)
        userName (str): Mining account
    Keyword Args:
        coin (str, optional): Coin Name
        startDate (int, optional): Search date, millisecond timestamp, while empty query all
        endDate (int, optional): Search date, millisecond timestamp, while empty query all
        pageIndex (int, optional): Page number, empty default first page, starting from 1
        pageSize (int, optional): Number of pages, minimum 10, maximum 200
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters([[algo, "algo"], [userName, "userName"]])

    payload = {"algo": algo, "userName": userName, **kwargs}
    return self.sign_request("GET", "/sapi/v1/mining/payment/other", payload)


def mining_statistics_list(self, algo: str, userName: str, **kwargs):
    """Statistic List (USER_DATA)

    GET /sapi/v1/mining/statistics/user/status

    https://binance-docs.github.io/apidocs/spot/en/#statistic-list-user_data

    Args:
        algo (str)
        userName (str): Mining account
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000

    """
    check_required_parameters([[algo, "algo"], [userName, "userName"]])

    payload = {"algo": algo, "userName": userName, **kwargs}
    return self.sign_request("GET", "/sapi/v1/mining/statistics/user/status", payload)


def mining_account_list(self, algo: str, userName: str, **kwargs):
    """Account List (USER_DATA)

    GET /sapi/v1/mining/statistics/user/list

    https://binance-docs.github.io/apidocs/spot/en/#account-list-user_data

    Args:
        algo (str)
        userName (str): Mining account
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000

    """
    check_required_parameters([[algo, "algo"], [userName, "userName"]])

    payload = {"algo": algo, "userName": userName, **kwargs}
    return self.sign_request("GET", "/sapi/v1/mining/statistics/user/list", payload)


def mining_hashrate_resale_request(
    self,
    algo: str,
    userName: str,
    startDate: int,
    endDate: int,
    toPoolUser: str,
    hashRate: int,
    **kwargs
):
    """Hashrate Resale Request (USER_DATA)

    POST /sapi/v1/mining/hash-transfer/config

    https://binance-docs.github.io/apidocs/spot/en/#hashrate-resale-request-user_data

    Args:
        algo (str)
        userName (str): Mining account
        startDate (int): Resale Start Time(Millisecond timestamp)
        endDate (int): Resale End Time (Millisecond timestamp)
        toPoolUser (str): Mining Account
        hashRate (int): Resale hashrate h/s must be transferred
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters(
        [
            [algo, "algo"],
            [userName, "userName"],
            [startDate, "startDate"],
            [endDate, "endDate"],
            [toPoolUser, "toPoolUser"],
            [hashRate, "hashRate"],
        ]
    )

    payload = {
        "algo": algo,
        "userName": userName,
        "startDate": startDate,
        "endDate": endDate,
        "toPoolUser": toPoolUser,
        "hashRate": hashRate,
        **kwargs,
    }
    return self.sign_request("POST", "/sapi/v1/mining/hash-transfer/config", payload)


def mining_hashrate_resale_cancellation(self, configId: int, userName: str, **kwargs):
    """Cancel hashrate resale configuration(USER_DATA)

    POST /sapi/v1/mining/hash-transfer/config/cancel

    https://binance-docs.github.io/apidocs/spot/en/#cancel-hashrate-resale-configuration-user_data

    Args:
        configId (int): Mining ID
        userName (str): Mining account
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters([[configId, "configId"], [userName, "userName"]])

    payload = {"configId": configId, "userName": userName, **kwargs}
    return self.sign_request(
        "POST", "/sapi/v1/mining/hash-transfer/config/cancel", payload
    )


def mining_hashrate_resale_list(self, **kwargs):
    """Hashrate Resale List (USER_DATA)

    GET /sapi/v1/mining/hash-transfer/config/details/list

    https://binance-docs.github.io/apidocs/spot/en/#hashrate-resale-list-user_data

    Keyword Args:
        pageIndex (int, optional): Page number, empty default first page, starting from 1
        pageSize (int, optional): Number of pages, minimum 10, maximum 200
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request(
        "GET", "/sapi/v1/mining/hash-transfer/config/details/list", kwargs
    )


def mining_hashrate_resale_details(self, configId: int, userName: str, **kwargs):
    """Hashrate Resale Detail (USER_DATA)

    GET /sapi/v1/mining/hash-transfer/profit/details

    https://binance-docs.github.io/apidocs/spot/en/#hashrate-resale-detail-user_data

    Args:
        configId (int): Mining ID
        userName (str): Mining account
    Keyword Args:
        pageIndex (int, optional): Page number, empty default first page, starting from 1
        pageSize (int, optional): Number of pages, minimum 10, maximum 200
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters([[configId, "configId"], [userName, "userName"]])

    payload = {"configId": configId, "userName": userName, **kwargs}
    return self.sign_request(
        "GET", "/sapi/v1/mining/hash-transfer/profit/details", payload
    )


def mining_account_earning(self, algo: str, **kwargs):
    """Mining Account Earning (USER_DATA)

    GET /sapi/v1/mining/payment/uid

    https://binance-docs.github.io/apidocs/spot/en/#mining-account-earning-user_data

    Args:
        algo (str): Algorithm(sha256)
    Keyword Args:
        startDate (int, optional): Millisecond timestamp
        endDate (int, optional): Millisecond timestamp
        pageIndex (int, optional): Default 1
        pageSize (int, optional): Min 10,Max 200
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(algo, "algo")

    payload = {"algo": algo, **kwargs}
    return self.sign_request("GET", "/sapi/v1/mining/payment/uid", payload)
