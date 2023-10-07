import responses

from binance.spot import Spot as Client
from tests.util import random_str
from tests.util import mock_http_response


mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()


@mock_http_response(
    responses.GET,
    "/sapi/v1/portfolio/collateralRate",
    mock_item,
    200,
)
def test_portfolio_margin_collateral_rate():
    """Tests the API endpoint to portfolio margin collateral rate"""

    client = Client(key, secret)
    response = client.portfolio_margin_collateral_rate()
    response.should.equal(mock_item)
