import responses

from binance.spot import Spot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_http_response
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

params = {"type": "BORROW", "recvWindow": 1000}


@mock_http_response(responses.GET, "/sapi/v1/margin/borrow-repay", mock_exception, 400)
def test_borrow_repay_record_without_type():
    """Tests the API endpoint to query borrow repay records without type"""

    client = Client(key, secret)
    client.borrow_repay_record.when.called_with("").should.throw(ParameterRequiredError)


@mock_http_response(
    responses.GET, "/sapi/v1/margin/borrow-repay\\?" + urlencode(params), mock_item, 200
)
def test_borrow_repay_record():
    """Tests the API endpoint to query borrow repay record"""

    client = Client(key, secret)
    response = client.borrow_repay_record(**params)
    response.should.equal(mock_item)
