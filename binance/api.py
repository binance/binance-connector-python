import requests
from . import version
from urllib.parse import urlencode
from binance.lib.utils import cleanNoneValue
from binance.lib.utils import check_required_parameter
from binance.lib.utils import check_required_parameters

class API(object):
    def __init__(self, key=None, secrect=None, **kwargs):
        self.key = key
        self.secret = secrect
        self.baseUrl = 'https://api.binance.com'
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json;charset=utf-8',
            'User-Agent': 'binance-python/' + version.__version__
        })
        if self.key is not None:
            self.session.headers.update({'X-MBX-APIKEY': self.key})
        self.response = None

        self.show_weight_usage = False
        if 'show_weight_usage' in kwargs:
            self.show_weight_usage = kwargs['show_weight_usage'] and kwargs['show_weight_usage'] == True

        self.show_header = False
        if 'show_header' in kwargs:
            self.show_header = kwargs['show_header'] and kwargs['show_header'] == True

        return

    def _prepare_params(self, params):
        return urlencode(cleanNoneValue(params))

    def _query(self, urlPath, payload={}):
        url = self.baseUrl + urlPath
        response = self.session.get(url, params=payload)
        result = {}
        if (self.show_weight_usage):
            weight_usage = {}
            for key in response.headers.keys():
                if key.startswith('X-MBX-USED-WEIGHT'):
                    weight_usage[key] = response.headers[key]
                    result = {'data': response.json(), 'weight_usage': weight_usage }

        if (self.show_header):
            result['header'] = response.headers

        if (len(result) != 0):
            return result

        return response.json()
