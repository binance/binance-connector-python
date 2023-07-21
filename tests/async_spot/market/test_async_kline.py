import pytest

from binance.async_spot import AsyncSpot as Client

from tests.util import mock_async_http_response
from tests.util import random_id
from tests.util import timestamp
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
fromId = random_id()
startTime = timestamp()
endTime = startTime + random_id()
client = Client()

@pytest.mark.asyncio
async def test_kline_without_symbol():
    """Tests the API endpoint to get kline without symbol"""

    try:
        response = await client.klines(symbol="", interval="1m")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_kline_without_interval():
    """Tests the API endpoint to get kline without interval"""

    try:
        response = await client.klines(symbol="BTCUSDT", interval="")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "GET", "/api/v3/klines\\?symbol=BTCUSDT&interval=1h", mock_item, 200
)
async def test_kline_with_default_limit():
    """Tests the API endpoint to get kline with default limit"""

    response = await client.klines(symbol="BTCUSDT", interval="1h")
    response.should.equal(mock_item)


@pytest.mark.asyncio
@mock_async_http_response(
    "GET",
    "/api/v3/klines\\?symbol=BTCUSDT&interval=1h&limit=10&startTime="
    + str(startTime)
    + "&endTime="
    + str(endTime),
    mock_item,
    200,
)
async def test_kline_with_given_params():
    """Tests the API endpoint to get kline with given parametes"""

    response = await client.klines(
        symbol="BTCUSDT", interval="1h", limit=10, startTime=startTime, endTime=endTime
    )
    response.should.equal(mock_item)
