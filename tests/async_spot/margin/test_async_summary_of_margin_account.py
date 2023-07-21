import pytest

from binance.async_spot import AsyncSpot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_async_http_response

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

params = {"recvWindow": 5000}


@pytest.mark.asyncio
@mock_async_http_response(
    "GET",
    "/sapi/v1/margin/tradeCoeff\\?" + urlencode(params),
    mock_item,
    200,
)
async def test_summary_of_margin_account():
    """Tests the API endpoint to margin dustlog"""

    client = Client(key, secret)
    response = await client.summary_of_margin_account(**params)
    response.should.equal(mock_item)
