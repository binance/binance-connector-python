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


def dust_convert():
    try:
        response = client.rest_api.dust_convert(
            asset="asset_example",
        )

        rate_limits = response.rate_limits
        logging.info(f"dust_convert() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"dust_convert() response: {data}")
    except Exception as e:
        logging.error(f"dust_convert() error: {e}")


if __name__ == "__main__":
    dust_convert()
