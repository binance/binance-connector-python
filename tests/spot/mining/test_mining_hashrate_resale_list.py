import responses

from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()


@mock_http_response(
    responses.GET, "/sapi/v1/mining/hash-transfer/config/details/list", mock_item, 200
)
def test_mining_hashrate_resale_list():
    """Tests the API endpoint to get hashrate resale list"""

    client = Client(key, secret)
    response = client.mining_hashrate_resale_list()
    response.should.equal(mock_item)
