import pytest
from binance.async_spot import AsyncSpot as Client
from urllib.parse import urlencode
from tests.util import random_str
from tests.util import random_id
from tests.util import mock_async_http_response
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

cross_params = {
    "orderListId": random_id(),
    "recvWindow": 1000,
}

isolated_params = {
    "orderListId": random_id(),
    "isIsolated": "TRUE",
    "symbol": "BTCUSDT",
    "recvWindow": 1000,
}

client = Client(key, secret)

@pytest.mark.asyncio
async def test_get_margin_oco_order_with_isIsolated_but_no_symbol():
    """Tests the API endpoint to get margin oco order without symbol when having isIsolated"""

    try:
        response = await client.get_margin_oco_order(
        orderListId=124, isIsolated="TRUE"
    )
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "GET",
    "/sapi/v1/margin/orderList\\?" + urlencode(cross_params),
    mock_item,
    200,
)
async def test_get_margin_oco_order_with_order_id():
    """Tests the API endpoint to get cross margin oco order"""

    response = await client.get_margin_oco_order(**cross_params)
    response.should.equal(mock_item)


@pytest.mark.asyncio
@mock_async_http_response(
    "GET",
    "/sapi/v1/margin/orderList\\?" + urlencode(isolated_params),
    mock_item,
    200,
)
async def test_get_margin_oco_order_with_order_id_and_isIsolated():
    """Tests the API endpoint to get isolated margin oco order"""

    response = await client.get_margin_oco_order(**isolated_params)
    response.should.equal(mock_item)
