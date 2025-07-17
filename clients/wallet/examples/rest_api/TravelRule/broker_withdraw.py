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


def broker_withdraw():
    try:
        response = client.rest_api.broker_withdraw(
            address="address_example",
            coin="coin_example",
            amount=1.0,
            withdraw_order_id="1",
            questionnaire="questionnaire_example",
            originator_pii="originator_pii_example",
            signature="signature_example",
        )

        rate_limits = response.rate_limits
        logging.info(f"broker_withdraw() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"broker_withdraw() response: {data}")
    except Exception as e:
        logging.error(f"broker_withdraw() error: {e}")


if __name__ == "__main__":
    broker_withdraw()
