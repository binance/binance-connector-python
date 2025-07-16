import os
import logging

from binance_crypto_loan.crypto_loan import (
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


def flexible_loan_adjust_ltv():
    try:
        response = client.rest_api.flexible_loan_adjust_ltv(
            loan_coin="loan_coin_example",
            collateral_coin="collateral_coin_example",
            adjustment_amount=1.0,
            direction="direction_example",
        )

        rate_limits = response.rate_limits
        logging.info(f"flexible_loan_adjust_ltv() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"flexible_loan_adjust_ltv() response: {data}")
    except Exception as e:
        logging.error(f"flexible_loan_adjust_ltv() error: {e}")


if __name__ == "__main__":
    flexible_loan_adjust_ltv()
