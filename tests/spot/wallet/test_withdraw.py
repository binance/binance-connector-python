import responses
from binance.spot import Spot as Client
from tests.util import mock_http_response
from tests.util import random_str
from urllib.parse import urlencode
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()

params = {
    "coin": "BNB",
    "amount": 1,
    "address": random_str(),
    "withdrawOrderId": "1234567",
    "network": "BNB",
    "addressTag": random_str(),
    "transactionFeeFlag": "true",
    "name": "test_address",
    "walletType": 0,
}


def test_withdraw_without_coin():
    """Tests the API endpoint to withdraw without coin"""

    client = Client(key, secret)
    client.withdraw.when.called_with("", 1, "address").should.throw(
        ParameterRequiredError
    )


def test_withdraw_without_amount():
    """Tests the API endpoint to withdraw without amount"""

    client = Client(key, secret)
    client.withdraw.when.called_with("BNB", "", "address").should.throw(
        ParameterRequiredError
    )


def test_withdraw_without_address():
    """Tests the API endpoint to withdraw without address"""

    client = Client(key, secret)
    client.withdraw.when.called_with("BNB", 1, "").should.throw(ParameterRequiredError)


@mock_http_response(
    responses.POST,
    "/sapi/v1/capital/withdraw/apply\\?" + urlencode(params),
    mock_item,
    200,
)
def test_withdraw():
    """Tests the API endpoint to withdraw"""

    client = Client(key, secret)
    response = client.withdraw(**params)
    response.should.equal(mock_item)
