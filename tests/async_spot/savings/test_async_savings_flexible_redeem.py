import pytest

from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

@pytest.mark.asyncio
async def test_savings_flexible_redeem_without_productId():
    """Tests the API endpoint to redeem flexible redemption without productId"""

    client = Client(key, secret)
    try:
        response = await client.savings_flexible_redeem("", 10, "NORMAL")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_savings_flexible_redeem_without_amount():
    """Tests the API endpoint to redeem flexible redemption without amount"""

    client = Client(key, secret)
    try:
        response = await client.savings_flexible_redeem("1", "", "NORMAL")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_savings_flexible_redeem_without_type():
    """Tests the API endpoint to redeem flexible redemption without type"""

    client = Client(key, secret)
    try:
        response = await client.savings_flexible_redeem("1", "10", "")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "POST",
    "/sapi/v1/lending/daily/redeem\\?productId=1&amount=2&type=NORMAL",
    mock_item,
    200,
)
async def test_savings_flexible_redeem():
    """Tests the API endpoint to get flexible redemption quota"""

    client = Client(key, secret)
    response = await client.savings_flexible_redeem(productId="1", amount=2, type="NORMAL")
    response.should.equal(mock_item)
