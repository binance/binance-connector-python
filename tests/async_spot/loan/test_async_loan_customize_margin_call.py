import pytest

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()
client = Client(key, secret)

params = {"marginCall": 0.1, "collateralCoin": "BUSD"}

@pytest.mark.asyncio
async def test_loan_customize_margin_call_without_margin_call():
    """Tests the API endpoint to customize margin call with missing parameter"""

    params = {"marginCall": ""}

    try:
        response = await client.loan_customize_margin_call(**params)
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "POST",
    "/sapi/v1/loan/customize/margin_call\\?" + urlencode(params),
    mock_item,
    200,
)
async def test_loan_customize_margin_call():
    """Tests the API endpoint to customize margin call for ongoing orders only"""

    response = await client.loan_customize_margin_call(**params)
    response.should.equal(mock_item)
