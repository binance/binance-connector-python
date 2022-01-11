import responses

from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.lib.utils import encoded_string
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

client = Client(key, secret)

params = {
    "fromAccountType": "SPOT",
    "toAccountType": "COIN_FUTURE",
    "asset": "BNB",
    "amount": 10.1,
    "clientTranId": "test",
    "recvWindow": 1000,
}


def test_sub_account_universal_transfer_without_fromAccountType():
    """Tests the API endpoint to transfer asset within master account without fromAccountType"""

    params = {
        "fromAccountType": "",
        "toAccountType": "COIN_FUTURE",
        "asset": "BNB",
        "amount": 10.1,
        "clientTranId": "test",
        "recvWindow": 1000,
    }
    client.sub_account_universal_transfer.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


def test_sub_account_universal_transfer_without_toAccountType():
    """Tests the API endpoint to transfer asset within master account without toAccountType"""

    params = {
        "fromAccountType": "SPOT",
        "toAccountType": "",
        "asset": "BNB",
        "amount": 10.1,
        "clientTranId": "test",
        "recvWindow": 1000,
    }
    client.sub_account_universal_transfer.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


def test_sub_account_universal_transfer_without_asset():
    """Tests the API endpoint to transfer asset within master account without asset"""

    params = {
        "fromAccountType": "SPOT",
        "toAccountType": "COIN_FUTURE",
        "asset": "",
        "amount": 10.1,
        "clientTranId": "test",
        "recvWindow": 1000,
    }
    client.sub_account_universal_transfer.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


def test_sub_account_universal_transfer_without_amount():
    """Tests the API endpoint to transfer asset within master account without amount"""

    params = {
        "fromAccountType": "SPOT",
        "toAccountType": "COIN_FUTURE",
        "asset": "BNB",
        "amount": "",
        "clientTranId": "test",
        "recvWindow": 1000,
    }
    client.sub_account_universal_transfer.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.POST,
    "/sapi/v1/sub-account/universalTransfer\\?" + encoded_string(params),
    mock_item,
    200,
)
def test_sub_account_universal_transfer():
    """Tests the API endpoint to transfer asset within master account"""

    response = client.sub_account_universal_transfer(**params)
    response.should.equal(mock_item)
