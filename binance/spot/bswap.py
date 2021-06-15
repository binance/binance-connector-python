from binance.lib.utils import check_required_parameters


def bswap_pools(self):
    """List All Swap Pools (MARKET_DATA)
    Get metadata about all swap pools.

    GET /sapi/v1/bswap/pools

    https://binance-docs.github.io/apidocs/spot/en/#list-all-swap-pools-market_data

    """

    return self.limit_request("GET", "/sapi/v1/bswap/pools", {})


def bswap_liquidity(self, **kwargs):
    """Get liquidity information of a pool (USER_DATA)
    Get liquidity information and user share of a pool

    GET /sapi/v1/bswap/liquidity

    https://binance-docs.github.io/apidocs/spot/en/#get-liquidity-information-of-a-pool-user_data

    Keyword Args:
        poolId (int, optional)
        recvWindow (int, optional): The value cannot be greater than 60000

    """
    return self.sign_request("GET", "/sapi/v1/bswap/liquidity", kwargs)


def bswap_liquidity_add(self, poolId: int, asset: str, quantity: float, **kwargs):
    """Add Liquidity (TRADE)
    Add liquidity to a pool.

    POST /sapi/v1/bswap/liquidityAdd

    https://binance-docs.github.io/apidocs/spot/en/#add-liquidity-trade

    Args:
        poolId (int)
        asset (str)
        quantity (float)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters(
        [[poolId, "poolId"], [asset, "asset"], [quantity, "quantity"]]
    )
    payload = {"poolId": poolId, "asset": asset, "quantity": quantity, **kwargs}

    return self.sign_request("POST", "/sapi/v1/bswap/liquidityAdd", payload)


def bswap_liquidity_remove(
    self, poolId: str, type: str, asset: list, shareAmount, **kwargs
):
    """Remove Liquidity (TRADE)
    Remove liquidity from a pool, type include SINGLE and COMBINATION, asset is mandatory for single asset removal

    POST /sapi/v1/bswap/liquidityRemove

    https://binance-docs.github.io/apidocs/spot/en/#remove-liquidity-trade

    Args:
        poolId (int)
        type (str): SINGLE for single asset removal, COMBINATION for combination of all coins removal
        asset (str)
        shareAmount (float): Mandatory for liquidity removal
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters(
        [
            [poolId, "poolId"],
            [type, "type"],
            [asset, "asset"],
            [shareAmount, "shareAmount"],
        ]
    )
    payload = {
        "poolId": poolId,
        "type": type,
        "asset": ",".join(asset),
        "shareAmount": shareAmount,
        **kwargs,
    }

    return self.sign_request("POST", "/sapi/v1/bswap/liquidityRemove", payload)


def bswap_liquidity_operation_record(self, **kwargs):
    """Get Liquidity Operation Record (USER_DATA)
    Get liquidity operation (add/remove) records.

    GET /sapi/v1/bswap/liquidityOps

    https://binance-docs.github.io/apidocs/spot/en/#get-liquidity-operation-record-user_data

    Keyword Args:
        operationId (int, optional)
        poolId (int, optional)
        operation (str, optional): ADD or REMOVE
        startTime (int, optional)
        endTime (int, optional)
        limit (int, optional): default 3, max 100
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    return self.sign_request("GET", "/sapi/v1/bswap/liquidityOps", kwargs)


def bswap_request_quote(
    self, quoteAsset: str, baseAsset: str, quoteQty: float, **kwargs
):
    """Request Quote (USER_DATA)
    Request a quote for swap quote asset (selling asset) for base asset (buying asset), essentially price/exchange rates.
    quoteQty is quantity of quote asset (to sell).

    Please be noted the quote is for reference only, the actual price will change as the liquidity changes,
    it's recommended to swap immediate after request a quote for slippage prevention.

    GET /sapi/v1/bswap/quote

    https://binance-docs.github.io/apidocs/spot/en/#request-quote-user_data

    Args:
        quoteAsset (str)
        baseAsset (str)
        quoteQty (float)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters(
        [[quoteAsset, "quoteAsset"], [baseAsset, "baseAsset"], [quoteQty, "quoteQty"]]
    )
    payload = {
        "quoteAsset": quoteAsset,
        "baseAsset": baseAsset,
        "quoteQty": quoteQty,
        **kwargs,
    }

    return self.sign_request("GET", "/sapi/v1/bswap/quote", payload)


def bswap_swap(self, quoteAsset: str, baseAsset: str, quoteQty: float, **kwargs):
    """Swap (TRADE)
    Swap quoteAsset for baseAsset.

    POST /sapi/v1/bswap/swap

    https://binance-docs.github.io/apidocs/spot/en/#swap-trade

    Args:
        baseAsset (str)
        quoteAsset (str)
        quoteQty (float)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters(
        [[quoteAsset, "quoteAsset"], [baseAsset, "baseAsset"], [quoteQty, "quoteQty"]]
    )
    payload = {
        "quoteAsset": quoteAsset,
        "baseAsset": baseAsset,
        "quoteQty": quoteQty,
        **kwargs,
    }
    return self.sign_request("POST", "/sapi/v1/bswap/swap", payload)


def bswap_swap_history(self, **kwargs):
    """Get Swap History (USER_DATA)
    Get swap history.

    GET /sapi/v1/bswap/swap

    https://binance-docs.github.io/apidocs/spot/en/#get-swap-history-user_data

    Keyword Args:
        swapId (int, optional)
        startTime (int, optional)
        endTime (int, optional)
        status (int, optional)
        baseAsset (str, optional)
        quoteAsset (str, optional)
        limit (int, optional)
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    return self.sign_request("GET", "/sapi/v1/bswap/swap", kwargs)
