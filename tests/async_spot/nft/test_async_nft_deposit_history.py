import pytest

from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client
from binance.lib.utils import urlencode as encoded_string

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()
client = Client(key, secret)

params = {"startTime": 1637186702000, "endTime": 1637690208000, "page": 1}


@pytest.mark.asyncio
@mock_async_http_response(
    "GET",
    "/sapi/v1/nft/history/deposit",
    mock_item,
    200,
)
async def test_nft_deposit_history_without_params():
    """Tests the API endpoint to get NFT Deposit History without params"""
    (await client.nft_deposit_history()).should.equal(mock_item)


@pytest.mark.asyncio
@mock_async_http_response(
    "GET",
    "/sapi/v1/nft/history/deposit\\?" + encoded_string(params, True),
    mock_item,
    200,
)
async def test_nft_deposit_history():
    """Tests the API endpoint to get NFT Deposit History"""

    (await client.nft_deposit_history(**params)).should.equal(mock_item)
