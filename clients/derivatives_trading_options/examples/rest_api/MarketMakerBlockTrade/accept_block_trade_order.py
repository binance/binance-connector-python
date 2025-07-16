import os
import logging

from binance_derivatives_trading_options.derivatives_trading_options import (
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


def accept_block_trade_order():
    try:
        response = client.rest_api.accept_block_trade_order(
            block_order_matching_key="block_order_matching_key_example",
        )

        rate_limits = response.rate_limits
        logging.info(f"accept_block_trade_order() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"accept_block_trade_order() response: {data}")
    except Exception as e:
        logging.error(f"accept_block_trade_order() error: {e}")


if __name__ == "__main__":
    accept_block_trade_order()
