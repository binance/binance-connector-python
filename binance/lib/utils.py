from binance.error import ParameterRequiredError

def cleanNoneValue(d) -> dict:
    out = {}
    for k in d.keys():
        if d[k] is not None:
            out[k] = d[k]
    return out

def check_required_parameter(value, name):
    if value is None or value is '':
        raise ParameterRequiredError([name])

def check_required_parameters(params):
    """ validate multipul parameters
        params = [
            ['btcusdt', 'symbol'],
            [10, 'price']
        ]

    """
    for p in params:
        check_required_parameter(p[0], p[1])
