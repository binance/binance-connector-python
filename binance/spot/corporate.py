from binance.lib.utils import check_required_parameter
from binance.lib.utils import check_required_parameters


def sub_account_list(self, **kwargs):
    """ Query Sub-account List(For Master Account)
    Fetch sub account list.

    GET /wapi/v3/sub-account/list.html

    https://binance-docs.github.io/apidocs/spot/en/#query-sub-account-list-for-master-account

    """

    return self.limited_encoded_sign_request('GET', '/wapi/v3/sub-account/list.html', kwargs)


def sub_account_transfer_history(self, email: str, **kwargs):
    """ Query Sub-account Transfer History(For Master Account)
    Fetch transfer history list

    GET /wapi/v3/sub-account/transfer/history.html

    https://binance-docs.github.io/apidocs/spot/en/#query-sub-account-list-for-master-account

    """

    check_required_parameter(email, 'email')
    payload = {'email': email, **kwargs}

    return self.limited_encoded_sign_request('GET', '/wapi/v3/sub-account/transfer/history.html', payload)


def sub_account_transfer(self, fromEmail: str, toEmail: str, asset: str, amount, **kwargs):
    """ Sub-account Transfer(For Master Account)
    Execute sub-account transfer

    POST /wapi/v3/sub-account/transfer.html

    https://binance-docs.github.io/apidocs/spot/en/#sub-account-transfer-for-master-account

    """

    check_required_parameters([
        [fromEmail, 'fromEmail'],
        [toEmail, 'toEmail'],
        [asset, 'asset'],
        [amount, 'amount']
    ])
    payload = {
        'fromEmail': fromEmail,
        'toEmail': toEmail,
        'asset': asset,
        'amount': amount,
        **kwargs
    }
    return self.limited_encoded_sign_request('POST', '/wapi/v3/sub-account/transfer.html', payload)


def sub_account_asset(self, email: str, **kwargs):
    """ Query Sub-account Assets(For Master Account)
    Fetch sub-account assets

    GET /wapi/v3/sub-account/assets.html

    https://binance-docs.github.io/apidocs/spot/en/#sub-account-transfer-for-master-account

    """

    check_required_parameter(email, 'email')
    payload = {'email': email, **kwargs}
    return self.limited_encoded_sign_request('GET', '/wapi/v3/sub-account/assets.html', payload)


def sub_account_deposit_address(self, email: str, coin: str, **kwargs):
    """ Get Sub-account Deposit Address (For Master Account)
    Fetch sub-account deposit address

    GET /sapi/v1/capital/deposit/subAddress

    https://binance-docs.github.io/apidocs/spot/en/#get-sub-account-deposit-address-for-master-account

    """

    check_required_parameters([[email, 'email'], [coin, 'coin']])
    payload = {'email': email, 'coin': coin, **kwargs}
    return self.limited_encoded_sign_request('GET', '/sapi/v1/capital/deposit/subAddress', payload)


def sub_account_deposit_history(self, email: str, **kwargs):
    """ Get Sub-account Deposit History (For Master Account)
    Fetch sub-account deposit history

    GET /sapi/v1/capital/deposit/subHisrec

    https://binance-docs.github.io/apidocs/spot/en/#get-sub-account-deposit-address-for-master-account

    """

    check_required_parameter(email, 'email')
    payload = {'email': email, **kwargs}
    return self.limited_encoded_sign_request('GET', '/sapi/v1/capital/deposit/subHisrec', payload)


def sub_account_status(self, **kwargs):
    """ Get Sub-account's Status on Margin/Futures(For Master Account)

    GET /sapi/v1/capital/status

    https://binance-docs.github.io/apidocs/spot/en/#get-sub-account-39-s-status-on-margin-futures-for-master-account

    """

    return self.limited_encoded_sign_request('GET', '/sapi/v1/sub-account/status', kwargs)


def sub_account_enable_margin(self, email: str, **kwargs):
    """ Enable Margin for Sub-account (For Master Account)

    POST /sapi/v1/sub-account/margin/enable

    https://binance-docs.github.io/apidocs/spot/en/#enable-margin-for-sub-account-for-master-account

    """

    check_required_parameter(email, 'email')
    payload = {'email': email, **kwargs}
    return self.limited_encoded_sign_request('POST', '/sapi/v1/sub-account/margin/enable', payload)


def sub_account_margin_account(self, email: str, **kwargs):
    """ Get Detail on Sub-account's Margin Account (For Master Account)

    GET /sapi/v1/sub-account/margin/account

    https://binance-docs.github.io/apidocs/spot/en/#get-detail-on-sub-account-39-s-margin-account-for-master-account

    """

    check_required_parameter(email, 'email')
    payload = {'email': email, **kwargs}
    return self.limited_encoded_sign_request('GET', '/sapi/v1/sub-account/margin/account', payload)


def sub_account_margin_account_summary(self, **kwargs):
    """ Get Summary of Sub-account's Margin Account (For Master Account)

    GET /sapi/v1/sub-account/margin/accountSummary

    https://binance-docs.github.io/apidocs/spot/en/#get-summary-of-sub-account-39-s-margin-account-for-master-account

    """

    return self.sign_request('GET', '/sapi/v1/sub-account/margin/accountSummary', kwargs)


def sub_account_enable_futures(self, email: str, **kwargs):
    """ Enable Futures for Sub-account (For Master Account)

    POST /sapi/v1/sub-account/futures/enable

    https://binance-docs.github.io/apidocs/spot/en/#enable-futures-for-sub-account-for-master-account

    """

    check_required_parameter(email, 'email')
    payload = {'email': email, **kwargs}
    return self.limited_encoded_sign_request('POST', '/sapi/v1/sub-account/futures/enable', payload)


def sub_account_futures_account(self, email: str, **kwargs):
    """ Get Detail on Sub-account's Futures Account (For Master Account)

    GET /sapi/v1/sub-account/futures/account

    https://binance-docs.github.io/apidocs/spot/en/#get-detail-on-sub-account-39-s-futures-account-for-master-account

    """

    check_required_parameter(email, 'email')
    payload = {'email': email, **kwargs}
    return self.limited_encoded_sign_request('GET', '/sapi/v1/sub-account/futures/account', payload)


def sub_account_futures_account_summary(self, **kwargs):
    """ Get Summary of Sub-account's Futures Account (For Master Account)

    GET /sapi/v1/sub-account/futures/accountSummary

    https://binance-docs.github.io/apidocs/spot/en/#get-summary-of-sub-account-39-s-futures-account-for-master-account

    """

    return self.sign_request('GET', '/sapi/v1/sub-account/futures/accountSummary', kwargs)


def sub_account_futures_position_risk(self, email: str, **kwargs):
    """ Get Futures Postion-Risk of Sub-account (For Master Account)

    GET /sapi/v1/sub-account/futures/positionRisk

    https://binance-docs.github.io/apidocs/spot/en/#get-futures-postion-risk-of-sub-account-for-master-account

    """

    check_required_parameter(email, 'email')
    payload = {'email': email, **kwargs}

    return self.limited_encoded_sign_request('GET', '/sapi/v1/sub-account/futures/positionRisk', payload)


def sub_account_futures_transfer(self, email: str, asset: str, amount, type: int, **kwargs):
    """ Futures Transfer for Sub-account（For Master Account）

    GET /sapi/v1/sub-account/futures/transfer

    https://binance-docs.github.io/apidocs/spot/en/#get-futures-postion-risk-of-sub-account-for-master-account

    """

    check_required_parameters([
        [email, 'email'],
        [asset, 'asset'],
        [amount, 'amount'],
        [type, 'type']
    ])
    payload = {'email': email, 'asset': asset, 'amount': amount, 'type': type, **kwargs}
    return self.limited_encoded_sign_request('POST', '/sapi/v1/sub-account/futures/transfer', payload)


def sub_account_margin_transfer(self, email: str, asset: str, amount, type: int, **kwargs):
    """ Margin Transfer for Sub-account（For Master Account)

    GET /sapi/v1/sub-account/margin/transfer

    https://binance-docs.github.io/apidocs/spot/en/#margin-transfer-for-sub-account-for-master-account

    """

    check_required_parameters([
        [email, 'email'],
        [asset, 'asset'],
        [amount, 'amount'],
        [type, 'type']
    ])
    payload = {'email': email, 'asset': asset, 'amount': amount, 'type': type, **kwargs}
    return self.limited_encoded_sign_request('POST', '/sapi/v1/sub-account/margin/transfer', payload)


def sub_account_transfer_to_sub(self, toEmail: str, asset: str, amount, **kwargs):
    """ Transfer to Sub-account of Same Master（For Sub-account）

    POST /sapi/v1/sub-account/transfer/subToSub

    https://binance-docs.github.io/apidocs/spot/en/#transfer-to-sub-account-of-same-master-for-sub-account

    """

    check_required_parameters([
        [toEmail, 'toEmail'],
        [asset, 'asset'],
        [amount, 'amount']
    ])
    payload = {'toEmail': toEmail, 'asset': asset, 'amount': amount, **kwargs}
    return self.limited_encoded_sign_request('POST', '/sapi/v1/sub-account/transfer/subToSub', payload)


def sub_account_transfer_to_master(self, asset: str, amount, **kwargs):
    """ Transfer to Master（For Sub-account）

    POST /sapi/v1/sub-account/transfer/subToMaster

    https://binance-docs.github.io/apidocs/spot/en/#transfer-to-master-for-sub-account

    """

    check_required_parameters([
        [asset, 'asset'],
        [amount, 'amount']
    ])
    payload = {'asset': asset, 'amount': amount, **kwargs}
    return self.sign_request('POST', '/sapi/v1/sub-account/transfer/subToMaster', payload)


def sub_account_transfer_sub_account_history(self, **kwargs):
    """ Sub-account Transfer History (For Sub-account)

    POST /sapi/v1/sub-account/transfer/subUserHistory

    https://binance-docs.github.io/apidocs/spot/en/#transfer-to-master-for-sub-account

    """

    return self.sign_request('GET', '/sapi/v1/sub-account/transfer/subUserHistory', kwargs)
