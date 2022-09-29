from binance.lib.utils import check_required_parameter
from binance.lib.utils import check_required_parameters


def savings_flexible_products(self, **kwargs):
    """Get Flexible Product List (USER_DATA)

    GET /sapi/v1/lending/daily/product/list

    https://binance-docs.github.io/apidocs/spot/en/#get-flexible-product-list-user_data

    Keyword Args:
        status (str, optional): "ALL", "SUBSCRIBABLE", "UNSUBSCRIBABLE"; default "ALL"
        featured (str, optional): "ALL", "true"; default "ALL"
        current (int, optional): Current query page. Default: 1, Min: 1
        size (int, optional): Default: 50, Max: 100
        recvWindow (int, optional): The value cannot be greater than 60000

    """

    return self.sign_request("GET", "/sapi/v1/lending/daily/product/list", kwargs)


def savings_flexible_user_left_quota(self, productId: str, **kwargs):
    """Get Left Daily Purchase Quota of Flexible Product (USER_DATA)

    GET /sapi/v1/lending/daily/userLeftQuota

    https://binance-docs.github.io/apidocs/spot/en/#get-left-daily-purchase-quota-of-flexible-product-user_data

    Args:
        productId (str)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000

    """

    check_required_parameter(productId, "productId")
    payload = {"productId": productId, **kwargs}
    return self.sign_request("GET", "/sapi/v1/lending/daily/userLeftQuota", payload)


def savings_purchase_flexible_product(self, productId: str, amount: float, **kwargs):
    """POST Purchase Flexible Product (USER_DATA)

    POST /sapi/v1/lending/daily/purchase

    https://binance-docs.github.io/apidocs/spot/en/#purchase-flexible-product-user_data

    Args:
        productId (str)
        amount (float)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000

    """

    check_required_parameters([[productId, "productId"], [amount, "amount"]])
    payload = {"productId": productId, "amount": amount, **kwargs}
    return self.sign_request("POST", "/sapi/v1/lending/daily/purchase", payload)


def savings_flexible_user_redemption_quota(self, productId: str, type: str, **kwargs):
    """Get Left Daily Redemption Quota of Flexible Product (USER_DATA)

    GET /sapi/v1/lending/daily/userRedemptionQuota

    https://binance-docs.github.io/apidocs/spot/en/#get-left-daily-redemption-quota-of-flexible-product-user_data

    Args:
        productId (str)
        type (str)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters([[productId, "productId"], [type, "type"]])
    payload = {"productId": productId, "type": type, **kwargs}
    return self.sign_request(
        "GET", "/sapi/v1/lending/daily/userRedemptionQuota", payload
    )


def savings_flexible_redeem(self, productId: str, amount: float, type: str, **kwargs):
    """Redeem Flexible Product (USER_DATA)

    POST /sapi/v1/lending/daily/redeem

    https://binance-docs.github.io/apidocs/spot/en/#redeem-flexible-product-user_data

    Args:
        productId (str)
        amount (float)
        type (str)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters(
        [[productId, "productId"], [amount, "amount"], [type, "type"]]
    )
    payload = {"productId": productId, "amount": amount, "type": type, **kwargs}
    return self.sign_request("POST", "/sapi/v1/lending/daily/redeem", payload)


def savings_flexible_product_position(self, **kwargs):
    """Get Flexible Product Position (USER_DATA)

    GET /sapi/v1/lending/daily/token/position

    https://binance-docs.github.io/apidocs/spot/en/#get-flexible-product-position-user_data

    Keyword Args:
        asset (str)
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/lending/daily/token/position", kwargs)


def savings_project_list(self, type: str, **kwargs):
    """Get Fixed and Activity Project List(USER_DATA)

    GET /sapi/v1/lending/project/list

    https://binance-docs.github.io/apidocs/spot/en/#get-fixed-and-activity-project-list-user_data

    Args:
        type (str)
    Keyword Args:
        asset (str, optional)
        status (str, optional): "ALL", "SUBSCRIBABLE", "UNSUBSCRIBABLE"; default "ALL"
        isSortAsc (bool, optional): By default, it's True
        sortBy (str, optional): "START_TIME", "LOT_SIZE", "INTEREST_RATE", "DURATION"; default "START_TIME"
        current (int, optional): Currently querying page. Start from 1. Default:1
        size (int, optional): Default:10, Max:100
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameter(type, "type")
    payload = {"type": type, **kwargs}
    return self.sign_request("GET", "/sapi/v1/lending/project/list", payload)


def savings_purchase_project(self, projectId: str, lot: int, **kwargs):
    """Purchase Fixed/Activity Project (USER_DATA)

    POST /sapi/v1/lending/customizedFixed/purchase

    https://binance-docs.github.io/apidocs/spot/en/#purchase-fixed-activity-project-user_data

    Args:
        projectId (str)
        lot (int)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters([[projectId, "projectId"], [lot, "lot"]])
    payload = {"projectId": projectId, "lot": lot, **kwargs}
    return self.sign_request(
        "POST", "/sapi/v1/lending/customizedFixed/purchase", payload
    )


def savings_project_position(self, **kwargs):
    """Get Fixed/Activity Project Position  (USER_DATA)

    GET /sapi/v1/lending/project/position/list

    https://binance-docs.github.io/apidocs/spot/en/#get-fixed-activity-project-position-user_data

    Keyword Args:
        asset (str, optional)
        projectId (str, optional)
        status (str, optional): "HOLDING", "REDEEMED"
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/lending/project/position/list", kwargs)


def savings_account(self, **kwargs):
    """Lending Account (USER_DATA)

    GET /sapi/v1/lending/union/account

    https://binance-docs.github.io/apidocs/spot/en/#lending-account-user_data

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/lending/union/account", kwargs)


def savings_purchase_record(self, lendingType: str, **kwargs):
    """Get Purchase Record (USER_DATA)

    GET /sapi/v1/lending/union/purchaseRecord

    https://binance-docs.github.io/apidocs/spot/en/#get-purchase-record-user_data

    Args:
        lendingType (str): "DAILY" for flexible, "ACTIVITY" for activity, "CUSTOMIZED_FIXED" for fixed
    Keyword Args:
        asset (str, optional)
        startTime (int, optional)
        endTime (int, optional)
        current (int, optional): Currently querying page. Start from 1. Default:1
        size (int, optional): Default:10 Max:100
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameter(lendingType, "lendingType")
    payload = {"lendingType": lendingType, **kwargs}
    return self.sign_request("GET", "/sapi/v1/lending/union/purchaseRecord", payload)


def savings_redemption_record(self, lendingType: str, **kwargs):
    """Get Redemption Record (USER_DATA)

    GET /sapi/v1/lending/union/redemptionRecord

    https://binance-docs.github.io/apidocs/spot/en/#get-redemption-record-user_data

    Args:
        lendingType (str): "DAILY" for flexible, "ACTIVITY" for activity, "CUSTOMIZED_FIXED" for fixed
    Keyword Args:
        asset (str, optional)
        startTime (int, optional)
        endTime (int, optional)
        current (int, optional): Currently querying page. Start from 1. Default:1
        size (int, optional): Default:10 Max:100
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameter(lendingType, "lendingType")
    payload = {"lendingType": lendingType, **kwargs}
    return self.sign_request("GET", "/sapi/v1/lending/union/redemptionRecord", payload)


def savings_interest_history(self, lendingType: str, **kwargs):
    """Get Interest History (USER_DATA)

    GET /sapi/v1/lending/union/interestHistory

    https://binance-docs.github.io/apidocs/spot/en/#get-interest-history-user_data-2

    Args:
        lendingType (str): "DAILY" for flexible, "ACTIVITY" for activity, "CUSTOMIZED_FIXED" for fixed
    Keyword Args:
        asset (str, optional)
        startTime (int, optional)
        endTime (int, optional)
        current (int, optional): Currently querying page. Start from 1. Default:1
        size (int, optional): Default:10 Max:100
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameter(lendingType, "lendingType")
    payload = {"lendingType": lendingType, **kwargs}
    return self.sign_request("GET", "/sapi/v1/lending/union/interestHistory", payload)


def savings_change_position(self, projectId: str, lot: int, **kwargs):
    """Change Fixed/Activity Position to Daily Position(USER_DATA)

    POST /sapi/v1/lending/positionChanged

    https://binance-docs.github.io/apidocs/spot/en/#change-fixed-activity-position-to-daily-position-user_data

    Args:
        projectId (str)
        lot (int)
    Keyword Args:
        positionId (int, optional): for fixed position
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters([[projectId, "projectId"], [lot, "lot"]])
    payload = {"projectId": projectId, "lot": lot, **kwargs}
    return self.sign_request("POST", "/sapi/v1/lending/positionChanged", payload)
