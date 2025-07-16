import os
import logging

from binance_spot.spot import Spot, ConfigurationRestAPI, SPOT_REST_API_PROD_URL
from binance_spot.rest_api.models import OrderCancelReplaceSideEnum
from binance_spot.rest_api.models import OrderCancelReplaceTypeEnum
from binance_spot.rest_api.models import OrderCancelReplaceCancelReplaceModeEnum


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv("BASE_PATH", SPOT_REST_API_PROD_URL),
)

# Initialize Spot client
client = Spot(config_rest_api=configuration_rest_api)


def order_cancel_replace():
    try:
        response = client.rest_api.order_cancel_replace(
            symbol="BNBUSDT",
            side=OrderCancelReplaceSideEnum["BUY"].value,
            type=OrderCancelReplaceTypeEnum["MARKET"].value,
            cancel_replace_mode=OrderCancelReplaceCancelReplaceModeEnum[
                "STOP_ON_FAILURE"
            ].value,
        )

        rate_limits = response.rate_limits
        logging.info(f"order_cancel_replace() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"order_cancel_replace() response: {data}")
    except Exception as e:
        logging.error(f"order_cancel_replace() error: {e}")


if __name__ == "__main__":
    order_cancel_replace()
