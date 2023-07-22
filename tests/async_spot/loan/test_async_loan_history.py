import pytest

from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client
from binance.lib.utils import urlencode as encoded_string
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()
params = {"asset": "BUSD", "recvWindow": 1000}

client = Client(key, secret)

@pytest.mark.asyncio
async def test_loan_history_without_asset():
    """Tests the API endpoint to query loan history without asset"""

    params = {"asset": "", "recvWindow": 1000}

    try:
        response = await client.loan_history(**params)
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "GET",
    "/sapi/v1/loan/income\\?" + encoded_string(params, True),
    mock_item,
    200,
)
async def test_loan_history():
    """Tests the API endpoint to query loan history"""

    response = await client.loan_history(**params)
    response.should.equal(mock_item)
