import responses

from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.lib.utils import encoded_string
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()
params = {"asset": "BUSD", "recvWindow": 1000}

client = Client(key, secret)


def test_loan_history_without_asset():
    """Tests the API endpoint to query loan history without asset"""

    params = {"asset": "", "recvWindow": 1000}
    client.loan_history.when.called_with(**params).should.throw(ParameterRequiredError)


@mock_http_response(
    responses.GET,
    "/sapi/v1/loan/income\\?" + encoded_string(params),
    mock_item,
    200,
)
def test_loan_history():
    """Tests the API endpoint to query loan history"""

    response = client.loan_history(**params)
    response.should.equal(mock_item)
