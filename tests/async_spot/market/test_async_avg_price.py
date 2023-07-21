from binance.async_spot import AsyncSpot as Client
import pytest

from tests.util import mock_async_http_response
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

@pytest.mark.asyncio
async def test_avg_price_without_symbol():
    """Tests the API endpoint to get avg price without symbol"""

    api = Client()
    try:
        response = await api.avg_price("")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response("GET", "/api/v3/avgPrice\\?symbol=BTCUSDT", mock_item, 200)
async def test_avg_price():
    """Tests the API endpoint to avg price"""

    api = Client()
    response = await api.avg_price("BTCUSDT")
    response.should.equal(mock_item)
