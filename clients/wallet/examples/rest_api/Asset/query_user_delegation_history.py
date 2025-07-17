import os
import logging

from binance_sdk_wallet.wallet import (
    Wallet,
    ConfigurationRestAPI,
    WALLET_REST_API_PROD_URL,
)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv("BASE_PATH", WALLET_REST_API_PROD_URL),
)

# Initialize Wallet client
client = Wallet(config_rest_api=configuration_rest_api)


def query_user_delegation_history():
    try:
        response = client.rest_api.query_user_delegation_history(
            email="email_example",
            start_time=1623319461670,
            end_time=1641782889000,
        )

        rate_limits = response.rate_limits
        logging.info(f"query_user_delegation_history() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"query_user_delegation_history() response: {data}")
    except Exception as e:
        logging.error(f"query_user_delegation_history() error: {e}")


if __name__ == "__main__":
    query_user_delegation_history()
