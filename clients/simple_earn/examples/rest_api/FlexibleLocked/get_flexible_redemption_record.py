import os
import logging

from binance_sdk_simple_earn.simple_earn import (
    SimpleEarn,
    ConfigurationRestAPI,
    SIMPLE_EARN_REST_API_PROD_URL,
)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv("BASE_PATH", SIMPLE_EARN_REST_API_PROD_URL),
)

# Initialize SimpleEarn client
client = SimpleEarn(config_rest_api=configuration_rest_api)


def get_flexible_redemption_record():
    try:
        response = client.rest_api.get_flexible_redemption_record()

        rate_limits = response.rate_limits
        logging.info(f"get_flexible_redemption_record() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"get_flexible_redemption_record() response: {data}")
    except Exception as e:
        logging.error(f"get_flexible_redemption_record() error: {e}")


if __name__ == "__main__":
    get_flexible_redemption_record()
