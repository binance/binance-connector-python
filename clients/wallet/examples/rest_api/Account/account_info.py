import os
import logging

from binance_wallet.wallet import Wallet, ConfigurationRestAPI, WALLET_REST_API_PROD_URL


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


def account_info():
    try:
        response = client.rest_api.account_info()

        rate_limits = response.rate_limits
        logging.info(f"account_info() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"account_info() response: {data}")
    except Exception as e:
        logging.error(f"account_info() error: {e}")


if __name__ == "__main__":
    account_info()
