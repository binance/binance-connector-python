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

params = {"orderId": 100000001, "amount": 100.5}


def test_loan_vip_repay_without_orderId():
    """Tests the API endpoint to repay vip loan without orderId"""

    params = {"orderId": "", "amount": 100.5}

    client.loan_vip_repay.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


def test_loan_vip_repay_without_amount():
    """Tests the API endpoint to repay vip loan without amount"""

    params = {
        "orderId": "USDT",
        "amount": "",
    }

    client.loan_vip_repay.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.POST,
    "/sapi/v1/loan/vip/repay\\?" + urlencode(params),
    mock_item,
    200,
)
def test_loan_vip_repay():
    """Tests the API endpoint to repay loan"""

    response = client.loan_vip_repay(**params)
    response.should.equal(mock_item)
