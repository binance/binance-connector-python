import pytest
from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client
from binance.error import ParameterRequiredError, ClientError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

params = {
    "symbol": "BTCUSDT",
    "orderListId": 1,
    "listClientOrderId": 2,
    "newClientOrderId": 3,
    "recvWindow": 1000,
}

@pytest.mark.asyncio
async def test_cancel_oco_order_without_symbol():
    """Tests the API endpoint to cancel oco order without symbol"""

    client = Client(key, secret)
    try:
        response = await client.cancel_oco_order("")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "DELETE",
    "/api/v3/orderList\\?symbol=ETHBTC&orderListId=",
    mock_exception,
    400,
)
async def test_cancel_oco_order_without_orderListId():
    """Tests the API endpoint to cancel order without value for orderListId"""

    client = Client(key, secret)
    try:
        response = await client.cancel_oco_order("ETHBTC", orderListId="")
    except Exception as e:
        assert isinstance(e, ClientError)
    else:
        assert isinstance(response, ClientError)


@pytest.mark.asyncio
@mock_async_http_response(
    "DELETE", "/api/v3/orderList\\?" + urlencode(params), mock_item, 200
)
async def test_cancel_order_with_order_id():
    """Tests the API endpoint to cancel order"""

    client = Client(key, secret)
    response = await client.cancel_oco_order(**params)
    response.should.equal(mock_item)
