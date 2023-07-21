import pytest

from tests.util import random_str
from tests.util import mock_async_http_response
from urllib.parse import urlencode
from binance.async_spot import AsyncSpot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

params = {"referenceNo": random_str()}

client = Client(key, secret)

@pytest.mark.asyncio
async def test_gift_card_verify_code_without_params():
    """Tests the API endpoint to verify a Binance Code without params"""

    try:
        response = await client.gift_card_verify_code("")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "GET",
    "/sapi/v1/giftcard/verify\\?" + urlencode(params),
    mock_item,
    200,
)
async def test_gift_card_verify_code():
    """Tests the API endpoint to verify a Binance Code"""

    response = await client.gift_card_verify_code(**params)
    response.should.equal(mock_item)
