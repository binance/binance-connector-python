import os
import logging

from binance_sdk_derivatives_trading_options.derivatives_trading_options import (
    DerivativesTradingOptions,
    ConfigurationRestAPI,
    DERIVATIVES_TRADING_OPTIONS_REST_API_PROD_URL,
)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv("BASE_PATH", DERIVATIVES_TRADING_OPTIONS_REST_API_PROD_URL),
)

# Initialize DerivativesTradingOptions client
client = DerivativesTradingOptions(config_rest_api=configuration_rest_api)


def query_block_trade_details():
    try:
        response = client.rest_api.query_block_trade_details(
            block_order_matching_key="block_order_matching_key_example",
        )

        rate_limits = response.rate_limits
        logging.info(f"query_block_trade_details() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"query_block_trade_details() response: {data}")
    except Exception as e:
        logging.error(f"query_block_trade_details() error: {e}")


if __name__ == "__main__":
    query_block_trade_details()
