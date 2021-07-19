import responses
from binance.spot import Spot as Client
from tests.util import mock_http_response
from tests.util import random_str

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()


@mock_http_response(responses.POST, "/sapi/v1/asset/get-funding-asset", mock_item, 200)
def test_funding_wallet():
    """Tests the API endpoint to obtain the assets from the funding wallet"""

    client = Client(key, secret)
    response = client.funding_wallet()
    response.should.equal(mock_item)
