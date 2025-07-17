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


def query_sub_account_futures_asset_transfer_history():
    try:
        response = client.rest_api.query_sub_account_futures_asset_transfer_history(
            email="sub-account-email@email.com",
            futures_type=56,
        )

        rate_limits = response.rate_limits
        logging.info(
            f"query_sub_account_futures_asset_transfer_history() rate limits: {rate_limits}"
        )

        data = response.data()
        logging.info(
            f"query_sub_account_futures_asset_transfer_history() response: {data}"
        )
    except Exception as e:
        logging.error(f"query_sub_account_futures_asset_transfer_history() error: {e}")


if __name__ == "__main__":
    query_sub_account_futures_asset_transfer_history()
