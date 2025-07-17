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


def get_future_hourly_interest_rate():
    try:
        response = client.rest_api.get_future_hourly_interest_rate(
            assets="assets_example", is_isolated=False
        )

        rate_limits = response.rate_limits
        logging.info(f"get_future_hourly_interest_rate() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"get_future_hourly_interest_rate() response: {data}")
    except Exception as e:
        logging.error(f"get_future_hourly_interest_rate() error: {e}")


if __name__ == "__main__":
    get_future_hourly_interest_rate()
