import pytest

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()
client = Client(key, secret)

params = {"orderId": 100000001}


@pytest.mark.asyncio
@mock_async_http_response(
    "GET",
    "/sapi/v1/loan/vip/collateral/account\\?" + urlencode(params),
    mock_item,
    200,
)
async def test_loan_vip_collateral_account():
    """Tests the API endpoint to get vip loan collateral account"""

    response = await client.loan_vip_collateral_account(**params)
    response.should.equal(mock_item)
