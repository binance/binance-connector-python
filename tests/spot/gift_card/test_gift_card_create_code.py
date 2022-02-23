import responses

from tests.util import random_str
from tests.util import mock_http_response
from urllib.parse import urlencode
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

params = {
    "token": "BNB",
    "amount": 0.2,
}

client = Client(key, secret)


def test_gift_card_create_code_without_params():
    """Tests the API endpoint to create a Binance Code without params"""

    client.gift_card_create_code.when.called_with("", "").should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.POST,
    "/sapi/v1/giftcard/createCode\\?" + urlencode(params),
    mock_item,
    200,
)
def test_gift_card_create_code():
    """Tests the API endpoint to create a Binance Code"""

    response = client.gift_card_create_code(**params)
    response.should.equal(mock_item)
