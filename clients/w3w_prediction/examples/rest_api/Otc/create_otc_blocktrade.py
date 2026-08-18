import os
import logging

from binance_sdk_w3w_prediction.w3w_prediction import (
    W3wPrediction,
    ConfigurationRestAPI,
    W3W_PREDICTION_REST_API_PROD_URL,
)
from binance_sdk_w3w_prediction.rest_api.models import CreateOtcBlocktradeSideEnum


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


def create_otc_blocktrade():
    try:
        response = client.rest_api.create_otc_blocktrade(
            market_id="123",
            token_id="71321045679252212594626385532706912750332728571942532289631379312455583992563",
            side=CreateOtcBlocktradeSideEnum["BUY"].value,
            maker_amount="600000000000000000000",
            taker_amount="1000000000000000000000",
            price_per_share="0.65",
            expiration=1790000000,
        )

        rate_limits = response.rate_limits
        logging.info(f"create_otc_blocktrade() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"create_otc_blocktrade() response: {data}")
    except Exception as e:
        logging.error(f"create_otc_blocktrade() error: {e}")


if __name__ == "__main__":
    create_otc_blocktrade()
