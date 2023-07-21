import pytest

from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

@pytest.mark.asyncio
async def test_savings_purchase_flexible_product_without_productId():
    """Tests the API endpoint to purchase flexible product without productId"""

    client = Client(key, secret)
    try:
        response = await client.savings_purchase_flexible_product("", 10)
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_savings_purchase_flexible_product_without_amount():
    """Tests the API endpoint to purchase flexible product without amount"""

    client = Client(key, secret)
    try:
        response = await client.savings_purchase_flexible_product("1", "")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "POST",
    "/sapi/v1/lending/daily/purchase\\?productId=1&amount=10",
    mock_item,
    200,
)
async def test_savings_purchase_flexible_product():
    """Tests the API endpoint to purchase flexible product list"""

    client = Client(key, secret)
    response = await client.savings_purchase_flexible_product(productId=1, amount=10)
    response.should.equal(mock_item)
