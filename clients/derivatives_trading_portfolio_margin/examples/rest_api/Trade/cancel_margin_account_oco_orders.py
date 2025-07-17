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


def cancel_margin_account_oco_orders():
    try:
        response = client.rest_api.cancel_margin_account_oco_orders(
            symbol="symbol_example",
        )

        rate_limits = response.rate_limits
        logging.info(f"cancel_margin_account_oco_orders() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"cancel_margin_account_oco_orders() response: {data}")
    except Exception as e:
        logging.error(f"cancel_margin_account_oco_orders() error: {e}")


if __name__ == "__main__":
    cancel_margin_account_oco_orders()
