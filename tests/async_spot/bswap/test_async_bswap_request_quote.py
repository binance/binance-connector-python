import pytest
from binance.async_spot import AsyncSpot as Client
from tests.util import mock_async_http_response
from tests.util import random_str
from binance.error import ParameterRequiredError


mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()

@pytest.mark.asyncio
async def test_bswap_request_quote_without_quoteAsset():
    """Tests the API endpoint to Request a quote for swap quote asset (selling asset) for base asset (buying asset),
    essentially price/exchange rates without quoteAsset"""

    client = Client(key, secret)
    try:
        response = await client.bswap_request_quote("", "BUSD", "30000")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_bswap_request_quote_without_baseAsset():
    """Tests the API endpoint to Request a quote for swap quote asset (selling asset) for base asset (buying asset),
    essentially price/exchange rates without baseAsset"""

    client = Client(key, secret)
    try:
        response = await client.bswap_request_quote("USDT", "", "30000")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_bswap_request_quote_without_quoteQty():
    """Tests the API endpoint to Request a quote for swap quote asset (selling asset) for base asset (buying asset),
    essentially price/exchange rates without quoteQty"""

    client = Client(key, secret)
    try:
        response = await client.bswap_request_quote("USDT", "BUSD", None)
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "GET",
    "/sapi/v1/bswap/quote\\?quoteAsset=USDT&baseAsset=BUSD&quoteQty=30000",
    mock_item,
    200,
)
async def test_bswap_liquidity_remove():
    """Tests the API endpoint to Request a quote for swap quote asset (selling asset) for base asset (buying asset),
    essentially price/exchange rates"""

    client = Client(key, secret)
    response = await client.bswap_request_quote("USDT", "BUSD", "30000")
    response.should.equal(mock_item)
