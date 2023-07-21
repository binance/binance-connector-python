import pytest

from binance.async_spot import AsyncSpot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_async_http_response
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

params = {"asset": "BNB", "recvWindow": 1000}


@pytest.mark.asyncio
async def test_margin_max_transferable_without_asset():
    """Tests the API endpoint to query margin max transferable without symbol"""

    client = Client(key, secret)
    with pytest.raises(ParameterRequiredError):
        await client.margin_max_transferable("")


@pytest.mark.asyncio
@mock_async_http_response(
    "GET",
    "/sapi/v1/margin/maxTransferable\\?" + urlencode(params),
    mock_item,
    200,
)
async def test_margin_max_transferable():
    """Tests the API endpoint to query margin max transferable"""

    client = Client(key, secret)
    response = await client.margin_max_transferable(**params)
    response.should.equal(mock_item)
