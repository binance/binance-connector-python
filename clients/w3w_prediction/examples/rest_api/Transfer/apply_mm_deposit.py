import os
import logging

from binance_sdk_w3w_prediction.w3w_prediction import (
    W3wPrediction,
    ConfigurationRestAPI,
    W3W_PREDICTION_REST_API_PROD_URL,
)
from binance_sdk_w3w_prediction.rest_api.models import ApplyMmDepositAccountTypeEnum


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv("BASE_PATH", W3W_PREDICTION_REST_API_PROD_URL),
)

# Initialize W3wPrediction client
client = W3wPrediction(config_rest_api=configuration_rest_api)


def apply_mm_deposit():
    try:
        response = client.rest_api.apply_mm_deposit(
            from_token="USDT",
            from_token_amount="1000000000000000000",
            to_token="USDT",
            account_type=ApplyMmDepositAccountTypeEnum["SPOT"].value,
        )

        rate_limits = response.rate_limits
        logging.info(f"apply_mm_deposit() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"apply_mm_deposit() response: {data}")
    except Exception as e:
        logging.error(f"apply_mm_deposit() error: {e}")


if __name__ == "__main__":
    apply_mm_deposit()
