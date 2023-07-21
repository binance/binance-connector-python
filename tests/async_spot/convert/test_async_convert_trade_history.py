import pytest
from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_async_http_response
from tests.util import current_timestamp
from binance.async_spot import AsyncSpot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()


params = {
    "startTime": current_timestamp(),
    "endTime": current_timestamp(),
}

client = Client(key, secret)

@pytest.mark.asyncio
async def test_convert_trade_history_without_startTime():
    """Tests the API endpoint to retrieve convert trade history without startTime"""

    try:
        response = await client.convert_trade_history(
        startTime="", endTime=1597130241000
    )
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_convert_trade_history_without_endTime():
    """Tests the API endpoint to retrieve convert trade history without endTime"""

    try:
        response = await client.convert_trade_history(
        startTime=1597130241000, endTime=""
    )
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "GET", "/sapi/v1/convert/tradeFlow\\?" + urlencode(params), mock_item, 200
)
async def test_convert_trade_history():
    """Tests the API endpoint to retrieve convert trade history"""

    response = await client.convert_trade_history(**params)
    response.should.equal(mock_item)
