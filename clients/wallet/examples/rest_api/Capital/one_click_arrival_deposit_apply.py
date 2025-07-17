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


def one_click_arrival_deposit_apply():
    try:
        response = client.rest_api.one_click_arrival_deposit_apply()

        rate_limits = response.rate_limits
        logging.info(f"one_click_arrival_deposit_apply() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"one_click_arrival_deposit_apply() response: {data}")
    except Exception as e:
        logging.error(f"one_click_arrival_deposit_apply() error: {e}")


if __name__ == "__main__":
    one_click_arrival_deposit_apply()
