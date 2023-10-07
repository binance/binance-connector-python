import responses

from binance.spot import Spot as Client
from tests.util import random_str
from binance.lib.utils import encoded_string
from tests.util import mock_http_response


mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

params = {"email": "alice@test.com", "recvWindow": 1000}


@mock_http_response(
    responses.GET,
    "/sapi/v1/sub-account/futures/positionRisk\\?" + encoded_string(params),
    mock_item,
    200,
)
def test_futures_position_risk_of_sub_account():
    """Tests the API endpoint to futures position-risk of sub-account"""

    client = Client(key, secret)
    response = client.futures_position_risk_of_sub_account(**params)
    response.should.equal(mock_item)
