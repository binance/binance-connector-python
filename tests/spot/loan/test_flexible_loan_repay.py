import responses

from binance.spot import Spot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_http_response


mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

send_params = {"repayAmount": 100, "collateralCoin": "USDT", "loanCoin": "BTC"}


@mock_http_response(
    responses.POST,
    "/sapi/v1/loan/flexible/repay\\?" + urlencode(send_params),
    mock_item,
    200,
)
def test_flexible_loan_repay():
    """Tests the API endpoint to repay - flexible loan repay"""

    client = Client(key, secret)
    response = client.flexible_loan_repay(**send_params)
    response.should.equal(mock_item)
