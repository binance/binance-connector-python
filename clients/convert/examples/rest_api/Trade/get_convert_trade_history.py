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


def get_convert_trade_history():
    try:
        response = client.rest_api.get_convert_trade_history(
            start_time=1623319461670,
            end_time=1641782889000,
        )

        rate_limits = response.rate_limits
        logging.info(f"get_convert_trade_history() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"get_convert_trade_history() response: {data}")
    except Exception as e:
        logging.error(f"get_convert_trade_history() error: {e}")


if __name__ == "__main__":
    get_convert_trade_history()
