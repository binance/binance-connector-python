import pytest
from binance.async_spot import AsyncSpot as Client
from tests.util import mock_async_http_response
from tests.util import random_str
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()

params = {"asset": ["LTC", "EOS"]}

@pytest.mark.asyncio
async def test_withdraw_without_coin():
    """Tests the API endpoint to transfer dust without coin"""

    client = Client(key, secret)
    try:
        response = await client.transfer_dust("")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "POST", "/sapi/v1/asset/dust\\?asset=LTC&asset=EOS", mock_item, 200
)
async def test_withdraw():
    """Tests the API endpoint to transfer dust"""

    client = Client(key, secret)
    response = await client.transfer_dust(**params)
    response.should.equal(mock_item)
