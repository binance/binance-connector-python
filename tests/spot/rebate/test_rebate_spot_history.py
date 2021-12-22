import responses

from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.lib.utils import encoded_string

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()
params = {"startTime": 1637186702000, "endTime": 1637690208000, "page": 1}

client = Client(key, secret)


@mock_http_response(
    responses.GET,
    "/sapi/v1/rebate/taxQuery",
    mock_item,
    200,
)
def test_rebate_spot_history_without_params():
    """Tests the API endpoint to get Spot Rebate History Records without parameters"""
    client.rebate_spot_history().should.equal(mock_item)


@mock_http_response(
    responses.GET,
    "/sapi/v1/rebate/taxQuery\\?" + encoded_string(params),
    mock_item,
    200,
)
def test_rebate_spot_history_with_params():
    """Tests the API endpoint to get Spot Rebate History Records"""
    client.rebate_spot_history(**params).should.equal(mock_item)
