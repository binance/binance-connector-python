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


def deposit_assets_into_the_managed_sub_account():
    try:
        response = client.rest_api.deposit_assets_into_the_managed_sub_account(
            to_email="to_email_example",
            asset="asset_example",
            amount=1.0,
        )

        rate_limits = response.rate_limits
        logging.info(
            f"deposit_assets_into_the_managed_sub_account() rate limits: {rate_limits}"
        )

        data = response.data()
        logging.info(f"deposit_assets_into_the_managed_sub_account() response: {data}")
    except Exception as e:
        logging.error(f"deposit_assets_into_the_managed_sub_account() error: {e}")


if __name__ == "__main__":
    deposit_assets_into_the_managed_sub_account()
