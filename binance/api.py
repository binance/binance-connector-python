import hmac
import json
import logging
import hashlib
import requests
from . import version
from urllib.parse import urlencode
from json.decoder import JSONDecodeError
from binance.error import ClientError, ServerError
from binance.lib.utils import get_timestamp
from binance.lib.utils import cleanNoneValue
from binance.lib.utils import check_required_parameter

logger = logging.getLogger(__name__)


class API(object):
    """ API base class

    supported arguments:
    - base_url: the API base url, useful to switch to testnet, etc. By default it's api.binance.com
    - timeout: the time waiting for server response.
    - show_weight_usage: whether return request weight usage
    - show_header: whether return the whole response header

    """

    def __init__(self, key=None, secret=None, **kwargs):
        self.key = key
        self.secret = secret
        self.timeout = None
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json;charset=utf-8',
            'User-Agent': 'binance-connector-python/' + version.__version__,
            'X-MBX-APIKEY': secret
        })
        self.session.headers.update({'X-MBX-APIKEY': self.key})

        self.base_url = 'https://api.binance.com'
        if 'base_url' in kwargs:
            self.base_url = kwargs['base_url']

        self.show_weight_usage = False
        if 'show_weight_usage' in kwargs and kwargs['show_weight_usage']:
            self.show_weight_usage = True

        self.show_header = False
        if 'show_header' in kwargs and kwargs['show_header']:
            self.show_header = True

        if 'timeout' in kwargs:
            self.timeout = kwargs['timeout']
        return

    def query(self, url_path, payload={}):
        return self.send_request('GET', url_path, payload=payload)

    def limit_request(self, http_method, url_path, payload={}):
        """ limit request is for those endpoints require API key in the header"""

        check_required_parameter(self.key, 'apiKey')
        return self.send_request(http_method, url_path, payload=payload)

    def sign_request(self, http_method, url_path, payload={}):
        payload['timestamp'] = get_timestamp()
        query_string = self._prepare_params(payload)
        signature = self._get_sign(query_string)
        payload['signature'] = signature
        query_string = query_string + '&signature=' + signature

        return self.send_request(http_method, url_path, payload)

    def send_request(self, http_method, url_path, payload={}):
        url = self.base_url + url_path

        logger.debug('url: ' + url)
        logger.debug('payload: ' + json.dumps(payload))

        params = cleanNoneValue({'url': url, 'params': payload, 'timeout': self.timeout})

        response = self._dispatch_request(http_method)(**params)

        logger.debug('raw response from server:' + response.text)

        self._handle_exception(response)

        data = response.json()
        result = {}
        if (self.show_weight_usage):
            weight_usage = {}
            for key in response.headers.keys():
                if key.startswith('X-MBX-USED-WEIGHT'):
                    weight_usage[key] = response.headers[key]
                    result['weight_usage'] = weight_usage

        if (self.show_header):
            result['header'] = response.headers

        if (len(result) != 0):
            result['data'] = data
            return result

        return data

    def _prepare_params(self, params):
        return urlencode(cleanNoneValue(params))

    def _get_sign(self, data):
        m = hmac.new(self.secret.encode('utf-8'),
                     data.encode('utf-8'), hashlib.sha256)
        return m.hexdigest()

    def _dispatch_request(self, http_method):

        return {
            'GET': self.session.get,
            'DELETE': self.session.delete,
            'PUT': self.session.put,
            'POST': self.session.post,
        }.get(http_method, 'GET')

    def _handle_exception(self, response):
        status_code = response.status_code
        if (status_code < 400):
            return

        if (status_code >= 400 and status_code < 500):
            try:
                data = response.json()
                raise ClientError(status_code, data)
            except JSONDecodeError:
                raise ClientError(status_code, None, response.text)

        raise ServerError(status_code, response.text)
