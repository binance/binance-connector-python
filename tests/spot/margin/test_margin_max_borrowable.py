import responses

from binance.spot import Spot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_http_response
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

params = {"asset": "BNB", "recvWindow": 1000}


@mock_http_response(responses.GET, "/sapi/v1/margin/maxBorrowable", mock_exception, 400)
def test_margin_max_borrowable_without_asset():
    """Tests the API endpoint to query margin max borrowable without symbol"""

    client = Client(key, secret)
    client.margin_max_borrowable.when.called_with("").should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.GET,
    "/sapi/v1/margin/maxBorrowable\\?" + urlencode(params),
    mock_item,
    200,
)
def test_margin_max_borrowable():
    """Tests the API endpoint to query margin max borrowable"""

    client = Client(key, secret)
    response = client.margin_max_borrowable(**params)
    response.should.equal(mock_item)
