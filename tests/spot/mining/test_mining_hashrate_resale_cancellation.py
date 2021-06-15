import responses
import pytest

from binance.error import ParameterRequiredError
from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

parameterized_test_data = [
    ({"configId": None, "userName": None}),
    ({"configId": "", "userName": "user_name"}),
    ({"configId": 123, "userName": ""}),
]


@pytest.mark.parametrize("params", parameterized_test_data)
def test_mining_hashrate_resale_cancellation_with_missing_field(params):
    """Tests the API endpoint to cancel hashrate resale configuration with missing field"""
    client = Client(key, secret)
    client.mining_hashrate_resale_cancellation.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.POST,
    "/sapi/v1/mining/hash-transfer/config/cancel\\?configId=123&userName=user_name",
    mock_item,
    200,
)
def test_mining_hashrate_resale_cancellation():
    """Tests the API endpoint to cancel hashrate resale configuration"""

    client = Client(key, secret)
    response = client.mining_hashrate_resale_cancellation(123, "user_name")
    response.should.equal(mock_item)
