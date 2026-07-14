import os
import logging

from binance_sdk_rebate.rebate import (
    Rebate,
    ConfigurationRestAPI,
    REBATE_REST_API_PROD_URL,
)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv("BASE_PATH", REBATE_REST_API_PROD_URL),
)

# Initialize Rebate client
client = Rebate(config_rest_api=configuration_rest_api)


def get_spot_rebate_history_records():
    try:
        response = client.rest_api.get_spot_rebate_history_records()

        rate_limits = response.rate_limits
        logging.info(f"get_spot_rebate_history_records() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"get_spot_rebate_history_records() response: {data}")
    except Exception as e:
        logging.error(f"get_spot_rebate_history_records() error: {e}")


if __name__ == "__main__":
    get_spot_rebate_history_records()
