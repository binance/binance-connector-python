import responses

from binance.spot import Spot as Client
from tests.util import random_str
from binance.lib.utils import encoded_string
from tests.util import mock_http_response


mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

send_params = {
    "startTime": 1679416673000,
    "endTime": 1689416673000,
    "page": 1,
    "limit": 100,
}


@mock_http_response(
    responses.GET,
    "/sapi/v1/managed-subaccount/query-trans-log\\?" + encoded_string(send_params),
    mock_item,
    200,
)
def test_query_managed_sub_account_transfer_log():
    """Tests the API endpoint to query Managed Sub Account Transfer Log"""

    client = Client(key, secret)
    response = client.query_managed_sub_account_transfer_log(**send_params)
    response.should.equal(mock_item)
