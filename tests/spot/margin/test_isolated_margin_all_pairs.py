import responses

from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1105, "msg": 'Parameter "orderId" was empty.'}

key = random_str()
secret = random_str()


@mock_http_response(responses.GET, "/sapi/v1/margin/isolated/allPairs", mock_item, 200)
def test_isolated_margin_all_pairs():
    """Tests the API endpoint to query isolated margin all pairs"""

    client = Client(key, secret)
    response = client.isolated_margin_all_pairs()
    response.should.equal(mock_item)
