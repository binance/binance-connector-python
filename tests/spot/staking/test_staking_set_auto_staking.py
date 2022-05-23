import responses

from binance.spot import Spot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_http_response

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

params = {
    "product": "STAKING",
    "positionId": "1234",
    "renewable": "true",
    "recvWindow": 5000,
}


@mock_http_response(
    responses.POST,
    "/sapi/v1/staking/setAutoStaking\\?" + urlencode(params),
    mock_item,
    200,
)
def test_staking_set_auto_staking():
    """Tests the API endpoint to staking set auto staking"""

    client = Client(key, secret)
    response = client.staking_set_auto_staking(**params)
    response.should.equal(mock_item)
