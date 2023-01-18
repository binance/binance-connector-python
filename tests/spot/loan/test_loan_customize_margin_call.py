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

params = {"marginCall": 0.1, "collateralCoin": "BUSD"}


def test_loan_customize_margin_call_without_margin_call():
    """Tests the API endpoint to customize margin call with missing parameter"""

    params = {"marginCall": ""}

    client.loan_customize_margin_call.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.POST,
    "/sapi/v1/loan/customize/margin_call\\?" + urlencode(params),
    mock_item,
    200,
)
def test_loan_customize_margin_call():
    """Tests the API endpoint to customize margin call for ongoing orders only"""

    response = client.loan_customize_margin_call(**params)
    response.should.equal(mock_item)
