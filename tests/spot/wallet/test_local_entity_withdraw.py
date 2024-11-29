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
    "coin": "BNB",
    "address": "address",
    "amount": 0.1,
    "questionnaire": '{"questionnaire"}',
}
expected_params = {
    "coin": "BNB",
    "address": "address",
    "amount": 0.1,
    "questionnaire": '{"questionnaire"}',
}


@mock_http_response(
    responses.POST,
    "/sapi/v1/localentity/withdraw/apply\\?" + urlencode(expected_params),
    mock_item,
    200,
)
def test_local_entity_withdraw():
    """Tests the API endpoint to submit a withdrawal request for local entities"""

    client = Client(key, secret)
    response = client.local_entity_withdraw(**send_params)
    response.should.equal(mock_item)
