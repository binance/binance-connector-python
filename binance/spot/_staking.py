from binance.lib.utils import check_required_parameter


def eth_staking_account(self, **kwargs):
    """ETH Staking account (USER_DATA)

    ETH Staking account

    Weight(IP): 150

    GET /sapi/v2/eth-staking/account

    https://developers.binance.com/docs/staking/eth-staking/account

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    url_path = "/sapi/v2/eth-staking/account"
    return self.sign_request("GET", url_path, {**kwargs})


def get_eth_staking_quota(self, **kwargs):
    """Get current ETH staking quota (USER_DATA)

    Get current ETH staking quota

    Weight(IP): 150

    GET /sapi/v1/eth-staking/eth/quota

    https://developers.binance.com/docs/staking/eth-staking/account/Get-current-ETH-staking-quota

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    url_path = "/sapi/v1/eth-staking/eth/quota"
    return self.sign_request("GET", url_path, {**kwargs})


def subscribe_eth_staking(self, amount: float, **kwargs):
    """Subscribe ETH Staking (TRADE)

    Subscribe ETH Staking

    Weight(IP): 150

    POST /sapi/v2/eth-staking/eth/stake

    https://developers.binance.com/docs/staking/eth-staking/staking

    Args:
        amount (float): Amount in ETH, limit 4 decimals

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(amount, "amount")

    params = {"amount": amount, **kwargs}
    url_path = "/sapi/v2/eth-staking/eth/stake"
    return self.sign_request("POST", url_path, params)


def redeem_eth(self, amount: float, **kwargs):
    """Redeem ETH (TRADE)

    Redeem WBETH or BETH and get ETH

    Weight(IP): 150

    POST /sapi/v1/eth-staking/eth/redeem

    https://developers.binance.com/docs/staking/eth-staking/staking/Redeem-ETH

    Args:
        amount (float): Amount in BETH, limit 8 decimals

    Keyword Args:
        asset (str, optional): WBETH or BETH, default to BETH
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(amount, "amount")

    params = {"amount": amount, **kwargs}
    url_path = "/sapi/v1/eth-staking/eth/redeem"
    return self.sign_request("POST", url_path, params)


def wrap_beth(self, amount: float, **kwargs):
    """Wrap BETH (TRADE)

    Wrap BETH

    Weight(IP): 150

    POST /sapi/v1/eth-staking/wbeth/wrap

    https://developers.binance.com/docs/staking/eth-staking/staking/Wrap-BETH

    Args:
        amount (float): Amount in BETH, limit 4 decimals
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(amount, "amount")

    params = {"amount": amount, **kwargs}
    url_path = "/sapi/v1/eth-staking/wbeth/wrap"
    return self.sign_request("POST", url_path, params)


def get_eth_staking_history(self, **kwargs):
    """Get ETH staking history (USER_DATA)

    Get ETH staking history

    Weight(IP): 150

    GET /sapi/v1/eth-staking/eth/history/stakingHistory

    https://developers.binance.com/docs/staking/eth-staking/history

    Keyword Args:
        startTime (int, optional)
        endTime (int, optional)
        current (int, optional): Currently querying page. Start from 1. Default: 1
        size (int, optional): Default: 10, Max: 100
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    url_path = "/sapi/v1/eth-staking/eth/history/stakingHistory"
    return self.sign_request("GET", url_path, {**kwargs})


def get_eth_redemption_history(self, **kwargs):
    """Get ETH redemption history (USER_DATA)

    Get ETH redemption history

    Weight(IP): 150

    GET /sapi/v1/eth-staking/eth/history/redemptionHistory

    https://developers.binance.com/docs/staking/eth-staking/history/Get-ETH-redemption-history

    Keyword Args:
        startTime (int, optional)
        endTime (int, optional)
        current (int, optional): Currently querying page. Start from 1. Default: 1
        size (int, optional): Default: 10, Max: 100
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    url_path = "/sapi/v1/eth-staking/eth/history/redemptionHistory"
    return self.sign_request("GET", url_path, {**kwargs})


def get_beth_rewards_distribution_history(self, **kwargs):
    """Get BETH rewards distribution history (USER_DATA)

    Get BETH rewards distribution history

    Weight(IP): 150

    GET /sapi/v1/eth-staking/eth/history/rewardsHistory

    https://developers.binance.com/docs/staking/eth-staking/history/Get-ETH-rewards-distribution-history

    Keyword Args:
        startTime (int, optional)
        endTime (int, optional)
        current (int, optional): Currently querying page. Start from 1. Default: 1
        size (int, optional): Default: 10, Max: 100
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    url_path = "/sapi/v1/eth-staking/eth/history/rewardsHistory"
    return self.sign_request("GET", url_path, {**kwargs})


def get_wbeth_rewards_history(self, **kwargs):
    """Get WBETH rewards history (USER_DATA)

    Get WBETH rewards history

    Weight(IP): 150

    GET /sapi/v1/eth-staking/eth/history/wbethRewardsHistory

    https://developers.binance.com/docs/staking/eth-staking/history/Get-WBETH-rewards-history

    Keyword Args:
        startTime (int, optional)
        endTime (int, optional)
        current (int, optional): Currently querying page. Start from 1. Default: 1
        size (int, optional): Default: 10, Max: 100
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    url_path = "/sapi/v1/eth-staking/eth/history/wbethRewardsHistory"
    return self.sign_request("GET", url_path, {**kwargs})


def get_wbeth_rate_history(self, **kwargs):
    """Get WBETH Rate History (USER_DATA)

    Get WBETH Rate History

    Weight(IP): 150

    GET /sapi/v1/eth-staking/eth/history/rateHistory

    https://developers.binance.com/docs/staking/eth-staking/history/Get-BETH-Rate-History

    Keyword Args:
        startTime (int, optional)
        endTime (int, optional)
        current (int, optional): Currently querying page. Start from 1. Default: 1
        size (int, optional): Default: 10, Max: 100
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    url_path = "/sapi/v1/eth-staking/eth/history/rateHistory"
    return self.sign_request("GET", url_path, {**kwargs})


def get_wbeth_wrap_history(self, **kwargs):
    """Get WBETH wrap history (USER_DATA)

    Get WBETH wrap history

    Weight(IP): 150

    GET /sapi/v1/eth-staking/wbeth/history/wrapHistory

    https://developers.binance.com/docs/staking/eth-staking/history/Get-WBETH-wrap-history

    Keyword Args:
        startTime (int, optional)
        endTime (int, optional)
        current (int, optional): Currently querying page. Start from 1. Default: 1
        size (int, optional): Default: 10, Max: 100
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    url_path = "/sapi/v1/eth-staking/wbeth/history/wrapHistory"
    return self.sign_request("GET", url_path, {**kwargs})


def get_wbeth_unwrap_history(self, **kwargs):
    """Get WBETH unwrap history (USER_DATA)

    Get WBETH unwrap history

    Weight(IP): 150

    GET /sapi/v1/eth-staking/wbeth/history/unwrapHistory

    https://developers.binance.com/docs/staking/eth-staking/history/Get-WBETH-unwrap-history

    Keyword Args:
        startTime (int, optional)
        endTime (int, optional)
        current (int, optional): Currently querying page. Start from 1. Default: 1
        size (int, optional): Default: 10, Max: 100
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    url_path = "/sapi/v1/eth-staking/wbeth/history/unwrapHistory"
    return self.sign_request("GET", url_path, {**kwargs})

def sol_staking_account(self, **kwargs):
    """SOL Staking account (USER_DATA)

    SOL Staking account

    Weight(IP): 150

    GET /sapi/v1/sol-staking/account

    https://developers.binance.com/docs/staking/sol-staking/account

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    url_path = "/sapi/v1/sol-staking/account"
    return self.sign_request("GET", url_path, {**kwargs})


def get_sol_staking_quota(self, **kwargs):
    """Get current SOL staking quota (USER_DATA)

    Get current SOL staking quota

    Weight(IP): 150

    GET /sapi/v1/sol-staking/sol/quota

    https://developers.binance.com/docs/staking/sol-staking/account/Get-current-SOL-staking-quota

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    url_path = "/sapi/v1/sol-staking/sol/quota"
    return self.sign_request("GET", url_path, {**kwargs})


def subscribe_sol_staking(self, amount: float, **kwargs):
    """Subscribe SOL Staking (TRADE)

    Subscribe SOL Staking

    Weight(IP): 150

    POST /sapi/v1/sol-staking/sol/stake

    https://developers.binance.com/docs/staking/sol-staking/staking

    Args:
        amount (float): Amount in SOL, limit 4 decimals

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(amount, "amount")

    params = {"amount": amount, **kwargs}
    url_path = "/sapi/v1/sol-staking/sol/stake"
    return self.sign_request("POST", url_path, params)


def redeem_sol(self, amount: float, **kwargs):
    """Redeem SOL (TRADE)

    Redeem BNSOL and get SOL

    Weight(IP): 150

    POST /sapi/v1/sol-staking/sol/redeem

    https://developers.binance.com/docs/staking/sol-staking/staking/Redeem-SOL

    Args:
        amount (float): Amount in BNSOL, limit 8 decimals

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(amount, "amount")

    params = {"amount": amount, **kwargs}
    url_path = "/sapi/v1/sol-staking/sol/redeem"
    return self.sign_request("POST", url_path, params)


def claim_boost_rewards(self, **kwargs):
    """Claim Boost Rewards (TRADE)

    Claim Boost APR Airdrop Rewards 

    Weight(IP): 150

    POST /sapi/v1/sol-staking/sol/claim

    https://developers.binance.com/docs/staking/sol-staking/staking/Claim-Boost-rewards

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    url_path = "/sapi/v1/sol-staking/sol/claim"
    return self.sign_request("POST", url_path, {**kwargs})


def get_sol_staking_history(self, **kwargs):
    """Get SOL staking history (USER_DATA)

    Get SOL staking history

    Weight(IP): 150

    GET /sapi/v1/sol-staking/sol/history/stakingHistory

    https://developers.binance.com/docs/staking/sol-staking/history

    Keyword Args:
        startTime (int, optional)
        endTime (int, optional)
        current (int, optional): Currently querying page. Start from 1. Default: 1
        size (int, optional): Default: 10, Max: 100
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    url_path = "/sapi/v1/sol-staking/sol/history/stakingHistory"
    return self.sign_request("GET", url_path, {**kwargs})


def get_sol_redemption_history(self, **kwargs):
    """Get SOL redemption history (USER_DATA)

    Get SOL redemption history

    Weight(IP): 150

    GET /sapi/v1/sol-staking/sol/history/redemptionHistory

    https://developers.binance.com/docs/staking/sol-staking/history/Get-SOL-redemption-history

    Keyword Args:
        startTime (int, optional)
        endTime (int, optional)
        current (int, optional): Currently querying page. Start from 1. Default: 1
        size (int, optional): Default: 10, Max: 100
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    url_path = "/sapi/v1/sol-staking/sol/history/redemptionHistory"
    return self.sign_request("GET", url_path, {**kwargs})


def get_bnsol_rewards_history(self, **kwargs):
    """Get BNSOL rewards history (USER_DATA)

    Get BNSOL rewards history

    Weight(IP): 150

    GET /sapi/v1/sol-staking/sol/history/bnsolRewardsHistory

    https://developers.binance.com/docs/staking/sol-staking/history/Get-BNSOL-rewards-history

    Keyword Args:
        startTime (int, optional)
        endTime (int, optional)
        current (int, optional): Currently querying page. Start from 1. Default: 1
        size (int, optional): Default: 10, Max: 100
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    url_path = "/sapi/v1/sol-staking/sol/history/bnsolRewardsHistory"
    return self.sign_request("GET", url_path, {**kwargs})


def get_bnsol_rate_history(self, **kwargs):
    """Get BNSOL Rate History (USER_DATA)

    Get BNSOL Rate History

    Weight(IP): 150

    GET /sapi/v1/sol-staking/sol/history/rateHistory

    https://developers.binance.com/docs/staking/sol-staking/history/Get-BNSOL-Rate-History

    Keyword Args:
        startTime (int, optional)
        endTime (int, optional)
        current (int, optional): Currently querying page. Start from 1. Default: 1
        size (int, optional): Default: 10, Max: 100
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    url_path = "/sapi/v1/sol-staking/sol/history/rateHistory"
    return self.sign_request("GET", url_path, {**kwargs})


def get_boost_rewards_history(self, **kwargs):
    """Get Boost rewards history (USER_DATA)

    Get Boost rewards history

    Weight(IP): 150

    GET /sapi/v1/sol-staking/sol/history/boostRewardsHistory

    https://developers.binance.com/docs/staking/sol-staking/history/Get-Boost-rewards-History

    Keyword Args:
        startTime (int, optional)
        endTime (int, optional)
        current (int, optional): Currently querying page. Start from 1. Default: 1
        size (int, optional): Default: 10, Max: 100
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    url_path = "/sapi/v1/sol-staking/sol/history/boostRewardsHistory"
    return self.sign_request("GET", url_path, {**kwargs})


def get_unclaimed_rewards(self, **kwargs):
    """Get Unclaimed Rewards (USER_DATA)

    Get Unclaimed Rewards

    Weight(IP): 150

    GET /sapi/v1/sol-staking/sol/history/unclaimedRewards

    https://developers.binance.com/docs/staking/sol-staking/history/Get-Unclaimed-rewards

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    url_path = "/sapi/v1/sol-staking/sol/history/unclaimedRewards"
    return self.sign_request("GET", url_path, {**kwargs})
