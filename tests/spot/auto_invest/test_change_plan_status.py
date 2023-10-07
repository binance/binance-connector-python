import responses

from binance.spot import Spot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_http_response


mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

send_params = {"planId": 1234, "status": random_str(), "recvWindow": 5000}


@mock_http_response(
    responses.POST,
    "/sapi/v1/lending/auto-invest/plan/edit-status\\?" + urlencode(send_params),
    mock_item,
    200,
)
def test_change_plan_status():
    """Tests the API endpoint to change plan status"""

    client = Client(key, secret)
    response = client.change_plan_status(**send_params)
    response.should.equal(mock_item)
