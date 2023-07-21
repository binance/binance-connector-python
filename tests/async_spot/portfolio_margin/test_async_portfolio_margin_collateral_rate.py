import pytest

from binance.async_spot import AsyncSpot as Client
from tests.util import random_str
from tests.util import mock_async_http_response

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()


@pytest.mark.asyncio
@mock_async_http_response(
    "GET",
    "/sapi/v1/portfolio/collateralRate",
    mock_item,
    200,
)
async def test_portfolio_margin_collateral_rate():
    """Tests the API endpoint to portfolio margin collateral rate"""

    client = Client(key, secret)
    response = await client.portfolio_margin_collateral_rate()
    response.should.equal(mock_item)
