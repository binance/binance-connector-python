import responses
import pytest

from binance.error import ParameterRequiredError, ParameterValueError
from binance.lib.utils import encoded_string
from binance.spot import Spot as Client
from tests.util import mock_http_response
from tests.util import random_str

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()

complete_params = {"type": "UMFUTURE_MAIN", "asset": "BNB", "amount": 0.1}

parameterized_test_params = [
    ({"type": None, "asset": None, "amount": None}),
    ({"type": "", "asset": "BNB", "amount": 0.1}),
    ({"type": "UMFUTURE_MAIN", "asset": "", "amount": 0.1}),
    ({"type": "UMFUTURE_MAIN", "asset": "BNB", "amount": ""}),
]


@pytest.mark.parametrize("params", parameterized_test_params)
def test_user_universal_transfer_with_missing_field(params):
    """Tests the API endpoint to transfer from one account to another with missing field"""

    client = Client(key, secret)
    client.user_universal_transfer.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


def test_user_universal_transfer_with_invalid_enum_string():
    """Tests the API endpoint to transfer from one account to another with invalid string"""

    invalid_params = {"type": random_str(), "asset": "BNB", "amount": 0.1}
    client = Client(key, secret)
    client.user_universal_transfer.when.called_with(**invalid_params).should.throw(
        ParameterValueError
    )


@mock_http_response(
    responses.POST,
    "/sapi/v1/asset/transfer\\?" + encoded_string(complete_params),
    mock_item,
    200,
)
def test_user_universal_transfer():
    """Tests the API endpoint to transfer from one account to another"""

    client = Client(key, secret)
    response = client.user_universal_transfer(**complete_params)
    response.should.equal(mock_item)
