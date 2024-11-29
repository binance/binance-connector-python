from binance.lib.utils import check_required_parameter
from binance.lib.utils import check_required_parameters


def sub_account_create(self, subAccountString: str, **kwargs):
    """Create a Virtual Sub-account(For Master Account)
    Generate a virtual sub account under the master account

    POST /sapi/v1/sub-account/virtualSubAccount

    https://developers.binance.com/docs/sub_account/account-management/Create-a-Virtual-Sub-account

    Args:
        subAccountString (str): Please input a string. We will create a virtual email using that string for you to register
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

    https://developers.binance.com/docs/sub_account/account-management/Query-Sub-account-List

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

    https://developers.binance.com/docs/sub_account/asset-management/Query-Sub-account-Assets-V3

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

    https://developers.binance.com/docs/sub_account/asset-management/Get-Sub-account-Deposit-Address

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

    https://developers.binance.com/docs/sub_account/asset-management/Get-Sub-account-Deposit-Address

    Args:
        email (str)
    Keyword Args:
        coin (str, optional)
        status (int, optional): Default 0 (0:pending,6: credited but cannot withdraw, 1:success)
        startTime (int, optional)
        endTime (int, optional)
        limit (int, optional)
        offset (int, optional): Default:0
        txId (str, optional)
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

    https://developers.binance.com/docs/sub_account/account-management/Get-Sub-accounts-Status-on-Margin-Or-Futures

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

    https://developers.binance.com/docs/sub_account/account-management/Enable-Margin-for-Sub-account

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

    https://developers.binance.com/docs/sub_account/asset-management/Get-Detail-on-Sub-accounts-Margin-Account

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

    https://developers.binance.com/docs/sub_account/asset-management/Get-Summary-of-Sub-accounts-Margin-Account

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request(
        "GET", "/sapi/v1/sub-account/margin/accountSummary", kwargs
    )


def sub_account_enable_futures(self, email: str, **kwargs):
    """Enable Futures for Sub-account (For Master Account)

    POST /sapi/v1/sub-account/futures/enable

    https://developers.binance.com/docs/sub_account/account-management/Enable-Futures-for-Sub-account

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

    POST /sapi/v1/sub-account/futures/transfer

    https://developers.binance.com/docs/sub_account/asset-management/Futures-Transfer-for-Sub-account

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

    POST /sapi/v1/sub-account/margin/transfer

    https://developers.binance.com/docs/sub_account/asset-management/Margin-Transfer-for-Sub-account

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

    https://developers.binance.com/docs/sub_account/asset-management/Transfer-to-Sub-account-of-Same-Master

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

    https://developers.binance.com/docs/sub_account/asset-management/Transfer-to-Master

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

    GET /sapi/v1/sub-account/transfer/subUserHistory

    https://developers.binance.com/docs/sub_account/asset-management/Sub-account-Transfer-History

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

    https://developers.binance.com/docs/sub_account/asset-management/Query-Sub-account-Futures-Asset-Transfer-History

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

    https://developers.binance.com/docs/sub_account/asset-management/Sub-account-Futures-Asset-Transfer

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

    https://developers.binance.com/docs/sub_account/asset-management/Query-Sub-account-Spot-Assets-Summary

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

    https://developers.binance.com/docs/sub_account/asset-management/Universal-Transfer

    You need to enable "internal transfer" option for the api key which requests this endpoint.
    Transfer from master account by default if fromEmail is not sent.
    Transfer to master account by default if toEmail is not sent.
    Supported transfer scenarios:
    - Master account SPOT transfer to sub-account SPOT, USDT_FUTURE, COIN_FUTURE, MARGIN(Cross), ISOLATED_MARGIN
    - Sub-account SPOT, USDT_FUTURE, COIN_FUTURE, MARGIN(Cross), ISOLATED_MARGIN transfer to master account SPOT
    - Transfer between two SPOT sub-accounts

    Args:
        fromAccountType (str): "SPOT", "USDT_FUTURE", "COIN_FUTURE", "MARGIN"(Cross), "ISOLATED_MARGIN"
        toAccountType (str): "SPOT", "USDT_FUTURE", "COIN_FUTURE", "MARGIN"(Cross), "ISOLATED_MARGIN"
        asset (str)
        amount (float)
    Keyword Args:
        fromEmail (str, optional)
        toEmail (str, optional)
        clientTranId (str, optional): Must be unique
        symbol (str, optional): Only supported under ISOLATED_MARGIN type
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

    https://developers.binance.com/docs/sub_account/asset-management/Query-Universal-Transfer-History

    fromEmail and toEmail cannot be sent at the same time.
    Return fromEmail equal master account email by default.
    Only get the latest history of past 30 days.

    Keyword Args:
        fromEmail (str, optional)
        toEmail (str, optional)
        clientTranId (str, optional)
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

    https://developers.binance.com/docs/sub_account/asset-management/Get-Detail-on-Sub-accounts-Futures-Account-V2

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

    https://developers.binance.com/docs/sub_account/asset-management/Get-Summary-of-Sub-accounts-Futures-Account-V2

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

    https://developers.binance.com/docs/sub_account/account-management/Get-Futures-Position-Risk-of-Sub-account-V2

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

    https://developers.binance.com/docs/sub_account/asset-management/Query-Sub-account-Spot-Asset-Transfer-History

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

    https://developers.binance.com/docs/sub_account/account-management/Enable-Leverage-Token-for-Sub-account

    Args:
        email (str): Sub-account email
        enableBlvt (bool): Only True for now
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

    https://developers.binance.com/docs/sub_account/managed-sub-account/Deposit-Assets-Into-The-Managed-Sub-account

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

    https://developers.binance.com/docs/sub_account/managed-sub-account/Query-Managed-Sub-account-Asset-Details

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

    https://developers.binance.com/docs/sub_account/managed-sub-account/Withdrawl-Assets-From-The-Managed-Sub-account

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


def sub_account_update_ip_restriction(
    self, email: str, subAccountApiKey: str, status: str, **kwargs
):
    """Update IP Restriction for Sub-Account API key (For Master Account)

    POST /sapi/v2/sub-account/subAccountApi/ipRestriction

    https://developers.binance.com/docs/sub_account/api-management/Add-IP-Restriction-for-Sub-Account-API-key

    Args:
        email (str): Sub-account email
        subAccountApiKey (str)
        status (str) : IP Restriction status. 1 = IP Unrestricted. 2 = Restrict access to trusted IPs only.
    Keyword Args:
        ipAddress (str, optional): Can be added in batches, separated by commas
        recvWindow (int, optional)
    """

    check_required_parameters(
        [
            [email, "email"],
            [subAccountApiKey, "subAccountApiKey"],
            [status, "status"],
        ]
    )
    payload = {
        "email": email,
        "subAccountApiKey": subAccountApiKey,
        "status": status,
        **kwargs,
    }

    return self.limited_encoded_sign_request(
        "POST", "/sapi/v2/sub-account/subAccountApi/ipRestriction", payload
    )


def sub_account_api_get_ip_restriction(
    self, email: str, subAccountApiKey: str, **kwargs
):
    """Get IP Restriction for a Sub-account API Key (For Master Account)

    GET /sapi/v1/sub-account/subAccountApi/ipRestriction

    https://developers.binance.com/docs/sub_account/api-management/Get-IP-Restriction-for-a-Sub-account-API-Key

    Args:
        email (str): Sub-account email
        subAccountApiKey (str)
    Keyword Args:
        recvWindow (int, optional)
    """

    check_required_parameters(
        [
            [email, "email"],
            [subAccountApiKey, "subAccountApiKey"],
        ]
    )
    payload = {"email": email, "subAccountApiKey": subAccountApiKey, **kwargs}

    return self.limited_encoded_sign_request(
        "GET", "/sapi/v1/sub-account/subAccountApi/ipRestriction", payload
    )


def sub_account_api_delete_ip(
    self, email: str, subAccountApiKey: str, ipAddress: str, **kwargs
):
    """Delete IP List for a Sub-account API Key (For Master Account)

    DELETE /sapi/v1/sub-account/subAccountApi/ipRestriction/ipList

    https://developers.binance.com/docs/sub_account/api-management/Delete-IP-List-For-a-Sub-account-API-Key

    Args:
        email (str): Sub-account email
        subAccountApiKey (str)
        ipAddress (str): Can be added in batches, separated by commas
    Keyword Args:
        thirdPartyName (str, optional)
        recvWindow (int, optional)
    """

    check_required_parameters(
        [
            [email, "email"],
            [subAccountApiKey, "subAccountApiKey"],
            [ipAddress, "ipAddress"],
        ]
    )
    payload = {
        "email": email,
        "subAccountApiKey": subAccountApiKey,
        "ipAddress": ipAddress,
        **kwargs,
    }

    return self.limited_encoded_sign_request(
        "DELETE", "/sapi/v1/sub-account/subAccountApi/ipRestriction/ipList", payload
    )


def managed_sub_account_get_snapshot(self, email: str, type: str, **kwargs):
    """Query Managed Sub-account Snapshot（For Investor Master Account）

    GET /sapi/v1/managed-subaccount/accountSnapshot (HMAC SHA256)

    https://developers.binance.com/docs/sub_account/managed-sub-account/Query-Managed-Sub-account-Snapshot

    Args:
        email (str): email
        type (str): "SPOT", "MARGIN"（cross）, "FUTURES"（UM）
    Keyword Args:
        startTime (int, optional)
        endTime (int, optional)
        limit (int, optional): min 7, max 30, default 7
        recvWindow (int, optional)
    """

    check_required_parameters(
        [
            [email, "email"],
            [type, "type"],
        ]
    )
    payload = {
        "email": email,
        "type": type,
        **kwargs,
    }

    return self.limited_encoded_sign_request(
        "GET", "/sapi/v1/managed-subaccount/accountSnapshot", payload
    )


def managed_sub_account_investor_trans_log(
    self, email: str, startTime: int, endTime: int, page: int, limit: int, **kwargs
):
    """Query Managed Sub Account Transfer Log (Investor) (USER_DATA)

    GET /sapi/v1/managed-subaccount/transfer/history (HMAC SHA256)

    https://developers.binance.com/en

    Args:
        email (str): email
        startTime (int): start time
        endTime (int): end time
        page (int): page
        limit (int): limit
    Keyword Args:
        transfers(str, optional): Transfer Direction (FROM/TO)
        transferFunctionAccountType(str, optional): Transfer function account type (SPOT/MARGIN/ISOLATED_MARGIN/USDT_FUTURE/COIN_FUTURE)
    """

    check_required_parameters(
        [
            [email, "email"],
            [startTime, "startTime"],
            [endTime, "endTime"],
            [page, "page"],
            [limit, "limit"],
        ]
    )
    payload = {
        "email": email,
        "startTime": startTime,
        "endTime": endTime,
        "page": page,
        "limit": limit,
        **kwargs,
    }

    return self.limited_encoded_sign_request(
        "GET", "/sapi/v1/managed-subaccount/queryTransLogForInvestor", payload
    )


def managed_sub_account_trading_trans_log(
    self, email: str, startTime: int, endTime: int, page: int, limit: int, **kwargs
):
    """Query Managed Sub Account Transfer Log (Trading Team) (USER_DATA)

    GET /sapi/v1/managed-subaccount/queryTransLogForTradeParent

    https://developers.binance.com/docs/sub_account/managed-sub-account/Query-Managed-Sub-Account-Transfer-Log-Trading-Team-Master

    Args:
        email (str): email
        startTime (int): start time
        endTime (int): end time
        page (int): page
        limit (int): limit
    Keyword Args:
        transfers(str, optional): Transfer Direction (FROM/TO)
        transferFunctionAccountType(str, optional): Transfer function account type (SPOT/MARGIN/ISOLATED_MARGIN/USDT_FUTURE/COIN_FUTURE)
    """

    check_required_parameters(
        [
            [email, "email"],
            [startTime, "startTime"],
            [endTime, "endTime"],
            [page, "page"],
            [limit, "limit"],
        ]
    )
    payload = {
        "email": email,
        "startTime": startTime,
        "endTime": endTime,
        "page": page,
        "limit": limit,
        **kwargs,
    }

    return self.limited_encoded_sign_request(
        "GET", "/sapi/v1/managed-subaccount/queryTransLogForTradeParent", payload
    )


def managed_sub_account_deposit_address(self, email: str, coin: str, **kwargs):
    """Get Managed Sub-account Deposit Address (For Investor Master Account) (USER_DATA)

    GET /sapi/v1/managed-subaccount/deposit/address (HMAC SHA256)

    https://developers.binance.com/docs/sub_account/managed-sub-account/Get-Managed-Sub-account-Deposit-Address

    Args:
        email (str): email
        coin (str): coin
    Keyword Args:
        network (str, optional)
        recvWindow (int, optional)
    """

    check_required_parameters(
        [
            [email, "email"],
            [coin, "coin"],
        ]
    )
    payload = {
        "email": email,
        "coin": coin,
        **kwargs,
    }

    return self.limited_encoded_sign_request(
        "GET", "/sapi/v1/managed-subaccount/deposit/address", payload
    )


def query_sub_account_assets(self, email: str, **kwargs):
    """Query Sub-account Assets (For Master Account) (USER_DATA)

    Fetch sub-account assets

    Weight(UID): 60

    GET /sapi/v4/sub-account/assets

    https://developers.binance.com/docs/sub_account/asset-management/Query-Sub-account-Assets-V4

    Args:
        email (str)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(email, "email")

    params = {"email": email, **kwargs}
    url_path = "/sapi/v4/sub-account/assets"
    return self.sign_request("GET", url_path, params)


def enable_options_for_sub_account(self, email: str, **kwargs):
    """Enable Options for Sub-account (For Master Account) (USER_DATA)

    Weight(IP): 1

    POST /sapi/v1/sub-account/eoptions/enable

    https://developers.binance.com/docs/sub_account/account-management/Enable-Options-for-Sub-account

    Args:
        email (str)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(email, "email")

    params = {"email": email, **kwargs}
    url_path = "/sapi/v1/sub-account/eoptions/enable"
    return self.sign_request("POST", url_path, params)


def query_sub_account_transaction_statistics(self, email: str, **kwargs):
    """Query Sub-account Transaction Statistics (For Master Account) (USER_DATA)

    Weight(UID): 60

    GET /sapi/v1/sub-account/transaction-statistics

    https://developers.binance.com/docs/sub_account/account-management/Query-Sub-account-Transaction-Statistics

    Args:
        email (str)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(email, "email")

    params = {"email": email, **kwargs}
    url_path = "/sapi/v1/sub-account/transaction-statistics"
    return self.sign_request("GET", url_path, params)


def query_managed_sub_account_transfer_log(
    self, startTime: int, endTime: int, page: int, limit: int, **kwargs
):
    """Query Managed Sub Account Transfer Log (For Trading Team Sub Account)

    Query Managed Sub Account Transfer Log (For Trading Team Sub Account)

    Weight(UID): 60

    GET /sapi/v1/managed-subaccount/query-trans-log

    https://developers.binance.com/docs/sub_account/managed-sub-account/Query-Managed-Sub-Account-Transfer-Log-Trading-Team-Sub

    Args:
        startTime (int): UTC timestamp in ms
        endTime (int): UTC timestamp in ms
        page (int): Default 1
        limit (int): Default 500; max 1000.
    Keyword Args:
        transfers (str, optional)
        transferFunctionAccountType (str, optional)
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters(
        [
            [startTime, "startTime"],
            [endTime, "endTime"],
            [page, "page"],
            [limit, "limit"],
        ]
    )

    params = {
        "startTime": startTime,
        "endTime": endTime,
        "page": page,
        "limit": limit,
        **kwargs,
    }
    url_path = "/sapi/v1/managed-subaccount/query-trans-log"
    return self.sign_request("GET", url_path, params)


def query_managed_sub_account_list(self, **kwargs):
    """Query Managed Sub-account List (For Investor) (USER_DATA)

    Get investor's managed sub-account list.

    Weight(UID): 60

    GET /sapi/v1/managed-subaccount/info

    https://developers.binance.com/docs/sub_account/managed-sub-account/Query-Managed-Sub-account-List

    Keyword Args:
        email (str, optional)
        page (int, optional): Default 1
        limit (int, optional): Default 500; max 1000.
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/sapi/v1/managed-subaccount/info"
    return self.sign_request("GET", url_path, kwargs)


def query_managed_sub_account_margin_asset_details(self, email: str, **kwargs):
    """Query Managed Sub-account Margin Asset Details (For Investor Master Account)

    Investor can use this api to query managed sub account margin asset details

    Weight(IP): 1

    GET /sapi/v1/managed-subaccount/marginAsset

    https://developers.binance.com/docs/sub_account/managed-sub-account/Query-Managed-Sub-account-Margin-Asset-Details

    Args:
        email (str)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(email, "email")

    params = {"email": email, **kwargs}
    url_path = "/sapi/v1/managed-subaccount/marginAsset"
    return self.sign_request("GET", url_path, params)


def query_managed_sub_account_futures_asset_details(self, email: str, **kwargs):
    """Query Managed Sub-account Futures Asset Details (For Investor Master Account)

    Investor can use this api to query managed sub account futures asset details

    Weight(UID): 60

    GET /sapi/v1/managed-subaccount/fetch-future-asset

    https://developers.binance.com/docs/sub_account/managed-sub-account/Query-Managed-Sub-account-Futures-Asset-Details

    Args:
        email (str)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(email, "email")

    params = {"email": email, **kwargs}
    url_path = "/sapi/v1/managed-subaccount/fetch-future-asset"
    return self.sign_request("GET", url_path, params)


def futures_position_risk_of_sub_account(self, email: str, **kwargs):
    """Get Futures Position-Risk of Sub-account (For Master Account)

    Weight(IP): 10

    GET /sapi/v1/sub-account/futures/positionRisk

    https://developers.binance.com/docs/sub_account/account-management/Get-Futures-Position-Risk-of-Sub-account

    Args:
        email (str)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(email, "email")

    params = {"email": email, **kwargs}
    url_path = "/sapi/v1/sub-account/futures/positionRisk"
    return self.sign_request("GET", url_path, params)


def summary_of_sub_account_s_futures_account(self, futuresType: int, **kwargs):
    """Get Summary of Sub-account's Futures Account V2 (For Master Account)

    Weight(IP): 10

    GET /sapi/v2/sub-account/futures/accountSummary

    https://developers.binance.com/docs/sub_account/asset-management/Get-Summary-of-Sub-accounts-Futures-Account-V2

    Args:
        futuresType (int): 1:USDT Margined Futures, 2:COIN Margined Futures
    Keyword Args:
        page (int, optional): default:1
        limit (int, optional): default 10, max 20
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameter(futuresType, "futuresType")

    params = {"futuresType": futuresType, **kwargs}
    url_path = "/sapi/v2/sub-account/futures/accountSummary"
    return self.sign_request("GET", url_path, params)


def detail_on_sub_account_s_futures_account(self, email: str, **kwargs):
    """Detail on Sub-account's Futures Account (For Master Account)

    Weight(IP): 10

    GET /sapi/v1/sub-account/futures/account

    https://developers.binance.com/docs/sub_account/asset-management/Get-Detail-on-Sub-accounts-Futures-Account

    Args:
        email (str)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(email, "email")

    params = {"email": email, **kwargs}
    url_path = "/sapi/v1/sub-account/futures/account"
    return self.sign_request("GET", url_path, params)
