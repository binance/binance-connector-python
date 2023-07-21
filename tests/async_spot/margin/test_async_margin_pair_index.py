import pytest

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

symbol = "BNBUSDT"
amount = "100"

params = {"symbol": symbol}

@pytest.mark.asyncio
async def test_margin_pair_index_without_asset():
    """Tests the API endpoint to margin pair index without asset"""

    client = Client(key, secret)
    try:
        response = await client.margin_pair_index("")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "GET", "/sapi/v1/margin/priceIndex\\?" + urlencode(params), mock_item, 200
)
async def test_margin_pair_index():
    """Tests the API endpoint to margin pair index"""

    client = Client(key, secret)
    response = await client.margin_pair_index(**params)
    response.should.equal(mock_item)
