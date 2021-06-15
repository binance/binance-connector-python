import responses

from binance.error import ParameterRequiredError
from binance.spot import Spot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_http_response

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

params = {
    "asset": "BNB",
    "startTime": "1590969041003",
    "endTime": "1590969041003",
    "limit": 10,
    "recvWindow": 1000,
}


def test_margin_interest_rate_history_without_asset():
    """Tests the API endpoint to query margin interest rate history without asset"""

    client = Client(key, secret)
    client.margin_interest_rate_history.when.called_with("").should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.GET,
    "/sapi/v1/margin/interestRateHistory\\?" + urlencode(params),
    mock_item,
    200,
)
def test_margin_interest_rate_history():
    """Tests the API endpoint to query margin interest rate history"""

    client = Client(key, secret)
    response = client.margin_interest_rate_history(**params)
    response.should.equal(mock_item)
