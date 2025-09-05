import os
import logging

from binance_sdk_convert.convert import (
    Convert,
    ConfigurationRestAPI,
    CONVERT_REST_API_PROD_URL,
)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key="CVp5zsxL61CJRCV7UJMZpDw4sgsDP1EUiLDLJvUFrrUXIdiAGYybe0gMDdB9pppG",
    api_secret="LIRgrJxa9vTw6gOxxheCLYDYpuMTiftdtwB8CUW09wlZVKrCswE7jWpWOiu9hEk0",
    base_path=os.getenv("BASE_PATH", CONVERT_REST_API_PROD_URL),
)

# Initialize Convert client
client = Convert(config_rest_api=configuration_rest_api)


def list_all_convert_pairs():
    try:
        response = client.rest_api.list_all_convert_pairs()

        rate_limits = response.rate_limits
        logging.info(f"list_all_convert_pairs() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"list_all_convert_pairs() response: {data}")
    except Exception as e:
        logging.error(f"list_all_convert_pairs() error: {e}")


if __name__ == "__main__":
    list_all_convert_pairs()
