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
    "/sapi/v1/margin/crossMarginCollateralRatio",
    mock_item,
    200,
)
def test_cross_margin_collateral_ratio():
    """Tests the API endpoint to cross margin collateral ratio"""

    client = Client(key, secret)
    response = client.cross_margin_collateral_ratio()
    response.should.equal(mock_item)
