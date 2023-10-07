import responses

from binance.spot import Spot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_http_response


mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

send_params = {
    "symbol": "BNBUSDT",
    "preventedMatchId": 1,
    "fromPreventedMatchId": 1,
    "limit": 5,
    "recvWindow": 5000,
}
expected_params = {
    "symbol": "BNBUSDT",
    "preventedMatchId": 1,
    "fromPreventedMatchId": 1,
    "limit": 5,
    "recvWindow": 5000,
}


@mock_http_response(
    responses.GET,
    "/api/v3/myPreventedMatches\\?" + urlencode(expected_params),
    mock_item,
    200,
)
def test_query_prevented_matches():
    """Tests the API endpoint to query prevented matches"""

    client = Client(key, secret)
    response = client.query_prevented_matches(**send_params)
    response.should.equal(mock_item)
