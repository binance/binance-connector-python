import responses
from binance.spot import Spot as Client
from tests.util import mock_http_response
from tests.util import random_str

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()


@mock_http_response(responses.GET, "/sapi/v1/asset/dribblet", mock_item, 200)
def test_dust_log():
    """Tests the API endpoint to check dust log"""

    client = Client(key, secret)
    response = client.dust_log()
    response.should.equal(mock_item)
