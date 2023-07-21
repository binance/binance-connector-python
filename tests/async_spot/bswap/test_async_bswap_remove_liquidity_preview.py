import pytest

from binance.async_spot import AsyncSpot as Client
from tests.util import mock_async_http_response
from tests.util import random_str
from binance.error import ParameterRequiredError
from binance.lib.utils import encoded_string


mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()

complete_params = {
    "poolId": 2,
    "type": "SINGLE",
    "quoteAsset": "USDT",
    "shareAmount": 0.01,
}

parameterized_test_params = [
    ({"poolId": None, "type": None, "quoteAsset": None, "shareAmount": None}),
    ({"poolId": "", "type": "SINGLE", "quoteAsset": "USDT", "shareAmount": 0.01}),
    ({"poolId": 2, "type": "", "quoteAsset": "USDT", "shareAmount": 0.01}),
    ({"poolId": 2, "type": "SINGLE", "quoteAsset": "", "shareAmount": 0.01}),
    ({"poolId": 2, "type": "SINGLE", "quoteAsset": "USDT", "shareAmount": ""}),
]

client = Client(key, secret)


@pytest.mark.asyncio
@pytest.mark.parametrize("params", parameterized_test_params)
async def test_bswap_remove_liquidity_preview_with_missing_param(params):
    """Tests the API endpoint to get remove liquidity preview with missing param"""

    with pytest.raises(ParameterRequiredError):
        await client.bswap_remove_liquidity_preview(**params)


@pytest.mark.asyncio
@mock_async_http_response(
    "GET",
    "/sapi/v1/bswap/removeLiquidityPreview\\?" + encoded_string(complete_params),
    mock_item,
    200,
)
async def test_bswap_remove_liquidity_preview():
    """Tests the API endpoint to get remove liquidity preview"""

    response = await client.bswap_remove_liquidity_preview(**complete_params)
    response.should.equal(mock_item)
