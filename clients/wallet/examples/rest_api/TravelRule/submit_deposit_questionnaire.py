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


def submit_deposit_questionnaire():
    try:
        response = client.rest_api.submit_deposit_questionnaire(
            sub_account_id="1",
            deposit_id=1,
            questionnaire="questionnaire_example",
            beneficiary_pii="beneficiary_pii_example",
            signature="signature_example",
        )

        rate_limits = response.rate_limits
        logging.info(f"submit_deposit_questionnaire() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"submit_deposit_questionnaire() response: {data}")
    except Exception as e:
        logging.error(f"submit_deposit_questionnaire() error: {e}")


if __name__ == "__main__":
    submit_deposit_questionnaire()
