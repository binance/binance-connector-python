import requests
from tests.util import random_str
from binance.version import __version__
from binance.api import API
from binance.error import ParameterRequiredError


def test_API_initial():
    """ Tests the API initialization """

    client = API()

    client.should.be.a(API)
    client.key.should.be.none
    client.timeout.should.be.none
    client.secret.should.be.none
    client.show_weight_usage.should.be.false
    client.show_header.should.be.false
    client.session.should.be.a(requests.Session)
    client.session.headers.should.have.key(
        'Content-Type').which.should.equal('application/json;charset=utf-8')
    client.session.headers.should.have.key(
        'User-Agent').which.should.equal('binance-connector-python/' + __version__)
    client.session.headers.should.have.key('X-MBX-APIKEY').which.should.be.none


def test_API_with_extra_parametes():
    """ Tests the API initialization with extra parameters"""

    key = random_str()
    secret = random_str()
    base_url = random_str()

    client = API(key, secret, base_url=base_url,
                 show_weight_usage=True, show_header=True, timeout=0.1)

    client.should.be.a(API)
    client.key.should.equal(key)
    client.timeout.should.equal(0.1)
    client.secret.should.equal(secret)
    client.base_url.should.equal(base_url)
    client.show_weight_usage.should.be.true
    client.show_header.should.be.true
    client.session.headers.should.have.key(
        'X-MBX-APIKEY').which.should.equal(key)


def test_limit_request_without_api_key():
    """ Tests the limit_request without api key """

    url = random_str()
    client = API()
    client.limit_request.when.called_with(
        'GET', url).should.throw(ParameterRequiredError)
