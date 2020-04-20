class BinanceError(Exception):
    pass

class ParameterRequiredError(BinanceError):

    def __init__(self, params):
        self.params = params

    def __str__(self):
        return '%s is mandatory, but received empty.' % (', '.join(self.params))
