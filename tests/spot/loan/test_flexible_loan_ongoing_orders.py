import responses

from binance.spot import Spot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_http_response


mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

send_params = {
    "loanCoin": "BUSD",
    "collateralCoin": "BNB",
    "current": 1,
    "limit": 5,
    "recvWindow": 5000,
}
expected_params = {
    "loanCoin": "BUSD",
    "collateralCoin": "BNB",
    "current": 1,
    "limit": 5,
    "recvWindow": 5000,
}


@mock_http_response(
    responses.GET,
    "/sapi/v1/loan/flexible/ongoing/orders\\?" + urlencode(expected_params),
    mock_item,
    200,
)
def test_flexible_loan_ongoing_orders():
    """Tests the API endpoint to borrow - get flexible loan ongoing orders"""

    client = Client(key, secret)
    response = client.flexible_loan_ongoing_orders(**send_params)
    response.should.equal(mock_item)
