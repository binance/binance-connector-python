import os
import logging

from binance_sdk_spot.spot import Spot, ConfigurationRestAPI, SPOT_REST_API_PROD_URL
from binance_sdk_spot.rest_api.models import OrderListOtocoWorkingTypeEnum
from binance_sdk_spot.rest_api.models import OrderListOtocoWorkingSideEnum
from binance_sdk_spot.rest_api.models import OrderListOtocoPendingSideEnum
from binance_sdk_spot.rest_api.models import OrderListOtocoPendingAboveTypeEnum


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


def order_list_otoco():
    try:
        response = client.rest_api.order_list_otoco(
            symbol="BNBUSDT",
            working_type=OrderListOtocoWorkingTypeEnum["LIMIT"].value,
            working_side=OrderListOtocoWorkingSideEnum["BUY"].value,
            working_price=1.0,
            working_quantity=1.0,
            pending_side=OrderListOtocoPendingSideEnum["BUY"].value,
            pending_quantity=1.0,
            pending_above_type=OrderListOtocoPendingAboveTypeEnum[
                "STOP_LOSS_LIMIT"
            ].value,
        )

        rate_limits = response.rate_limits
        logging.info(f"order_list_otoco() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"order_list_otoco() response: {data}")
    except Exception as e:
        logging.error(f"order_list_otoco() error: {e}")


if __name__ == "__main__":
    order_list_otoco()
