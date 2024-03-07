import json
import time
import uuid

from urllib.parse import urlparse
from collections import OrderedDict
from urllib.parse import urlencode
from binance.lib.authentication import hmac_hashing
from binance.error import (
    ParameterRequiredError,
    ParameterValueError,
    ParameterTypeError,
    WebsocketClientError,
)


def cleanNoneValue(d) -> dict:
    out = {}
    for k in d.keys():
        if d[k] is not None:
            out[k] = d[k]
    return out


def check_required_parameter(value, name):
    if not value and value != 0:
        raise ParameterRequiredError([name])


def check_required_parameters(params):
    """Validate multiple parameters
    params = [
        ['btcusdt', 'symbol'],
        [10, 'price']
    ]

    """
    for p in params:
        check_required_parameter(p[0], p[1])


def check_enum_parameter(value, enum_class):
    if value not in set(item.value for item in enum_class):
        raise ParameterValueError([value])


def check_type_parameter(value, name, data_type):
    if value is not None and not isinstance(value, data_type):
        raise ParameterTypeError([name, data_type])


def get_timestamp():
    return int(time.time() * 1000)


def encoded_string(query):
    return urlencode(query, True).replace("%40", "@")


def convert_list_to_json_array(symbols):
    if symbols is None:
        return symbols
    res = json.dumps(symbols)
    return res.replace(" ", "")


def config_logging(logging, logging_level, log_file: str = None):
    """Configures logging to provide a more detailed log format, which includes date time in UTC
    Example: 2021-11-02 19:42:04.849 UTC <logging_level> <log_name>: <log_message>

    Args:
        logging: python logging
        logging_level (int/str): For logging to include all messages with log levels >= logging_level. Ex: 10 or "DEBUG"
                                 logging level should be based on https://docs.python.org/3/library/logging.html#logging-levels
    Keyword Args:
        log_file (str, optional): The filename to pass the logging to a file, instead of using console. Default filemode: "a"
    """

    logging.Formatter.converter = time.gmtime  # date time in GMT/UTC
    logging.basicConfig(
        level=logging_level,
        filename=log_file,
        format="%(asctime)s.%(msecs)03d UTC %(levelname)s %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def get_uuid():
    return str(uuid.uuid4())


def purge_map(map: map):
    """Remove None values from map"""
    return {k: v for k, v in map.items() if v is not None and v != "" and v != 0}


def websocket_api_signature(api_key: str, api_secret: str, parameters: dict):
    """Generate signature for websocket API
    Args:
        api_key (str): API key.
        api_secret (str): API secret.
        params (dict): Parameters.
    """

    if not api_key or not api_secret:
        raise WebsocketClientError(
            "api_key and api_secret are required for websocket API signature"
        )

    parameters["timestamp"] = get_timestamp()
    parameters["apiKey"] = api_key

    parameters = OrderedDict(sorted(parameters.items()))
    parameters["signature"] = hmac_hashing(api_secret, urlencode(parameters))

    return parameters


def parse_proxies(proxies: dict):
    """Parse proxy url from dict, only support http and https proxy, not support socks5 proxy"""
    proxy_url = proxies.get("http") or proxies.get("https")
    if not proxy_url:
        return {}

    parsed = urlparse(proxy_url)
    return {
        "http_proxy_host": parsed.hostname,
        "http_proxy_port": parsed.port,
        "http_proxy_auth": (
            (parsed.username, parsed.password)
            if parsed.username and parsed.password
            else None
        ),
    }
