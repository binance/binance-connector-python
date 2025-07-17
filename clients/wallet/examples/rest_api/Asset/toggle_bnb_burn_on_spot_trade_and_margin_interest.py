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


def toggle_bnb_burn_on_spot_trade_and_margin_interest():
    try:
        response = client.rest_api.toggle_bnb_burn_on_spot_trade_and_margin_interest()

        rate_limits = response.rate_limits
        logging.info(
            f"toggle_bnb_burn_on_spot_trade_and_margin_interest() rate limits: {rate_limits}"
        )

        data = response.data()
        logging.info(
            f"toggle_bnb_burn_on_spot_trade_and_margin_interest() response: {data}"
        )
    except Exception as e:
        logging.error(f"toggle_bnb_burn_on_spot_trade_and_margin_interest() error: {e}")


if __name__ == "__main__":
    toggle_bnb_burn_on_spot_trade_and_margin_interest()
