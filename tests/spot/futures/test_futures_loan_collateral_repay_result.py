import responses

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1105, "msg": "error message."}

key = random_str()
secret = random_str()

params = {
    "quoteId": "3eece81ca2734042b2f538ea0d9cbdd3",
}


def test_futures_loan_collateral_repay_result_without_quoteId():
    """Tests the API endpoint to get Collateral Repayment Result without quoteId"""

    params = {"quoteId": ""}
    client = Client(key, secret)
    client.futures_loan_collateral_repay_result.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.GET,
    "/sapi/v1/futures/loan/collateralRepayResult\\?" + urlencode(params),
    mock_item,
    200,
)
def test_futures_loan_collateral_repay_result():
    """Tests the API endpoint to get Collateral Repayment Result"""

    client = Client(key, secret)
    response = client.futures_loan_collateral_repay_result(**params)
    response.should.equal(mock_item)
