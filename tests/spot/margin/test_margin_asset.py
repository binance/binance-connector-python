import responses

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

asset = "BNB"
amount = "100"

params = {"asset": asset}


def test_margin_asset_without_asset():
    """Tests the API endpoint to margin asset without asset"""

    client = Client(key, secret)
    client.margin_asset.when.called_with("").should.throw(ParameterRequiredError)


@mock_http_response(
    responses.GET, "/sapi/v1/margin/asset\\?" + urlencode(params), mock_item, 200
)
def test_margin_asset():
    """Tests the API endpoint to margin asset"""

    client = Client(key, secret)
    response = client.margin_asset(**params)
    response.should.equal(mock_item)
