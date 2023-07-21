import pytest
from binance.async_spot import AsyncSpot as Client
from tests.util import mock_async_http_response
from tests.util import random_str
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()

@pytest.mark.asyncio
async def test_bswap_liquidity_add_without_poolId():
    """Tests the API endpoint to add liquidity to a pool without poolId."""

    client = Client(key, secret)
    try:
        response = await client.bswap_liquidity_add("", "BUSD", "1")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_bswap_liquidity_add_without_asset():
    """Tests the API endpoint to add liquidity to a pool without asset."""

    client = Client(key, secret)
    try:
        response = await client.bswap_liquidity_add("2", "", "1")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_bswap_liquidity_add_without_quantity():
    """Tests the API endpoint to add liquidity to a pool without quantity."""

    client = Client(key, secret)
    try:
        response = await client.bswap_liquidity_add("2", "BUSD", "")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "POST",
    "/sapi/v1/bswap/liquidityAdd\\?poolId=2&asset=BUSD&quantity=1",
    mock_item,
    200,
)
async def test_subscribe_blvt():
    """Tests the API endpoint to add liquidity to a pool."""

    client = Client(key, secret)
    response = await client.bswap_liquidity_add("2", "BUSD", "1")
    response.should.equal(mock_item)
