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
    "POST",
    "/sapi/v1/portfolio/repay\\?" + urlencode(params),
    mock_item,
    200,
)
async def test_portfolio_margin_bankruptcy_loan_repay():
    """Tests the API endpoint to portfolio margin bankruptcy loan repay"""

    client = Client(key, secret)
    response = await client.portfolio_margin_bankruptcy_loan_repay(**params)
    response.should.equal(mock_item)
