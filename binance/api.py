import time
import hmac
import hashlib
import requests
from . import version
from urllib.parse import urlencode
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
            'User-Agent': 'binance-python/' + version.__version__,
            'X-MBX-APIKEY': secret
        })
        self.session.headers.update({'X-MBX-APIKEY': self.key})
        self.response = None

        self.baseUrl = 'https://api.binance.com'
        if 'base_url' in kwargs:
            self.baseUrl = kwargs['base_url']

        self.show_weight_usage = False
        if 'show_weight_usage' in kwargs:
            self.show_weight_usage = kwargs['show_weight_usage'] and kwargs['show_weight_usage'] == True

        self.show_header = False
        if 'show_header' in kwargs:
            self.show_header = kwargs['show_header'] and kwargs['show_header'] == True

        return

    def _prepare_params(self, params):
        return urlencode(cleanNoneValue(params))

    def query(self, urlPath, payload={}):
        url = self.baseUrl + urlPath
        print(url)
        response = self.session.get(url, params=payload)
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

    def sign_query(self, urlPath, payload={}):
        ts = self.get_timestamp()
        payload['timestamp'] = ts
        query_string = self._prepare_params(payload)
        signature = self._get_sign(query_string)
        payload['signature'] = signature
        query_string = query_string + '&signature=' + signature
        return self.query(urlPath + '?' + query_string)

    def get_timestamp(self):
        return int(time.time() * 1000)

    def _get_sign(self, data):
        m = hmac.new(self.secret.encode('utf-8'), data.encode('utf-8'), hashlib.sha256)
        return m.hexdigest()
