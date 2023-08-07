import pytest

from binance.error import (
    ParameterRequiredError,
    ParameterTypeError,
    ParameterValueError,
)
from binance.lib.utils import (
    check_required_parameter,
    check_type_parameter,
    convert_list_to_json_array,
    purge_map,
    parse_proxies,
)
from binance.lib.utils import check_required_parameters
from binance.lib.utils import check_enum_parameter
from binance.lib.utils import encoded_string
from binance.lib.enums import TransferType


def test_pass_check_required_parameter():
    check_required_parameter.when.called_with("btcusdt", "symbol").should_not.throw(
        ParameterRequiredError
    )


def test_failed_when_required_parameter_is_none():
    check_required_parameter.when.called_with(None, "symbol").should.throw(
        ParameterRequiredError
    )


def test_failed_when_required_parameter_is_empty():
    check_required_parameter.when.called_with("", "symbol").should.throw(
        ParameterRequiredError
    )


def test_pass_check_required_parameters():
    check_required_parameters.when.called_with(
        [["btcusdt", "symbol"]]
    ).should_not.throw(ParameterRequiredError)


def test_pass_check_required_parameter_value_0():
    check_required_parameters.when.called_with(
        [[0, "transactionType"]]
    ).should_not.throw(ParameterRequiredError)


def test_pass_check_required_parameter_value_1():
    check_required_parameters.when.called_with(
        [[1, "transactionType"]]
    ).should_not.throw(ParameterRequiredError)


def test_pass_check_required_parameters_multi_params():
    check_required_parameters.when.called_with(
        [["btcusdt", "symbol"], [10, "price"]]
    ).should_not.throw(ParameterRequiredError)


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
    check_enum_parameter.when.called_with("MAIN_MARGIN", TransferType).should_not.throw(
        ParameterValueError
    )


def test_fail_check_enum_parameter():
    check_enum_parameter.when.called_with(
        "INVALID_ENUM_STRING", TransferType
    ).should.throw(ParameterValueError)


def test_pass_check_type_parameter():
    check_type_parameter.when.called_with([], "value", list).should_not.throw(
        ParameterTypeError
    )


def test_fail_check_type_parameter():
    check_type_parameter.when.called_with([], "value", dict).should.throw(
        ParameterTypeError
    )


def test_encode_query_string():
    encoded_string({"foo": "bar", "foo2": "bar2"}).should.equal("foo=bar&foo2=bar2")


def test_encode_query_without_email_symbol():
    encoded_string({"email": "alice@test.com"}).should.equal("email=alice@test.com")


def test_convert_list_to_json_array():
    convert_list_to_json_array(["symbol"]).should.equal('["symbol"]')


def test_remove_empty_parameter():
    purge_map({"foo": "bar", "foo2": None}).should.equal({"foo": "bar"})
    purge_map({"foo": "bar", "foo2": ""}).should.equal({"foo": "bar"})
    purge_map({"foo": "bar", "foo2": 0}).should.equal({"foo": "bar"})
    purge_map({"foo": "bar", "foo2": []}).should.equal({"foo": "bar", "foo2": []})
    purge_map({"foo": "bar", "foo2": {}}).should.equal({"foo": "bar", "foo2": {}})


def test_parse_proxies():
    proxies = {"http": "http://1.2.3.4:8080"}
    output = {
        "http_proxy_host": "1.2.3.4",
        "http_proxy_port": 8080,
        "http_proxy_auth": None,
    }

    proxy_data = parse_proxies(proxies)
    assert proxy_data == output

    proxies_2 = {"https": "http://1.2.3.4:8080"}

    proxy_data_2 = parse_proxies(proxies_2)
    assert proxy_data_2 == output


def test_parse_proxies_non_supported():
    proxies = {"socks5": "http://1.2.3.4:8080"}

    proxy_data = parse_proxies(proxies)
    assert proxy_data == {}


def test_parse_proxies_invalid():
    proxies = {"http": "http://x1.2.3.4.6-8080:x"}

    with pytest.raises(ValueError):
        parse_proxies(proxies)
