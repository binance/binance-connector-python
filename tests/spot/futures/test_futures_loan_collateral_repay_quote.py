import responses

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1105, "msg": "error message."}

key = random_str()
secret = random_str()

params = {"coin": "USDT", "collateralCoin": "BTC", "amount": "0.00222"}


def test_futures_loan_collateral_repay_quote_without_coin():
    """Tests the API endpoint to Get Collateral Repay Quote without coin"""

    params = {
        "coin": "",
        "collateralCoin": "BTC",
        "amount": "0.00222",
    }
    client = Client(key, secret)
    client.futures_loan_collateral_repay_quote.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


def test_futures_loan_collateral_repay_quote_without_collateralCoin():
    """Tests the API endpoint to Get Collateral Repay Quote without collateralCoin"""

    params = {"coin": "USDT", "collateralCoin": "", "amount": "0.00222"}
    client = Client(key, secret)
    client.futures_loan_collateral_repay_quote.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


def test_futures_loan_collateral_repay_quote_without_amount():
    """Tests the API endpoint to Get Collateral Repay Quote without amount"""

    params = {"coin": "USDT", "collateralCoin": "", "amount": ""}
    client = Client(key, secret)
    client.futures_loan_collateral_repay_quote.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.GET,
    "/sapi/v1/futures/loan/collateralRepay\\?" + urlencode(params),
    mock_item,
    200,
)
def test_futures_loan_collateral_repay_quote():
    """Tests the API endpoint to Get Collateral Repay Quote"""

    client = Client(key, secret)
    response = client.futures_loan_collateral_repay_quote(**params)
    response.should.equal(mock_item)
