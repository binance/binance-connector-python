import os
import logging

from binance_sdk_crypto_loan.crypto_loan import (
    CryptoLoan,
    ConfigurationRestAPI,
    CRYPTO_LOAN_REST_API_PROD_URL,
)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv("BASE_PATH", CRYPTO_LOAN_REST_API_PROD_URL),
)

# Initialize CryptoLoan client
client = CryptoLoan(config_rest_api=configuration_rest_api)


def check_collateral_repay_rate_stable_rate():
    try:
        response = client.rest_api.check_collateral_repay_rate_stable_rate(
            loan_coin="loan_coin_example",
            collateral_coin="collateral_coin_example",
            repay_amount=1.0,
        )

        rate_limits = response.rate_limits
        logging.info(
            f"check_collateral_repay_rate_stable_rate() rate limits: {rate_limits}"
        )

        data = response.data()
        logging.info(f"check_collateral_repay_rate_stable_rate() response: {data}")
    except Exception as e:
        logging.error(f"check_collateral_repay_rate_stable_rate() error: {e}")


if __name__ == "__main__":
    check_collateral_repay_rate_stable_rate()
