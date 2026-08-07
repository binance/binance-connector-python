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


def build_swap_transaction():
    try:
        response = client.rest_api.build_swap_transaction(
            binance_chain_id="56",
            amount="1000000",
            from_token_address="0x55d398326f99059fF775485246999027B3197955",
            to_token_address="0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d",
            user_wallet_address="0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
            quote_id="a1b2c3d4e5f64a8b9c0d1e2f3a4b5c6d",
        )

        rate_limits = response.rate_limits
        logging.info(f"build_swap_transaction() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"build_swap_transaction() response: {data}")
    except Exception as e:
        logging.error(f"build_swap_transaction() error: {e}")


if __name__ == "__main__":
    build_swap_transaction()
