import responses

from binance.spot import Spot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_http_response


mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

send_params = {"asset": "BTC"}
expected_params = {"asset": "BTC"}


@mock_http_response(
    responses.GET,
    "/sapi/v1/portfolio/asset-index-price\\?" + urlencode(expected_params),
    mock_item,
    200,
)
def test_query_portfolio_margin_asset_index_price():
    """Tests the API endpoint to query portfolio margin asset index price"""

    client = Client(key, secret)
    response = client.query_portfolio_margin_asset_index_price(**send_params)
    response.should.equal(mock_item)
