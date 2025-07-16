import os
import logging

from binance_convert.convert import (
    Convert,
    ConfigurationRestAPI,
    CONVERT_REST_API_PROD_URL,
)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv("BASE_PATH", CONVERT_REST_API_PROD_URL),
)

# Initialize Convert client
client = Convert(config_rest_api=configuration_rest_api)


def query_limit_open_orders():
    try:
        response = client.rest_api.query_limit_open_orders()

        rate_limits = response.rate_limits
        logging.info(f"query_limit_open_orders() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"query_limit_open_orders() response: {data}")
    except Exception as e:
        logging.error(f"query_limit_open_orders() error: {e}")


if __name__ == "__main__":
    query_limit_open_orders()
