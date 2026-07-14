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


def market_search():
    try:
        response = client.rest_api.market_search(
            query="BTC price",
        )

        rate_limits = response.rate_limits
        logging.info(f"market_search() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"market_search() response: {data}")
    except Exception as e:
        logging.error(f"market_search() error: {e}")


if __name__ == "__main__":
    market_search()
