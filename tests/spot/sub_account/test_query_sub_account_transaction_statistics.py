import responses

from binance.spot import Spot as Client
from tests.util import random_str
from binance.lib.utils import encoded_string
from tests.util import mock_http_response


mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

send_params = {"email": "alice@test.com", "recvWindow": 5000}
expected_params = {"email": "alice@test.com", "recvWindow": 5000}


@mock_http_response(
    responses.GET,
    "/sapi/v1/sub-account/transaction-statistics\\?" + encoded_string(expected_params),
    mock_item,
    200,
)
def test_query_sub_account_transaction_statistics():
    """Tests the API endpoint to query sub-account transaction statistics"""

    client = Client(key, secret)
    response = client.query_sub_account_transaction_statistics(**send_params)
    response.should.equal(mock_item)
