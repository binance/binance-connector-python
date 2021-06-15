import responses

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

params = {"symbol": "BNBUSDT"}


def test_margin_pair_without_asset():
    """Tests the API endpoint to margin pair without asset"""

    client = Client(key, secret)
    client.margin_pair.when.called_with("").should.throw(ParameterRequiredError)


@mock_http_response(
    responses.GET, "/sapi/v1/margin/pair\\?" + urlencode(params), mock_item, 200
)
def test_margin_pair():
    """Tests the API endpoint to margin pair"""

    client = Client(key, secret)
    response = client.margin_pair(**params)
    response.should.equal(mock_item)
