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
    "recvWindow": 5000,
}


@mock_http_response(
    responses.GET,
    "/sapi/v1/giftcard/cryptography/rsa-public-key\\?" + urlencode(params),
    mock_item,
    200,
)
def test_gift_card_rsa_public_key():
    """Tests the API endpoint to gift card rsa public key"""

    client = Client(key, secret)
    response = client.gift_card_rsa_public_key(**params)
    response.should.equal(mock_item)
