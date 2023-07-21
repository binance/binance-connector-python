import pytest

from tests.util import mock_async_http_response
from tests.util import random_id
from tests.util import timestamp
from binance.async_spot import AsyncSpot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
fromId = random_id()
startTime = timestamp()
endTime = startTime + random_id()

@pytest.mark.asyncio
async def test_agg_trades_without_symbol():
    """Tests the API endpoint to get old trades without symbol"""

    api = Client()
    try:
        response = await api.agg_trades("")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response("GET", "/api/v3/aggTrades\\?symbol=BTCUSDT", mock_item, 200)
async def test_agg_trades_with_default_limit():
    """Tests the API endpoint to get agg trades by default limit"""

    api = Client()
    response = await api.agg_trades("BTCUSDT")
    response.should.equal(mock_item)


@pytest.mark.asyncio
@mock_async_http_response(
    "GET", "/api/v3/aggTrades\\?symbol=BTCUSDT&limit=1000", mock_item, 200
)
async def test_agg_trades_with_limit_1000():
    """Tests the API endpoint to get agg trades with given limit"""

    api = Client()
    response = await api.agg_trades("BTCUSDT", limit=1000)
    response.should.equal(mock_item)


@pytest.mark.asyncio
@mock_async_http_response(
    "GET",
    "/api/v3/aggTrades\\?symbol=BTCUSDT&fromId=" + str(fromId),
    mock_item,
    200,
)
async def test_agg_trades_with_formId():
    """Tests the API endpoint to get agg trades with fromId"""

    api = Client()
    response = await api.agg_trades("BTCUSDT", fromId=fromId)
    response.should.equal(mock_item)


@pytest.mark.asyncio
@mock_async_http_response(
    "GET",
    "/api/v3/aggTrades\\?symbol=BTCUSDT&startTime="
    + str(startTime)
    + "&endTime="
    + str(endTime),
    mock_item,
    200,
)
async def test_agg_trades_with_timestamp():
    """Tests the API endpoint to get agg trades with specific timestamp"""

    api = Client()
    response = await api.agg_trades("BTCUSDT", startTime=startTime, endTime=endTime)
    response.should.equal(mock_item)
