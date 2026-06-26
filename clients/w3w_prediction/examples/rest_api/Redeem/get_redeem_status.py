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


def get_redeem_status():
    try:
        response = client.rest_api.get_redeem_status(
            wallet_address="0x12e32db8817e292508c34111cbc4b23340df542c",
            tx_hash="0xabc123def456789abcdef123456789abcdef123456789abcdef123456789abcd",
        )

        rate_limits = response.rate_limits
        logging.info(f"get_redeem_status() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"get_redeem_status() response: {data}")
    except Exception as e:
        logging.error(f"get_redeem_status() error: {e}")


if __name__ == "__main__":
    get_redeem_status()
