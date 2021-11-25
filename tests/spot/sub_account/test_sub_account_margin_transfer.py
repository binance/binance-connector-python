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
    "asset": "BNB",
    "amount": 100,
    "type": 1,
    "recvWindow": 1000,
}


def test_sub_account_margin_transfer_without_email():
    """Tests the API endpoint to margin transfer for Sub-account without email"""

    params = {"email": "", "asset": "BNB", "amount": 100, "type": 1, "recvWindow": 1000}
    client = Client(key, secret)
    client.sub_account_margin_transfer.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


def test_sub_account_margin_transfer_without_asset():
    """Tests the API endpoint to margin transfer for Sub-account without asset"""

    params = {
        "email": "alice@test.com",
        "asset": "",
        "amount": 100,
        "type": 1,
        "recvWindow": 1000,
    }
    client = Client(key, secret)
    client.sub_account_margin_transfer.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


def test_sub_account_margin_transfer_without_amount():
    """Tests the API endpoint to margin transfer for Sub-account without amount"""

    params = {
        "email": "alice@test.com",
        "asset": "BNB",
        "amount": "",
        "type": 1,
        "recvWindow": 1000,
    }
    client = Client(key, secret)
    client.sub_account_margin_transfer.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


def test_sub_account_margin_transfer_without_type():
    """Tests the API endpoint to margin transfer for Sub-account without type"""

    params = {
        "email": "alice@test.com",
        "asset": "BNB",
        "amount": 100,
        "type": "",
        "recvWindow": 1000,
    }
    client = Client(key, secret)
    client.sub_account_margin_transfer.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.POST,
    "/sapi/v1/sub-account/margin/transfer\\?" + encoded_string(params),
    mock_item,
    200,
)
def test_sub_account_margin_transfer():
    """Tests the API endpoint to margin transfer for Sub-account"""

    client = Client(key, secret)
    response = client.sub_account_margin_transfer(**params)
    response.should.equal(mock_item)
