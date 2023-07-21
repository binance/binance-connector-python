import pytest
from binance.async_spot import AsyncSpot as Client
from tests.util import mock_async_http_response
from tests.util import random_str

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()
client = Client(key, secret)


@pytest.mark.asyncio
@mock_async_http_response("POST", "/sapi/v1/bswap/claimRewards", mock_item, 200)
async def test_bswap_claim_rewards():
    """Tests the API endpoint to get liquidity information and user share of a pool"""

    response = await client.bswap_claim_rewards()
    response.should.equal(mock_item)
