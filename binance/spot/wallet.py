from binance.lib.utils import check_required_parameter
from binance.lib.utils import check_required_parameters
from binance.lib.utils import check_enum_parameter
from binance.lib.enums import TransferType


def system_status(self):
    """ System Status (System)
    Fetch system status.

    GET /sapi/v1/system/status

    https://binance-docs.github.io/apidocs/spot/en/#system-status-sapi-system

    """

    return self.query('/sapi/v1/system/status')


def coin_info(self, **kwargs):
    """ All Coins' Information (USER_DATA)
    Get information of coins (available for deposit and withdraw) for user.

    GET /sapi/v1/capital/config/getall

    https://binance-docs.github.io/apidocs/spot/en/#all-coins-39-information-user_data

    """

    return self.sign_request('GET', '/sapi/v1/capital/config/getall', kwargs)


def account_snapshot(self, type: str, **kwargs):
    """ Daily Account Snapshot (USER_DATA)

    GET /sapi/v1/accountSnapshot

    https://binance-docs.github.io/apidocs/spot/en/#daily-account-snapshot-user_data

    Parameteres:
    type -- mandatory/string -- "SPOT", "MARGIN", "FUTURES"
    """

    check_required_parameter(type, 'type')
    payload = {'type': type, **kwargs}
    return self.sign_request('GET', '/sapi/v1/accountSnapshot', payload)


def disable_fast_withdraw(self, **kwargs):
    """ Disable Fast Withdraw Switch (USER_DATA)

    POST /sapi/v1/account/disableFastWithdrawSwitch

    https://binance-docs.github.io/apidocs/spot/en/#disable-fast-withdraw-switch-user_data

    """

    return self.sign_request('POST', '/sapi/v1/account/disableFastWithdrawSwitch', kwargs)


def enable_fast_withdraw(self, **kwargs):
    """ Enable Fast Withdraw Switch (USER_DATA)

    POST /sapi/v1/account/enableFastWithdrawSwitch

    https://binance-docs.github.io/apidocs/spot/en/#enable-fast-withdraw-switch-user_data

    """

    return self.sign_request('POST', '/sapi/v1/account/enableFastWithdrawSwitch', kwargs)


def withdraw(self, coin: str, amount, address: str, **kwargs):
    """ Withdraw
    Submit a withdraw request.

    POST /sapi/v1/capital/withdraw/apply

    https://binance-docs.github.io/apidocs/spot/en/#withdraw-sapi

    """

    check_required_parameters([[coin, 'coin'], [amount, 'amount'], [address, 'address']])
    payload = {'coin': coin, 'amount': amount, 'address': address, **kwargs}
    return self.sign_request('POST', '/sapi/v1/capital/withdraw/apply', payload)


def deposit_history(self, **kwargs):
    """ Deposit History（supporting network） (USER_DATA)
    Fetch deposit history.

    GET /sapi/v1/capital/deposit/hisrec

    https://binance-docs.github.io/apidocs/spot/en/#deposit-history-supporting-network-user_data

    """

    return self.sign_request('GET', '/sapi/v1/capital/deposit/hisrec', kwargs)


def withdraw_history(self, **kwargs):
    """ Withdraw History (supporting network) (USER_DATA)
    Fetch withdraw history.

    GET /sapi/v1/capital/withdraw/history

    https://binance-docs.github.io/apidocs/spot/en/#deposit-history-user_data

    """

    return self.sign_request('GET', '/sapi/v1/capital/withdraw/history', kwargs)


def deposit_address(self, coin: str, **kwargs):
    """ Deposit Address (supporting network) (USER_DATA)
    Fetch deposit address with network.

    GET /sapi/v1/capital/deposit/address

    https://binance-docs.github.io/apidocs/spot/en/#deposit-address-supporting-network-user_data

    """

    check_required_parameter(coin, 'coin')
    payload = {'coin': coin, **kwargs}
    return self.sign_request('GET', '/sapi/v1/capital/deposit/address', payload)


def account_status(self, **kwargs):
    """ Account Status (USER_DATA)
    Fetch account status detail.

    GET /sapi/v1/account/status

    https://binance-docs.github.io/apidocs/spot/en/#account-status-sapi-user_data

    """

    return self.sign_request('GET', '/sapi/v1/account/status', kwargs)


def api_trading_status(self, **kwargs):
    """ Account API Trading Status (USER_DATA)
    Fetch account api trading status detail.

    GET /sapi/v1/account/apiTradingStatus

    https://binance-docs.github.io/apidocs/spot/en/#account-api-trading-status-sapi-user_data

    """

    return self.sign_request('GET', '/sapi/v1/account/apiTradingStatus', kwargs)


def dust_log(self, **kwargs):
    """ DustLog (USER_DATA)
    Fetch small amounts of assets exchanged BNB records.

    GET /sapi/v1/asset/dribblet

    https://binance-docs.github.io/apidocs/spot/en/#dustlog-sapi-user_data

    """

    return self.sign_request('GET', '/sapi/v1/asset/dribblet', kwargs)


def user_universal_transfer(self, type: str, asset: int, amount: str, **kwargs):
    """ User Universal Transfer

    POST /sapi/v1/asset/transfer

    https://binance-docs.github.io/apidocs/spot/en/#user-universal-transfer

    Parameters:
    | type       | mandatory  | string |               |
    | asset      | mandatory  | string |               |
    | amount     | mandatory  | string |               |
    | recvWindow | optional   | int    |               |
    """
    check_required_parameters([[type, 'type'], [asset, 'asset'], [amount, 'amount']])
    check_enum_parameter(type, TransferType)
    payload = {'type': type, 'asset': asset, 'amount': amount, **kwargs}
    return self.sign_request('POST', '/sapi/v1/asset/transfer', payload)


def user_universal_transfer_history(self, type: str, **kwargs):
    """ Query User Universal Transfer History

    GET /sapi/v1/asset/transfer

    https://binance-docs.github.io/apidocs/spot/en/#query-user-universal-transfer-history

    Parameters:
    | type       | mandatory  | string |                     |
    | startTime  | optional   | int    |                     |
    | endTime    | optional   | int    |                     |
    | current    | optional   | int    | Default 1           |
    | size       | optional   | int    | Default 10, Max 100 |
    | recvWindow | optional   | int    |                     |
    """
    check_required_parameter(type, 'type')
    check_enum_parameter(type, TransferType)
    payload = {'type': type, **kwargs}
    return self.sign_request('GET', '/sapi/v1/asset/transfer', payload)


def transfer_dust(self, asset, **kwargs):
    """ Dust Transfer (USER_DATA)
    Convert dust assets to BNB.

    POST /sapi/v1/asset/dust

    https://binance-docs.github.io/apidocs/spot/en/#dust-transfer-user_data

    """

    check_required_parameter(asset, 'asset')
    payload = {'asset': asset, **kwargs}

    return self.sign_request('POST', '/sapi/v1/asset/dust', payload)


def asset_dividen_record(self, **kwargs):
    """ Asset Dividend Record (USER_DATA)
    Query asset dividend record.

    GET /sapi/v1/asset/assetDividend

    https://binance-docs.github.io/apidocs/spot/en/#asset-dividend-record-user_data

    """

    return self.sign_request('GET', '/sapi/v1/asset/assetDividend', kwargs)


def asset_detail(self, **kwargs):
    """ Asset Detail (USER_DATA)
    Fetch details of assets supported on Binance.

    GET /sapi/v1/asset/assetDetail

    https://binance-docs.github.io/apidocs/spot/en/#asset-detail-sapi-user_data

    """

    return self.sign_request('GET', '/sapi/v1/asset/assetDetail', kwargs)


def trade_fee(self, **kwargs):
    """ Trade Fee (USER_DATA)
    Fetch trade fee, values in percentage.

    GET /sapi/v1/asset/tradeFee

    https://binance-docs.github.io/apidocs/spot/en/#trade-fee-sapi-user_data

    """

    return self.sign_request('GET', '/sapi/v1/asset/tradeFee', kwargs)
