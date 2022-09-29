import responses

from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()
client = Client(key, secret)


@mock_http_response(
    responses.GET,
    "/sapi/v1/loan/repay/history\\?loanCoin=BUSD",
    mock_item,
    200,
)
def test_loan_repay_history():
    """Tests the API endpoint to get repay history"""

    response = client.loan_repay_history(loanCoin="BUSD")
    response.should.equal(mock_item)
