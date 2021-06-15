import responses
from binance.spot import Spot as Client
from tests.util import mock_http_response
from tests.util import random_str
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()


def test_deposit_address_without_coin():
    """Tests the API endpoint to get deposit address without coin"""

    client = Client(key, secret)
    client.deposit_address.when.called_with("").should.throw(ParameterRequiredError)


@mock_http_response(
    responses.GET, "/sapi/v1/capital/deposit/address\\?coin=BNB", mock_item, 200
)
def test_deposit_address():
    """Tests the API endpoint to get deposit address"""

    client = Client(key, secret)
    response = client.deposit_address(coin="BNB")
    response.should.equal(mock_item)
