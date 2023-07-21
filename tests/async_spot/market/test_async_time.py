from binance.async_spot import AsyncSpot as Client
import pytest

from tests.util import mock_async_http_response

mock_item = {"key_1": "value_1", "key_2": "value_2"}


@pytest.mark.asyncio
@mock_async_http_response("GET", "/api/v3/time", mock_item, 200)
async def test_time():
    """Tests the API endpoint to get exchange time"""

    api = Client()
    response = await api.time()
    response.should.equal(mock_item)
