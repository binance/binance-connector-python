import responses

from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()


@mock_http_response(responses.GET, "/sapi/v1/margin/allAssets", mock_item, 200)
def test_margin_all_assets():
    """Tests the API endpoint to margin all assets"""

    client = Client(key, secret)
    response = client.margin_all_assets()
    response.should.equal(mock_item)
