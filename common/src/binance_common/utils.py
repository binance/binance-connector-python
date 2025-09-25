import copy
import hashlib
import hmac
import importlib
import json
import re
import requests
import requests.adapters
import ssl
import time
import uuid

from base64 import b64encode
from collections import OrderedDict
from Crypto.Hash import SHA256
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from enum import Enum
from pydantic import BaseModel
from typing import Dict, List, Optional, Type, TypeVar, Union, get_args
from urllib.parse import urlencode
from urllib3.util.ssl_ import create_urllib3_context

from binance_common.configuration import ConfigurationRestAPI, ConfigurationWebSocketAPI
from binance_common.constants import TimeUnit
from binance_common.errors import (
    BadRequestError,
    ClientError,
    ForbiddenError,
    NetworkError,
    NotFoundError,
    RateLimitBanError,
    ServerError,
    TooManyRequestsError,
    UnauthorizedError,
)
from binance_common.models import (
    ApiResponse,
    RateLimit,
    WebsocketApiOptions,
    WebsocketApiRateLimit
)
from binance_common.signature import Signers


T = TypeVar("T", bound=BaseModel)


class CustomHTTPSAdapter(requests.adapters.HTTPAdapter):
    """A custom HTTPS adapter that supports SSLContext (including certificate pinning)."""

    def __init__(self, ssl_context: ssl.SSLContext = None, **kwargs):
        self.ssl_context = ssl_context or create_urllib3_context()
        super().__init__(**kwargs)

    def init_poolmanager(self, *args, **kwargs):
        """Initialize the connection pool with custom SSL context."""
        kwargs["ssl_context"] = self.ssl_context
        super().init_poolmanager(*args, **kwargs)

    def proxy_manager_for(self, *args, **kwargs):
        """Ensure proxy support is also handled with the SSL context."""
        kwargs["ssl_context"] = self.ssl_context
        return super().proxy_manager_for(*args, **kwargs)


def hmac_hashing(api_secret: str, payload: str) -> str:
    """Generates an HMAC-SHA256 hash of the provided payload using the given API secret.

    Args:
        api_secret (str): The API secret to use for the HMAC-SHA256 hashing.
        payload (str): The payload to hash.

    Returns:
        str: The hexadecimal HMAC-SHA256 hash of the payload.
    """

    m = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), hashlib.sha256)
    return m.hexdigest()


def clean_none_value(d: dict) -> dict:
    """Removes any `None` values from the input dictionary `d` and returns a new
    dictionary with only non-`None` values.

    Args:
        d (dict): The input dictionary to clean.

    Returns:
        dict: A new dictionary with only non-`None` values from the input dictionary.
    """

    if isinstance(d, Enum):
        return d.value
    elif isinstance(d, dict):
        out = {}
        for k, v in d.items():
            cleaned = clean_none_value(v)
            if cleaned not in (None, {}, []):
                out[k] = cleaned
        return out
    elif isinstance(d, list):
        out_list = []
        for item in d:
            cleaned_item = clean_none_value(item)
            if cleaned_item not in (None, {}, []):
                out_list.append(cleaned_item)
        return out_list
    elif hasattr(d, "__dict__"):
        return clean_none_value(d.__dict__)
    else:
        return d


def get_timestamp() -> int:
    """Returns the current timestamp in milliseconds."""

    return int(time.time() * 1000)


def snake_to_camel(snake_str: str) -> str:
    """Converts a snake_case string to camelCase.

    Args:
        snake_str (str): The snake_case string to convert.
    Returns:
        str: The converted camelCase string.
    """

    parts = snake_str.split("_")
    return parts[0] + "".join(word.capitalize() for word in parts[1:])


def make_serializable(val) -> Union[dict, list, str, int, float, bool]:
    """Converts a value to a serializable format.

    Args:
        val: The value to convert.
    Returns:
        The converted value, which can be a dictionary, list, or the original value if it is already serializable.
    """

    if isinstance(val, list):
        return [v.__dict__ if hasattr(v, "__dict__") else v for v in val]
    if isinstance(val, bool):
        return str(val).lower()
    if isinstance(val, float):
        return str(val)
    if isinstance(val, Enum):
        return val.value
    if hasattr(val, "__dict__"):
        return transform_query(val.__dict__)
    return val


def transform_query(data: Union[dict, list, str, int, float, bool]) -> Union[dict, list, str, int, float, bool]:
    """Recursively transform keys to camelCase and values to serializable.

    Args:
        data (Union[dict, list, str, int, float, bool]): The data to transform.
    Returns:
        Union[dict, list, str, int, float, bool]: The transformed data.
    """

    if isinstance(data, dict):
        return {
            snake_to_camel(k): transform_query(v)
            for k, v in data.items()
        }
    elif isinstance(data, list):
        return [transform_query(v) for v in data]
    else:
        return make_serializable(data)


def encoded_string(query: str) -> str:
    """Encodes the given query string.

    Args:
        query (str): The query string to encode.

    Returns:
        str: The encoded query string.
    """

    query = transform_query(query)
    query = {
        snake_to_camel(k): json.dumps(make_serializable(v), separators=(",", ":")) if isinstance(v, (dict, list)) else make_serializable(v)
        for k, v in query.items()
    }
    return urlencode(query, True)


def is_one_of_model(model_cls: Type[BaseModel]) -> bool:
    """Checks if the given model class is a one-of model.

    Args:
        model_cls (Type[BaseModel]): The model class to check.
    Returns:
        bool: True if the model class is a one-of model, False otherwise.
    """

    return (hasattr(model_cls, "is_oneof_model") and model_cls.is_oneof_model())


def get_uuid() -> str:
    """Returns a new universally unique identifier (UUID) as a string."""

    return str(uuid.uuid4())


def validate_time_unit(time_unit: Optional[str]) -> Optional[str]:
    """Validates the time unit against the defined TimeUnit constants.

    :param time_unit: The time unit to validate.
    :return: The validated time unit if valid, or None if time_unit is None.
    :raises ValueError: If the time unit is not valid.
    """

    if time_unit is None:
        return None

    if time_unit not in TimeUnit._value2member_map_:
        valid_values = ", ".join(TimeUnit._value2member_map_.keys())
        raise ValueError(f"time_unit must be one of {valid_values}")

    return time_unit


def get_signature(
    configuration: Union[ConfigurationWebSocketAPI, ConfigurationRestAPI], payload: dict, signer: Optional[Signers] = None
) -> str:
    if configuration.api_secret:
        return hmac_hashing(configuration.api_secret, payload)
    elif configuration.private_key:
        if not signer:
            raise ValueError("Signer must be provided when using private_key for signing.")
        elif isinstance(signer, PKCS115_SigScheme):
            digest = SHA256.new(payload.encode("utf-8"))
            return b64encode(signer.sign(digest)).decode("utf-8")
        else:
            return b64encode(signer.sign(payload.encode("utf-8"))).decode("utf-8")
    else:
        raise ValueError(
            "Either 'api_secret' or 'private_key' must be provided for signed requests."
        )


def should_retry_request(error, method: str = None, retries_left: int = None) -> bool:
    """Determines whether a request should be retried based on the error.

    :param error: The error object to check.
    :param method: The HTTP method of the request (optional).
    :param retries_left: The number of retries left (optional).
    :return: True if the request should be retried, False otherwise.
    """

    retriable_methods = ["GET", "DELETE"]
    retriable_status_codes = [500, 502, 503, 504]

    if retries_left is None or retries_left <= 0:
        return False

    if method is None or method.upper() not in retriable_methods:
        return False

    if not hasattr(error, "response") or error.response is None:
        return True

    status = getattr(error.response, "status_code", 0)
    return status in retriable_status_codes


def send_request(
    session: requests.Session,
    configuration: ConfigurationRestAPI,
    method: str,
    path: str,
    payload: Optional[dict] = None,
    time_unit: Optional[str] = None,
    response_model: Type[T] = None,
    is_signed: bool = False,
    signer: Optional[Signers]=None
) -> ApiResponse[T]:
    """Sends an HTTP request with the specified configuration, method, path, and
    optional payload and time unit.

    The `send_request` function is responsible for sending an HTTP request with the provided parameters. It handles retries, error handling, and response processing. The function takes the following parameters:

    - `configuration`: The configuration object containing the necessary information for sending the request.
    - `method`: The HTTP method to use (e.g. "GET", "POST", etc.).
    - `path`: The API endpoint path.
    - `payload`: The request payload (optional).
    - `time_unit`: The time unit for the `X-MBX-TIME-UNIT` header (optional).
    - `response_model`: The response model to use for deserializing the response (optional).
    - `is_signed`: A boolean indicating whether the request should be signed (optional).

    The function returns the JSON response from the server, or raises an appropriate exception if an error occurs.
    """

    if payload is None:
        payload = {}

    if is_signed:
        cleaned_payload = clean_none_value(payload)
        cleaned_payload["timestamp"] = get_timestamp()
        query_string = encoded_string(cleaned_payload)
        cleaned_payload["signature"] = get_signature(configuration, query_string, signer)
        payload = cleaned_payload

    headers = configuration.base_headers.copy()

    if time_unit:
        headers["X-MBX-TIME-UNIT"] = time_unit

    if configuration.compression:
        headers["Accept-Encoding"] = "gzip, deflate, br"

    url = f"{configuration.base_path}{path}"
    retries = configuration.retries if configuration else 0
    backoff = configuration.backoff if configuration else 1
    timeout = configuration.timeout / 1000 if configuration else 10
    proxies = (
        parse_proxies(configuration.proxy)
        if configuration and configuration.proxy
        else None
    )

    if configuration.https_agent:
        if isinstance(configuration.https_agent, ssl.SSLContext):
            https_adapter = CustomHTTPSAdapter(configuration.https_agent)
        else:
            https_adapter = requests.adapters.HTTPAdapter()
        session.mount("https://", https_adapter)
        session.mount("http://", https_adapter)

    if not configuration.keep_alive:
        headers["Connection"] = "close"

    attempt = 0

    while attempt <= retries:
        try:
            response = session.request(
                method=method,
                url=url,
                params=encoded_string(clean_none_value(payload)),
                headers=headers,
                timeout=timeout,
                proxies=proxies,
            )

            if response.status_code >= 400:
                status = response.status_code
                data = (
                    response.json()
                    if response.headers.get("Content-Type").startswith(
                        "application/json"
                    )
                    else {}
                )

                if status == 400:
                    raise BadRequestError(error_message=data.get("msg"))
                elif status == 401:
                    raise UnauthorizedError(error_message=data.get("msg"))
                elif status == 403:
                    raise ForbiddenError(error_message=data.get("msg"))
                elif status == 404:
                    raise NotFoundError(error_message=data.get("msg"))
                elif status == 418:
                    raise RateLimitBanError(error_message=data.get("msg"))
                elif status == 429:
                    raise TooManyRequestsError(error_message=data.get("msg"))
                elif 500 <= status < 600:
                    raise ServerError(
                        error_message=f"Server error: {status}", status_code=status
                    )
                else:
                    raise ClientError(error_message=data.get("msg"))

            parsed = json.loads(response.text)
            is_list = isinstance(parsed, list)
            is_oneof = is_one_of_model(response_model)
            is_flat_list = is_list and (
                len(parsed) == 0 or
                (not isinstance(parsed[0], list) if is_list else False)
            )
            if (is_list and not is_flat_list) or not response_model:
                data_function = lambda: parsed
            elif is_oneof or is_list:
                data_function = lambda: response_model.from_dict(parsed)
            else:
                data_function = lambda: response_model.model_validate(parsed)

            try:
                data_function()  
                final_data_function = data_function
            except Exception:
                final_data_function = lambda: parsed

            return ApiResponse[T](
                data_function=final_data_function,
                status=response.status_code,
                headers=response.headers,
                rate_limits=parse_rate_limit_headers(response.headers),
            )
        except requests.RequestException as e:
            attempt += 1

            if should_retry_request(e, method, retries - attempt):
                time.sleep(backoff * attempt)
            else:
                raise NetworkError(error_message=f"Network error: {str(e)}") from e

    raise Exception(f"Request failed after {retries} retries.")


def parse_rate_limit_headers(headers: Dict[str, str]) -> List[RateLimit]:
    """Parses rate limit headers from the response headers.

    :param headers: The response headers.
    :return: A list of RateLimit objects.
    """
    rate_limits: List[RateLimit] = []

    def parse_interval_details(key: str) -> Optional[Dict[str, Union[str,int]]]:
        """Parses interval details from a header key.

        :param key: The header key to parse.
        :return: A dictionary with interval and intervalNum, or None if not matched.
        """
        match = re.match(
            r"x-mbx-used-weight-(\d+)([smhd])|x-mbx-order-count-(\d+)([smhd])",
            key,
            re.IGNORECASE,
        )
        if not match:
            return None

        interval_num = int(match.group(1) or match.group(3))
        interval_letter = (match.group(2) or match.group(4)).upper()

        interval_map = {
            "S": "SECOND",
            "M": "MINUTE",
            "H": "HOUR",
            "D": "DAY",
        }
        interval = interval_map.get(interval_letter)

        if not interval:
            return None

        return {"interval": interval, "intervalNum": interval_num}

    for key, value in headers.items():
        normalized_key = key.lower()
        if value is None:
            continue

        if normalized_key.startswith("x-mbx-used-weight-"):
            details = parse_interval_details(normalized_key)
            if details:
                rate_limits.append(
                    RateLimit(
                        rateLimitType="REQUEST_WEIGHT",
                        interval=details["interval"],
                        intervalNum=details["intervalNum"],
                        count=int(value),
                        retryAfter=None,
                    )
                )
        elif normalized_key.startswith("x-mbx-order-count-"):
            details = parse_interval_details(normalized_key)
            if details:
                rate_limits.append(
                    RateLimit(
                        rateLimitType="ORDERS",
                        interval=details["interval"],
                        intervalNum=details["intervalNum"],
                        count=int(value),
                        retryAfter=None,
                    )
                )

    retry_after = headers.get("retry-after")
    if retry_after:
        retry_after_seconds = int(retry_after)
        for limit in rate_limits:
            limit.retryAfter = retry_after_seconds

    return rate_limits


def parse_proxies(
    proxy: Optional[Dict[str, Union[str, int, Dict[str, str]]]],
) -> Optional[Dict[str, str]]:
    """Parses proxy settings and returns a `requests`-compatible format.

    Args:
        proxy (Optional[Dict[str, Union[str, int, Dict[str, str]]]]): Proxy configuration dictionary.

    Returns:
        Optional[Dict[str, str]]: A dictionary with formatted proxy URLs for HTTP and HTTPS.
    """
    if not proxy:
        return None

    protocol = proxy.get("protocol", "https")
    host = proxy.get("host", "")
    port = proxy.get("port", "")

    if "auth" in proxy:
        username = proxy["auth"].get("username", "")
        password = proxy["auth"].get("password", "")
        proxy_url = f"{protocol}://{username}:{password}@{host}:{port}"
    else:
        proxy_url = f"{protocol}://{host}:{port}"

    return {"https": proxy_url, "http": proxy_url}


def ws_streams_placeholder(stream: str, params: dict = {}) -> str:
    """Replaces placeholders in the stream string with values from the params dictionary.

    Args:
        stream (str): The stream string with placeholders.
        params (dict): A dictionary containing values to replace the placeholders.

    Returns:
        str: The stream string with placeholders replaced by actual values.
    """
    params = {k: v for k, v in params.items() if v is not None}

    normalized_variables = {
        re.sub(r"[-_]", "", key.lower()): value for key, value in params.items()
    }

    return re.sub(
        r"(@)?<([^>]+)>",
        lambda m: (
            (
                lambda nf, v=normalized_variables: (
                    (
                        str(v[nf]).lower()
                        if nf in ("symbol", "windowsize")
                        else (
                            f"@{v[nf]}"
                            if nf == "updatespeed"
                            else (m.group(1) or "") + str(v[nf])
                        )
                    )
                    if nf in v and v[nf] is not None
                    else ""
                )
            )(re.sub(r"[-_]", "", m.group(2).lower()))
        ),
        stream,
    )


def parse_ws_rate_limit_headers(
    headers: List[Dict[str, Union[str, int]]],
) -> List[WebsocketApiRateLimit]:
    """Parses WebSocket API rate limit headers from the response headers.

    Args:
        headers (List[Dict[str, Union[str, int]]]): A list of dictionaries representing the rate limit headers.

    Returns:
        List[WebsocketApiRateLimit]: A list of WebsocketApiRateLimit objects parsed from the headers.
    """
    rate_limits: List[WebsocketApiRateLimit] = []
    for header in headers:
        rate_limits.append(WebsocketApiRateLimit(**header))
    return rate_limits


def normalize_query_values(parsed, expected_types=None):
    """Normalizes the values in a parsed query dictionary.

    Args:
        parsed (dict): The parsed query dictionary with string values.
        expected_types (dict, optional): A dictionary specifying the expected types for each key.

    Returns:
        dict: A new dictionary with normalized values.
    """
    def convert(val, expected_type=None):
        val_stripped = val.strip()
        if expected_type:
            if expected_type == bool:
                return val_stripped.lower() == "true"
            elif expected_type == int:
                return int(val_stripped)
            elif expected_type == float:
                return float(val_stripped)
            elif expected_type == str:
                return val_stripped
        val_lower = val_stripped.lower()
        if val_lower == "true":
            return True
        elif val_lower == "false":
            return False
        try:
            return int(val_stripped)
        except ValueError:
            try:
                return float(val_stripped)
            except ValueError:
                return val_stripped

    normalized = {}
    for k, vs in parsed.items():
        ref = expected_types.get(k) if expected_types else None
        converted = [convert(v, type(ref)) for v in vs]
        normalized[k] = converted[0] if len(converted) == 1 else converted

    return normalized


def ws_api_payload(config, payload: Dict, websocket_options: WebsocketApiOptions):
    """Generate payload for websocket API

    Args:
        config: The API configuration.
        payload (Dict): The payload to send.
        websocket_options (WebsocketApiOptions): The WebSocket API options.

    Returns:
        Dict: The generated payload for the WebSocket API.
    """

    payload = copy.copy(payload)

    if websocket_options.api_key and websocket_options.skip_auth is False:
        payload["params"]["apiKey"] = config.api_key

    payload["id"] = payload["id"] if "id" in payload else get_uuid()

    payload["params"] = {
        snake_to_camel(k): json.dumps(make_serializable(v), separators=(",", ":"))
        if isinstance(v, (list, dict))
        else make_serializable(v)
        for k, v in payload["params"].items()
    }

    if websocket_options.is_signed:
        if websocket_options.skip_auth is True:
            payload["params"]["timestamp"] = get_timestamp()
        else:
            payload["params"] = websocket_api_signature(config, payload["params"], websocket_options.signer)

    return payload


def websocket_api_signature(config, payload: Optional[Dict] = {}, signer: Signers = None) -> dict:
    """Generate signature for websocket API

    Args:
        payload (Optional[Dict]): Payload.
        signer (Signers): Signer for the payload.
    Returns:
        dict: The generated signature for the WebSocket API.
    """

    payload["apiKey"] = config.api_key
    payload["timestamp"] = get_timestamp()
    parameters = OrderedDict(sorted(payload.items()))
    parameters["signature"] = get_signature(
        config, urlencode(parameters), signer
    )
    return parameters


def get_validator_field_map(response_model_cls: Type[BaseModel]) -> dict[str, str]:
    """Map User Data response schema class name to oneof_schema_N_validator field dynamically

    Args:
        response_model_cls (Type[BaseModel]): The response model class.

    Returns:
        dict[str, str]: The mapping of field names to validator field names.
    """

    field_map = {}
    annotations = getattr(response_model_cls, "__annotations__", {})

    for field_name, annotation in annotations.items():
        if field_name.startswith("oneof_schema_") and field_name.endswith("_validator"):
            if getattr(annotation, "__origin__", None) is Union:
                type_ = next((arg for arg in get_args(annotation) if arg is not type(None)), None)
            else:
                type_ = annotation
            if isinstance(type_, str):
                type_ = re.sub(r'^Optional\[(.*)\]$', r'\1', type_)

            if type_:
                field_map[type_] = field_name

    return field_map


def resolve_model_from_event(response_model_cls: Type[BaseModel], event_name: str) -> Type[BaseModel]:
    """Resolve the correct model class for the websocket event dynamically.

    Args:
        response_model_cls (Type[BaseModel]): The response model class.
        event_name (str): The name of the event.

    Returns:
        Type[BaseModel]: The resolved model class or None.
    """

    if not event_name:
        return None

    one_of_schemas_field = response_model_cls.__pydantic_fields__.get("one_of_schemas")
    if not one_of_schemas_field:
        return None

    one_of_schemas = list(one_of_schemas_field.default)
    event_to_class_map = {name[0].lower() + name[1:]: name for name in one_of_schemas}

    class_name = event_to_class_map.get(event_name)
    if not class_name:
        return None

    module = importlib.import_module(response_model_cls.__module__)
    return getattr(module, class_name, None)


def parse_user_event(payload: dict, response_model_cls: Type[BaseModel]) -> BaseModel:
    """Parse user event to response model.

    Args:
        payload (dict): The payload dictionary containing event data.
        response_model_cls (Type[BaseModel]): The response model class.

    Returns:
        BaseModel: The parsed response model instance.
    """

    event_name = payload.get("e")
    model_cls = resolve_model_from_event(response_model_cls, event_name)

    if not model_cls:
        return response_model_cls(actual_instance=payload)

    try:
        instance = model_cls.model_validate(payload)
        validator_field_map = get_validator_field_map(response_model_cls)
        kwargs = {"actual_instance": instance}
        if validator_field := validator_field_map.get(model_cls.__name__):
            kwargs[validator_field] = instance
        return response_model_cls(**kwargs)

    except Exception as e:
        print(f"Failed to parse {event_name}: {e}")
        return response_model_cls(actual_instance=payload)
