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
    "fromEmail": "alice@test.com",
    "asset": "BNB",
    "amount": 1,
    "transferDate": 1624023242,
    "recvWindow": 1000,
}


def test_managed_sub_account_withdraw_assets_without_fromEmail():
    """Tests the API endpoint to withdraw asset from managed sub account without toEmail"""

    params = {
        "fromEmail": "",
        "asset": "BNB",
        "amount": 1,
        "transferDate": 1624023242,
        "recvWindow": 1000,
    }
    client = Client(key, secret)
    client.managed_sub_account_withdraw.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


def test_managed_sub_account_withdraw_assets_without_asset():
    """Tests the API endpoint to withdraw asset from managed sub account without asset"""

    params = {
        "fromEmail": "alice@test.com",
        "asset": "",
        "amount": 1,
        "transferDate": 1624023242,
        "recvWindow": 1000,
    }
    client = Client(key, secret)
    client.managed_sub_account_withdraw.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


def test_managed_sub_account_withdraw_assets_without_amount():
    """Tests the API endpoint to withdraw asset from managed sub account without amount"""

    params = {
        "fromEmail": "alice@test.com",
        "asset": "BNB",
        "amount": "",
        "transferDate": 1624023242,
        "recvWindow": 1000,
    }

    client = Client(key, secret)
    client.managed_sub_account_withdraw.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.POST,
    "/sapi/v1/managed-subaccount/withdraw\\?" + encoded_string(params),
    mock_item,
    200,
)
def test_managed_sub_account_withdraw_assets():
    """Tests the API endpoint to withdraw asset from managed sub account"""

    client = Client(key, secret)
    response = client.managed_sub_account_withdraw(**params)
    response.should.equal(mock_item)
