import os
import logging

from binance_sdk_derivatives_trading_portfolio_margin.derivatives_trading_portfolio_margin import (
    DerivativesTradingPortfolioMargin,
    ConfigurationRestAPI,
    DERIVATIVES_TRADING_PORTFOLIO_MARGIN_REST_API_PROD_URL,
)
from binance_sdk_derivatives_trading_portfolio_margin.rest_api.models import (
    NewUmAlgoOrderAlgoTypeEnum,
)
from binance_sdk_derivatives_trading_portfolio_margin.rest_api.models import (
    NewUmAlgoOrderSideEnum,
)
from binance_sdk_derivatives_trading_portfolio_margin.rest_api.models import (
    NewUmAlgoOrderTypeEnum,
)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv(
        "BASE_PATH", DERIVATIVES_TRADING_PORTFOLIO_MARGIN_REST_API_PROD_URL
    ),
)

# Initialize DerivativesTradingPortfolioMargin client
client = DerivativesTradingPortfolioMargin(config_rest_api=configuration_rest_api)


def new_um_algo_order():
    try:
        response = client.rest_api.new_um_algo_order(
            algo_type=NewUmAlgoOrderAlgoTypeEnum["CONDITIONAL"].value,
            symbol="BNBUSDT",
            side=NewUmAlgoOrderSideEnum["SELL"].value,
            type=NewUmAlgoOrderTypeEnum["TAKE_PROFIT"].value,
            quantity=0.01,
        )

        rate_limits = response.rate_limits
        logging.info(f"new_um_algo_order() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"new_um_algo_order() response: {data}")
    except Exception as e:
        logging.error(f"new_um_algo_order() error: {e}")


if __name__ == "__main__":
    new_um_algo_order()
