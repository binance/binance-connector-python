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

params = {"loanCoin": "BNB", "collateralCoin": "BTC"}

parameterized_test_data = [
    ({"loanCoin": "BNB", "collateralCoin": ""}),
    ({"loanCoin": "", "collateralCoin": "BTC"}),
]


@pytest.mark.parametrize("params", parameterized_test_data)
def test_futures_loan_calc_max_adjust_amount_with_missing_field(params):
    """Tests the API endpoint to Adjust Cross-Collateral LTV without collateralCoin"""

    client = Client(key, secret)
    client.futures_loan_calc_max_adjust_amount.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.GET,
    "/sapi/v2/futures/loan/calcMaxAdjustAmount\\?" + urlencode(params),
    mock_item,
    200,
)
def test_futures_loan_calc_max_adjust_amount():
    """Tests the API endpoint to get Adjust Cross-Collateral LTV"""

    client = Client(key, secret)
    response = client.futures_loan_calc_max_adjust_amount(**params)
    response.should.equal(mock_item)
