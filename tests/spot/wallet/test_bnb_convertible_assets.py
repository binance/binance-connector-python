import responses
from binance.spot import Spot as Client
from tests.util import mock_http_response
from tests.util import random_str

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()


@mock_http_response(responses.POST, "/sapi/v1/asset/dust-btc", mock_item, 200)
def test_bnb_convertible_assets():
    """Tests the API endpoint to get Assets That Can Be Converted Into BNB"""

    client = Client(key, secret)
    response = client.bnb_convertible_assets()
    response.should.equal(mock_item)
