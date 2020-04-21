import re
import time
import random
import responses

def mock_http_response(method, uri, response_data, http_status=200):

    def decorator(fn):

        @responses.activate
        def wrapper(*args, **kwargs):
            responses.add(
                method,
                re.compile('.*' + uri + '$'),
                json=response_data,
                status=http_status
            )
            return fn(*args, **kwargs)
        return wrapper
    return decorator

def random_id() -> int:
    return random.randint(1, 10000)

def current_timestamp():
    return int(round(time.time() * 1000))

def timestamp(in_future: int = 0):
    return current_timestamp() + in_future
