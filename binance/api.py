import hmac
import hashlib
import requests
from . import version
from urllib.parse import urlencode
from binance.lib.utils import get_timestamp
from binance.lib.utils import cleanNoneValue
from binance.lib.utils import check_required_parameter
from binance.lib.utils import check_required_parameters


class API(object):
    def __init__(self, key=None, secret=None, **kwargs):
        self.key = key
        self.secret = secret
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json;charset=utf-8',
            'User-Agent': 'binance-connector-python/' + version.__version__,
            'X-MBX-APIKEY': secret
        })
        self.session.headers.update({'X-MBX-APIKEY': self.key})
        self.response = None

        self.base_url = 'https://api.binance.com'
        if 'base_url' in kwargs:
            self.base_url = kwargs['base_url']

        self.show_weight_usage = False
        if 'show_weight_usage' in kwargs:
            self.show_weight_usage = kwargs['show_weight_usage'] and kwargs['show_weight_usage'] == True

        self.show_header = False
        if 'show_header' in kwargs:
            self.show_header = kwargs['show_header'] and kwargs['show_header'] == True
        return

    def query(self, url_path, payload={}):
        return self.send_request('GET', url_path, payload=payload)

    def sign_request(self, http_method, url_path, payload={}):
        payload['timestamp'] = get_timestamp()
        query_string = self._prepare_params(payload)
        signature = self._get_sign(query_string)
        payload['signature'] = signature
        query_string = query_string + '&signature=' + signature

        return self.send_request(http_method, url_path, payload)

    def send_request(self, http_method, url_path, payload={}):
        url = self.base_url + url_path

        response = self._dispatch_request(http_method)(url, params=payload)

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
        m = hmac.new(self.secret.encode('utf-8'), data.encode('utf-8'), hashlib.sha256)
        return m.hexdigest()

    def _dispatch_request(self, http_method):

        print(http_method)
        return {
            'GET': self.session.get,
            'DELETE': self.session.delete
        }.get(http_method, 'GET')
