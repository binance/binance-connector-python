import pytest

from binance.async_spot import AsyncSpot as Client
from tests.util import random_str
from tests.util import mock_async_http_response
from binance.error import ParameterRequiredError, ClientError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()

listen_key = random_str()

@pytest.mark.asyncio
async def test_new_listen_key_without_key():
    """Tests the API endpoint to renew margin listenkey but without the key"""

    client = Client(key)
    try:
        response = await client.renew_margin_listen_key("")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "PUT",
    "/sapi/v1/userDataStream\\?listenKey=" + listen_key,
    mock_exception,
    400,
)
async def test_rewnew_listen_key_with_wrong_key():
    """Tests the API endpoint to renew margin listekn key with wrong key"""

    client = Client(key)
    try:
        response = await client.renew_margin_listen_key(listen_key)
    except Exception as e:
        assert isinstance(e, ClientError)
    else:
        assert isinstance(response, ClientError)


@pytest.mark.asyncio
@mock_async_http_response(
    "PUT", "/sapi/v1/userDataStream\\?listenKey=" + listen_key, mock_item, 200
)
async def test_rewnew_listen_key():
    """Tests the API endpoint to renew an existing margin listen key"""

    client = Client(key)
    response = await client.renew_margin_listen_key(listen_key)
    response.should.equal(mock_item)
