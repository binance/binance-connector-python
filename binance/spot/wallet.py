from binance.lib.utils import check_required_parameter
from binance.lib.utils import check_required_parameters
from binance.lib.utils import check_enum_parameter
from binance.lib.enums import TransferType


def system_status(self):
    """System Status (System)
    Fetch system status.

    GET /sapi/v1/system/status

    https://binance-docs.github.io/apidocs/spot/en/#system-status-sapi-system
    """

    return self.query("/sapi/v1/system/status")


def coin_info(self, **kwargs):
    """All Coins' Information (USER_DATA)
    Get information of coins (available for deposit and withdraw) for user.

    GET /sapi/v1/capital/config/getall

    https://binance-docs.github.io/apidocs/spot/en/#all-coins-39-information-user_data

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/capital/config/getall", kwargs)


def account_snapshot(self, type: str, **kwargs):
    """Daily Account Snapshot (USER_DATA)

    GET /sapi/v1/accountSnapshot

    https://binance-docs.github.io/apidocs/spot/en/#daily-account-snapshot-user_data

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

    https://binance-docs.github.io/apidocs/spot/en/#disable-fast-withdraw-switch-user_data

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request(
        "POST", "/sapi/v1/account/disableFastWithdrawSwitch", kwargs
    )


def enable_fast_withdraw(self, **kwargs):
    """Enable Fast Withdraw Switch (USER_DATA)

    POST /sapi/v1/account/enableFastWithdrawSwitch

    https://binance-docs.github.io/apidocs/spot/en/#enable-fast-withdraw-switch-user_data

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

    https://binance-docs.github.io/apidocs/spot/en/#withdraw-user_data

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

    https://binance-docs.github.io/apidocs/spot/en/#deposit-history-supporting-network-user_data

    Keyword Args:
        coin (str, optional)
        status (int, optional): Default 0 (0:pending, 6: credited but cannot withdraw, 1:success)
        startTime (int, optional): Default: 90 days from current timestamp
        endTime (int, optional): Default: present timestamp
        offset (int, optional): Default value: 0
        limit (int, optional): Default:1000, Max:1000
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/capital/deposit/hisrec", kwargs)


def withdraw_history(self, **kwargs):
    """Withdraw History (supporting network) (USER_DATA)
    Fetch withdraw history.

    GET /sapi/v1/capital/withdraw/history

    https://binance-docs.github.io/apidocs/spot/en/#deposit-history-user_data

    Keyword Args:
        coin (str, optional)
        withdrawOrderId (str, optional)
        status (int, optional): Default 0 (0:Email Sent,1:Cancelled, 2:Awaiting Approval,
                3:Rejected, 4:Processing, 5:Failure, 6:Completed)
        offset (int, optional)
        limit (int, optional): Default: 1000, Max: 1000
        startTime (int, optional): Default: 90 days from current timestamp
        endTime (int, optional): Default: present timestamp
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/capital/withdraw/history", kwargs)


def deposit_address(self, coin: str, **kwargs):
    """Deposit Address (supporting network) (USER_DATA)
    Fetch deposit address with network.

    GET /sapi/v1/capital/deposit/address

    https://binance-docs.github.io/apidocs/spot/en/#deposit-address-supporting-network-user_data

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

    https://binance-docs.github.io/apidocs/spot/en/#account-status-sapi-user_data

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/account/status", kwargs)


def api_trading_status(self, **kwargs):
    """Account API Trading Status (USER_DATA)
    Fetch account api trading status detail.

    GET /sapi/v1/account/apiTradingStatus

    https://binance-docs.github.io/apidocs/spot/en/#account-api-trading-status-sapi-user_data

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/account/apiTradingStatus", kwargs)


def dust_log(self, **kwargs):
    """DustLog (USER_DATA)
    Fetch small amounts of assets exchanged BNB records.

    GET /sapi/v1/asset/dribblet

    https://binance-docs.github.io/apidocs/spot/en/#dustlog-sapi-user_data

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/asset/dribblet", kwargs)


def user_universal_transfer(self, type: str, asset: str, amount: str, **kwargs):
    """User Universal Transfer (USER_DATA)

    POST /sapi/v1/asset/transfer

    https://binance-docs.github.io/apidocs/spot/en/#user-universal-transfer-user_data

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

    https://binance-docs.github.io/apidocs/spot/en/#query-user-universal-transfer-history-user_data

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


def transfer_dust(self, asset, **kwargs):
    """Dust Transfer (USER_DATA)
    Convert dust assets to BNB.

    POST /sapi/v1/asset/dust

    https://binance-docs.github.io/apidocs/spot/en/#dust-transfer-user_data

    Args:
        asset (str)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameter(asset, "asset")
    payload = {"asset": asset, **kwargs}

    return self.sign_request("POST", "/sapi/v1/asset/dust", payload)


def asset_dividend_record(self, **kwargs):
    """Asset Dividend Record (USER_DATA)
    Query asset dividend record.

    GET /sapi/v1/asset/assetDividend

    https://binance-docs.github.io/apidocs/spot/en/#asset-dividend-record-user_data

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

    https://binance-docs.github.io/apidocs/spot/en/#asset-detail-sapi-user_data

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/asset/assetDetail", kwargs)


def trade_fee(self, **kwargs):
    """Trade Fee (USER_DATA)
    Fetch trade fee, values in percentage.

    GET /sapi/v1/asset/tradeFee

    https://binance-docs.github.io/apidocs/spot/en/#trade-fee-sapi-user_data

    Keyword Args:
        symbol (str, optional)
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/asset/tradeFee", kwargs)


def funding_wallet(self, **kwargs):
    """Funding Wallet (USER_DATA)

    POST /sapi/v1/asset/get-funding-asset

    https://binance-docs.github.io/apidocs/spot/en/#funding-wallet-user_data

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

    https://binance-docs.github.io/apidocs/spot/en/#user-asset-user_data

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

    https://binance-docs.github.io/apidocs/spot/en/#get-api-key-permission-user_data

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/account/apiRestrictions", kwargs)


def bnb_convertible_assets(self, **kwargs):
    """Get Assets That Can Be Converted Into BNB (USER_DATA)

    POST /sapi/v1/asset/dust-btc

    https://binance-docs.github.io/apidocs/spot/en/#get-assets-that-can-be-converted-into-bnb-user_data

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("POST", "/sapi/v1/asset/dust-btc", kwargs)
