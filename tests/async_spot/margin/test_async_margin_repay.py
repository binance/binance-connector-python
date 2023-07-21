import pytest

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

asset = "BNB"
amount = "100"

params = {"asset": asset, "amount": amount}

@pytest.mark.asyncio
async def test_margin_repay_without_asset():
    """Tests the API endpoint to margin repay without asset"""

    client = Client(key, secret)
    try:
        response = await client.margin_repay("", amount)
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_margin_repay_without_amount():
    """Tests the API endpoint to margin repay without amount"""

    client = Client(key, secret)
    try:
        response = await client.margin_repay(asset, "")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "POST", "/sapi/v1/margin/repay\\?" + urlencode(params), mock_item, 200
)
async def test_margin_repay():
    """Tests the API endpoint to margin repay"""

    client = Client(key, secret)
    response = await client.margin_repay(**params)
    response.should.equal(mock_item)
