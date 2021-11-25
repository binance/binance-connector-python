import responses
import pytest

from binance.spot import Spot as Client
from tests.util import mock_http_response
from tests.util import random_str
from binance.lib.utils import encoded_string
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

email = "alice@test.com"
subAccountApiKey = random_str()

complete_params = {"email": email, "subAccountApiKey": subAccountApiKey}

parameterized_test_params = [
    ({"email": None, "subAccountApiKey": None}),
    ({"email": "", "subAccountApiKey": subAccountApiKey}),
    ({"email": email, "subAccountApiKey": ""}),
]

client = Client(key, secret)


@pytest.mark.parametrize("params", parameterized_test_params)
def test_sub_account_api_get_ip_restriction_without_missing_param(params):
    """Tests the API endpoint to get IP Restriction for a sub-account API key without subAccountApiKey"""

    client.sub_account_api_get_ip_restriction.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.GET,
    "/sapi/v1/sub-account/subAccountApi/ipRestriction\\?"
    + encoded_string(complete_params),
    mock_item,
    200,
)
def test_sub_account_api_get_ip_restriction():
    """Tests the API endpoint to get IP Restriction for a sub-account API key"""

    client.sub_account_api_get_ip_restriction(**complete_params).should.equal(mock_item)
