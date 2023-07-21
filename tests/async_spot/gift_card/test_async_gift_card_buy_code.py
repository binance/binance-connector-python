import pytest
from tests.util import random_str
from tests.util import mock_async_http_response
from urllib.parse import urlencode
from binance.async_spot import AsyncSpot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

client = Client(key, secret)

parameterized_test_data = [
    ({"baseToken": None, "faceToken": "BNB", "baseTokenAmount": 100}),
    ({"baseToken": "BUSD", "faceToken": None, "baseTokenAmount": 100}),
    ({"baseToken": "BUSD", "faceToken": "BNB", "baseTokenAmount": None}),
]


@pytest.mark.asyncio
@pytest.mark.parametrize("params", parameterized_test_data)
async def test_gift_card_buy_code_without_params(params):
    """Tests the API endpoint to verify a Binance Code without params"""
    with pytest.raises(ParameterRequiredError):
        await client.gift_card_buy_code(**params)


params = {"baseToken": "BUSD", "faceToken": "BNB", "baseTokenAmount": 100}


@pytest.mark.asyncio
@mock_async_http_response(
    "POST",
    "/sapi/v1/giftcard/buyCode\\?" + urlencode(params),
    mock_item,
    200,
)
async def test_gift_card_buy_code():
    """Tests the API endpoint to buy gift card"""

    response = await client.gift_card_buy_code(**params)
    response.should.equal(mock_item)
