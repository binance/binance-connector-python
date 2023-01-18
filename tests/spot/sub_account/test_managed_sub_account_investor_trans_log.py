import responses
import pytest
from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.lib.utils import encoded_string
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

parameterized_test_params = [
    (
        {
            "email": "",
            "startTime": 1600000000000,
            "endTime": 1620000000000,
            "page": 1,
            "limit": 10,
        }
    ),
    (
        {
            "email": "alice@test.com",
            "startTime": None,
            "endTime": 1620000000000,
            "page": 1,
            "limit": 10,
        }
    ),
    (
        {
            "email": "alice@test.com",
            "startTime": 1600000000000,
            "endTime": None,
            "page": 1,
            "limit": 10,
        }
    ),
    (
        {
            "email": "alice@test.com",
            "startTime": 1600000000000,
            "endTime": 1620000000000,
            "page": None,
            "limit": 10,
        }
    ),
    (
        {
            "email": "alice@test.com",
            "startTime": 1600000000000,
            "endTime": 1620000000000,
            "page": 1,
            "limit": None,
        }
    ),
]


@pytest.mark.parametrize("params", parameterized_test_params)
def test_managed_sub_account_investor_trans_log_with_missing_parameters(params):
    """Tests the API endpoint to query managed sub account transfer log with missing parameters"""

    client = Client(key, secret)
    client.managed_sub_account_investor_trans_log.when.called_with(
        **params
    ).should.throw(ParameterRequiredError)


params = {
    "email": "alice@test.com",
    "startTime": 1600000000000,
    "endTime": 1620000000000,
    "page": 1,
    "limit": 1,
}


@mock_http_response(
    responses.GET,
    "/sapi/v1/managed-subaccount/queryTransLogForInvestor\\?" + encoded_string(params),
    mock_item,
    200,
)
def test_managed_sub_account_investor_trans_log():
    """Tests the API endpoint to query managed sub account transfer log"""

    client = Client(key, secret)
    response = client.managed_sub_account_investor_trans_log(**params)
    response.should.equal(mock_item)
