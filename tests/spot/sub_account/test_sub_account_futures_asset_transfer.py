import responses

from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.lib.utils import encoded_string
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

param = {
    "fromEmail": "alice@test.com",
    "toEmail": "bob@test.com",
    "futuresType": 1,
    "asset": "USDT",
    "amount": 10,
}


def test_sub_account_futures_asset_transfer_without_fromEmail():
    """Tests the API endpoint to transfer futures asset without from email"""

    param["fromEmail"] = ""
    client = Client(key, secret)
    client.sub_account_futures_asset_transfer.when.called_with(**param).should.throw(
        ParameterRequiredError
    )


def test_sub_account_futures_asset_transfer_without_toEmail():
    """Tests the API endpoint to transfer futures asset without to email"""

    param["toEmail"] = ""
    client = Client(key, secret)
    client.sub_account_futures_asset_transfer.when.called_with(**param).should.throw(
        ParameterRequiredError
    )


def test_sub_account_futures_asset_transfer_without_futuresType():
    """Tests the API endpoint to transfer futures asset without futures type"""

    param["futuresType"] = ""
    client = Client(key, secret)
    client.sub_account_futures_asset_transfer.when.called_with(**param).should.throw(
        ParameterRequiredError
    )


def test_sub_account_futures_asset_transfer_without_asset():
    """Tests the API endpoint to transfer futures asset without asset"""

    param["asset"] = ""
    client = Client(key, secret)
    client.sub_account_futures_asset_transfer.when.called_with(**param).should.throw(
        ParameterRequiredError
    )


def test_sub_account_futures_asset_transfer_without_amount():
    """Tests the API endpoint to transfer futures asset without amount"""

    param["amount"] = ""
    client = Client(key, secret)
    client.sub_account_futures_asset_transfer.when.called_with(**param).should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.POST,
    "/sapi/v1/sub-account/futures/internalTransfer\\?" + encoded_string(param),
    mock_item,
    200,
)
def test_sub_account_futures_asset_transfer():
    """Tests the API endpoint to transfer futures asset"""
    params = {
        "fromEmail": "alice@test.com",
        "toEmail": "bob@test.com",
        "futuresType": 1,
        "asset": "USDT",
        "amount": 10,
    }
    client = Client(key, secret)
    response = client.sub_account_futures_asset_transfer(**params)
    response.should.equal(mock_item)
