import re
import uuid
import time
import random
import responses


def mock_http_response(
    method, uri, response_data, http_status=200, headers=None, body_data=""
):
    if headers is None:
        headers = {}

    def decorator(fn):
        @responses.activate
        def wrapper(*args, **kwargs):
            responses.add(
                method,
                re.compile(".*" + uri),
                json=response_data,
                body=body_data,
                status=http_status,
                headers=headers,
            )
            return fn(*args, **kwargs)

        return wrapper

    return decorator


def random_id() -> int:
    return random.randint(1, 10000)


def random_str() -> str:
    return uuid.uuid4().hex


def current_timestamp() -> int:
    return int(round(time.time() * 1000))


def timestamp(in_future: int = 0) -> int:
    return current_timestamp() + in_future
