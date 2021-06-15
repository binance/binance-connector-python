import responses
from binance.spot import Spot as Client
from tests.util import mock_http_response
from tests.util import random_str

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()


@mock_http_response(responses.GET, "/sapi/v1/blvt/redeem/record", mock_item, 200)
def test_redemption_record():
    """Tests the API endpoint to Query Redemption Record"""

    client = Client(key, secret)
    response = client.redemption_record()
    response.should.equal(mock_item)
