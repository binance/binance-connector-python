import pytest

from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client
from binance.lib.utils import urlencode as encoded_string
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()


params = {"asset": "BNB", "amount": 1, "recvWindow": 1000}

@pytest.mark.asyncio
async def test_sub_account_transfer_to_master_without_asset():
    """Tests the API endpoint to transfer asset to master account without asset"""

    params = {"asset": "", "amount": 1, "recvWindow": 1000}
    client = Client(key, secret)
    try:
        response = await client.sub_account_transfer_to_master(**params)
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_sub_account_transfer_to_master_without_amount():
    """Tests the API endpoint to transfer asset to master account without amount"""

    params = {"asset": "BNB", "amount": "", "recvWindow": 1000}
    client = Client(key, secret)
    try:
        response = await client.sub_account_transfer_to_master(**params)
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "POST",
    "/sapi/v1/sub-account/transfer/subToMaster\\?" + encoded_string(params, True),
    mock_item,
    200,
)
async def test_sub_account_transfer_to_master():
    """Tests the API endpoint to transfer asset to master account"""

    client = Client(key, secret)
    response = await client.sub_account_transfer_to_master(**params)
    response.should.equal(mock_item)
