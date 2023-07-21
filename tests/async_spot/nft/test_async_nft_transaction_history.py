import pytest

from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client
from binance.error import ParameterRequiredError
from binance.lib.utils import encoded_string

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()
client = Client(key, secret)

params = {
    "orderType": 0,
    "startTime": 1637186702000,
    "endTime": 1637690208000,
    "limit": 50,
    "page": 1,
}

@pytest.mark.asyncio
async def test_nft_transaction_history_without_orderType():
    """Tests the API endpoint to NFT Transaction History without orderType"""

    try:
        response = await client.nft_transaction_history("")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "GET",
    "/sapi/v1/nft/history/transactions\\?" + encoded_string(params),
    mock_item,
    200,
)
async def test_nft_transaction_history():
    """Tests the API endpoint to NFT Transaction History"""

    (await client.nft_transaction_history(**params)).should.equal(mock_item)
