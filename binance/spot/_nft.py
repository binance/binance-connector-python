from binance.lib.utils import check_required_parameter


def nft_transaction_history(self, orderType: int, **kwargs):
    """Get NFT Transaction History (USER_DATA)

    GET /sapi/v1/nft/history/transactions

    https://binance-docs.github.io/apidocs/spot/en/#get-nft-transaction-history-user_data

    Args:
      orderType (int): 0: purchase order, 1: sell order, 2: royalty income, 3: primary market order, 4: mint fee
    Keyword Args:
      startTime (int, optional)
      endTime (int, optional)
      limit (int, optional): Default 50, Max 50
      page (int, optional): Default 1
      recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(orderType, "orderType")
    params = {"orderType": orderType, **kwargs}
    return self.sign_request("GET", "/sapi/v1/nft/history/transactions", params)


def nft_deposit_history(self, **kwargs):
    """Get NFT Deposit History(USER_DATA)

    GET /sapi/v1/nft/history/deposit

    https://binance-docs.github.io/apidocs/spot/en/#get-nft-deposit-history-user_data

    Keyword Args:
      startTime (int, optional)
      endTime (int, optional)
      limit (int, optional): Default 50, Max 50
      page (int, optional): Default 1
      recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/nft/history/deposit", kwargs)


def nft_withdraw_history(self, **kwargs):
    """Get NFT Withdraw History (USER_DATA)

    GET /sapi/v1/nft/history/withdraw

    https://binance-docs.github.io/apidocs/spot/en/#get-nft-withdraw-history-user_data

    Keyword Args:
      startTime (int, optional)
      endTime (int, optional)
      limit (int, optional): Default 50, Max 50
      page (int, optional): Default 1
      recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/nft/history/withdraw", kwargs)


def nft_asset(self, **kwargs):
    """Get NFT Asset (USER_DATA)

    GET /sapi/v1/nft/user/getAsset

    https://binance-docs.github.io/apidocs/spot/en/#get-nft-asset-user_data

    Keyword Args:
      limit (int, optional): Default 50, Max 50
      page (int, optional): Default 1
      recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/nft/user/getAsset", kwargs)
