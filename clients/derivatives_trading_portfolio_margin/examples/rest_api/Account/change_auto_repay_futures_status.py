import os
import logging

from binance_sdk_derivatives_trading_portfolio_margin.derivatives_trading_portfolio_margin import (
    DerivativesTradingPortfolioMargin,
    ConfigurationRestAPI,
    DERIVATIVES_TRADING_PORTFOLIO_MARGIN_REST_API_PROD_URL,
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


def change_auto_repay_futures_status():
    try:
        response = client.rest_api.change_auto_repay_futures_status(
            auto_repay="True",
        )

        rate_limits = response.rate_limits
        logging.info(f"change_auto_repay_futures_status() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"change_auto_repay_futures_status() response: {data}")
    except Exception as e:
        logging.error(f"change_auto_repay_futures_status() error: {e}")


if __name__ == "__main__":
    change_auto_repay_futures_status()
