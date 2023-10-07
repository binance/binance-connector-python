import responses
from binance.spot import Spot as Client
from tests.util import mock_http_response
from tests.util import random_str
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()

params = {"asset": ["LTC", "EOS"]}


def test_withdraw_without_coin():
    """Tests the API endpoint to transfer dust without coin"""

    client = Client(key, secret)
    client.transfer_dust.when.called_with("").should.throw(ParameterRequiredError)


@mock_http_response(
    responses.POST, "/sapi/v1/asset/dust\\?asset=LTC%2CEOS", mock_item, 200
)
def test_withdraw():
    """Tests the API endpoint to transfer dust"""

    client = Client(key, secret)
    response = client.transfer_dust(**params)
    response.should.equal(mock_item)
