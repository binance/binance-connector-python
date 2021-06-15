import responses

from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()


@mock_http_response(responses.POST, "/sapi/v1/bnbBurn", mock_item, 200)
def test_toggle_bnbBurn():
    """Tests the API endpoint to Toggle BNBBurn On Spot Trade And Margin Interest"""

    client = Client(key, secret)
    response = client.toggle_bnbBurn()
    response.should.equal(mock_item)
