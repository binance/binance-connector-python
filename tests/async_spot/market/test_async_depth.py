import pytest

from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

@pytest.mark.asyncio
async def test_depth_without_symbol():
    """Tests the API endpoint to get exchange order book depth without symbol"""

    api = Client()
    try:
        response = await api.depth("")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response("GET", "/api/v3/depth\\?symbol=BTCUSDT", mock_item, 200)
async def test_depth():
    """Tests the API endpoint to get exchange order book depth with default parameters"""

    api = Client()
    response = await api.depth("BTCUSDT")
    response.should.equal(mock_item)


@pytest.mark.asyncio
@mock_async_http_response(
    "GET", "/api/v3/depth\\?symbol=BTCUSDT&limit=10", mock_item, 200
)
async def test_depth_fixed_limit():
    """Tests the API endpoint to get exchange order book depth with limit 10"""

    api = Client()
    response = await api.depth("BTCUSDT", limit=10)
    response.should.equal(mock_item)
