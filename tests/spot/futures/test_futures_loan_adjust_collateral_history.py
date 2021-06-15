import responses

from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()


@mock_http_response(
    responses.GET, "/sapi/v1/futures/loan/adjustCollateral/history", mock_item, 200
)
def test_futures_loan_adjust_collateral_history():
    """Tests the API endpoint to Adjust Cross-Collateral LTV History"""

    client = Client(key, secret)
    response = client.futures_loan_adjust_collateral_history()
    response.should.equal(mock_item)
