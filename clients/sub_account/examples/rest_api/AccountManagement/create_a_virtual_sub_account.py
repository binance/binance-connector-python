import os
import logging

from binance_sdk_sub_account.sub_account import (
    SubAccount,
    ConfigurationRestAPI,
    SUB_ACCOUNT_REST_API_PROD_URL,
)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv("BASE_PATH", SUB_ACCOUNT_REST_API_PROD_URL),
)

# Initialize SubAccount client
client = SubAccount(config_rest_api=configuration_rest_api)


def create_a_virtual_sub_account():
    try:
        response = client.rest_api.create_a_virtual_sub_account(
            sub_account_string="sub_account_string_example",
        )

        rate_limits = response.rate_limits
        logging.info(f"create_a_virtual_sub_account() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"create_a_virtual_sub_account() response: {data}")
    except Exception as e:
        logging.error(f"create_a_virtual_sub_account() error: {e}")


if __name__ == "__main__":
    create_a_virtual_sub_account()
