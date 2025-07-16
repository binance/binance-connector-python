import os
import logging

from binance_margin_trading.margin_trading import (
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


def query_special_key():
    try:
        response = client.rest_api.query_special_key()

        rate_limits = response.rate_limits
        logging.info(f"query_special_key() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"query_special_key() response: {data}")
    except Exception as e:
        logging.error(f"query_special_key() error: {e}")


if __name__ == "__main__":
    query_special_key()
