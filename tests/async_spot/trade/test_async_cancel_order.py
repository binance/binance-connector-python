import pytest

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client
from binance.error import ParameterRequiredError, ClientError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1105, "msg": 'Parameter "orderId" was empty.'}

key = random_str()
secret = random_str()

orderId = "1234567"
origClientOrderId = "2345678"

params = {
    "symbol": "BTCUSDT",
    "orderId": orderId,
    "origClientOrderId": origClientOrderId,
    "recvWindow": 1000,
}

@pytest.mark.asyncio
async def test_cancel_order_without_symbol():
    """Tests the API endpoint to cancel order without symbol"""

    client = Client(key, secret)
    try:
        response = await client.cancel_order("")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "DELETE", "/api/v3/order\\?symbol=ETHBTC&orderId=", mock_exception, 400
)
async def test_cancel_order_without_order_id():
    """Tests the API endpoint to cancel order without provide order id"""

    client = Client(key, secret)
    try:
        response = await client.cancel_order("ETHBTC", orderId="")
    except Exception as e:
        assert isinstance(e, ClientError)
    else:
        assert isinstance(response, ClientError)


@pytest.mark.asyncio
@mock_async_http_response(
    "DELETE", "/api/v3/order\\?symbol=ETHBTC&orderId=" + orderId, mock_item, 200
)
async def test_cancel_order_with_order_id():
    """Tests the API endpoint to cancel order"""

    client = Client(key, secret)
    response = await client.cancel_order("ETHBTC", orderId=orderId)
    response.should.equal(mock_item)


@pytest.mark.asyncio
@mock_async_http_response(
    "DELETE", "/api/v3/order\\?" + urlencode(params), mock_item, 200
)
async def test_cancel_order_with_more_params():
    """Tests the API endpoint to cancel order with other parameters"""

    client = Client(key, secret)
    response = await client.cancel_order(**params)
    response.should.equal(mock_item)
