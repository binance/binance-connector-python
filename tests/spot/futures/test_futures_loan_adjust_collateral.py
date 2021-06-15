import responses
import pytest

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

complete_params = {
    "loanCoin": "BTC",
    "collateralCoin": "BNB",
    "amount": "1",
    "direction": "ADDITIONAL",
}

parameterized_test_data = [
    ({"loanCoin": None, "collateralCoin": None, "amount": None, "direction": None}),
    (
        {
            "loanCoin": "",
            "collateralCoin": "BTC",
            "amount": "1",
            "direction": "ADDITIONAL",
        }
    ),
    (
        {
            "loanCoin": "BNB",
            "collateralCoin": "",
            "amount": "1",
            "direction": "ADDITIONAL",
        }
    ),
    (
        {
            "loanCoin": "BNB",
            "collateralCoin": "BTC",
            "amount": "",
            "direction": "ADDITIONAL",
        }
    ),
    ({"loanCoin": "BNB", "collateralCoin": "BTC", "amount": "1", "direction": ""}),
]


@pytest.mark.parametrize("params", parameterized_test_data)
def test_futures_loan_adjust_collateral_with_missing_field(params):
    """Tests the API endpoint to Adjust Cross-Collateral LTV with missing field"""

    client = Client(key, secret)
    client.futures_loan_adjust_collateral.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.POST,
    "/sapi/v2/futures/loan/adjustCollateral\\?" + urlencode(complete_params),
    mock_item,
    200,
)
def test_futures_loan_adjust_collateral():
    """Tests the API endpoint to Adjust Cross-Collateral LTV"""

    client = Client(key, secret)
    response = client.futures_loan_adjust_collateral(**complete_params)
    response.should.equal(mock_item)
