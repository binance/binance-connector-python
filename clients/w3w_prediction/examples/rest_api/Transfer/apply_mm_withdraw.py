import os
import logging

from binance_sdk_w3w_prediction.w3w_prediction import (
    W3wPrediction,
    ConfigurationRestAPI,
    W3W_PREDICTION_REST_API_PROD_URL,
)


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


def apply_mm_withdraw():
    try:
        response = client.rest_api.apply_mm_withdraw(
            coin="USDT",
            network="BEP20",
            amount="100.00",
        )

        rate_limits = response.rate_limits
        logging.info(f"apply_mm_withdraw() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"apply_mm_withdraw() response: {data}")
    except Exception as e:
        logging.error(f"apply_mm_withdraw() error: {e}")


if __name__ == "__main__":
    apply_mm_withdraw()
