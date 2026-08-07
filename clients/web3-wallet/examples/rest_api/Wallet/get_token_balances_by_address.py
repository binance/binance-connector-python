import os
import logging

from binance_sdk_web3_wallet.web3_wallet import (
    Web3Wallet,
    ConfigurationRestAPI,
    WEB3_WALLET_REST_API_PROD_URL,
)

from src.rest_api.models.get_token_balances_by_address_request_token_contract_addresses_inner import (
    GetTokenBalancesByAddressRequestTokenContractAddressesInner,
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


def get_token_balances_by_address():
    try:
        response = client.rest_api.get_token_balances_by_address(
            address="address_example",
            token_contract_addresses=[
                GetTokenBalancesByAddressRequestTokenContractAddressesInner(
                    binance_chain_id="1",
                    token_contract_address="0x2260fac5e5542a773aa44fbcfedf7c193bc2c599",
                )
            ],
        )

        rate_limits = response.rate_limits
        logging.info(f"get_token_balances_by_address() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"get_token_balances_by_address() response: {data}")
    except Exception as e:
        logging.error(f"get_token_balances_by_address() error: {e}")


if __name__ == "__main__":
    get_token_balances_by_address()
