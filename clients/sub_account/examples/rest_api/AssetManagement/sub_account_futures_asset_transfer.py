import os
import logging

from binance_sub_account.sub_account import (
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


def sub_account_futures_asset_transfer():
    try:
        response = client.rest_api.sub_account_futures_asset_transfer(
            from_email="from_email_example",
            to_email="to_email_example",
            futures_type=56,
            asset="asset_example",
            amount=1.0,
        )

        rate_limits = response.rate_limits
        logging.info(f"sub_account_futures_asset_transfer() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"sub_account_futures_asset_transfer() response: {data}")
    except Exception as e:
        logging.error(f"sub_account_futures_asset_transfer() error: {e}")


if __name__ == "__main__":
    sub_account_futures_asset_transfer()
