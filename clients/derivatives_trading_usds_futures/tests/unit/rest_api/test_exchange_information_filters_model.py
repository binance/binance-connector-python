"""
Regression tests for the USDⓈ-M exchangeInfo symbol filter model.

Covers https://github.com/binance/binance-connector-python/issues/575: the
POSITION_RISK_CONTROL filter's positionControlSide field was not declared on
ExchangeInformationResponseSymbolsInnerFiltersInner and was therefore silently
sunk into additional_properties instead of being surfaced as a typed field.
"""

from binance_sdk_derivatives_trading_usds_futures.rest_api.models.exchange_information_response_symbols_inner_filters_inner import (
    ExchangeInformationResponseSymbolsInnerFiltersInner,
)


class TestPositionRiskControlFilter:
    def test_position_risk_control_filter_exposes_position_control_side(self):
        filter_dict = {
            "filterType": "POSITION_RISK_CONTROL",
            "positionControlSide": "NONE",
        }

        parsed = ExchangeInformationResponseSymbolsInnerFiltersInner.from_dict(
            filter_dict
        )

        assert parsed.position_control_side == "NONE"
        assert "positionControlSide" not in parsed.additional_properties
        assert parsed.to_dict()["positionControlSide"] == "NONE"

    def test_position_control_side_defaults_to_none_when_absent(self):
        filter_dict = {
            "filterType": "PRICE_FILTER",
            "maxPrice": "300",
        }

        parsed = ExchangeInformationResponseSymbolsInnerFiltersInner.from_dict(
            filter_dict
        )

        assert parsed.position_control_side is None
