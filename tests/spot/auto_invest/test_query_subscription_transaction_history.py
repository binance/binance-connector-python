import responses

from binance.spot import Spot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_http_response


mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

send_params = {"size": 100, "current": 1, "recvWindow": 5000}
expected_params = {"size": 100, "current": 1, "recvWindow": 5000}


@mock_http_response(
    responses.GET,
    "/sapi/v1/lending/auto-invest/history/list\\?" + urlencode(expected_params),
    mock_item,
    200,
)
def test_query_subscription_transaction_history():
    """Tests the API endpoint to query subscription transaction history"""

    client = Client(key, secret)
    response = client.query_subscription_transaction_history(**send_params)
    response.should.equal(mock_item)
