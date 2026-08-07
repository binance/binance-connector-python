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


def get_gas_price():
    try:
        response = client.rest_api.get_gas_price(
            binance_chain_id="1",
        )

        rate_limits = response.rate_limits
        logging.info(f"get_gas_price() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"get_gas_price() response: {data}")
    except Exception as e:
        logging.error(f"get_gas_price() error: {e}")


if __name__ == "__main__":
    get_gas_price()
