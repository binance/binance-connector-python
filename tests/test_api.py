import responses

import requests
from tests.util import random_str, mock_http_response
from binance.__version__ import __version__
from binance.api import API
from binance.error import ParameterRequiredError, ServerError
from binance.error import ClientError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_error_body = "<HTML><HEAD><META HTTP-EQUIV></HEAD></HTML>"
mock_error_response = {
    "code": -1102,
    "msg": "Mandatory parameter 'type' was not sent, was empty/null, or malformed.",
}
mock_base_url = "https://api.binance.com"

request_limit_usage = {"x-mbx-used-weight": "15", "x-mbx-used-weight-1m": "5"}
order_limit_usage = {"x-mbx-order-count-1d": "1000", "x-mbx-order-count-10s": "6"}
sapi_limit_usage = {"x-sapi-used-ip-weight-1m": "1200"}


def test_API_initial():
    """Tests the API initialization"""

    client = API()

    client.should.be.a(API)
    client.key.should.be.none
    client.timeout.should.be.none
    client.secret.should.be.none
    client.show_limit_usage.should.be.false
    client.show_header.should.be.false
    client.session.should.be.a(requests.Session)
    client.session.headers.should.have.key("Content-Type").which.should.equal(
        "application/json;charset=utf-8"
    )
    client.session.headers.should.have.key("User-Agent").which.should.equal(
        "binance-connector/" + __version__
    )
    client.session.headers.should.have.key("X-MBX-APIKEY").which.should.be.none


def test_API_with_extra_parameters():
    """Tests the API initialization with extra parameters"""

    key = random_str()
    secret = random_str()
    base_url = random_str()
    proxies = {"https": "https://1.2.3.4:8080"}

    client = API(
        key,
        secret,
        base_url=base_url,
        show_limit_usage=True,
        show_header=True,
        timeout=0.1,
        proxies=proxies,
    )

    client.should.be.a(API)
    client.key.should.equal(key)
    client.timeout.should.equal(0.1)
    client.secret.should.equal(secret)
    client.base_url.should.equal(base_url)
    client.show_limit_usage.should.be.true
    client.show_header.should.be.true
    client.proxies.should.equal(proxies)
    client.session.headers.should.have.key("X-MBX-APIKEY").which.should.equal(key)


def test_API_with_none_time_out():
    """Tests the timeout should be None if not provided"""

    client = API(timeout=None)
    client.timeout.should.be.none
    client = API()
    client.timeout.should.be.none


def test_API_with_illegal_proxies():
    """Tests the proxies with illegal value"""

    client = API(proxies="aaa")
    client.proxies.should.be.none


def test_limit_request_without_api_key():
    """Tests the limit_request without api key"""

    url = random_str()
    client = API()
    client.limit_request.when.called_with("GET", url).should.throw(
        ParameterRequiredError
    )


@mock_http_response(responses.GET, "/test/throw/client/error", None, 402)
def test_throw_client_error():
    """Tests throw client error"""

    client = API(base_url=mock_base_url)
    client.send_request.when.called_with(
        "GET", "/test/throw/client/error"
    ).should.throw(ClientError)


@mock_http_response(responses.GET, "/test/throw/server/error", mock_item, 502)
def test_throw_server_error():
    """Tests throw server error"""

    client = API(base_url=mock_base_url)
    client.send_request.when.called_with(
        "GET", "/test/throw/server/error"
    ).should.throw(ServerError)


@mock_http_response(
    responses.GET,
    "/test/limit/usage",
    mock_item,
    200,
    headers={**request_limit_usage, **order_limit_usage, **sapi_limit_usage},
)
def test_limit_usage_parameter():
    """Tests limit usage parameter"""

    client = API(base_url=mock_base_url, show_limit_usage=True)
    response = client.send_request("GET", "/test/limit/usage")
    response.should.equal(
        {
            "limit_usage": {
                **request_limit_usage,
                **order_limit_usage,
                **sapi_limit_usage,
            },
            "data": mock_item,
        }
    )


@mock_http_response(
    responses.GET,
    "/test/limit/usage",
    mock_item,
    200,
    headers={**request_limit_usage, **order_limit_usage, **sapi_limit_usage},
)
def test_limit_usage_parameter_with_illegal_value():
    """Tests limit usage parameter with illegal value"""

    client = API(base_url=mock_base_url, show_limit_usage="aaa")
    response = client.send_request("GET", "/test/limit/usage")
    response.should.equal(mock_item)


@mock_http_response(responses.GET, "/test/headers", mock_item, 200)
def test_header_parameter():
    """Tests header parameter"""

    client = API(base_url=mock_base_url, show_header=True)
    response = client.send_request("GET", "/test/headers")
    response.should.contain("header")


@mock_http_response(responses.GET, "/test/headers", mock_item, 200)
def test_header_parameter_with_illegal_value():
    """Tests header parameter with illegal value"""

    client = API(base_url=mock_base_url, show_header="aaa")
    response = client.send_request("GET", "/test/headers")
    response.should_not.contain("header")


@mock_http_response(
    responses.GET, "/test/non/json/with/200", None, 200, body_data=mock_error_body
)
def test_non_json_with_200_status_code():
    """Tests non json response with 200 status code"""

    client = API(base_url=mock_base_url)
    response = client.send_request("GET", "/test/non/json/with/200")
    response.should.equal(mock_error_body)


@mock_http_response(
    responses.GET, "/test/non/json/with/403", None, 403, body_data=mock_error_body
)
def test_non_json_with_403_status_code():
    """Tests non json response with 403 status code"""

    url = "/test/non/json/with/403"
    client = API(base_url=mock_base_url)
    client.send_request.when.called_with("GET", url).should.throw(ClientError)


@mock_http_response(
    responses.GET, "/test/error/response/with/400", mock_error_response, 400
)
def test_error_response_with_400_status_code():
    """Tests json response with 400 status code"""

    url = "/test/error/response/with/400"
    client = API(base_url=mock_base_url)
    client.send_request.when.called_with("GET", url).should.throw(ClientError)
