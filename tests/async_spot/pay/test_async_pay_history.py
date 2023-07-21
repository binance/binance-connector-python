import pytest

from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client
from binance.lib.utils import encoded_string

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()
params = {"startTime": 1637186702000, "endTime": 1637690208000, "limit": 50}

client = Client(key, secret)


@pytest.mark.asyncio
@mock_async_http_response(
    "GET",
    "/sapi/v1/pay/transactions",
    mock_item,
    200,
)
async def test_pay_history_without_params():
    """Tests the API endpoint to get Pay Trade History without parameters"""
    (await client.pay_history()).should.equal(mock_item)


@pytest.mark.asyncio
@mock_async_http_response(
    "GET",
    "/sapi/v1/pay/transactions\\?" + encoded_string(params),
    mock_item,
    200,
)
async def test_pay_history_with_params():
    """Tests the API endpoint to get Pay Trade History"""
    (await client.pay_history(**params)).should.equal(mock_item)
