import pytest

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1105, "msg": "error message."}

key = random_str()
secret = random_str()
client = Client(key, secret)

params = {"loanCoin": "BUSD", "collateralCoin": "BNB", "loanTerm": 7}

@pytest.mark.asyncio
async def test_loan_borrow_without_loanCoin():
    """Tests the API endpoint to borrow loan without loanCoin"""

    params = {"loanCoin": "", "collateralCoin": "BNB", "loanTerm": 7}

    try:
        response = await client.loan_borrow(**params)
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_loan_borrow_without_collateralCoin():
    """Tests the API endpoint to borrow loan without collateralCoin"""

    params = {
        "loanCoin": "USDT",
        "collateralCoin": "",
        "loanTerm": 7,
    }

    try:
        response = await client.loan_borrow(**params)
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_loan_borrow_without_loanTerm():
    """Tests the API endpoint to borrow loan without loanTerm"""

    params = {
        "loanCoin": "USDT",
        "collateralCoin": "BNB",
        "loanTerm": "",
        "loanAmount": 1.1,
    }

    try:
        response = await client.loan_borrow(**params)
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "POST",
    "/sapi/v1/loan/borrow\\?" + urlencode(params),
    mock_item,
    200,
)
async def test_loan_borrow():
    """Tests the API endpoint to loan"""

    response = await client.loan_borrow(**params)
    response.should.equal(mock_item)
