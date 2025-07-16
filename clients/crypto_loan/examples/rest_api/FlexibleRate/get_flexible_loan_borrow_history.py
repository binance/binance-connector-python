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


def get_flexible_loan_borrow_history():
    try:
        response = client.rest_api.get_flexible_loan_borrow_history()

        rate_limits = response.rate_limits
        logging.info(f"get_flexible_loan_borrow_history() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"get_flexible_loan_borrow_history() response: {data}")
    except Exception as e:
        logging.error(f"get_flexible_loan_borrow_history() error: {e}")


if __name__ == "__main__":
    get_flexible_loan_borrow_history()
