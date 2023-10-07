from binance.lib.utils import (
    check_required_parameter,
)
from binance.lib.utils import check_required_parameters


def get_simple_earn_flexible_product_list(self, **kwargs):
    """Get Simple Earn Flexible Product List (USER_DATA)

    Get available Simple Earn flexible product list

    Weight(IP): 150

    GET /sapi/v1/simple-earn/flexible/list

    https://binance-docs.github.io/apidocs/spot/en/#get-simple-earn-flexible-product-list-user_data

    Keyword Args:
        asset (str, optional)
        current (int, optional): Current querying page. Start from 1. Default:1
        size (int, optional): Default:10 Max:100
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/sapi/v1/simple-earn/flexible/list"
    return self.sign_request("GET", url_path, {**kwargs})


def get_simple_earn_locked_product_list(self, **kwargs):
    """Get Simple Earn Locked Product List (USER_DATA)

    Weight(IP): 150

    GET /sapi/v1/simple-earn/locked/list

    https://binance-docs.github.io/apidocs/spot/en/#get-simple-earn-locked-product-list-user_data

    Keyword Args:
        asset (str, optional)
        current (int, optional): Current querying page. Start from 1. Default:1
        size (int, optional): Default:10 Max:100
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/sapi/v1/simple-earn/locked/list"
    return self.sign_request("GET", url_path, {**kwargs})


def subscribe_flexible_product(self, productId: str, amount: float, **kwargs):
    """Subscribe Flexible Product (TRADE)

    Weight(IP): 1

    Rate Limit: 1/3s per account

    POST /sapi/v1/simple-earn/flexible/subscribe

    https://binance-docs.github.io/apidocs/spot/en/#subscribe-flexible-product-trade

    Args:
        productId (str)
        amount (float)
    Keyword Args:
        autoSubscribe (boolean, optional): true or false, default true.
        sourceAccount (str, optional): SPOT,FUND,ALL, default SPOT
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters([[productId, "productId"], [amount, "amount"]])

    params = {"productId": productId, "amount": amount, **kwargs}
    url_path = "/sapi/v1/simple-earn/flexible/subscribe"
    return self.sign_request("POST", url_path, params)


def subscribe_locked_product(self, projectId: str, amount: float, **kwargs):
    """Subscribe Locked Product (TRADE)

    Weight(IP): 1

    Rate Limit: 1/3s per account

    POST /sapi/v1/simple-earn/locked/subscribe

    https://binance-docs.github.io/apidocs/spot/en/#subscribe-locked-product-trade

    Args:
        projectId (str)
        amount (float)
    Keyword Args:
        autoSubscribe (boolean, optional): true or false, default true.
        sourceAccount (str, optional): SPOT,FUND,ALL, default SPOT
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters([[projectId, "projectId"], [amount, "amount"]])

    params = {"projectId": projectId, "amount": amount, **kwargs}
    url_path = "/sapi/v1/simple-earn/locked/subscribe"
    return self.sign_request("POST", url_path, params)


def redeem_flexible_product(self, productId: str, **kwargs):
    """Redeem Flexible Product (TRADE)

    Weight(IP): 1

    Rate Limit: 1/3s per account

    POST /sapi/v1/simple-earn/flexible/redeem

    https://binance-docs.github.io/apidocs/spot/en/#redeem-flexible-product-trade

    Args:
        productId (str)
    Keyword Args:
        redeemAll (boolean, optional): true or false, default to false
        amount (float, optional): if redeemAll is false, amount is mandatory
        destAccount (str, optional): SPOT,FUND,ALL, default SPOT
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(productId, "productId")

    params = {"productId": productId, **kwargs}
    url_path = "/sapi/v1/simple-earn/flexible/redeem"
    return self.sign_request("POST", url_path, params)


def redeem_locked_product(self, positionId: str, **kwargs):
    """Redeem Locked Product (TRADE)

    Weight(IP): 1

    Rate Limit: 1/3s per account

    POST /sapi/v1/simple-earn/locked/redeem

    https://binance-docs.github.io/apidocs/spot/en/#redeem-locked-product-trade

    Args:
        positionId (str)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(positionId, "positionId")

    params = {"positionId": positionId, **kwargs}
    url_path = "/sapi/v1/simple-earn/locked/redeem"
    return self.sign_request("POST", url_path, params)


def get_flexible_product_position(self, **kwargs):
    """Get Flexible Product Position (USER_DATA)

    Weight(IP): 150

    GET /sapi/v1/simple-earn/flexible/position

    https://binance-docs.github.io/apidocs/spot/en/#get-flexible-product-position-user_data

    Keyword Args:
        asset (str, optional)
        productId (str, optional)
        current (int, optional): Current querying page. Start from 1. Default:1
        size (int, optional): Default:10 Max:100
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/sapi/v1/simple-earn/flexible/position"
    return self.sign_request("GET", url_path, {**kwargs})


def get_locked_product_position(self, **kwargs):
    """Get Locked Product Position (USER_DATA)

    Weight(IP): 150

    GET /sapi/v1/simple-earn/locked/position

    https://binance-docs.github.io/apidocs/spot/en/#get-locked-product-position-user_data

    Keyword Args:
        asset (str, optional)
        positionId (str, optional)
        projectId (str, optional)
        current (int, optional): Current querying page. Start from 1. Default:1
        size (int, optional): Default:10 Max:100
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/sapi/v1/simple-earn/locked/position"
    return self.sign_request("GET", url_path, {**kwargs})


def simple_account(self, **kwargs):
    """Simple Account (USER_DATA)

    Weight(IP): 150

    GET /sapi/v1/simple-earn/account

    https://binance-docs.github.io/apidocs/spot/en/#simple-account-user_data

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/sapi/v1/simple-earn/account"
    return self.sign_request("GET", url_path, {**kwargs})


def get_flexible_subscription_record(self, **kwargs):
    """Get Flexible Subscription Record (USER_DATA)

    Weight(IP): 150

    GET /sapi/v1/simple-earn/flexible/history/subscriptionRecord

    https://binance-docs.github.io/apidocs/spot/en/#get-flexible-subscription-record-user_data

    Keyword Args:
        productId (str, optional)
        purchaseId (str, optional)
        asset (str, optional)
        startTime (int, optional): UTC timestamp in ms
        endTime (int, optional): UTC timestamp in ms
        current (int, optional): Current querying page. Start from 1. Default:1
        size (int, optional): Default:10 Max:100
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/sapi/v1/simple-earn/flexible/history/subscriptionRecord"
    return self.sign_request("GET", url_path, {**kwargs})


def get_locked_subscription_record(self, **kwargs):
    """Get Locked Subscription Record (USER_DATA)

    Weight(IP): 150

    GET /sapi/v1/simple-earn/locked/history/subscriptionRecord

    https://binance-docs.github.io/apidocs/spot/en/#get-locked-subscription-record-user_data

    Keyword Args:
        purchaseId (str, optional)
        asset (str, optional)
        startTime (int, optional): UTC timestamp in ms
        endTime (int, optional): UTC timestamp in ms
        current (int, optional): Current querying page. Start from 1. Default:1
        size (int, optional): Default:10 Max:100
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/sapi/v1/simple-earn/locked/history/subscriptionRecord"
    return self.sign_request("GET", url_path, {**kwargs})


def get_flexible_redemption_record(self, **kwargs):
    """Get Flexible Redemption Record (USER_DATA)

    Weight(IP): 150

    GET /sapi/v1/simple-earn/flexible/history/redemptionRecord

    https://binance-docs.github.io/apidocs/spot/en/#get-flexible-redemption-record-user_data

    Keyword Args:
        productId (str, optional)
        redeemId (str, optional)
        asset (str, optional)
        startTime (int, optional): UTC timestamp in ms
        endTime (int, optional): UTC timestamp in ms
        current (int, optional): Current querying page. Start from 1. Default:1
        size (int, optional): Default:10 Max:100
    """

    url_path = "/sapi/v1/simple-earn/flexible/history/redemptionRecord"
    return self.sign_request("GET", url_path, {**kwargs})


def get_locked_redemption_record(self, **kwargs):
    """Get Locked Redemption Record (USER_DATA)

    Weight(IP): 150

    GET /sapi/v1/simple-earn/locked/history/redemptionRecord

    https://binance-docs.github.io/apidocs/spot/en/#get-locked-redemption-record-user_data

    Keyword Args:
        positionId (str, optional)
        redeemId (str, optional)
        asset (str, optional)
        startTime (int, optional): UTC timestamp in ms
        endTime (int, optional): UTC timestamp in ms
        current (int, optional): Current querying page. Start from 1. Default:1
        size (int, optional): Default:10 Max:100
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/sapi/v1/simple-earn/locked/history/redemptionRecord"
    return self.sign_request("GET", url_path, {**kwargs})


def get_flexible_rewards_history(self, type: str, **kwargs):
    """Get Flexible Rewards History (USER_DATA)

    Weight(IP): 150

    GET /sapi/v1/simple-earn/flexible/history/rewardsRecord

    https://binance-docs.github.io/apidocs/spot/en/#get-flexible-rewards-history-user_data

    Args:
        type (str)
    Keyword Args:
        productId (str, optional)
        asset (str, optional)
        startTime (int, optional): UTC timestamp in ms
        endTime (int, optional): UTC timestamp in ms
    """
    check_required_parameter(type, "type")

    params = {"type": type, **kwargs}
    url_path = "/sapi/v1/simple-earn/flexible/history/rewardsRecord"
    return self.sign_request("GET", url_path, params)


def get_locked_rewards_history(self, **kwargs):
    """Get Locked Rewards History (USER_DATA)

    Weight(IP): 150

    GET /sapi/v1/simple-earn/locked/history/rewardsRecord

    https://binance-docs.github.io/apidocs/spot/en/#get-locked-rewards-history-user_data

    Keyword Args:
        positionId (str, optional)
        asset (str, optional)
        startTime (int, optional): UTC timestamp in ms
        endTime (int, optional): UTC timestamp in ms
        current (int, optional): Currently querying the page. Start from 1. Default:1
        size (int, optional): Default:10 Max:100
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/sapi/v1/simple-earn/locked/history/rewardsRecord"
    return self.sign_request("GET", url_path, {**kwargs})


def set_flexible_auto_subscribe(self, productId: str, autoSubscribe: bool, **kwargs):
    """Set Flexible Auto Subscribe (USER_DATA)

    Weight(IP): 150

    POST /sapi/v1/simple-earn/flexible/setAutoSubscribe

    https://binance-docs.github.io/apidocs/spot/en/#set-flexible-auto-subscribe-user_data

    Args:
        productId (str)
        autoSubscribe (boolean)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters(
        [[productId, "productId"], [autoSubscribe, "autoSubscribe"]]
    )

    params = {"productId": productId, "autoSubscribe": autoSubscribe, **kwargs}
    url_path = "/sapi/v1/simple-earn/flexible/setAutoSubscribe"
    return self.sign_request("POST", url_path, params)


def set_locked_auto_subscribe(self, positionId: str, autoSubscribe: bool, **kwargs):
    """Set Locked Auto Subscribe (USER_DATA)

    Weight(IP): 150

    POST /sapi/v1/simple-earn/locked/setAutoSubscribe

    https://binance-docs.github.io/apidocs/spot/en/#set-locked-auto-subscribe-user_data

    Args:
        positionId (str)
        autoSubscribe (boolean)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters(
        [[positionId, "positionId"], [autoSubscribe, "autoSubscribe"]]
    )

    params = {"positionId": positionId, "autoSubscribe": autoSubscribe, **kwargs}
    url_path = "/sapi/v1/simple-earn/locked/setAutoSubscribe"
    return self.sign_request("POST", url_path, params)


def get_flexible_personal_left_quota(self, productId: str, **kwargs):
    """Get Flexible Personal Left Quota (USER_DATA)

    Weight(IP): 150

    GET /sapi/v1/simple-earn/flexible/personalLeftQuota

    https://binance-docs.github.io/apidocs/spot/en/#get-flexible-personal-left-quota-user_data

    Args:
        productId (str)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(productId, "productId")

    params = {"productId": productId, **kwargs}
    url_path = "/sapi/v1/simple-earn/flexible/personalLeftQuota"
    return self.sign_request("GET", url_path, params)


def get_locked_personal_left_quota(self, projectId: str, **kwargs):
    """Get Locked Personal Left Quota (USER_DATA)

    Weight(IP): 150

    GET /sapi/v1/simple-earn/locked/personalLeftQuota

    https://binance-docs.github.io/apidocs/spot/en/#get-locked-personal-left-quota-user_data

    Args:
        projectId (str)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(projectId, "projectId")

    params = {"projectId": projectId, **kwargs}
    url_path = "/sapi/v1/simple-earn/locked/personalLeftQuota"
    return self.sign_request("GET", url_path, params)


def get_flexible_subscription_preview(self, productId: str, amount: float, **kwargs):
    """Get Flexible Subscription Preview (USER_DATA)

    Weight(IP): 150

    GET /sapi/v1/simple-earn/flexible/subscriptionPreview

    https://binance-docs.github.io/apidocs/spot/en/#get-flexible-subscription-preview-user_data

    Args:
        productId (str)
        amount (float)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters([[productId, "productId"], [amount, "amount"]])

    params = {"productId": productId, "amount": amount, **kwargs}
    url_path = "/sapi/v1/simple-earn/flexible/subscriptionPreview"
    return self.sign_request("GET", url_path, params)


def get_locked_subscription_preview(self, projectId: str, amount: float, **kwargs):
    """Get Locked Subscription Preview (USER_DATA)

    Weight(IP): 150

    GET /sapi/v1/simple-earn/locked/subscriptionPreview

    https://binance-docs.github.io/apidocs/spot/en/#get-locked-subscription-preview-user_data

    Args:
        projectId (str)
        amount (float)
    Keyword Args:
        autoSubscribe (boolean, optional): true or false, default true.
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters([[projectId, "projectId"], [amount, "amount"]])

    params = {"projectId": projectId, "amount": amount, **kwargs}
    url_path = "/sapi/v1/simple-earn/locked/subscriptionPreview"
    return self.sign_request("GET", url_path, params)


def get_rate_history(self, productId: str, **kwargs):
    """Get Rate History (USER_DATA)

    Weight(IP): 150

    GET /sapi/v1/simple-earn/flexible/history/rateHistory

    https://binance-docs.github.io/apidocs/spot/en/#get-rate-history-user_data

    Args:
        productId (str)
    Keyword Args:
        startTime (int, optional): UTC timestamp in ms
        endTime (int, optional): UTC timestamp in ms
        current (int, optional): Current querying page. Start from 1. Default:1
        size (int, optional): Default:10 Max:100
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(productId, "productId")

    params = {"productId": productId, **kwargs}
    url_path = "/sapi/v1/simple-earn/flexible/history/rateHistory"
    return self.sign_request("GET", url_path, params)


def get_collateral_record(self, **kwargs):
    """Get Collateral Record (USER_DATA)

    Weight(IP): 150

    GET /sapi/v1/simple-earn/flexible/history/collateralRecord

    https://binance-docs.github.io/apidocs/spot/en/#get-collateral-record-user_data

    Keyword Args:
        productId (str, optional)
        startTime (int, optional): UTC timestamp in ms
        endTime (int, optional): UTC timestamp in ms
        current (int, optional): Current querying page. Start from 1. Default:1
        size (int, optional): Default:10 Max:100
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/sapi/v1/simple-earn/flexible/history/collateralRecord"
    return self.sign_request("GET", url_path, {**kwargs})
