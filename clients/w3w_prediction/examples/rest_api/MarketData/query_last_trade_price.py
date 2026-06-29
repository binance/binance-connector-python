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


def query_last_trade_price():
    try:
        response = client.rest_api.query_last_trade_price(market_id=5567895)

        rate_limits = response.rate_limits
        logging.info(f"query_last_trade_price() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"query_last_trade_price() response: {data}")
    except Exception as e:
        logging.error(f"query_last_trade_price() error: {e}")


if __name__ == "__main__":
    query_last_trade_price()
