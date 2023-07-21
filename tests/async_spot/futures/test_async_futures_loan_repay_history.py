import pytest

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1105, "msg": "error message."}

key = random_str()
secret = random_str()

params = {
    "coin": "BTC",
    "startTime": "1597130241000",
    "endTime": "1597130241001",
}


@pytest.mark.asyncio
@mock_async_http_response(
    "GET",
    "/sapi/v1/futures/loan/repay/history\\?" + urlencode(params),
    mock_item,
    200,
)
async def test_futures_loan_repay_history():
    """Tests the API endpoint to get repay history"""

    client = Client(key, secret)
    response = await client.futures_loan_repay_history(**params)
    response.should.equal(mock_item)
