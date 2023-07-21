import pytest
from binance.async_spot import AsyncSpot as Client
from tests.util import mock_async_http_response
from tests.util import random_str
from binance.error import ParameterRequiredError


mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()

@pytest.mark.asyncio
async def test_bswap_swap_without_quoteAsset():
    """Swap quoteAsset for baseAsset without quoteAsset"""

    client = Client(key, secret)
    try:
        response = await client.bswap_swap("", "BUSD", "30000")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_bswap_swap_without_baseAsset():
    """Swap quoteAsset for baseAsset without baseAsset"""

    client = Client(key, secret)
    try:
        response = await client.bswap_swap("USDT", "", "30000")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_bswap_swap_without_quoteQty():
    """Swap quoteAsset for baseAsset without quoteQty"""

    client = Client(key, secret)
    try:
        response = await client.bswap_swap("USDT", "BUSD", None)
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "POST",
    "/sapi/v1/bswap/swap\\?quoteAsset=USDT&baseAsset=BUSD&quoteQty=30000",
    mock_item,
    200,
)
async def test_bswap_swap():
    """Swap quoteAsset for baseAsset."""

    client = Client(key, secret)
    response = await client.bswap_swap("USDT", "BUSD", "30000")
    response.should.equal(mock_item)
