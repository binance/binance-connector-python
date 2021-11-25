import responses

from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.lib.utils import encoded_string
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()


params = {"toEmail": "alice@test.com", "asset": "BNB", "amount": 1, "recvWindow": 1000}


def test_sub_account_transfer_to_sub_without_toEmail():
    """Tests the API endpoint to transfer asset to sub account without toEmail"""

    params = {"toEmail": "", "asset": "BNB", "amount": 1, "recvWindow": 1000}
    client = Client(key, secret)
    client.sub_account_transfer_to_sub.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


def test_sub_account_transfer_to_sub_without_asset():
    """Tests the API endpoint to transfer asset to sub account without asset"""

    params = {"toEmail": "alice@test.com", "asset": "", "amount": 1, "recvWindow": 1000}
    client = Client(key, secret)
    client.sub_account_transfer_to_sub.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


def test_sub_account_transfer_to_sub_without_amount():
    """Tests the API endpoint to transfer asset to sub account without amount"""

    params = {
        "toEmail": "alice@test.com",
        "asset": "BNB",
        "amount": "",
        "recvWindow": 1000,
    }

    client = Client(key, secret)
    client.sub_account_transfer_to_sub.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.POST,
    "/sapi/v1/sub-account/transfer/subToSub\\?" + encoded_string(params),
    mock_item,
    200,
)
def test_sub_account_transfer_to_sub():
    """Tests the API endpoint to transfer asset to sub account"""

    client = Client(key, secret)
    response = client.sub_account_transfer_to_sub(**params)
    response.should.equal(mock_item)
