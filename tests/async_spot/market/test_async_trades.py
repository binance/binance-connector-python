from binance.async_spot import AsyncSpot as Client
import pytest

from tests.util import mock_async_http_response
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

@pytest.mark.asyncio
async def test_trades_without_symbol():
    """Tests the API endpoint to get recent trade list without symbol"""

    api = Client()
    try:
        response = await api.trades("")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response("GET", "/api/v3/trades\\?symbol=BTCUSDT", mock_item, 200)
async def test_trades_with_default_limit():
    """Tests the API endpoint to get recent trades with default limit"""

    api = Client()
    response = await api.trades("BTCUSDT")
    response.should.equal(mock_item)


@pytest.mark.asyncio
@mock_async_http_response(
    "GET", "/api/v3/trades\\?symbol=BTCUSDT&limit=1000", mock_item, 200
)
async def test_trades_with_limit_1000():
    """Tests the API endpoint to get recent trades with given limit"""

    api = Client()
    response = await api.trades("BTCUSDT", limit=1000)
    response.should.equal(mock_item)
