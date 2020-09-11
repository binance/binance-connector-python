from binance.lib.utils import check_required_parameter
from binance.lib.utils import check_required_parameters

"""
  Endpoints that for moving funds between spot and futures accounts.
  It's not for trading on futures.

"""

def futures_transfer(self, asset: str, amount, type: int, **kwargs):
    """ New Future Account Transfer (FUTURES)
    Execute transfer between spot account and futures account.

    POST /sapi/v1/futures/transfer

    https://binance-docs.github.io/apidocs/spot/en/#new-future-account-transfer-futures

    Parameteres:
    | asset      | mandatory | string | The asset being transferred, e.g., USDT |
    | symbol     | mandatory | float  | The amount to be transferred            |
    | type       | mandatory | int    |                                         |
    | recvWindow | optional  | int    |                                         |

    type:
      1: transfer from spot account to USDT-Ⓜ futures account.
      2: transfer from USDT-Ⓜ futures account to spot account.
      3: transfer from spot account to COIN-Ⓜ futures account.
      4: transfer from COIN-Ⓜ futures account to spot account.
    """

    check_required_parameters([
      [asset, 'asset'], 
      [amount, 'amount'], 
      [type, 'type']
    ])

    payload = {
        'asset': asset,
        'amount': amount,
        'type': type,
        **kwargs
    }
    return self.sign_request('POST', '/sapi/v1/futures/transfer', payload)


def futures_transfer_history(self, asset: str, startTime, **kwargs):
    """ Get Future Account Transaction History List (USER_DATA)

    GET /sapi/v1/futures/transfer

    https://binance-docs.github.io/apidocs/spot/en/#get-future-account-transaction-history-list-user_data

    Parameteres:
    | asset      | mandatory | string | The asset being transferred, e.g., USDT          |
    | startTime  | mandatory | int    |                                                  |
    | endTime    | optional  | int    |                                                  |
    | current    | optional  | int    | Currently querying page. Start from 1. Default:1 |
    | size       | optional  | int    |                                                  |
    | recvWindow | optional  | int    |                                                  |
    """

    check_required_parameters([
      [asset, 'asset'], 
      [startTime, 'startTime']
    ])

    payload = {
        'asset': asset,
        'startTime': startTime,
        **kwargs
    }
    return self.sign_request('GET', '/sapi/v1/futures/transfer', payload)


def futures_loan_borrow(self, coin: str, collateralCoin: str, **kwargs):
    """ Borrow For Cross-Collateral (TRADE)

    POST /sapi/v1/futures/loan/borrow

    https://binance-docs.github.io/apidocs/spot/en/#borrow-for-cross-collateral-trade

    Parameteres:
    | coin             | mandatory | string |                                          |
    | amount           | -         | float  | mandatory when collateralAmount is empty |
    | collateralCoin   | mandatory | string |                                          |
    | collateralAmount | -         | float  | mandatory when amount is empty           |
    | recvWindow       | optional  | int    |                                          |
    """

    check_required_parameters([
      [coin, 'coin'], 
      [collateralCoin, 'collateralCoin']
    ])

    payload = {
        'coin': coin,
        'collateralCoin': collateralCoin,
        **kwargs
    }
    return self.sign_request('POST', '/sapi/v1/futures/loan/borrow', payload)


def futures_loan_borrow_history(self, **kwargs):
    """ Cross-Collateral Borrow History (USER_DATA)

    GET /sapi/v1/futures/loan/borrow/history

    https://binance-docs.github.io/apidocs/spot/en/#cross-collateral-borrow-history-user_data

    Parameteres:
    | coin       | optional | string |                       |
    | startTime  | optional | int    |                       |
    | endTime    | optional | int    |                       |
    | limit      | optional | int    | default 500, max 1000 |
    | recvWindow | optional | int    |                       |
    """

    return self.sign_request('GET', '/sapi/v1/futures/loan/borrow/history', kwargs)


def futures_loan_repay(self, coin: str, collateralCoin: str, amount, **kwargs):
    """ Repay For Cross-Collateral (TRADE)

    POST /sapi/v1/futures/loan/repay

    https://binance-docs.github.io/apidocs/spot/en/#repay-for-cross-collateral-trade

    Parameteres:
    | coin           | mandatory | string |
    | collateralCoin | mandatory | string |
    | amount         | mandatory | float  |
    | recvWindow     | optional  | int    |
    """

    check_required_parameters([
      [coin, 'coin'], 
      [collateralCoin, 'collateralCoin'],
      [amount, 'amount']
    ])

    payload = {
        'coin': coin,
        'collateralCoin': collateralCoin,
        'amount': amount,
        **kwargs
    }
    return self.sign_request('POST', '/sapi/v1/futures/loan/repay', payload)


def futures_loan_repay_history(self, **kwargs):
    """ Cross-Collateral Repayment History (USER_DATA)

    GET /sapi/v1/futures/loan/repay/history

    https://binance-docs.github.io/apidocs/spot/en/#cross-collateral-repayment-history-user_data

    Parameteres:
    | coin       | optional | string |                       |
    | startTime  | optional | int    |                       |
    | endTime    | optional | int    |                       |
    | limit      | optional | int    | default 500, max 1000 |
    | recvWindow | optional | int    |                       |
    """

    return self.sign_request('GET', '/sapi/v1/futures/loan/repay/history', kwargs)


def futures_loan_wallet(self, **kwargs):
    """ Cross-Collateral Wallet (USER_DATA)

    GET /sapi/v1/futures/loan/wallet

    https://binance-docs.github.io/apidocs/spot/en/#cross-collateral-wallet-user_data

    Parameteres:
    | recvWindow | optional | int    |                       |
    """

    return self.sign_request('GET', '/sapi/v1/futures/loan/wallet', kwargs)


def futures_loan_configs(self, **kwargs):
    """ Cross-Collateral Information (USER_DATA)

    GET /sapi/v1/futures/loan/configs

    https://binance-docs.github.io/apidocs/spot/en/#cross-collateral-information-user_data

    Parameteres:
    | collateralCoin | optional | string |
    | recvWindow     | optional | int    |
    """

    return self.sign_request('GET', '/sapi/v1/futures/loan/configs', kwargs)


def futures_loan_calc_adjust_level(self, collateralCoin: str, amount, direction: str, **kwargs):
    """ Calculate Rate After Adjust Cross-Collateral LTV (USER_DATA)

    GET /sapi/v1/futures/loan/calcAdjustLevel

    https://binance-docs.github.io/apidocs/spot/en/#calculate-rate-after-adjust-cross-collateral-ltv-user_data

    Parameteres:
    | collateralCoin | mandatory | string |                         |
    | amount         | mandatory | string |                         |
    | direction      | mandatory | string | "ADDITIONAL", "REDUCED" |
    | recvWindow     | optional  | int    |                         |
    """

    check_required_parameters([
      [collateralCoin, 'collateralCoin'], 
      [amount, 'amount'],
      [direction, 'direction']
    ])

    payload = {
        'collateralCoin': collateralCoin,
        'amount': amount,
        'direction': direction,
        **kwargs
    }

    return self.sign_request('GET', '/sapi/v1/futures/loan/calcAdjustLevel', payload)


def futures_loan_calc_max_adjust_amount(self, collateralCoin: str, **kwargs):
    """ Get Max Amount for Adjust Cross-Collateral LTV (USER_DATA)

    GET /sapi/v1/futures/loan/calcMaxAdjustAmount

    https://binance-docs.github.io/apidocs/spot/en/#get-max-amount-for-adjust-cross-collateral-ltv-user_data

    Parameteres:
    | collateralCoin | mandatory | string |                         |
    | recvWindow     | optional  | int    |                         |
    """

    check_required_parameter(collateralCoin, 'collateralCoin')

    payload = {
        'collateralCoin': collateralCoin,
        **kwargs
    }

    return self.sign_request('GET', '/sapi/v1/futures/loan/calcMaxAdjustAmount', payload)


def futures_loan_adjust_collateral(self, collateralCoin: str, amount, direction: str, **kwargs):
    """ Adjust Cross-Collateral LTV (TRADE)

    POST /sapi/v1/futures/loan/adjustCollateral

    https://binance-docs.github.io/apidocs/spot/en/#adjust-cross-collateral-ltv-trade

    Parameteres:
    | collateralCoin | mandatory | string |                         |
    | amount         | mandatory | string |                         |
    | direction      | mandatory | string | "ADDITIONAL", "REDUCED" |
    | recvWindow     | optional  | int    |                         |
    """

    check_required_parameters([
      [collateralCoin, 'collateralCoin'], 
      [amount, 'amount'],
      [direction, 'direction']
    ])

    payload = {
        'collateralCoin': collateralCoin,
        'amount': amount,
        'direction': direction,
        **kwargs
    }

    return self.sign_request('POST', '/sapi/v1/futures/loan/adjustCollateral', payload)


def futures_loan_adjust_collateral_history(self, **kwargs):
    """ Adjust Cross-Collateral LTV History (USER_DATA)

    GET /sapi/v1/futures/loan/adjustCollateral/history

    https://binance-docs.github.io/apidocs/spot/en/#adjust-cross-collateral-ltv-history-user_data

    Parameteres:
    | collateralCoin | optional | string |                       |
    | startTime      | optional | int    |                       |
    | endTime        | optional | int    |                       |
    | limit          | optional | int    | default 500, max 1000 |
    | recvWindow     | optional | int    |                       |
    """

    return self.sign_request('GET', '/sapi/v1/futures/loan/adjustCollateral/history', kwargs)


def futures_loan_liquidation_history(self, **kwargs):
    """ Cross-Collateral Liquidation History (USER_DATA)

    GET /sapi/v1/futures/loan/liquidationHistory

    https://binance-docs.github.io/apidocs/spot/en/#cross-collateral-liquidation-history-user_data

    Parameteres:
    | collateralCoin | optional | string |                       |
    | startTime      | optional | int    |                       |
    | endTime        | optional | int    |                       |
    | limit          | optional | int    | default 500, max 1000 |
    | recvWindow     | optional | int    |                       |
    """

    return self.sign_request('GET', '/sapi/v1/futures/loan/liquidationHistory', kwargs)
