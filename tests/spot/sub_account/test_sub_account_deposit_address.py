import responses

from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.lib.utils import encoded_string
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()


params = {
    "email": "alice@test.com",
    "coin": "BNB",
    "network": "BNB",
    "recvWindow": 1000,
}


def test_sub_account_deposit_address_without_email():
    """Tests the API endpoint to get deposit address without email"""

    params = {"email": "", "coin": "BNB", "network": "BNB", "recvWindow": 1000}
    client = Client(key, secret)
    client.sub_account_deposit_address.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


def test_sub_account_deposit_address_without_coin():
    """Tests the API endpoint to get deposit address without coin"""

    params = {
        "email": "alice@test.com",
        "coin": "",
        "network": "BNB",
        "recvWindow": 1000,
    }
    client = Client(key, secret)
    client.sub_account_deposit_address.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.GET,
    "/sapi/v1/capital/deposit/subAddress\\?" + encoded_string(params),
    mock_item,
    200,
)
def test_sub_account_deposit_address():
    """Tests the API endpoint to get deposit address"""

    client = Client(key, secret)
    response = client.sub_account_deposit_address(**params)
    response.should.equal(mock_item)
