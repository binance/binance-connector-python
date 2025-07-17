import os
import logging

from binance_sdk_derivatives_trading_usds_futures.derivatives_trading_usds_futures import (
    DerivativesTradingUsdsFutures,
    ConfigurationRestAPI,
    DERIVATIVES_TRADING_USDS_FUTURES_REST_API_PROD_URL,
)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv(
        "BASE_PATH", DERIVATIVES_TRADING_USDS_FUTURES_REST_API_PROD_URL
    ),
)

# Initialize DerivativesTradingUsdsFutures client
client = DerivativesTradingUsdsFutures(config_rest_api=configuration_rest_api)


def change_multi_assets_mode():
    try:
        response = client.rest_api.change_multi_assets_mode(
            multi_assets_margin="multi_assets_margin_example",
        )

        rate_limits = response.rate_limits
        logging.info(f"change_multi_assets_mode() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"change_multi_assets_mode() response: {data}")
    except Exception as e:
        logging.error(f"change_multi_assets_mode() error: {e}")


if __name__ == "__main__":
    change_multi_assets_mode()
