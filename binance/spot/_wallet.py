from binance.lib.utils import check_required_parameter
from binance.lib.utils import check_required_parameters
from binance.lib.utils import check_enum_parameter
from binance.lib.enums import TransferType


def system_status(self):
    """System Status (System)
    Fetch system status.

    GET /sapi/v1/system/status

    https://developers.binance.com/docs/wallet/others/system-status
    """

    return self.query("/sapi/v1/system/status")


def coin_info(self, **kwargs):
    """All Coins' Information (USER_DATA)
    Get information of coins (available for deposit and withdraw) for user.

    GET /sapi/v1/capital/config/getall

    https://developers.binance.com/docs/wallet/capital/all-coins-info

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/capital/config/getall", kwargs)


def account_snapshot(self, type: str, **kwargs):
    """Daily Account Snapshot (USER_DATA)

    GET /sapi/v1/accountSnapshot

    https://developers.binance.com/docs/wallet/account/daily-account-snapshoot

    Parameteres:
    type -- mandatory/string -- "SPOT", "MARGIN", "FUTURES"

    Args:
        type (str): "SPOT", "MARGIN", "FUTURES"
    Keyword Args:
        startTime (int, optional)
        endTime (int, optional)
        limit (int, optional): min 7, max 30, default 7
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameter(type, "type")
    payload = {"type": type, **kwargs}
    return self.sign_request("GET", "/sapi/v1/accountSnapshot", payload)


def disable_fast_withdraw(self, **kwargs):
    """Disable Fast Withdraw Switch (USER_DATA)

    POST /sapi/v1/account/disableFastWithdrawSwitch

    https://developers.binance.com/docs/wallet/account/disable-fast-withdraw-switch

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request(
        "POST", "/sapi/v1/account/disableFastWithdrawSwitch", kwargs
    )


def enable_fast_withdraw(self, **kwargs):
    """Enable Fast Withdraw Switch (USER_DATA)

    POST /sapi/v1/account/enableFastWithdrawSwitch

    https://developers.binance.com/docs/wallet/account/enable-fast-withdraw-switch

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request(
        "POST", "/sapi/v1/account/enableFastWithdrawSwitch", kwargs
    )


def withdraw(self, coin: str, amount: float, address: str, **kwargs):
    """Withdraw (USER_DATA)
    Submit a withdraw request.

    POST /sapi/v1/capital/withdraw/apply

    https://developers.binance.com/docs/wallet/capital/withdraw

    Args:
        coin (str)
        amount (float)
        address (str)
    Keyword Args:
        withdrawOrderId (str, optional): Client id for withdraw
        network (str, optional)
        addressTag (str, optional): Secondary address identifier for coins like XRP,XMR etc.
        transactionFeeFlag (bool, optional): When making internal transfer, True for returning the fee to the destination account; False for returning the fee back to the departure account. Default False.
        name (str, optional): Description of the address. Space in name should be encoded into %20.
        walletType (int, optional): The wallet type for withdraw，0-spot wallet，1-funding wallet. Default is spot wallet
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters(
        [[coin, "coin"], [amount, "amount"], [address, "address"]]
    )
    payload = {"coin": coin, "amount": amount, "address": address, **kwargs}
    return self.sign_request("POST", "/sapi/v1/capital/withdraw/apply", payload)


def deposit_history(self, **kwargs):
    """Deposit History（supporting network） (USER_DATA)
    Fetch deposit history.

    GET /sapi/v1/capital/deposit/hisrec

    https://developers.binance.com/docs/wallet/capital/deposite-history

    Keyword Args:
        includeSource (bool, optional): Default: false, return sourceAddressfield when set to true
        coin (str, optional)
        status (int, optional): Default 0 (0:pending, 6: credited but cannot withdraw, 1:success)
        startTime (int, optional): Default: 90 days from current timestamp
        endTime (int, optional): Default: present timestamp
        offset (int, optional): Default value: 0
        limit (int, optional): Default:1000, Max:1000
        txId (str, optional)
    """

    return self.sign_request("GET", "/sapi/v1/capital/deposit/hisrec", kwargs)


def withdraw_history(self, **kwargs):
    """Withdraw History (supporting network) (USER_DATA)
    Fetch withdraw history.

    GET /sapi/v1/capital/withdraw/history

    https://developers.binance.com/docs/wallet/capital/withdraw-history

    Keyword Args:
        coin (str, optional)
        withdrawOrderId (str, optional)
        status (int, optional): Default 0 (0:Email Sent,1:Cancelled, 2:Awaiting Approval,
                3:Rejected, 4:Processing, 5:Failure, 6:Completed)
        offset (int, optional)
        limit (int, optional): Default: 1000, Max: 1000
        idList (str, optional): id list returned in the response of POST /sapi/v1/capital/withdraw/apply, separated by commas
        startTime (int, optional): Default: 90 days from current timestamp
        endTime (int, optional): Default: present timestamp
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/capital/withdraw/history", kwargs)


def deposit_address(self, coin: str, **kwargs):
    """Deposit Address (supporting network) (USER_DATA)
    Fetch deposit address with network.

    GET /sapi/v1/capital/deposit/address

    https://developers.binance.com/docs/wallet/capital/deposite-address

    Keyword Args:
        coin (str, optional)
        network (str, optional)
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameter(coin, "coin")
    payload = {"coin": coin, **kwargs}
    return self.sign_request("GET", "/sapi/v1/capital/deposit/address", payload)


def account_status(self, **kwargs):
    """Account Status (USER_DATA)
    Fetch account status detail.

    GET /sapi/v1/account/status

    https://developers.binance.com/docs/wallet/account/account-status

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/account/status", kwargs)


def api_trading_status(self, **kwargs):
    """Account API Trading Status (USER_DATA)
    Fetch account api trading status detail.

    GET /sapi/v1/account/apiTradingStatus

    https://developers.binance.com/docs/wallet/account/account-api-trading-status

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/account/apiTradingStatus", kwargs)


def dust_log(self, **kwargs):
    """DustLog (USER_DATA)
    Fetch small amounts of assets exchanged BNB records.

    GET /sapi/v1/asset/dribblet

    https://developers.binance.com/docs/wallet/asset/dust-log

    Keyword Args:
        accountType (str, optional): SPOT or MARGIN, default SPOT
        startTime (int, optional)
        endTime (int, optional)
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/asset/dribblet", kwargs)


def user_universal_transfer(self, type: str, asset: str, amount: str, **kwargs):
    """User Universal Transfer (USER_DATA)

    POST /sapi/v1/asset/transfer

    https://developers.binance.com/docs/wallet/asset/user-universal-transfer

    Args:
        type (str)
        asset (str)
        amount (str)
    Keyword Args:
        fromSymbol (str, optional): Must be sent when type are ISOLATEDMARGIN_MARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
        toSymbol (str, optional): Must be sent when type are MARGIN_ISOLATEDMARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters([[type, "type"], [asset, "asset"], [amount, "amount"]])
    check_enum_parameter(type, TransferType)
    payload = {"type": type, "asset": asset, "amount": amount, **kwargs}
    return self.sign_request("POST", "/sapi/v1/asset/transfer", payload)


def user_universal_transfer_history(self, type: str, **kwargs):
    """Query User Universal Transfer History (USER_DATA)

    GET /sapi/v1/asset/transfer

    https://developers.binance.com/docs/wallet/asset/query-user-universal-transfer

     Args:
        type (str)
     Keyword Args:
        startTime (int, optional)
        endTime (int, optional)
        current (int, optional): Default 1
        size (int, optional): Default 10, Max 100
        fromSymbol (str, optional): Must be sent when type are ISOLATEDMARGIN_MARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
        toSymbol (str, optional): Must be sent when type are MARGIN_ISOLATEDMARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(type, "type")
    check_enum_parameter(type, TransferType)
    payload = {"type": type, **kwargs}
    return self.sign_request("GET", "/sapi/v1/asset/transfer", payload)


def transfer_dust(self, asset: list, **kwargs):
    """Dust Transfer (USER_DATA)
    Convert dust assets to BNB.

    POST /sapi/v1/asset/dust

    https://developers.binance.com/docs/wallet/asset/dust-transfer

    Args:
        asset (str)
    Keyword Args:
        accountType (str, optional): SPOT or MARGIN, default SPOT
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameter(asset, "asset")

    payload = {"asset": ",".join(asset), **kwargs}

    return self.sign_request("POST", "/sapi/v1/asset/dust", payload)


def asset_dividend_record(self, **kwargs):
    """Asset Dividend Record (USER_DATA)
    Query asset dividend record.

    GET /sapi/v1/asset/assetDividend

    https://developers.binance.com/docs/wallet/asset/assets-divided-record

    Keyword Args:
        asset (str, optional)
        startTime (int, optional)
        endTime (int, optional)
        limit (int, optional): Default 20, max 500
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/asset/assetDividend", kwargs)


def asset_detail(self, **kwargs):
    """Asset Detail (USER_DATA)
    Fetch details of assets supported on Binance.

    GET /sapi/v1/asset/assetDetail

    https://developers.binance.com/docs/wallet/asset/asset-detail

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/asset/assetDetail", kwargs)


def trade_fee(self, **kwargs):
    """Trade Fee (USER_DATA)
    Fetch trade fee, values in percentage.

    GET /sapi/v1/asset/tradeFee

    https://developers.binance.com/docs/wallet/asset/trade-fee

    Keyword Args:
        symbol (str, optional)
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/asset/tradeFee", kwargs)


def funding_wallet(self, **kwargs):
    """Funding Wallet (USER_DATA)

    POST /sapi/v1/asset/get-funding-asset

    https://developers.binance.com/docs/wallet/asset/funding-wallet

    Keyword Args:
        asset (str, optional)
        needBtcValuation (str, optional): true or false
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("POST", "/sapi/v1/asset/get-funding-asset", kwargs)


def user_asset(self, **kwargs):
    """User Asset (USER_DATA)

    Get user assets, just for positive data.

    Weight(IP): 5

    POST /sapi/v3/asset/getUserAsset

    https://developers.binance.com/docs/wallet/asset/user-assets

    Keyword Args:
        asset (str, optional): If asset is blank, then query all positive assets user have.
        needBtcValuation (str, optional)
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/sapi/v3/asset/getUserAsset"
    return self.sign_request("POST", url_path, {**kwargs})


def api_key_permissions(self, **kwargs):
    """Get API Key Permission (USER_DATA)

    GET /sapi/v1/account/apiRestrictions

    https://developers.binance.com/docs/wallet/account/api-key-permission

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/account/apiRestrictions", kwargs)


def local_entity_withdraw(
    self, coin: str, address: str, amount: float, questionnaire: str, **kwargs
):
    """Withdraw (for local entities that require travel rule) (USER_DATA)

    Submit a withdrawal request for local entities that required travel rule.

    Weight(UID): 600

    POST /sapi/v1/localentity/withdraw/apply

    https://developers.binance.com/docs/wallet/travel-rule/withdraw

    Args:
        coin (str)
        address (str)
        amount (float)
        questionnaire (str): Questionnaire ID
    Keyword Args:
        withdrawOrderId (str, optional): withdrawID defined by the client (i.e. client's internal withdrawID)
        network (str, optional)
        addressTag (str, optional): Secondary address identifier for coins like XRP,XMR etc.
        transactionFeeFlag (bool, optional): When making internal transfer, true for returning the fee to the destination account; false for returning the fee back to the departure account. Default false.
        name (str, optional): Description of the address. Address book cap is 200, space in name should be encoded into %20
        walletType (int, optional): The wallet type for withdraw, 0-spot wallet, 1-funding wallet. Default walletType is the current "selected wallet" under wallet->Fiat and Spot/Funding->Deposit
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters(
        [
            [coin, "coin"],
            [address, "address"],
            [amount, "amount"],
            [questionnaire, "questionnaire"],
        ]
    )

    payload = {
        "coin": coin,
        "address": address,
        "amount": amount,
        "questionnaire": questionnaire,
        **kwargs,
    }
    return self.sign_request("POST", "/sapi/v1/localentity/withdraw/apply", payload)


def local_entity_withdraw_history(self, **kwargs):
    """Withdraw History (for local entities that require travel rule) (supporting network) (USER_DATA)

    Fetch withdraw history for local entities that required travel rule.

    Weight(IP): 18000 Request limit: 10 requests per second

    GET /sapi/v1/localentity/withdraw/history

    https://developers.binance.com/docs/wallet/travel-rule/withdraw-history

    Keyword Args:
        trId (str, optional): Separated list of travel rule record Ids
        txId (str, optional): Separated list of transaction Ids
        withdrawOrderId (str, optional): Separated list of withdrawID defined by the client (i.e. client's internal withdrawID).
        network (str, optional)
        coin (str, optional)
        travelRuleStatus (int, optional): 0: Completed, 1: Pending, 2: Failed
        offset (int, optional): Default: 0
        limit (int, optional): Default: 1000, Max: 1000
        startTime (int, optional): Default: 90 days from current timestamp
        endTime (int, optional): Default: present timestamp
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    url_path = "/sapi/v1/localentity/withdraw/history"
    return self.sign_request("GET", url_path, {**kwargs})


def local_entity_submit_deposit_questionnaire(
    self, tranId: int, questionnaire: str, **kwargs
):
    """Submit Deposit Questionnaire (For local entities that require travel rule) (supporting network) (USER_DATA)

    Submit questionnaire for local entities that require travel rule.
    The questionnaire is only applies to transactions from unhosted wallets or VASPs that are not yet onboarded with GTR.

    Weight(UID): 600

    PUT /sapi/v1/localentity/deposit/provide-info

    https://developers.binance.com/docs/wallet/travel-rule/deposit-provide-info

    Args:
        tranId (int): Wallet tran Id
        questionnaire (str): JSON format questionnaire answers.
    """
    check_required_parameters([[tranId, "tranId"], [questionnaire, "questionnaire"]])

    payload = {"tranId": tranId, "questionnaire": questionnaire, **kwargs}
    return self.sign_request(
        "PUT", "/sapi/v1/localentity/deposit/provide-info", payload
    )


def local_entity_deposit_history(self, **kwargs):
    """Deposit History (for local entities that required travel rule) (supporting network) (USER_DATA)

    Fetch deposit history for local entities that required travel rule.

    Weight(IP): 1

    GET /sapi/v1/localentity/deposit/history

    https://developers.binance.com/docs/wallet/travel-rule/deposit-history

    Keyword Args:
        trId (str, optional): Separated list of travel rule record Ids
        txId (str, optional): Separated list of transaction Ids
        tranId (str, optional): Separated list of wallet tran Ids
        network (str, optional)
        coin (str, optional)
        travelRuleStatus (int, optional): 0: Completed, 1: Pending, 2: Failed
        pendingQuestionnaire (bool, optional): true: Only return records that pending deposit questionnaire. false/not provided: return all records.
        startTime (int, optional): Default: 90 days from current timestamp
        endTime (int, optional): Default: present timestamp
        offset (int, optional): Default: 0
        limit (int, optional): Default: 1000, Max: 1000
    """
    url_path = "/sapi/v1/localentity/deposit/history"
    return self.sign_request("GET", url_path, {**kwargs})


def bnb_convertible_assets(self, **kwargs):
    """Get Assets That Can Be Converted Into BNB (USER_DATA)

    POST /sapi/v1/asset/dust-btc

    https://developers.binance.com/docs/wallet/asset/assets-can-convert-bnb

    Keyword Args:
        accountType (str, optional): SPOT or MARGIN, default SPOT
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("POST", "/sapi/v1/asset/dust-btc", kwargs)


def list_deposit_address(self, coin: str, **kwargs):
    """Fetch deposit address list with network(USER_DATA)

    GET /sapi/v1/capital/deposit/address/list

    https://developers.binance.com/docs/wallet/capital/fetch-deposit-address-list-with-network

    Args:
        coin (str): coin refers to the parent network address format that the address is using
    Keyword Args:
        network (str, optional)
    """
    check_required_parameter(coin, "coin")
    payload = {"coin": coin, **kwargs}
    return self.sign_request("GET", "/sapi/v1/capital/deposit/address/list", payload)


def cloud_mining_trans_history(self, startTime: int, endTime: int, **kwargs):
    """Get Cloud-Mining payment and refund history (USER_DATA)

    GET /sapi/v1/asset/ledger-transfer/cloud-mining/queryByPage

    https://developers.binance.com/docs/wallet/asset/cloud-mining-payment-and-refund-history

    Args:
        startTime (int)
        endTime (int)
    Keyword Args:
        tranId (int, optional)
        clientTranId (str, optional)
        asset (str, optional)
        current (int, optional): Default Value: 1
        size (int, optional): Default Value: 100; Max Value: 100
        recvWindow (int, optional)
    """

    check_required_parameters([[startTime, "startTime"], [endTime, "endTime"]])

    url_path = "/sapi/v1/asset/ledger-transfer/cloud-mining/queryByPage"
    payload = {"startTime": startTime, "endTime": endTime, **kwargs}
    return self.sign_request("GET", url_path, payload)


def one_click_arrival_deposit_apply(self, **kwargs):
    """One click arrival deposit apply (USER_DATA)

    Apply deposit credit for expired address (One click arrival)

    Weight(IP): 1

    POST /sapi/v1/capital/deposit/credit-apply

    https://developers.binance.com/docs/wallet/capital/one-click-arrival-deposite-apply

    Keyword Args:
        depositId (int, optional): Deposit record Id, priority use
        txId (str, optional): Deposit txId, used when depositId is not specified
        subAccountId (int, optional)
        subUserId (int, optional)
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/sapi/v1/capital/deposit/credit-apply"
    return self.sign_request("POST", url_path, {**kwargs})


def balance(self, **kwargs):
    """Query User Wallet Balance (USER_DATA)

    Weight(IP): 60

    GET /sapi/v1/asset/wallet/balance

    https://developers.binance.com/docs/wallet/asset/query-user-wallet-balance

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/sapi/v1/asset/wallet/balance"
    return self.sign_request("GET", url_path, {**kwargs})


def delist_schedule_symbols(self, **kwargs):
    """Get symbols delist schedule for spot (MARKET_DATA)

    GET /sapi/v1/spot/delist-schedule

    https://developers.binance.com/docs/wallet/others/delist-schedule

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/sapi/v1/spot/delist-schedule"
    return self.sign_request("GET", url_path, {**kwargs})
