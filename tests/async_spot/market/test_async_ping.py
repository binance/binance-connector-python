from binance.async_spot import AsyncSpot as Client
import pytest

from tests.util import mock_async_http_response


@pytest.mark.asyncio
@mock_async_http_response("GET", "/api/v3/ping", {}, 200)
async def test_ping():
    """Tests the API endpoint to get connectivity"""

    api = Client()
    response = await api.ping()
    response.should.equal({})
