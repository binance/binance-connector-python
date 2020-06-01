from binance.lib.utils import check_required_parameter
from binance.lib.utils import check_required_parameters


def savings_flexible_products(self, **kwargs):
    """ Get Flexible Product List (USER_DATA)

    GET /sapi/v1/lending/daily/product/list

    https://binance-docs.github.io/apidocs/spot/en/#get-flexible-product-list-user_data

    """

    return self.sign_request('GET', '/sapi/v1/lending/daily/product/list', kwargs)


def savings_flexible_user_left_quota(self, productId: str, **kwargs):
    """ Get Left Daily Purchase Quota of Flexible Product (USER_DATA)

    GET /sapi/v1/lending/daily/userLeftQuota

    https://binance-docs.github.io/apidocs/spot/en/#get-left-daily-purchase-quota-of-flexible-product-user_data

    """

    check_required_parameter(productId, 'productId')
    payload = {'productId': productId, **kwargs}
    return self.sign_request('GET', '/sapi/v1/lending/daily/userLeftQuota', payload)


def savings_purchase_flexible_product(self, productId: str, amount, **kwargs):
    """ POST Left Daily Purchase Quota of Flexible Product (USER_DATA)

    POST /sapi/v1/lending/daily/purchase

    https://binance-docs.github.io/apidocs/spot/en/#get-left-daily-purchase-quota-of-flexible-product-user_data

    """

    check_required_parameters([[productId, 'productId'], [amount, 'amount']])
    payload = {'productId': productId, 'amount': amount, **kwargs}
    return self.sign_request('POST', '/sapi/v1/lending/daily/purchase', payload)


def savings_flexible_user_redemption_quota(self, productId: str, type: str, **kwargs):
    """ Get Left Daily Redemption Quota of Flexible Product (USER_DATA)

    GET /sapi/v1/lending/daily/userRedemptionQuota

    https://binance-docs.github.io/apidocs/spot/en/#get-left-daily-purchase-quota-of-flexible-product-user_data

    """

    check_required_parameters([[productId, 'productId'], [type, 'type']])
    payload = {'productId': productId, 'type': type, **kwargs}
    return self.sign_request('GET', '/sapi/v1/lending/daily/userRedemptionQuota', payload)


def savings_flexible_redeem(self, productId: str, amount, type: str, **kwargs):
    """ Redeem Flexible Product (USER_DATA)

    POST /sapi/v1/lending/daily/redeem

    https://binance-docs.github.io/apidocs/spot/en/#redeem-flexible-product-user_data

    """

    check_required_parameters([[productId, 'productId'], [amount, 'amount'], [type, 'type']])
    payload = {'productId': productId, 'amount': amount, 'type': type, **kwargs}
    return self.sign_request('POST', '/sapi/v1/lending/daily/redeem', payload)


def savings_flexible_product_position(self, asset: str, **kwargs):
    """ Get Flexible Product Position (USER_DATA)

    GET /sapi/v1/lending/daily/token/position

    https://binance-docs.github.io/apidocs/spot/en/#get-flexible-product-position-user_data

    """

    check_required_parameter(asset, 'asset')
    payload = {'asset': asset, **kwargs}
    return self.sign_request('GET', '/sapi/v1/lending/daily/token/position', payload)


def savings_product_list(self, type: str, **kwargs):
    """ Get Fixed and Customized Fixed Project List(USER_DATA)

    GET /sapi/v1/lending/project/list

    https://binance-docs.github.io/apidocs/spot/en/#get-fixed-and-customized-fixed-project-list-user_data

    """

    check_required_parameter(type, 'type')
    payload = {'type': type, **kwargs}
    return self.sign_request('GET', '/sapi/v1/lending/project/list', payload)


def savings_purchase_customized_project(self, type: str, **kwargs):
    """ Purchase Customized Fixed Project (USER_DATA)

    POST /sapi/v1/lending/customizedFixed/purchase

    https://binance-docs.github.io/apidocs/spot/en/#purchase-customized-fixed-project-user_data

    """

    check_required_parameter(type, 'type')
    payload = {'type': type, **kwargs}
    return self.sign_request('POST', '/sapi/v1/lending/customizedFixed/purchase', payload)


def savings_customized_position(self, asset: str, **kwargs):
    """ Get Customized Fixed Project Position (USER_DATA)

    GET /sapi/v1/lending/project/position/list

    https://binance-docs.github.io/apidocs/spot/en/#purchase-customized-fixed-project-user_data

    """

    check_required_parameter(asset, 'asset')
    payload = {'asset': asset, **kwargs}
    return self.sign_request('GET', '/sapi/v1/lending/project/position/list', payload)


def savings_account(self, **kwargs):
    """ Lending Account (USER_DATA)

    GET /sapi/v1/lending/union/account

    https://binance-docs.github.io/apidocs/spot/en/#lending-account-user_data

    """

    return self.sign_request('GET', '/sapi/v1/lending/union/account', kwargs)


def savings_purchase_record(self, lendingType: str, **kwargs):
    """ Get Purchase Record (USER_DATA)

    GET /sapi/v1/lending/union/purchaseRecord

    https://binance-docs.github.io/apidocs/spot/en/#get-purchase-record-user_data

    """

    check_required_parameter(lendingType, 'lendingType')
    payload = {'lendingType': lendingType, **kwargs}
    return self.sign_request('GET', '/sapi/v1/lending/union/purchaseRecord', payload)


def savings_redemption_record(self, lendingType: str, **kwargs):
    """ Get Redemption Record (USER_DATA)

    GET /sapi/v1/lending/union/redemptionRecord

    https://binance-docs.github.io/apidocs/spot/en/#get-redemption-record-user_data

    """

    check_required_parameter(lendingType, 'lendingType')
    payload = {'lendingType': lendingType, **kwargs}
    return self.sign_request('GET', '/sapi/v1/lending/union/redemptionRecord', payload)


def savings_interest_history(self, lendingType: str, **kwargs):
    """ Get Interest History (USER_DATA)

    GET /sapi/v1/lending/union/interestHistory

    https://binance-docs.github.io/apidocs/spot/en/#get-interest-history-user_data-2

    """

    check_required_parameter(lendingType, 'lendingType')
    payload = {'lendingType': lendingType, **kwargs}
    return self.sign_request('GET', '/sapi/v1/lending/union/interestHistory', payload)
