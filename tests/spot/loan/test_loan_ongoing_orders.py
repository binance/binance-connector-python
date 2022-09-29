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
    "/sapi/v1/loan/ongoing/orders\\?loanCoin=BUSD",
    mock_item,
    200,
)
def test_loan_ongoing_orders():
    """Tests the API endpoint to get loan borrow ongoing orders"""

    response = client.loan_ongoing_orders(loanCoin="BUSD")
    response.should.equal(mock_item)
