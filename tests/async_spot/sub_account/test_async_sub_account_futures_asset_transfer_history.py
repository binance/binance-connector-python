import pytest

from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

@pytest.mark.asyncio
async def test_sub_account_futures_asset_transfer_history_without_email():
    """Tests the API endpoint to  query sub account futures asset transfer history without email"""

    param = {"email": "", "futuresType": 1}
    client = Client(key, secret)
    try:
        response = await client.sub_account_futures_asset_transfer_history(
        **param
    )
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_sub_account_futures_asset_transfer_history_without_futurestype():
    """Tests the API endpoint to  query sub account futures asset transfer history without email"""

    param = {"email": "alice@test.com", "futuresType": ""}
    client = Client(key, secret)
    try:
        response = await client.sub_account_futures_asset_transfer_history(
        **param
    )
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "GET",
    "/sapi/v1/sub-account/futures/internalTransfer\\?email=alice@test.com&futuresType=1",
    mock_item,
    200,
)
async def test_sub_account_futures_asset_transfer_history():
    """Tests the API endpoint to query sub account futures asset transfer history"""

    params = {"email": "alice@test.com", "futuresType": 1}
    client = Client(key, secret)
    response = await client.sub_account_futures_asset_transfer_history(**params)
    response.should.equal(mock_item)
