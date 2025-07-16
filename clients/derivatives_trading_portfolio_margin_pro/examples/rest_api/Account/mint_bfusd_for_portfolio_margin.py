import os
import logging

from binance_derivatives_trading_portfolio_margin_pro.derivatives_trading_portfolio_margin_pro import (
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


def mint_bfusd_for_portfolio_margin():
    try:
        response = client.rest_api.mint_bfusd_for_portfolio_margin(
            from_asset="from_asset_example",
            target_asset="target_asset_example",
            amount=1.0,
        )

        rate_limits = response.rate_limits
        logging.info(f"mint_bfusd_for_portfolio_margin() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"mint_bfusd_for_portfolio_margin() response: {data}")
    except Exception as e:
        logging.error(f"mint_bfusd_for_portfolio_margin() error: {e}")


if __name__ == "__main__":
    mint_bfusd_for_portfolio_margin()
