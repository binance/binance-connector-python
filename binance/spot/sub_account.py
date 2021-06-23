from binance.lib.utils import check_required_parameter
from binance.lib.utils import check_required_parameters


def sub_account_create(self, subAccountString: str, **kwargs):
    """Create a Virtual Sub-account(For Master Account)
    Generate a virtual sub account under the master account

    POST /sapi/v1/sub-account/virtualSubAccount

    https://binance-docs.github.io/apidocs/spot/en/#create-a-virtual-sub-account-for-master-account

    Args:
        subAccountString (str)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameter(subAccountString, "subAccountString")
    payload = {"subAccountString": subAccountString, **kwargs}

    return self.limited_encoded_sign_request(
        "POST", "/sapi/v1/sub-account/virtualSubAccount", payload
    )


def sub_account_list(self, **kwargs):
    """Query Sub-account List(For Master Account)
    Fetch sub account list.

    GET /sapi/v1/sub-account/list

    https://binance-docs.github.io/apidocs/spot/en/#query-sub-account-list-sapi-for-master-account

    Keyword Args:
        email (str, optional): Sub-account email
        isFreeze (str, optional): true or false
        page (int, optional): default 1
        limit (int, optional): default 10, max 200
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.limited_encoded_sign_request("GET", "/sapi/v1/sub-account/list", kwargs)


def sub_account_assets(self, email: str, **kwargs):
    """Query Sub-account Assets(For Master Account)
    Fetch sub-account assets

    GET /sapi/v3/sub-account/assets

    https://binance-docs.github.io/apidocs/spot/en/#query-sub-account-assets-sapi-for-master-account

    Args:
        email (str)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameter(email, "email")
    payload = {"email": email, **kwargs}
    return self.limited_encoded_sign_request(
        "GET", "/sapi/v3/sub-account/assets", payload
    )


def sub_account_deposit_address(self, email: str, coin: str, **kwargs):
    """Get Sub-account Deposit Address (For Master Account)
    Fetch sub-account deposit address

    GET /sapi/v1/capital/deposit/subAddress

    https://binance-docs.github.io/apidocs/spot/en/#get-sub-account-deposit-address-for-master-account

    Args:
        email (str)
        coin (str)
    Keyword Args:
        network (str, optional)
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters([[email, "email"], [coin, "coin"]])
    payload = {"email": email, "coin": coin, **kwargs}
    return self.limited_encoded_sign_request(
        "GET", "/sapi/v1/capital/deposit/subAddress", payload
    )


def sub_account_deposit_history(self, email: str, **kwargs):
    """Get Sub-account Deposit History (For Master Account)
    Fetch sub-account deposit history

    GET /sapi/v1/capital/deposit/subHisrec

    https://binance-docs.github.io/apidocs/spot/en/#get-sub-account-deposit-address-for-master-account

    Args:
        email (str)
    Keyword Args:
        coin (str, optional)
        status (int, optional): Default 0 (0:pending,6: credited but cannot withdraw, 1:success)
        startTime (int, optional)
        endTime (int, optional)
        limit (int, optional)
        offset (int, optional): Default:0
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameter(email, "email")
    payload = {"email": email, **kwargs}
    return self.limited_encoded_sign_request(
        "GET", "/sapi/v1/capital/deposit/subHisrec", payload
    )


def sub_account_status(self, **kwargs):
    """Get Sub-account's Status on Margin/Futures(For Master Account)

    GET /sapi/v1/sub-account/status

    https://binance-docs.github.io/apidocs/spot/en/#get-sub-account-39-s-status-on-margin-futures-for-master-account

    Keyword Args:
        email (str, optional): Sub-account email
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.limited_encoded_sign_request(
        "GET", "/sapi/v1/sub-account/status", kwargs
    )


def sub_account_enable_margin(self, email: str, **kwargs):
    """Enable Margin for Sub-account (For Master Account)

    POST /sapi/v1/sub-account/margin/enable

    https://binance-docs.github.io/apidocs/spot/en/#enable-margin-for-sub-account-for-master-account

    Args:
        email (str)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameter(email, "email")
    payload = {"email": email, **kwargs}
    return self.limited_encoded_sign_request(
        "POST", "/sapi/v1/sub-account/margin/enable", payload
    )


def sub_account_margin_account(self, email: str, **kwargs):
    """Get Detail on Sub-account's Margin Account (For Master Account)

    GET /sapi/v1/sub-account/margin/account

    https://binance-docs.github.io/apidocs/spot/en/#get-detail-on-sub-account-39-s-margin-account-for-master-account

    Args:
        email (str)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameter(email, "email")
    payload = {"email": email, **kwargs}
    return self.limited_encoded_sign_request(
        "GET", "/sapi/v1/sub-account/margin/account", payload
    )


def sub_account_margin_account_summary(self, **kwargs):
    """Get Summary of Sub-account's Margin Account (For Master Account)

    GET /sapi/v1/sub-account/margin/accountSummary

    https://binance-docs.github.io/apidocs/spot/en/#get-summary-of-sub-account-39-s-margin-account-for-master-account

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request(
        "GET", "/sapi/v1/sub-account/margin/accountSummary", kwargs
    )


def sub_account_enable_futures(self, email: str, **kwargs):
    """Enable Futures for Sub-account (For Master Account)

    POST /sapi/v1/sub-account/futures/enable

    https://binance-docs.github.io/apidocs/spot/en/#enable-futures-for-sub-account-for-master-account

    Args:
        email (str)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameter(email, "email")
    payload = {"email": email, **kwargs}
    return self.limited_encoded_sign_request(
        "POST", "/sapi/v1/sub-account/futures/enable", payload
    )


def sub_account_futures_transfer(
    self, email: str, asset: str, amount: float, type: int, **kwargs
):
    """Futures Transfer for Sub-account（For Master Account）

    GET /sapi/v1/sub-account/futures/transfer

    https://binance-docs.github.io/apidocs/spot/en/#get-futures-postion-risk-of-sub-account-for-master-account

    Args:
        email (str)
        asset (str)
        amount (float)
        type (int)
    """

    check_required_parameters(
        [[email, "email"], [asset, "asset"], [amount, "amount"], [type, "type"]]
    )
    payload = {"email": email, "asset": asset, "amount": amount, "type": type, **kwargs}
    return self.limited_encoded_sign_request(
        "POST", "/sapi/v1/sub-account/futures/transfer", payload
    )


def sub_account_margin_transfer(
    self, email: str, asset: str, amount: float, type: int, **kwargs
):
    """Margin Transfer for Sub-account（For Master Account)

    GET /sapi/v1/sub-account/margin/transfer

    https://binance-docs.github.io/apidocs/spot/en/#margin-transfer-for-sub-account-for-master-account

    Args:
        email (str)
        asset (str)
        amount (float)
        type (int)
    """

    check_required_parameters(
        [[email, "email"], [asset, "asset"], [amount, "amount"], [type, "type"]]
    )
    payload = {"email": email, "asset": asset, "amount": amount, "type": type, **kwargs}
    return self.limited_encoded_sign_request(
        "POST", "/sapi/v1/sub-account/margin/transfer", payload
    )


def sub_account_transfer_to_sub(
    self, toEmail: str, asset: str, amount: float, **kwargs
):
    """Transfer to Sub-account of Same Master（For Sub-account）

    POST /sapi/v1/sub-account/transfer/subToSub

    https://binance-docs.github.io/apidocs/spot/en/#transfer-to-sub-account-of-same-master-for-sub-account

    Args:
        toEmail (str)
        asset (str)
        amount (float)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters(
        [[toEmail, "toEmail"], [asset, "asset"], [amount, "amount"]]
    )
    payload = {"toEmail": toEmail, "asset": asset, "amount": amount, **kwargs}
    return self.limited_encoded_sign_request(
        "POST", "/sapi/v1/sub-account/transfer/subToSub", payload
    )


def sub_account_transfer_to_master(self, asset: str, amount: float, **kwargs):
    """Transfer to Master（For Sub-account）

    POST /sapi/v1/sub-account/transfer/subToMaster

    https://binance-docs.github.io/apidocs/spot/en/#transfer-to-master-for-sub-account

    Args:
        asset (str)
        amount (float)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters([[asset, "asset"], [amount, "amount"]])
    payload = {"asset": asset, "amount": amount, **kwargs}
    return self.sign_request(
        "POST", "/sapi/v1/sub-account/transfer/subToMaster", payload
    )


def sub_account_transfer_sub_account_history(self, **kwargs):
    """Sub-account Transfer History (For Sub-account)

    POST /sapi/v1/sub-account/transfer/subUserHistory

    https://binance-docs.github.io/apidocs/spot/en/#transfer-to-master-for-sub-account

    Keyword Args:
        asset (str, optional): If not sent, result of all assets will be returned
        type (int, optional): 1: transfer in, 2: transfer out
        startTime (int, optional)
        endTime (int, optional)
        limit (int, optional): Default 500
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request(
        "GET", "/sapi/v1/sub-account/transfer/subUserHistory", kwargs
    )


def sub_account_futures_asset_transfer_history(
    self, email: str, futuresType: int, **kwargs
):
    """Query Sub-account Futures Asset Transfer History(For Master Account)

    GET /sapi/v1/sub-account/futures/internalTransfer

    https://binance-docs.github.io/apidocs/spot/en/#sub-account-spot-asset-transfer-for-master-account

    Args:
        email (str): Sub-account email
        futuresType (int): 1 : USDT-maringed Futues, 2: Coin-margined Futures
    Keyword Args:
        startTime (int, optional): Default return the history with in 100 days
        endTime (int, optional): Default return the history with in 100 days
        page (int, optional): Default value: 1
        limit (int, optional): Default value: 50, Max value: 500
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters([[email, "email"], [futuresType, "futuresType"]])
    payload = {"email": email, "futuresType": futuresType, **kwargs}
    return self.sign_request(
        "GET", "/sapi/v1/sub-account/futures/internalTransfer", payload
    )


def sub_account_futures_asset_transfer(
    self,
    fromEmail: str,
    toEmail: str,
    futuresType: int,
    asset: str,
    amount: float,
    **kwargs
):
    """Query Sub-account Futures Asset Transfer History(For Master Account)

    POST /sapi/v1/sub-account/futures/internalTransfer

    https://binance-docs.github.io/apidocs/spot/en/#sub-account-futures-asset-transfer-for-master-account

    Args:
        fromEmail (str): Sender email
        toEmail (str): Recipient email
        futuresType (int): 1 : USDT-maringed Futues, 2: Coin-margined Futures
        asset (str)
        amount (float)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters(
        [
            [fromEmail, "fromEmail"],
            [toEmail, "toEmail"],
            [futuresType, "futuresType"],
            [asset, "asset"],
            [amount, "amount"],
        ]
    )
    payload = {
        "fromEmail": fromEmail,
        "toEmail": toEmail,
        "futuresType": futuresType,
        "asset": asset,
        "amount": amount,
        **kwargs,
    }
    return self.sign_request(
        "POST", "/sapi/v1/sub-account/futures/internalTransfer", payload
    )


def sub_account_spot_summary(self, **kwargs):
    """Query Sub-account Spot Assets Summary (For Master Account)

    GET /sapi/v1/sub-account/spotSummary

    https://binance-docs.github.io/apidocs/spot/en/#query-sub-account-assets-for-master-account

    Keyword Args:
        email (str, optional): Sub account email
        page (int, optional): Default: 1
        size (int, optional): Default 10, max 20
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/sub-account/spotSummary", kwargs)


def sub_account_universal_transfer(
    self, fromAccountType: str, toAccountType: str, asset: str, amount: float, **kwargs
):
    """Universal Transfer (For Master Account)

    POST /sapi/v1/sub-account/universalTransfer

    https://binance-docs.github.io/apidocs/spot/en/#universal-transfer-for-master-account

    You need to enable "internal transfer" option for the api key which requests this endpoint.
    Transfer from master account by default if fromEmail is not sent.
    Transfer to master account by default if toEmail is not sent.
    Transfer between futures accounts is not supported.

    Args:
        fromAccountType (str): "SPOT","USDT_FUTURE","COIN_FUTURE"
        toAccountType (str): "SPOT","USDT_FUTURE","COIN_FUTURE"
        asset (str)
        amount (float)
    Keyword Args:
        fromEmail (str, optional)
        toEmail (str, optional)
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters(
        [
            [fromAccountType, "fromAccountType"],
            [toAccountType, "toAccountType"],
            [asset, "asset"],
            [amount, "amount"],
        ]
    )

    payload = {
        "fromAccountType": fromAccountType,
        "toAccountType": toAccountType,
        "asset": asset,
        "amount": amount,
        **kwargs,
    }
    return self.limited_encoded_sign_request(
        "POST", "/sapi/v1/sub-account/universalTransfer", payload
    )


def sub_account_universal_transfer_history(self, **kwargs):
    """Query Universal Transfer History (For Master Account)

    GET /sapi/v1/sub-account/universalTransfer

    https://binance-docs.github.io/apidocs/spot/en/#query-universal-transfer-history-for-master-account

    fromEmail and toEmail cannot be sent at the same time.
    Return fromEmail equal master account email by default.
    Only get the latest history of past 30 days.

    Keyword Args:
        fromEmail (str, optional)
        toEmail (str, optional)
        startTime (int, optional)
        endTime (int, optional)
        page (int, optional)
        limit (int, optional): Default 10, max 20
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.limited_encoded_sign_request(
        "GET", "/sapi/v1/sub-account/universalTransfer", kwargs
    )


def sub_account_futures_account(self, email: str, futuresType: int, **kwargs):
    """Get Detail on Sub-account's Futures Account V2 (For Master Account)

    GET /sapi/v2/sub-account/futures/account

    https://binance-docs.github.io/apidocs/spot/en/#get-detail-on-sub-account-39-s-futures-account-v2-for-master-account

    Args:
        email (str): Sub-account email
        futuresType (int): 1 : USDT-maringed Futues, 2: Coin-margined Futures
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters([[email, "email"], [futuresType, "futuresType"]])

    payload = {"email": email, "futuresType": futuresType, **kwargs}
    return self.limited_encoded_sign_request(
        "GET", "/sapi/v2/sub-account/futures/account", payload
    )


def sub_account_futures_account_summary(self, futuresType: int, **kwargs):
    """Get Summary of Sub-account's Futures Account V2 (For Master Account)

    GET /sapi/v2/sub-account/futures/accountSummary

    https://binance-docs.github.io/apidocs/spot/en/#get-detail-on-sub-account-39-s-futures-account-v2-for-master-account

    Args:
        futuresType (int): 1 : USDT-maringed Futues, 2: Coin-margined Futures
    Keyword Args:
        page (int, optional): Default:1
        limit (int, optional): Default 10, max 20
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(futuresType, "futuresType")

    payload = {"futuresType": futuresType, **kwargs}

    return self.sign_request(
        "GET", "/sapi/v2/sub-account/futures/accountSummary", payload
    )


def sub_account_futures_position_risk(self, email: str, futuresType: str, **kwargs):
    """Get Futures Position-Risk of Sub-account V2 (For Master Account)

    GET /sapi/v2/sub-account/futures/positionRisk

    https://binance-docs.github.io/apidocs/spot/en/#get-futures-position-risk-of-sub-account-v2-for-master-account

    Args:
        email (str): Sub-account email
        futuresType (int): 1 : USDT-maringed Futues, 2: Coin-margined Futures
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters([[email, "email"], [futuresType, "futuresType"]])

    payload = {"email": email, "futuresType": futuresType, **kwargs}
    return self.limited_encoded_sign_request(
        "GET", "/sapi/v2/sub-account/futures/positionRisk", payload
    )


def sub_account_spot_transfer_history(self, **kwargs):
    """Query Sub-account Spot Asset Transfer History (SAPI For Master Account)

    GET /sapi/v1/sub-account/sub/transfer/history

    https://binance-docs.github.io/apidocs/spot/en/#query-sub-account-spot-asset-transfer-history-for-master-account

    Keyword Args:
        fromEmail (str, optional)
        toEmail (str, optional)
        startTime (int, optional): Default return the history with in 100 days
        endTime (int, optional): Default return the history with in 100 days
        page (int, optional): Default value: 1
        limit (int, optional): Default value: 500
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.limited_encoded_sign_request(
        "GET", "/sapi/v1/sub-account/sub/transfer/history", kwargs
    )


def sub_account_enable_leverage_token(self, email: str, enableBlvt: bool, **kwargs):
    """Enable Leverage Token for Sub-account(For Master Account)
    Enable leverage token for sub-account

    POST /sapi/v1/sub-account/blvt/enable

    https://binance-docs.github.io/apidocs/spot/en/#enable-leverage-token-for-sub-account-for-master-account

    Args:
        email (str): Sub-account email
        enableBlvt (bool): Only true for now
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters([[email, "email"], [enableBlvt, "enableBlvt"]])
    payload = {"email": email, "enableBlvt": enableBlvt, **kwargs}

    return self.limited_encoded_sign_request(
        "POST", "/sapi/v1/sub-account/blvt/enable", payload
    )


def managed_sub_account_deposit(
    self, toEmail: str, asset: str, amount: float, **kwargs
):
    """Deposit assets into the managed sub-account（For Investor Master Account）

    POST /sapi/v1/managed-subaccount/deposit

    https://binance-docs.github.io/apidocs/spot/en/#deposit-assets-into-the-managed-sub-account-for-investor-master-account

    Args:
        toEmail (str): Sub-account email
        asset (str)
        amount (float)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters(
        [[toEmail, "toEmail"], [asset, "asset"], [amount, "amount"]]
    )
    payload = {"toEmail": toEmail, "asset": asset, "amount": amount, **kwargs}
    return self.limited_encoded_sign_request(
        "POST", "/sapi/v1/managed-subaccount/deposit", payload
    )


def managed_sub_account_assets(self, email: str, **kwargs):
    """Query managed sub-account asset details（For Investor Master Account）

    GET /sapi/v1/managed-subaccount/asset

    https://binance-docs.github.io/apidocs/spot/en/#query-managed-sub-account-asset-details-for-investor-master-account

    Args:
        email (str): Sub-account email
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters([[email, "email"]])
    payload = {"email": email, **kwargs}
    return self.limited_encoded_sign_request(
        "GET", "/sapi/v1/managed-subaccount/asset", payload
    )


def managed_sub_account_withdraw(
    self, fromEmail: str, asset: str, amount: float, **kwargs
):
    """Withdrawl assets from the managed sub-account（For Investor Master Account）

    POST /sapi/v1/managed-subaccount/withdraw

    https://binance-docs.github.io/apidocs/spot/en/#withdrawl-assets-from-the-managed-sub-account-for-investor-master-account

    Args:
        fromEmail (str): Sub-account email
        asset (str)
        amount (float)
    Keyword Args:
        transferDate (int, optional): Withdrawals is automatically occur on the transfer date(UTC0).
        If a date is not selected, the withdrawal occurs right now
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters(
        [[fromEmail, "fromEmail"], [asset, "asset"], [amount, "amount"]]
    )
    payload = {"fromEmail": fromEmail, "asset": asset, "amount": amount, **kwargs}
    return self.limited_encoded_sign_request(
        "POST", "/sapi/v1/managed-subaccount/withdraw", payload
    )
