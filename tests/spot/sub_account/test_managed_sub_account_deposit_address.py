import responses
import pytest

from binance.spot import Spot as Client
from tests.util import mock_http_response
from tests.util import random_str
from binance.error import ParameterRequiredError
from binance.lib.utils import encoded_string


mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()

email = "alice@test.com"
coin = random_str()

complete_params = {
    "email": email,
    "coin": coin,
}

parameterized_test_params = [
    ({"email": None, "coin": None}),
    ({"email": email, "coin": ""}),
    ({"email": "", "coin": coin}),
]

client = Client(key, secret)


@pytest.mark.parametrize("params", parameterized_test_params)
def test_managed_sub_account_deposit_address_with_missing_param(params):
    """Tests the API endpoint to get managed sub account deposit address with missing param"""

    client.managed_sub_account_deposit_address.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.POST,
    "/sapi/v2/sub-account/subAccountApi/ipRestriction\\?"
    + encoded_string(complete_params),
    mock_item,
    200,
)
def tet_managed_sub_account_deposit_address():
    """Tests the API endpoint to get managed sub account deposit address"""

    client.managed_sub_account_deposit_address(**complete_params).should.equal(
        mock_item
    )
