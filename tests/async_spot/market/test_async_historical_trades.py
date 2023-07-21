import pytest

from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

api_key = random_str()
fromId = "123456789"

@pytest.mark.asyncio
async def test_historical_trades_with_empty_api_key():
    """Tests the API endpoint to without provide api key"""

    api = Client(api_key=api_key)
    try:
        response = await api.historical_trades("")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_historical_trades_without_symbol():
    """Tests the API endpoint to get old trades without symbol"""

    api = Client(api_key=api_key)
    try:
        response = await api.historical_trades("")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "GET", "/api/v3/historicalTrades\\?symbol=BTCUSDT", mock_item, 200
)
async def test_historical_trades_with_default_params():
    """Tests the API endpoint to get old trades by default params"""

    api = Client(api_key=api_key)
    response = await api.historical_trades("BTCUSDT")
    response.should.equal(mock_item)


@pytest.mark.asyncio
@mock_async_http_response(
    "GET",
    "/api/v3/historicalTrades\\?symbol=BTCUSDT&limit=1000&fromId=" + fromId,
    mock_item,
    200,
)
async def test_historical_trades_with_provide_params():
    """Tests the API endpoint to get recent trades with given limit"""

    api = Client(api_key=api_key)
    response = await api.historical_trades("BTCUSDT", limit=1000, fromId=fromId)
    response.should.equal(mock_item)
