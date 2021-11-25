import responses
import pytest

from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError
from binance.lib.utils import encoded_string

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

complete_params = {"email": "alice@test.com", "enableBlvt": True, "recvWindow": 1000}

parameterized_test_data = [
    ({"email": None, "enableBlvt": None}),
    ({"email": "", "enableBlvt": True}),
    ({"email": "alice@test.com", "enableBlvt": ""}),
    ({"email": "alice@test.com", "enableBlvt": "", "recvWindow": 1000}),
]


@pytest.mark.parametrize("params", parameterized_test_data)
def test_sub_account_enable_leverage_token_with_missing_fields(params):
    """Tests the API endpoint to enable leverage token for sub-account with missing fields"""
    client = Client(key, secret)
    client.sub_account_enable_leverage_token.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.POST,
    "/sapi/v1/sub-account/blvt/enable\\?" + encoded_string(complete_params),
    mock_item,
    200,
)
def test_sub_account_enable_leverage_token():
    """Tests the API endpoint to enable leverage for token sub-account"""

    client = Client(key, secret)
    response = client.sub_account_enable_leverage_token(**complete_params)
    response.should.equal(mock_item)
