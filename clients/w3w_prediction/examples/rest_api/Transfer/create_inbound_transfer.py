import os
import logging

from binance_sdk_w3w_prediction.w3w_prediction import (
    W3wPrediction,
    ConfigurationRestAPI,
    W3W_PREDICTION_REST_API_PROD_URL,
)
from binance_sdk_w3w_prediction.rest_api.models import (
    CreateInboundTransferAccountTypeEnum,
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


def create_inbound_transfer():
    try:
        response = client.rest_api.create_inbound_transfer(
            wallet_id="5b5c1ec3be4e4416a5872b21c1ca5d20",
            wallet_address="0x12e32db8817e292508c34111cbc4b23340df542c",
            from_token_amount="1000000000000000000",
            account_type=CreateInboundTransferAccountTypeEnum["SPOT"].value,
        )

        rate_limits = response.rate_limits
        logging.info(f"create_inbound_transfer() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"create_inbound_transfer() response: {data}")
    except Exception as e:
        logging.error(f"create_inbound_transfer() error: {e}")


if __name__ == "__main__":
    create_inbound_transfer()
