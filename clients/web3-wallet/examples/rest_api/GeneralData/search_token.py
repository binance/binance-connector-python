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


def search_token():
    try:
        response = client.rest_api.search_token(
            chains="1,56,CT_501",
            search="USDT",
        )

        rate_limits = response.rate_limits
        logging.info(f"search_token() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"search_token() response: {data}")
    except Exception as e:
        logging.error(f"search_token() error: {e}")


if __name__ == "__main__":
    search_token()
