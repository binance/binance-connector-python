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

parameterized_test_data = [({"baseToken": None})]


@pytest.mark.asyncio
@pytest.mark.parametrize("params", parameterized_test_data)
async def test_gift_card_token_limit_without_params(params):
    """Tests the API endpoint to get token limit without param"""
    with pytest.raises(ParameterRequiredError):
        await client.gift_card_token_limit(**params)


params = {"baseToken": "BUSD"}


@pytest.mark.asyncio
@mock_async_http_response(
    "GET",
    "/sapi/v1/giftcard/buyCode/token-limit\\?" + urlencode(params),
    mock_item,
    200,
)
async def test_gift_card_token_limit():
    """Tests the API endpoint to get token limit"""

    response = await client.gift_card_token_limit(**params)
    response.should.equal(mock_item)
