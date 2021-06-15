import responses
from binance.spot import Spot as Client
from tests.util import mock_http_response
from tests.util import random_str
from binance.error import ParameterRequiredError


mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()


def test_bswap_request_quote_without_quoteAsset():
    """Tests the API endpoint to Request a quote for swap quote asset (selling asset) for base asset (buying asset),
    essentially price/exchange rates without quoteAsset"""

    client = Client(key, secret)
    client.bswap_request_quote.when.called_with("", "BUSD", "30000").should.throw(
        ParameterRequiredError
    )


def test_bswap_request_quote_without_baseAsset():
    """Tests the API endpoint to Request a quote for swap quote asset (selling asset) for base asset (buying asset),
    essentially price/exchange rates without baseAsset"""

    client = Client(key, secret)
    client.bswap_request_quote.when.called_with("USDT", "", "30000").should.throw(
        ParameterRequiredError
    )


def test_bswap_request_quote_without_quoteQty():
    """Tests the API endpoint to Request a quote for swap quote asset (selling asset) for base asset (buying asset),
    essentially price/exchange rates without quoteQty"""

    client = Client(key, secret)
    client.bswap_request_quote.when.called_with("USDT", "BUSD", None).should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.GET,
    "/sapi/v1/bswap/quote\\?quoteAsset=USDT&baseAsset=BUSD&quoteQty=30000",
    mock_item,
    200,
)
def test_bswap_liquidity_remove():
    """Tests the API endpoint to Request a quote for swap quote asset (selling asset) for base asset (buying asset),
    essentially price/exchange rates"""

    client = Client(key, secret)
    response = client.bswap_request_quote("USDT", "BUSD", "30000")
    response.should.equal(mock_item)
