import os
import logging

from binance_sdk_derivatives_trading_portfolio_margin_pro.derivatives_trading_portfolio_margin_pro import (
    DerivativesTradingPortfolioMarginPro,
    ConfigurationRestAPI,
    DERIVATIVES_TRADING_PORTFOLIO_MARGIN_PRO_REST_API_PROD_URL,
)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv(
        "BASE_PATH", DERIVATIVES_TRADING_PORTFOLIO_MARGIN_PRO_REST_API_PROD_URL
    ),
)

# Initialize DerivativesTradingPortfolioMarginPro client
client = DerivativesTradingPortfolioMarginPro(config_rest_api=configuration_rest_api)


def portfolio_margin_pro_tiered_collateral_rate():
    try:
        response = client.rest_api.portfolio_margin_pro_tiered_collateral_rate()

        rate_limits = response.rate_limits
        logging.info(
            f"portfolio_margin_pro_tiered_collateral_rate() rate limits: {rate_limits}"
        )

        data = response.data()
        logging.info(f"portfolio_margin_pro_tiered_collateral_rate() response: {data}")
    except Exception as e:
        logging.error(f"portfolio_margin_pro_tiered_collateral_rate() error: {e}")


if __name__ == "__main__":
    portfolio_margin_pro_tiered_collateral_rate()
