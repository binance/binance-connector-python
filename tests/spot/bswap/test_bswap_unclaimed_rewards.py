import responses
from binance.spot import Spot as Client
from tests.util import mock_http_response
from tests.util import random_str

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()
client = Client(key, secret)


@mock_http_response(responses.GET, "/sapi/v1/bswap/unclaimedRewards", mock_item, 200)
def test_bswap_unclaimed_rewards():
    """Tests the API endpoint to get unclaimed rewards record."""

    response = client.bswap_unclaimed_rewards()
    response.should.equal(mock_item)
