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
    "startTime": "1590969041003",
    "endTime": "1590969041003",
    "size": 10,
    "recvWindow": 1000,
}


@mock_http_response(
    responses.GET,
    "/sapi/v1/margin/forceLiquidationRec\\?" + urlencode(params),
    mock_item,
    200,
)
def test_margin_force_liquidation_record():
    """Tests the API endpoint to query margin Force Liquidation Record"""

    client = Client(key, secret)
    response = client.margin_force_liquidation_record(**params)
    response.should.equal(mock_item)
