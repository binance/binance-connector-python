import pytest
from binance.async_spot import AsyncSpot as Client
from tests.util import mock_async_http_response
from tests.util import random_str
from urllib.parse import urlencode
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()

parameterized_test_params = [
    ({"coin": "", "enable": True}),
    ({"coin": "USDC", "enable": None}),
]


@pytest.mark.asyncio
@pytest.mark.parametrize("params", parameterized_test_params)
async def test_toggle_auto_convertion_with_missing_field(params):
    """Tests the API endpoint to toggle auto convertion with missing field"""

    client = Client(key, secret)
    with pytest.raises(ParameterRequiredError):
        await client.toggle_auto_convertion(**params)


params = {"coin": "USDC", "enable": True}


@pytest.mark.asyncio
@mock_async_http_response(
    "POST",
    "/sapi/v1/capital/contract/convertible-coins\\?" + urlencode(params),
    mock_item,
    200,
)
async def test_toggle_auto_convertion():
    """Tests the API endpoint to toggle auto convertion"""

    client = Client(key, secret)
    response = await client.toggle_auto_convertion(**params)
    response.should.equal(mock_item)
