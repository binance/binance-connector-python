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
        type (str, optional): "Single" to add a single token; "Combination" to add dual tokens. Default "Single"
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


def bswap_pool_configure(self, **kwargs):
    """Get Pool Configure (USER_DATA)

    GET /sapi/v1/bswap/poolConfigure

    https://binance-docs.github.io/apidocs/spot/en/#get-pool-configure-user_data

    Keyword Args:
        poolId (int, optional)
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    return self.sign_request("GET", "/sapi/v1/bswap/poolConfigure", kwargs)


def bswap_add_liquidity_preview(
    self, poolId: int, type: str, quoteAsset: str, quoteQty: float, **kwargs
):
    """Add Liquidity Preview (USER_DATA)
    Calculate expected share amount for adding liquidity in single or dual token.

    GET /sapi/v1/bswap/addLiquidityPreview

    https://binance-docs.github.io/apidocs/spot/en/#add-liquidity-preview-user_data

    Args:
        poolId (int)
        type (str): "SINGLE" for adding a single token;"COMBINATION" for adding dual tokens
        quoteAsset (str)
        quoteQty (float)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters(
        [
            [poolId, "poolId"],
            [type, "type"],
            [quoteAsset, "quoteAsset"],
            [quoteQty, "quoteQty"],
        ]
    )
    payload = {
        "poolId": poolId,
        "type": type,
        "quoteAsset": quoteAsset,
        "quoteQty": quoteQty,
        **kwargs,
    }
    return self.sign_request("GET", "/sapi/v1/bswap/addLiquidityPreview", payload)


def bswap_remove_liquidity_preview(
    self, poolId: int, type: str, quoteAsset: str, shareAmount: float, **kwargs
):
    """Remove Liquidity Preview (USER_DATA)
    Calculate the expected asset amount of single token redemption or dual token redemption.

    GET /sapi/v1/bswap/removeLiquidityPreview

    https://binance-docs.github.io/apidocs/spot/en/#remove-liquidity-preview-user_data

    Args:
        poolId (int)
        type (str): Type is "SINGLE", remove and obtain a single token;Type is "COMBINATION", remove and obtain dual token
        quoteAsset (str)
        shareAmount (float)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters(
        [
            [poolId, "poolId"],
            [type, "type"],
            [quoteAsset, "quoteAsset"],
            [shareAmount, "shareAmount"],
        ]
    )
    payload = {
        "poolId": poolId,
        "type": type,
        "quoteAsset": quoteAsset,
        "shareAmount": shareAmount,
        **kwargs,
    }
    return self.sign_request("GET", "/sapi/v1/bswap/removeLiquidityPreview", payload)


def bswap_unclaimed_rewards(self, **kwargs):
    """Get Unclaimed Rewards Record (USER_DATA)
    Get unclaimed rewards record.

    GET /sapi/v1/bswap/unclaimedRewards

    https://binance-docs.github.io/apidocs/spot/en/#get-unclaimed-rewards-record-user_data

    Keyword Args:
        type (int, optional): 0: Swap rewards,1:Liquidity rewards, default to 0
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/bswap/unclaimedRewards", kwargs)


def bswap_claim_rewards(self, **kwargs):
    """Claim rewards (TRADE)
    Claim swap rewards or liquidity rewards

    POST /sapi/v1/bswap/claimRewards

    https://binance-docs.github.io/apidocs/spot/en/#claim-rewards-trade

    Keyword Args:
        type (int, optional): 0: Swap rewards,1:Liquidity rewards, default to 0
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("POST", "/sapi/v1/bswap/claimRewards", kwargs)


def bswap_claimed_rewards(self, **kwargs):
    """Get Claimed History (USER_DATA)
    Get history of claimed rewards.

    GET /sapi/v1/bswap/claimedHistory

    https://binance-docs.github.io/apidocs/spot/en/#get-claimed-history-user_data

    Keyword Args:
        poolId (int, optional)
        assetRewards (str, optional)
        type (int, optional): 0: Swap rewards,1:Liquidity rewards, default to 0
        startTime (int, optional)
        endTime (int, optional)
        limit (int, optional): default 3, max 100
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/bswap/claimedHistory", kwargs)
