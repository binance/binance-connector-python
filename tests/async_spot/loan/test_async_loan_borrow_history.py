import pytest

from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()
client = Client(key, secret)


@pytest.mark.asyncio
@mock_async_http_response(
    "GET",
    "/sapi/v1/loan/borrow/history\\?loanCoin=BUSD",
    mock_item,
    200,
)
async def test_loan_borrow_history():
    """Tests the API endpoint to get borrow history"""

    response = await client.loan_borrow_history(loanCoin="BUSD")
    response.should.equal(mock_item)
