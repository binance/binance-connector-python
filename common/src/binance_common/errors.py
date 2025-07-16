from typing import Optional


class Error(Exception):
    pass


class ClientError(Error):
    """Represents an error that occurred in the Connector client."""

    def __init__(self, error_message: Optional[str] = None):
        self.error_message = error_message or "An unexpected error occurred."
        super().__init__(error_message)


class RequiredError(Error):
    """Represents an error when a required parameter is missing or undefined."""

    def __init__(self, field: str, error_message: Optional[str] = None):
        self.error_message = (
            error_message or f"Required parameter {field} was null or undefined."
        )
        self.field = field
        super().__init__(error_message)


class UnauthorizedError(Error):
    """Represents an error when a client is unauthorized to access a resource."""

    def __init__(self, error_message: Optional[str] = None):
        self.error_message = (
            error_message or "Unauthorized access. Authentication required."
        )
        super().__init__(error_message)


class ForbiddenError(Error):
    """Represents an error when access to the resource is forbidden."""

    def __init__(self, error_message: Optional[str] = None):
        self.error_message = (
            error_message or "Access to the requested resource is forbidden."
        )
        super().__init__(error_message)


class TooManyRequestsError(Error):
    """Represents an error when the client is doing too many requests."""

    def __init__(self, error_message: Optional[str] = None):
        self.error_message = (
            error_message or "Too many requests. You are being rate-limited."
        )
        super().__init__(error_message)


class RateLimitBanError(Error):
    """Represents an error when the client's IP has been banned for exceeding rate
    limits."""

    def __init__(self, error_message: Optional[str] = None):
        self.error_message = (
            error_message or "The IP address has been banned for exceeding rate limits."
        )
        super().__init__(error_message)


class ServerError(Error):
    """Represents an error when there is an internal server error."""

    def __init__(
        self,
        error_message: Optional[str] = None,
        status_code: Optional[int] = None,
    ):
        self.error_message = error_message or "An internal server error occurred."
        self.status_code = status_code
        super().__init__(error_message)


class NetworkError(Error):
    """Represents an error when a network error occurs."""

    def __init__(self, error_message: Optional[str] = None):
        self.error_message = error_message or "A network error occurred."
        super().__init__(error_message)


class NotFoundError(Error):
    """Represents an error when the requested resource was not found."""

    def __init__(self, error_message: Optional[str] = None):
        self.error_message = error_message or "The requested resource was not found."
        super().__init__(error_message)


class BadRequestError(Error):
    """Represents an error when a request is invalid or cannot be otherwise served."""

    def __init__(self, error_message: Optional[str] = None):
        self.error_message = (
            error_message or "The request was invalid or cannot be otherwise served."
        )
        super().__init__(self.error_message)
