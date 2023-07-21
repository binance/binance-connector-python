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

params = {"orderId": 100000001, "amount": 100.5}

@pytest.mark.asyncio
async def test_loan_vip_repay_without_orderId():
    """Tests the API endpoint to repay vip loan without orderId"""

    params = {"orderId": "", "amount": 100.5}

    try:
        response = await client.loan_vip_repay(**params)
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_loan_vip_repay_without_amount():
    """Tests the API endpoint to repay vip loan without amount"""

    params = {
        "orderId": "USDT",
        "amount": "",
    }

    try:
        response = await client.loan_vip_repay(**params)
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "POST",
    "/sapi/v1/loan/vip/repay\\?" + urlencode(params),
    mock_item,
    200,
)
async def test_loan_vip_repay():
    """Tests the API endpoint to repay loan"""

    response = await client.loan_vip_repay(**params)
    response.should.equal(mock_item)
