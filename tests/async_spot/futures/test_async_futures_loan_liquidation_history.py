import pytest

from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()


@pytest.mark.asyncio
@mock_async_http_response(
    "GET", "/sapi/v1/futures/loan/liquidationHistory", mock_item, 200
)
async def test_futures_loan_liquidation_history():
    """Tests the API endpoint to Cross-Collateral Liquidation History"""

    client = Client(key, secret)
    response = await client.futures_loan_liquidation_history()
    response.should.equal(mock_item)
