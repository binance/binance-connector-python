import responses

from binance.spot import Spot as Client
from tests.util import random_str
from binance.lib.utils import encoded_string
from tests.util import mock_http_response


mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

param = {"email": "alice@test.com", "recvWindow": 1000}


@mock_http_response(
    responses.POST,
    "/sapi/v1/sub-account/eoptions/enable\\?" + encoded_string(param),
    mock_item,
    200,
)
def test_enable_options_for_sub_account():
    """Tests the API endpoint to enable options for sub-account"""

    client = Client(key, secret)
    response = client.enable_options_for_sub_account(**param)
    response.should.equal(mock_item)
