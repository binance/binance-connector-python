import pytest
from binance.async_spot import AsyncSpot as Client
from tests.util import mock_async_http_response
from tests.util import random_str
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()

@pytest.mark.asyncio
async def test_redeem_blvt_without_tokenName():
    """Tests the API endpoint to Redeem BLVT without tokenName"""

    client = Client(key, secret)
    try:
        response = await client.redeem_blvt("", "1")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)

@pytest.mark.asyncio
async def test_redeem_blvt_without_amount():
    """Tests the API endpoint to Redeem BLVT without amount"""

    client = Client(key, secret)
    try:
        response = await client.redeem_blvt("BTCUP", "")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "POST", "/sapi/v1/blvt/redeem\\?tokenName=BTCUP&amount=1", mock_item, 200
)
async def test_redeem_blvt():
    """Tests the API endpoint to Redeem BLVT"""

    client = Client(key, secret)
    response = await client.redeem_blvt("BTCUP", "1")
    response.should.equal(mock_item)
