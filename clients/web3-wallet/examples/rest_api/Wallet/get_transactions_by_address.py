import os
import logging

from binance_sdk_web3_wallet.web3_wallet import (
    Web3Wallet,
    ConfigurationRestAPI,
    WEB3_WALLET_REST_API_PROD_URL,
)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv("BASE_PATH", WEB3_WALLET_REST_API_PROD_URL),
)

# Initialize Web3Wallet client
client = Web3Wallet(config_rest_api=configuration_rest_api)


def get_transactions_by_address():
    try:
        response = client.rest_api.get_transactions_by_address(
            address="0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
            chains="1,56",
        )

        rate_limits = response.rate_limits
        logging.info(f"get_transactions_by_address() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"get_transactions_by_address() response: {data}")
    except Exception as e:
        logging.error(f"get_transactions_by_address() error: {e}")


if __name__ == "__main__":
    get_transactions_by_address()
