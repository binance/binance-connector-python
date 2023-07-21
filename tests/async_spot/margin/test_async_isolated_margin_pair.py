import pytest

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1105, "msg": 'Parameter "orderId" was empty.'}

key = random_str()
secret = random_str()

@pytest.mark.asyncio
async def test_isolated_margin_pair_without_symbol():
    """Tests the API endpoint to query isolated margin pair without symbol"""

    client = Client(key, secret)
    try:
        response = await client.isolated_margin_pair("")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "GET",
    "/sapi/v1/margin/isolated/pair\\?" + urlencode({"symbol": "BTCUSDT"}),
    mock_item,
    200,
)
async def test_isolated_margin_pair():
    """Tests the API endpoint to query isolated margin pair"""

    client = Client(key, secret)
    response = await client.isolated_margin_pair("BTCUSDT")
    response.should.equal(mock_item)
