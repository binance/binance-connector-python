import os
import logging

from binance_simple_earn.simple_earn import (
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


def set_locked_product_redeem_option():
    try:
        response = client.rest_api.set_locked_product_redeem_option(
            position_id="1",
            redeem_to="redeem_to_example",
        )

        rate_limits = response.rate_limits
        logging.info(f"set_locked_product_redeem_option() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"set_locked_product_redeem_option() response: {data}")
    except Exception as e:
        logging.error(f"set_locked_product_redeem_option() error: {e}")


if __name__ == "__main__":
    set_locked_product_redeem_option()
