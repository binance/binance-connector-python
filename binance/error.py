class Error(Exception):
    pass


class ClientError(Error):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message


class ServerError(Error):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.code = None
        self.message = message


class ParameterRequiredError(Error):
    def __init__(self, params):
        self.params = params

    def __str__(self):
        return '%s is mandatory, but received empty.' % (
            ', '.join(self.params))
