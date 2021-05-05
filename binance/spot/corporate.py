from binance.lib.utils import check_required_parameter
from binance.lib.utils import check_required_parameters


def sub_account_create(self, subAccountString: str, **kwargs):
    """ Create a Virtual Sub-account(For Master Account)
    Generate a virtual sub account under the master account

    Parameteres:
    | subAccountString | mandatory | string | Sub-account string |
    | recvWindow       | optional  | long   |                    |

    POST /sapi/v1/sub-account/virtualSubAccount

    https://binance-docs.github.io/apidocs/spot/en/#create-a-virtual-sub-account-for-master-account

    """

    check_required_parameter(subAccountString, 'subAccountString')
    payload = {'subAccountString': subAccountString, **kwargs}

    return self.limited_encoded_sign_request('POST', '/sapi/v1/sub-account/virtualSubAccount', payload)


def sub_account_list(self, **kwargs):
    """ Query Sub-account List(For Master Account)
    Fetch sub account list.

    Parameteres:
    | email      | optional | string | Sub-account email   |
    | isFreeze   | optional | string | true or false       |
    | page       | optional | int    | default 1           |
    | limit      | optional | int    | default 10, max 200 |
    | recvWindow | optional | long   |                     |

    GET /sapi/v1/sub-account/list

    https://binance-docs.github.io/apidocs/spot/en/#query-sub-account-list-sapi-for-master-account

    """

    return self.limited_encoded_sign_request('GET', '/sapi/v1/sub-account/list', kwargs)


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


def sub_account_assets(self, email: str, **kwargs):
    """ Query Sub-account Assets(For Master Account)
    Fetch sub-account assets

    GET /sapi/v3/sub-account/assets

    https://binance-docs.github.io/apidocs/spot/en/#query-sub-account-assets-sapi-for-master-account

    """

    check_required_parameter(email, 'email')
    payload = {'email': email, **kwargs}
    return self.limited_encoded_sign_request('GET', '/sapi/v3/sub-account/assets', payload)


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


def sub_account_futures_asset_transfer_history(self, email: str, futuresType: int, **kwargs):
    """ Query Sub-account Futures Asset Transfer History(For Master Account)

    GET /sapi/v1/sub-account/futures/internalTransfer
    
    https://binance-docs.github.io/apidocs/spot/en/#sub-account-spot-asset-transfer-for-master-account

    Parameters:
    | email       | mandatory | string | Sub-account email                                   |
    | futuresType | mandatory | int    | 1  : USDT-maringed Futues，2: Coin-margined Futures |
    | startTime   | optional  | int    | Default return the history with in 100 days         |
    | endTime     | optional  | int    | Default return the history with in 100 days         |
    | page        | optional  | int    | Default value: 1                                    |
    | limit       | optional  | int    | Default value: 50, Max value: 500                   |
    | recvWindow  | optional  | int    |                                                     |

    """
    check_required_parameters([
        [email, 'email'],
        [futuresType, 'futuresType']
    ])
    payload = {'email': email, 'futuresType': futuresType, **kwargs}
    return self.sign_request('GET', '/sapi/v1/sub-account/futures/internalTransfer', payload)


def sub_account_futures_asset_transfer(self, fromEmail: str, toEmail: str, futuresType: int, asset: str, amount, **kwargs):
    """ Query Sub-account Futures Asset Transfer History(For Master Account)

    POST /sapi/v1/sub-account/futures/internalTransfer

    https://binance-docs.github.io/apidocs/spot/en/#sub-account-futures-asset-transfer-for-master-account

    Parameters:
    | fromEmail   | mandatory | string | Sender email                                     |
    | toEmail     | mandatory | string | Recipient email                                  |
    | futuresType | mandatory | int    | 1:USDT-margined Futues，2: Coin-margined Futures |
    | asset       | mandatory | string |                                                  |
    | amount      | mandatory | float  |                                                  |
    | recvWindow  | optional  | int    |                                                  |

    """
    check_required_parameters([
        [fromEmail, 'fromEmail'],
        [toEmail, 'toEmail'],
        [futuresType, 'futuresType'],
        [asset, 'asset'],
        [amount, 'amount']
    ])
    payload = {
        'fromEmail': fromEmail,
        'toEmail': toEmail,
        'futuresType': futuresType,
        'asset': asset,
        'amount': amount,
        **kwargs
    }
    return self.sign_request('POST', '/sapi/v1/sub-account/futures/internalTransfer', payload)


def sub_account_spot_summary(self, **kwargs):
    """ Query Sub-account Spot Assets Summary (For Master Account)

    GET /sapi/v1/sub-account/spotSummary

    https://binance-docs.github.io/apidocs/spot/en/#query-sub-account-assets-for-master-account

    Parameters:
    | email      | optional | string | Sub account email  |
    | page       | optional | int    | default 1          |
    | size       | optional | int    | default 10, max 20 |
    | recvWindow | optional | int    |                    |
    """
    
    return self.sign_request('GET', '/sapi/v1/sub-account/spotSummary', kwargs)


def sub_account_universal_transfer(self, fromAccountType: str, toAccountType: str, asset: str, amount: float, **kwargs):
    """ Universal Transfer (For Master Account)

    POST /sapi/v1/sub-account/universalTransfer

    https://binance-docs.github.io/apidocs/spot/en/#universal-transfer-for-master-account

    Parameters:
    | fromEmail       | optional  | string  |                                    |
    | toEmail         | optional  | string  |                                    |
    | fromAccountType | mandatory | string  | "SPOT","USDT_FUTURE","COIN_FUTURE" |
    | toAccountType   | mandatory | string  | "SPOT","USDT_FUTURE","COIN_FUTURE" |
    | asset           | mandatory | string  |                                    |
    | amount          | mandatory | float  |                                    |
    | recvWindow      | optional  | int     |                                    |

    You need to enable "internal transfer" option for the api key which requests this endpoint.
    Transfer from master account by default if fromEmail is not sent.
    Transfer to master account by default if toEmail is not sent.
    Transfer between futures accounts is not supported.

    """
    check_required_parameters([
        [fromAccountType, 'fromAccountType'],
        [toAccountType, 'toAccountType'],
        [asset, 'asset'],
        [amount, 'amount']
    ])

    payload = {
        'fromAccountType': fromAccountType,
        'toAccountType': toAccountType,
        'asset': asset,
        'amount': amount,
        **kwargs
    }
    return self.limited_encoded_sign_request('POST', '/sapi/v1/sub-account/universalTransfer', payload)


def sub_account_universal_transfer_history(self, **kwargs):
    """ Query Universal Transfer History (For Master Account)

    GET /sapi/v1/sub-account/universalTransfer

    https://binance-docs.github.io/apidocs/spot/en/#query-universal-transfer-history-for-master-account

    Parameters:
    | fromEmail   | optional | string |                    |
    | toEmail     | optional | string |                    |
    | startTime   | optional | int    |                    |
    | endTime     | optional | int    |                    |
    | page        | optional | int    |                    |
    | limit       | optional | int    | default 10, max 20 |
    | recvWindow  | optional | int    |                    |

    fromEmail and toEmail cannot be sent at the same time.
    Return fromEmail equal master account email by default.
    Only get the latest history of past 30 days.

    """

    return self.limited_encoded_sign_request('GET', '/sapi/v1/sub-account/universalTransfer', kwargs)


def sub_account_futures_account(self, email: str, futuresType: int, **kwargs):
    """ Get Detail on Sub-account's Futures Account V2 (For Master Account)

    GET /sapi/v2/sub-account/futures/account

    https://binance-docs.github.io/apidocs/spot/en/#get-detail-on-sub-account-39-s-futures-account-v2-for-master-account

    Parameters:
    | email       | mandatory | string | Sub-account email                                |
    | futuresType | mandatory | int    | 1:USDT Margined Futures, 2:COIN Margined Futures |
    | recvWindow  | optional  | int    |                                                  |

    """

    check_required_parameters([
        [email, 'email'],
        [futuresType, 'futuresType']
    ])

    payload = {
        'email': email,
        'futuresType': futuresType,
        **kwargs
    }
    return self.limited_encoded_sign_request('GET', '/sapi/v2/sub-account/futures/account', payload)


def sub_account_futures_account_summary(self, futuresType: int, **kwargs):
    """ Get Summary of Sub-account's Futures Account V2 (For Master Account)

    GET /sapi/v2/sub-account/futures/accountSummary

    https://binance-docs.github.io/apidocs/spot/en/#get-detail-on-sub-account-39-s-futures-account-v2-for-master-account

    Parameters:
    | futuresType | mandatory | int    | 1:USDT Margined Futures, 2:COIN Margined Futures |
    | page        | optional  | int    | default:1                                        |
    | limit       | optional | int     | default 10, max 20                               |
    | recvWindow  | optional  | int    |                                                  |

    """
    check_required_parameter(futuresType, 'futuresType')

    payload = {
        'futuresType': futuresType,
        **kwargs
    }

    return self.sign_request('GET', '/sapi/v2/sub-account/futures/accountSummary', payload)


def sub_account_futures_position_risk(self, email: str, futuresType: str, **kwargs):
    """ Get Futures Position-Risk of Sub-account V2 (For Master Account)

    GET /sapi/v2/sub-account/futures/positionRisk

    https://binance-docs.github.io/apidocs/spot/en/#get-futures-position-risk-of-sub-account-v2-for-master-account

    Parameters:
    | email       | mandatory | string | Sub-account email                                |
    | futuresType | mandatory | int    | 1:USDT Margined Futures, 2:COIN Margined Futures |
    | recvWindow  | optional  | int    |                                                  |

    """

    check_required_parameters([
        [email, 'email'],
        [futuresType, 'futuresType']
    ])

    payload = {
        'email': email,
        'futuresType': futuresType,
        **kwargs
    }
    return self.limited_encoded_sign_request('GET', '/sapi/v2/sub-account/futures/positionRisk', payload)


def sub_account_spot_transfer_history(self, **kwargs):
    """ Query Sub-account Spot Asset Transfer History (SAPI For Master Account)

    GET /sapi/v1/sub-account/sub/transfer/history

    https://binance-docs.github.io/apidocs/spot/en/#query-sub-account-spot-asset-transfer-history-for-master-account

    Parameters:
    | fromEmail   | optional | string | Sub-account email                           |
    | toEmail     | optional | string | Sub-account email                           |
    | startTime   | optional | int    | Default return the history with in 100 days |
    | endTime     | optional | int    | Default return the history with in 100 days |
    | page        | optional | int    | Default value: 1                            |
    | limit       | optional | int    | Default value: 500                          |
    | recvWindow  | optional | int    |                                             |

    """

    return self.limited_encoded_sign_request('GET', '/sapi/v1/sub-account/sub/transfer/history', kwargs)


def sub_account_enable_leverage_token(self, email: str, enableBlvt: bool, **kwargs):
    """ Enable Leverage Token for Sub-account(For Master Account)
    Enable leverage token for sub-account

    Parameteres:
    | email      | mandatory | string | Sub-account email |
    | enableBlvt | mandatory | bool   | Only true for now |
    | recvWindow | optional  | long   |                   |

    POST /sapi/v1/sub-account/blvt/enable

    https://binance-docs.github.io/apidocs/spot/en/#enable-leverage-token-for-sub-account-for-master-account

    """

    check_required_parameters([[email, 'email'], [enableBlvt, 'enableBlvt']])
    payload = {'email': email, 'enableBlvt': enableBlvt, **kwargs}

    return self.limited_encoded_sign_request('POST', '/sapi/v1/sub-account/blvt/enable', payload)
