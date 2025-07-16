from typing import List, Optional, Callable, TypeVar, Generic
from pydantic import BaseModel

T = TypeVar("T")


class RateLimit(BaseModel):
    """Represents a single rate limit entry.

    :param rateLimitType: The type of the rate limit (e.g., 'REQUEST_WEIGHT', 'ORDERS').
    :param interval: The time interval (e.g., 'SECOND', 'MINUTE', 'HOUR', 'DAY').
    :param intervalNum: The interval number (e.g., 1, 10, etc.).
    :param count: The number of requests/orders used in the interval.
    :param retryAfter: Optional retry time in seconds if rate-limited.
    """

    rateLimitType: str
    interval: str
    intervalNum: int
    count: int
    retryAfter: Optional[int]


class ApiResponse(Generic[T]):
    """A wrapper for API responses that includes parsed data and rate limit headers.

    :param data_function: A callable that lazily returns the parsed data of type T.
    :param status: The HTTP status code of the response.
    :param headers: A dictionary of response headers.
    :param rate_limits: A list of rate limit headers parsed from the response.
    """

    def __init__(
        self,
        data_function: Callable[[], T],
        status: int,
        headers: dict,
        rate_limits: List[RateLimit] = None,
    ):
        self._data_function = data_function
        self.status = status
        self.headers = headers or {}
        self.rate_limits = rate_limits or []

    def data(self) -> T:
        """Lazily retrieves the response data.

        :return: The parsed data of type T.
        """
        return self._data_function()


class WebsocketApiRateLimit(BaseModel):
    """Represents a single rate limit entry for WebSocket API.

    :param rateLimitType: The type of the rate limit (e.g., 'REQUEST_WEIGHT', 'ORDERS').
    :param interval: The time interval (e.g., 'SECOND', 'MINUTE', 'HOUR', 'DAY').
    :param intervalNum: The number of intervals for the rate limit.
    :param limit: The maximum number of requests or orders allowed within the specified interval.
    :param count: The current count of requests or orders for the rate limit.
    """

    rateLimitType: str
    interval: str
    intervalNum: int
    limit: int
    count: int = 0


class WebsocketApiResponse(Generic[T]):
    """A wrapper for WebSocket API responses that includes parsed data and rate limit headers.

    :param data_function: A callable that lazily returns the parsed data of type T.
    :param status: The HTTP status code of the response.
    :param headers: A dictionary of response headers.
    :param rate_limits: A list of rate limit headers parsed from the response.
    """

    def __init__(
        self,
        data_function: T = None,
        rate_limits: List[WebsocketApiRateLimit] = None,
    ):
        self._data_function = data_function
        self.rate_limits = rate_limits or []

    def data(self) -> T:
        """Lazily retrieves the response data.

        :return: The parsed data of type T.
        """
        return self._data_function()
