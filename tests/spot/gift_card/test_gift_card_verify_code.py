import responses

from tests.util import random_str
from tests.util import mock_http_response
from urllib.parse import urlencode
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

params = {"referenceNo": random_str()}

client = Client(key, secret)


def test_gift_card_verify_code_without_params():
    """Tests the API endpoint to verify a Binance Code without params"""

    client.gift_card_verify_code.when.called_with("").should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.GET,
    "/sapi/v1/giftcard/verify\\?" + urlencode(params),
    mock_item,
    200,
)
def test_gift_card_verify_code():
    """Tests the API endpoint to verify a Binance Code"""

    response = client.gift_card_verify_code(**params)
    response.should.equal(mock_item)
