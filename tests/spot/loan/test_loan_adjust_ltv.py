import responses

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()
client = Client(key, secret)

params = {"orderId": 756783308056935434, "amount": 100.1, "direction": "ADDITIONAL"}


def test_loan_adjust_ltv_without_orderId():
    """Tests the API endpoint to adjust LTV without orderId"""

    params = {"orderId": "", "amount": 100.1, "direction": "ADDITIONAL"}

    client.loan_adjust_ltv.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


def test_loan_adjust_ltv_without_amount():
    """Tests the API endpoint to adjust LTV without amount"""

    params = {"orderId": 756783308056935434, "amount": "", "direction": "ADDITIONAL"}

    client.loan_adjust_ltv.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


def test_loan_adjust_ltv_without_direction():
    """Tests the API endpoint to adjust LTV without direction"""

    params = {"orderId": 756783308056935434, "amount": 100.1, "direction": ""}

    client.loan_adjust_ltv.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.POST,
    "/sapi/v1/loan/adjust/ltv\\?" + urlencode(params),
    mock_item,
    200,
)
def test_loan_adjust_ltv():
    """Tests the API endpoint to adjust LTV"""

    response = client.loan_adjust_ltv(**params)
    response.should.equal(mock_item)
