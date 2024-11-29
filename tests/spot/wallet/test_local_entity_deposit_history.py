import responses

from binance.spot import Spot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_http_response


mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

send_params = {"trId": "1234", "coin": "BNB"}
expected_params = {"trId": "1234", "coin": "BNB"}


@mock_http_response(
    responses.GET,
    "/sapi/v1/localentity/deposit/history\\?" + urlencode(expected_params),
    mock_item,
    200,
)
def test_local_entity_deposit_history():
    """Tests the API endpoint to fetch deposit history for local entities that required travel rule"""

    client = Client(key, secret)
    response = client.local_entity_deposit_history(**send_params)
    response.should.equal(mock_item)
