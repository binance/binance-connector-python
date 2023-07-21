import pytest

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client
from binance.error import ParameterRequiredError, ClientError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -2011, "msg": "unknown order sent"}

key = random_str()
secret = random_str()

orderId = "1234567"
origClientOrderId = "2345678"

params = {"symbol": "ETHBTC", "recvWindow": 1000}

@pytest.mark.asyncio
async def test_cancel_open_orders_without_symbol():
    """Tests the API endpoint to cancel all open orders without symbol"""

    client = Client(key, secret)
    try:
        response = await client.cancel_open_orders("")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "DELETE", "/api/v3/openOrders\\?symbol=ETHBTC", mock_exception, 400
)
async def test_cancel_open_orders_when_no_open_orders():
    """Tests the API endpoint to cancel all open orders when there is no open order"""

    client = Client(key, secret)
    try:
        response = await client.cancel_open_orders("ETHBTC")
    except Exception as e:
        assert isinstance(e, ClientError)
    else:
        assert isinstance(response, ClientError)


@pytest.mark.asyncio
@mock_async_http_response(
    "DELETE", "/api/v3/openOrders\\?" + urlencode(params), mock_item, 200
)
async def test_cancel_open_orders():
    """Tests the API endpoint to cancel all open orders"""

    client = Client(key, secret)
    response = await client.cancel_open_orders("ETHBTC", recvWindow=1000)
    response.should.equal(mock_item)
