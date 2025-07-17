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


def add_ip_restriction_for_sub_account_api_key():
    try:
        response = client.rest_api.add_ip_restriction_for_sub_account_api_key(
            email="sub-account-email@email.com",
            sub_account_api_key="sub_account_api_key_example",
            status="status_example",
        )

        rate_limits = response.rate_limits
        logging.info(
            f"add_ip_restriction_for_sub_account_api_key() rate limits: {rate_limits}"
        )

        data = response.data()
        logging.info(f"add_ip_restriction_for_sub_account_api_key() response: {data}")
    except Exception as e:
        logging.error(f"add_ip_restriction_for_sub_account_api_key() error: {e}")


if __name__ == "__main__":
    add_ip_restriction_for_sub_account_api_key()
