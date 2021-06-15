import responses

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1105, "msg": 'Parameter "orderId" was empty.'}

key = random_str()
secret = random_str()


def test_isolated_margin_pair_without_symbol():
    """Tests the API endpoint to query isolated margin pair without symbol"""

    client = Client(key, secret)
    client.isolated_margin_pair.when.called_with("").should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.GET,
    "/sapi/v1/margin/isolated/pair\\?" + urlencode({"symbol": "BTCUSDT"}),
    mock_item,
    200,
)
def test_isolated_margin_pair():
    """Tests the API endpoint to query isolated margin pair"""

    client = Client(key, secret)
    response = client.isolated_margin_pair("BTCUSDT")
    response.should.equal(mock_item)
