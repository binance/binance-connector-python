from binance.lib.utils import (
    check_required_parameter,
)
from binance.lib.utils import check_required_parameters


def staking_product_list(self, product: str, **kwargs):
    """Get Staking Product List (USER_DATA)

    Get available Staking product list.

    Weight(IP): 1

    GET /sapi/v1/staking/productList

    https://binance-docs.github.io/apidocs/spot/en/#get-staking-product-list-user_data

    Args:
        product (str)
    Keyword Args:
        asset (str, optional)
        current (int, optional): Currently querying page. Start from 1. Default:1
        size (int, optional): Default:10, Max:100
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(product, "product")

    params = {"product": product, **kwargs}
    url_path = "/sapi/v1/staking/productList"
    return self.sign_request("GET", url_path, params)


def staking_purchase_product(
    self, product: str, productId: str, amount: float, **kwargs
):
    """Purchase Staking Product (USER_DATA)

    Weight(IP): 1

    POST /sapi/v1/staking/purchase

    https://binance-docs.github.io/apidocs/spot/en/#purchase-staking-product-user_data

    Args:
        product (str)
        productId (str)
        amount (float)
    Keyword Args:
        renewable (str, optional): true or false, default false. Active if product is `STAKING` or `L_DEFI`
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters(
        [[product, "product"], [productId, "productId"], [amount, "amount"]]
    )

    params = {"product": product, "productId": productId, "amount": amount, **kwargs}
    url_path = "/sapi/v1/staking/purchase"
    return self.sign_request("POST", url_path, params)


def staking_redeem_product(self, product: str, productId: str, **kwargs):
    """Redeem Staking Product (USER_DATA)

    Redeem Staking product. Locked staking and Locked DeFI staking belong to early redemption, redeeming in advance will result in loss of interest that you have earned.

    Weight(IP): 1

    POST /sapi/v1/staking/redeem

    https://binance-docs.github.io/apidocs/spot/en/#redeem-staking-product-user_data

    Args:
        product (str)
        productId (str)
    Keyword Args:
        positionId (str, optional): Mandatory if product is `STAKING` or `L_DEFI`
        amount (float, optional): Mandatory if product is `F_DEFI`
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters([[product, "product"], [productId, "productId"]])

    params = {"product": product, "productId": productId, **kwargs}
    url_path = "/sapi/v1/staking/redeem"
    return self.sign_request("POST", url_path, params)


def staking_product_position(self, product: str, **kwargs):
    """Get Staking Product Position (USER_DATA)

    Weight(IP): 1

    GET /sapi/v1/staking/position

    https://binance-docs.github.io/apidocs/spot/en/#get-staking-product-position-user_data

    Args:
        product (str)
    Keyword Args:
        productId (str, optional)
        asset (str, optional)
        current (int, optional): Currently querying the page. Start from 1. Default:1
        size (int, optional): Default:10, Max:100
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(product, "product")

    params = {"product": product, **kwargs}
    url_path = "/sapi/v1/staking/position"
    return self.sign_request("GET", url_path, params)


def staking_history(self, product: str, txnType: str, **kwargs):
    """Get Staking History (USER_DATA)

    Weight(IP): 1

    GET /sapi/v1/staking/stakingRecord

    https://binance-docs.github.io/apidocs/spot/en/#get-staking-history-user_data

    Args:
        product (str)
        txnType (str)
    Keyword Args:
        asset (str, optional)
        startTime (int, optional)
        endTime (int, optional)
        current (int, optional): Currently querying the page. Start from 1. Default:1
        size (int, optional): Default:10, Max:100
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters([[product, "product"], [txnType, "txnType"]])

    params = {"product": product, "txnType": txnType, **kwargs}
    url_path = "/sapi/v1/staking/stakingRecord"
    return self.sign_request("GET", url_path, params)


def staking_set_auto_staking(
    self, product: str, positionId: str, renewable: str, **kwargs
):
    """Set Auto Staking (USER_DATA)

    Set auto staking on Locked Staking or Locked DeFi Staking

    Weight(IP): 1

    POST /sapi/v1/staking/setAutoStaking

    https://binance-docs.github.io/apidocs/spot/en/#set-auto-staking-user_data

    Args:
        product (str)
        positionId (str)
        renewable (str)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters(
        [[product, "product"], [positionId, "positionId"], [renewable, "renewable"]]
    )

    params = {
        "product": product,
        "positionId": positionId,
        "renewable": renewable,
        **kwargs,
    }
    url_path = "/sapi/v1/staking/setAutoStaking"
    return self.sign_request("POST", url_path, params)


def staking_product_quota(self, product: str, productId: str, **kwargs):
    """Get Personal Left Quota of Staking Product (USER_DATA)

    Weight(IP): 1

    GET /sapi/v1/staking/personalLeftQuota

    https://binance-docs.github.io/apidocs/spot/en/#get-personal-left-quota-of-staking-product-user_data

    Args:
        product (str)
        productId (str)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters([[product, "product"], [productId, "productId"]])

    params = {"product": product, "productId": productId, **kwargs}
    url_path = "/sapi/v1/staking/personalLeftQuota"
    return self.sign_request("GET", url_path, params)
