import responses

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

symbol = "BNBUSDT"
amount = "100"

params = {"symbol": symbol}


def test_margin_pair_index_without_asset():
    """Tests the API endpoint to margin pair index without asset"""

    client = Client(key, secret)
    client.margin_pair_index.when.called_with("").should.throw(ParameterRequiredError)


@mock_http_response(
    responses.GET, "/sapi/v1/margin/priceIndex\\?" + urlencode(params), mock_item, 200
)
def test_margin_pair_index():
    """Tests the API endpoint to margin pair index"""

    client = Client(key, secret)
    response = client.margin_pair_index(**params)
    response.should.equal(mock_item)
