import responses

from binance.spot import Spot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_http_response


mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

send_params = {"collateralCoin": "BNB", "recvWindow": 5000}
expected_params = {"collateralCoin": "BNB", "recvWindow": 5000}


@mock_http_response(
    responses.GET,
    "/sapi/v1/loan/flexible/collateral/data\\?" + urlencode(expected_params),
    mock_item,
    200,
)
def test_flexible_loan_collateral_assets_data():
    """Tests the API endpoint to get flexible loan collateral assets data"""

    client = Client(key, secret)
    response = client.flexible_loan_collateral_assets_data(**send_params)
    response.should.equal(mock_item)
