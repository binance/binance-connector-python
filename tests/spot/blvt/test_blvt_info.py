import responses
from binance.spot import Spot as Client
from tests.util import mock_http_response
from tests.util import random_str

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()


@mock_http_response(responses.GET, "/sapi/v1/blvt/tokenInfo", mock_item, 200)
def test_blvt_info():
    """Tests the API endpoint to get BLVT Info"""

    client = Client(key, secret)
    response = client.blvt_info()
    response.should.equal(mock_item)


@mock_http_response(
    responses.GET, "/sapi/v1/blvt/tokenInfo\\?tokenName=LINKUP", mock_item, 200
)
def test_blvt_info_with_tokenName():
    """Tests the API endpoint to get BLVT Info with tokenName"""

    client = Client(key, secret)
    response = client.blvt_info("LINKUP")
    response.should.equal(mock_item)
