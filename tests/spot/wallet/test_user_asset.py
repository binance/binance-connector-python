import responses

from binance.spot import Spot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_http_response

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

params = {"asset": "BNB", "recvWindow": 5000}


@mock_http_response(
    responses.POST,
    "/sapi/v3/asset/getUserAsset\\?" + urlencode(params),
    mock_item,
    200,
)
def test_user_asset():
    """Tests the API endpoint to user asset"""

    client = Client(key, secret)
    response = client.user_asset(**params)
    response.should.equal(mock_item)
