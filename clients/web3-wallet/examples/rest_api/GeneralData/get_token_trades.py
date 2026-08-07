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


def get_token_trades():
    try:
        response = client.rest_api.get_token_trades(
            binance_chain_id="1",
            token_contract_address="0x6982508145454ce325ddbe47a25d4ec3d2311933",
        )

        rate_limits = response.rate_limits
        logging.info(f"get_token_trades() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"get_token_trades() response: {data}")
    except Exception as e:
        logging.error(f"get_token_trades() error: {e}")


if __name__ == "__main__":
    get_token_trades()
