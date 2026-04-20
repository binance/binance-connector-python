import os
import logging

from binance_sdk_spot.spot import Spot, ConfigurationRestAPI, SPOT_REST_API_PROD_URL
from binance_sdk_spot.rest_api.models import OrderListOpocoWorkingTypeEnum
from binance_sdk_spot.rest_api.models import OrderListOpocoWorkingSideEnum
from binance_sdk_spot.rest_api.models import OrderListOpocoPendingSideEnum
from binance_sdk_spot.rest_api.models import OrderListOpocoPendingAboveTypeEnum


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


def order_list_opoco():
    try:
        response = client.rest_api.order_list_opoco(
            symbol="BNBUSDT",
            working_type=OrderListOpocoWorkingTypeEnum["LIMIT"].value,
            working_side=OrderListOpocoWorkingSideEnum["BUY"].value,
            working_price=1.0,
            working_quantity=1.0,
            pending_side=OrderListOpocoPendingSideEnum["BUY"].value,
            pending_above_type=OrderListOpocoPendingAboveTypeEnum[
                "STOP_LOSS_LIMIT"
            ].value,
        )

        rate_limits = response.rate_limits
        logging.info(f"order_list_opoco() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"order_list_opoco() response: {data}")
    except Exception as e:
        logging.error(f"order_list_opoco() error: {e}")


if __name__ == "__main__":
    order_list_opoco()
