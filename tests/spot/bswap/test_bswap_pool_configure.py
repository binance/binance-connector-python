import responses
from binance.spot import Spot as Client
from tests.util import mock_http_response
from tests.util import random_str

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()


@mock_http_response(responses.GET, "sapi/v1/bswap/poolConfigure", mock_item, 200)
def test_bswap_pool_configure():
    """Tests the API endpoint to get pool configure"""

    client = Client(key, secret)
    response = client.bswap_pool_configure()
    response.should.equal(mock_item)


@mock_http_response(
    responses.GET, "sapi/v1/bswap/poolConfigure\\?poolId=2", mock_item, 200
)
def test_bswap_pool_configure_with_poolId():
    """Tests the API endpoint to get pool configure with poolId"""

    client = Client(key, secret)
    response = client.bswap_pool_configure(poolId=2)
    response.should.equal(mock_item)
