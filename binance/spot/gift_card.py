from binance.lib.utils import check_required_parameters, check_required_parameter


def gift_card_create_code(self, token: str, amount: float, **kwargs):
    """Create a Binance Code (USER_DATA)

    POST /sapi/v1/giftcard/createCode

    This API is for creating a Binance Code. To get started with, please make sure:

    - You have a sufﬁcient balance in your Binance funding wallet
    - You need Enable Withdrawals for the API Key which requests this endpoint.

    https://binance-docs.github.io/apidocs/spot/en/#create-a-binance-code-user_data

    Args:
      token (str): The coin type contained in the Binance Code
      amount (float): The amount of the coin
    Keyword Args:
      recvWindow (int, optional): The value cannot be greater than 60000
    """
    params = [[token, "token"], [amount, "amount"]]
    check_required_parameters(params)

    payload = {"token": token, "amount": amount, **kwargs}

    return self.sign_request("POST", "/sapi/v1/giftcard/createCode", payload)


def gift_card_redeem_code(self, code: str, **kwargs):
    """Redeem a Binance Code (USER_DATA)

    POST /sapi/v1/giftcard/redeemCode

    This API is for redeeming the Binance Code. Once redeemed, the coins will be deposited in your funding wallet.

    Please note that if you enter the wrong code 5 times within 24 hours, you will no longer be able to redeem any Binance Code that day.

    https://binance-docs.github.io/apidocs/spot/en/#redeem-a-binance-code-user_data

    Args:
      code (str): Binance Code
    Keyword Args:
      recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(code, "code")

    payload = {"code": code, **kwargs}

    return self.sign_request("POST", "/sapi/v1/giftcard/redeemCode", payload)


def gift_card_verify_code(self, referenceNo: str, **kwargs):
    """Verify a Binance Code (USER_DATA)

    GET /sapi/v1/giftcard/verify

    This API is for verifying whether the Binance Code is valid or not by entering Binance Code or reference number.

    Please note that if you enter the wrong binance code 5 times within an hour, you will no longer be able to verify any binance code for that hour.

    https://binance-docs.github.io/apidocs/spot/en/#verify-a-binance-code-user_data

    Args:
      referenceNo (str): reference number
    Keyword Args:
      recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(referenceNo, "referenceNo")

    payload = {"referenceNo": referenceNo, **kwargs}

    return self.sign_request("GET", "/sapi/v1/giftcard/verify", payload)
