import re
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
