import pytest

from tests.util import random_str, timestamp
from tests.util import mock_async_http_response
from urllib.parse import urlencode
from binance.async_spot import AsyncSpot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

params = {
    "transactionType": 0,
    "beginTime": timestamp(),
    "endTime": timestamp(),
    "page": 1,
    "rows": 100,
}

@pytest.mark.asyncio
async def test_fiat_order_history_without_type():
    """Tests the API endpoint to get fiat order history"""

    client = Client(key, secret)
    try:
        response = await client.fiat_order_history("")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "GET",
    "/sapi/v1/fiat/orders\\?" + urlencode(params),
    mock_item,
    200,
)
async def test_fiat_order_history():
    """Tests the API endpoint to get fiat order history"""

    client = Client(key, secret)

    response = await client.fiat_order_history(**params)
    response.should.equal(mock_item)
