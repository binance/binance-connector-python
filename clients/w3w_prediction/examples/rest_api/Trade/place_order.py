import os
import logging

from binance_sdk_w3w_prediction.w3w_prediction import (
    W3wPrediction,
    ConfigurationRestAPI,
    W3W_PREDICTION_REST_API_PROD_URL,
)
from binance_sdk_w3w_prediction.rest_api.models import PlaceOrderAccountTypeEnum
from binance_sdk_w3w_prediction.rest_api.models import PlaceOrderOrderTypeEnum


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


def place_order():
    try:
        response = client.rest_api.place_order(
            wallet_address="0x12e32db8817e292508c34111cbc4b23340df542c",
            wallet_id="5b5c1ec3be4e4416a5872b21c1ca5d20",
            quote_id="q_20260525_abc123xyz",
            time_in_force="FOK",
            account_type=PlaceOrderAccountTypeEnum["SPOT"].value,
            order_type=PlaceOrderOrderTypeEnum["MARKET"].value,
            slippage_bps=1200,
        )

        rate_limits = response.rate_limits
        logging.info(f"place_order() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"place_order() response: {data}")
    except Exception as e:
        logging.error(f"place_order() error: {e}")


if __name__ == "__main__":
    place_order()
