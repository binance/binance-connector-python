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

params = {"coin": "USDT", "collateralCoin": "BTC", "amount": "1"}


def test_futures_loan_borrow_without_coin():
    """Tests the API endpoint to borrow cross funds without coin"""

    params = {"coin": "", "collateralCoin": "BTC"}

    client = Client(key, secret)
    client.futures_loan_borrow.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


def test_futures_loan_borrow_without_collateralCoin():
    """Tests the API endpoint to borrow cross funds without collateralCoin"""

    params = {"coin": "USDT", "collateralCoin": ""}

    client = Client(key, secret)
    client.futures_loan_borrow.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.POST,
    "/sapi/v1/futures/loan/borrow\\?" + urlencode(params),
    mock_item,
    200,
)
def test_futures_loan_borrow():
    """Tests the API endpoint to borrow cross funds"""

    client = Client(key, secret)
    response = client.futures_loan_borrow(**params)
    response.should.equal(mock_item)
