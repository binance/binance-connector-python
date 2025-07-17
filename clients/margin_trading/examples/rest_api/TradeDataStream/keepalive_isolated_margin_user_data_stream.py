import os
import logging

from binance_sdk_margin_trading.margin_trading import (
    MarginTrading,
    ConfigurationRestAPI,
    MARGIN_TRADING_REST_API_PROD_URL,
)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv("BASE_PATH", MARGIN_TRADING_REST_API_PROD_URL),
)

# Initialize MarginTrading client
client = MarginTrading(config_rest_api=configuration_rest_api)


def keepalive_isolated_margin_user_data_stream():
    try:
        response = client.rest_api.keepalive_isolated_margin_user_data_stream(
            symbol="symbol_example", listen_key="listen_key_example"
        )

        rate_limits = response.rate_limits
        logging.info(
            f"keepalive_isolated_margin_user_data_stream() rate limits: {rate_limits}"
        )

        data = response.data()
        logging.info(f"keepalive_isolated_margin_user_data_stream() response: {data}")
    except Exception as e:
        logging.error(f"keepalive_isolated_margin_user_data_stream() error: {e}")


if __name__ == "__main__":
    keepalive_isolated_margin_user_data_stream()
