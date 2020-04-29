class BinanceException(Exception):
    pass

class APIException(BinanceException):
    def __init__(self, status_code, code, message):
        self.status_code = status_code
        self.code = code
        self.message = message

class ServerException(BinanceException):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.code = None
        self.message = message

class ParameterRequiredError(BinanceException):
    def __init__(self, params):
        self.params = params

    def __str__(self):
        return '%s is mandatory, but received empty.' % (', '.join(self.params))
