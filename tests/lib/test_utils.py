from binance.error import ParameterRequiredError
from binance.error import ParameterValueError
from binance.lib.utils import check_required_parameter
from binance.lib.utils import check_required_parameters
from binance.lib.utils import check_enum_parameter
from binance.lib.utils import encoded_string
from binance.lib.enums import TransferType


def test_pass_check_required_parameter():
    check_required_parameter("btcusdt", "symbol")


def test_failed_when_required_parameter_is_none():
    check_required_parameter.when.called_with(None, "symbol").should.throw(
        ParameterRequiredError
    )


def test_failed_when_required_parameter_is_empty():
    check_required_parameter.when.called_with("", "symbol").should.throw(
        ParameterRequiredError
    )


def test_pass_check_required_parameters():
    check_required_parameters([["btcusdt", "symbol"]])


def test_pass_check_required_parameters_multi_params():
    check_required_parameters([["btcusdt", "symbol"], [10, "price"]])


def test_fail_check_required_parameters_single_param():
    check_required_parameters.when.called_with([["", "symbol"]]).should.throw(
        ParameterRequiredError
    )
    check_required_parameters.when.called_with([[None, "symbol"]]).should.throw(
        ParameterRequiredError
    )


def test_fail_check_required_parameters_multi_params():
    check_required_parameters.when.called_with(
        [["btcusdt", "symbol"], [None, "price"]]
    ).should.throw(ParameterRequiredError)
    check_required_parameters.when.called_with(
        [["", "symbol"], [10, "price"]]
    ).should.throw(ParameterRequiredError)


def test_pass_check_enum_parameter():
    check_enum_parameter("MAIN_MARGIN", TransferType)


def test_fail_check_enum_parameter():
    check_enum_parameter.when.called_with(
        "INVALID_ENUM_STRING", TransferType
    ).should.throw(ParameterValueError)


def test_encode_query_string():
    encoded_string({"foo": "bar", "foo2": "bar2"}).should.equal("foo=bar&foo2=bar2")


def test_encode_query_without_email_symbol():
    encoded_string({"email": "alice@test.com"}).should.equal("email=alice@test.com")
