from binance.lib.utils import check_required_parameters


async def blvt_info(self, tokenName: str = None):
    """Get BLVT Info (MARKET_DATA)

    GET /sapi/v1/blvt/tokenInfo

    https://binance-docs.github.io/apidocs/spot/en/#get-blvt-info-market_data

    Args:
        tokenName (str, optional): BTCDOWN, BTCUP
    """
    payload = {"tokenName": tokenName}

    return await self.limit_request("GET", "/sapi/v1/blvt/tokenInfo", payload)


async def subscribe_blvt(self, tokenName: str, cost, **kwargs):
    """Subscribe BLVT (USER_DATA)

    POST /sapi/v1/blvt/subscribe (HMAC SHA256)

    https://binance-docs.github.io/apidocs/spot/en/#subscribe-blvt-user_data

    Args:
        tokenName (str): BTCDOWN, BTCUP.
        cost (str): spot balance.
    Keyword Args:
        recvWindow (int, optional)
    """

    check_required_parameters([[tokenName, "tokenName"], [cost, "cost"]])

    payload = {"tokenName": tokenName, "cost": cost, **kwargs}
    return await self.sign_request("POST", "/sapi/v1/blvt/subscribe", payload)


async def subscription_record(self, **kwargs):
    """Query Subscription Record (USER_DATA)

    GET /sapi/v1/blvt/subscribe/record (HMAC SHA256)

    https://binance-docs.github.io/apidocs/spot/en/#query-subscription-record-user_data

    Keyword Args:
        tokenName (str, optional): BTCDOWN, BTCUP.
        id (int, optional)
        startTime (int, optional)
        endTime (int, optional)
        limit (int, optional): default 1000, max 1000.
        recvWindow (int, optional)
    """

    return await self.sign_request("GET", "/sapi/v1/blvt/subscribe/record", kwargs)


async def redeem_blvt(self, tokenName: str, amount, **kwargs):
    """Redeem BLVT (USER_DATA)

    POST /sapi/v1/blvt/redeem (HMAC SHA256)

    https://binance-docs.github.io/apidocs/spot/en/#redeem-blvt-user_data

    Args:
        tokenName (str): BTCDOWN, BTCUP
        amount (str)
    Keyword Args:
        recvWindow (int, optional)
    """

    check_required_parameters([[tokenName, "tokenName"], [amount, "amount"]])

    payload = {"tokenName": tokenName, "amount": amount, **kwargs}
    return await self.sign_request("POST", "/sapi/v1/blvt/redeem", payload)


async def redemption_record(self, **kwargs):
    """Query Redemption Record (USER_DATA)

    GET /sapi/v1/blvt/redeem/record (HMAC SHA256)

    https://binance-docs.github.io/apidocs/spot/en/#query-redemption-record-user_data

    Keyword Args:
        tokenName (str, optional): BTCDOWN, BTCUP
        id (int, optional)
        startTime (int, optional)
        endTime (int, optional)
        limit (int, optional): default 1000, max 1000
        recvWindow (int, optional)
    """

    return await self.sign_request("GET", "/sapi/v1/blvt/redeem/record", kwargs)


async def user_limit_info(self, **kwargs):
    """Get BLVT User Limit Info

    GET /sapi/v1/blvt/userLimit

    https://binance-docs.github.io/apidocs/spot/en/#get-blvt-user-limit-info

    Keyword Args:
        tokenName (str, optional): BTCDOWN, BTCUP
        recvWindow (int, optional)
    """

    return await self.sign_request("GET", "/sapi/v1/blvt/userLimit", kwargs)
