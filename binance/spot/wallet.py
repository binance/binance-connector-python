from binance.lib.utils import check_required_parameter
from binance.lib.utils import check_required_parameters


def system_status(self):
    """ System Status (System)
    Fetch system status.

    GET /wapi/v3/systemStatus.html

    https://binance-docs.github.io/apidocs/spot/en/#wallet-endpoints

    """

    return self.query('/wapi/v3/systemStatus.html')


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

    GET /wapi/v3/accountStatus.html

    https://binance-docs.github.io/apidocs/spot/en/#account-status-user_data

    """

    return self.sign_request('GET', '/wapi/v3/accountStatus.html', kwargs)


def api_trading_status(self, **kwargs):
    """ Account API Trading Status (USER_DATA)
    Fetch account api trading status detail.

    GET /wapi/v3/apiTradingStatus.html

    https://binance-docs.github.io/apidocs/spot/en/#account-api-trading-status-user_data

    """

    return self.sign_request('GET', '/wapi/v3/apiTradingStatus.html', kwargs)


def dust_log(self, **kwargs):
    """ DustLog (USER_DATA)
    Fetch small amounts of assets exchanged BNB records.

    GET /wapi/v3/userAssetDribbletLog.html

    https://binance-docs.github.io/apidocs/spot/en/#dustlog-user_data

    """

    return self.sign_request('GET', '/wapi/v3/userAssetDribbletLog.html', kwargs)


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

    GET /wapi/v3/assetDetail.html

    https://binance-docs.github.io/apidocs/spot/en/#asset-detail-user_data

    """

    return self.sign_request('GET', '/wapi/v3/assetDetail.html', kwargs)


def trade_fee(self, **kwargs):
    """ Trade Fee (USER_DATA)
    Fetch trade fee, values in percentage.

    GET /wapi/v3/tradeFee.html

    https://binance-docs.github.io/apidocs/spot/en/#trade-fee-user_data

    """

    return self.sign_request('GET', '/wapi/v3/tradeFee.html', kwargs)
