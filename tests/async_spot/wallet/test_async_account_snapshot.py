import pytest
from binance.async_spot import AsyncSpot as Client
from tests.util import mock_async_http_response
from tests.util import random_str
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()

@pytest.mark.asyncio
async def test_account_snapshot_without_type():
    """Tests the API endpoint to get account snapshot without type"""

    client = Client(key, secret)
    try:
        response = await client.account_snapshot("")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "GET", "/sapi/v1/accountSnapshot\\?type=SPOT", mock_item, 200
)
async def test_account_snapshot():
    """Tests the API endpoint to get account snapshot"""

    client = Client(key, secret)
    response = await client.account_snapshot(type="SPOT")
    response.should.equal(mock_item)
