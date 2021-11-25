import responses
from binance.spot import Spot as Client
from tests.util import mock_http_response
from tests.util import random_str
from urllib.parse import urlencode

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()

params = {
    "asset": "BNB",
    "startTime": 1591063000087,
    "endTime": 1591063000087,
    "limit": 200,
}


@mock_http_response(
    responses.GET, "/sapi/v1/asset/assetDividend\\?" + urlencode(params), mock_item, 200
)
def test_asset_dividend_record():
    """Tests the API endpoint to get asset dividen record"""

    client = Client(key, secret)
    response = client.asset_dividend_record(**params)
    response.should.equal(mock_item)
