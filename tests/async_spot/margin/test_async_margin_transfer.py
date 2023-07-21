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
type = 1

params = {"asset": asset, "amount": amount, "type": type}

@pytest.mark.asyncio
async def test_margin_transfer_without_asset():
    """Tests the API endpoint to margin tranfer without asset"""

    client = Client(key, secret)
    try:
        response = await client.margin_transfer("", amount, type)
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_margin_transfer_without_amount():
    """Tests the API endpoint to margin tranfer without amount"""

    client = Client(key, secret)
    try:
        response = await client.margin_transfer("", amount, type)
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_margin_transfer_without_type():
    """Tests the API endpoint to margin tranfer without type"""

    client = Client(key, secret)
    try:
        response = await client.margin_transfer("", amount, type)
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "POST", "/sapi/v1/margin/transfer\\?" + urlencode(params), mock_item, 200
)
async def test_margin_transfer():
    """Tests the API endpoint to margin tranfer"""

    client = Client(key, secret)
    response = await client.margin_transfer(**params)
    response.should.equal(mock_item)
