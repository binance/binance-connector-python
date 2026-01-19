import os
import logging

from binance_sdk_spot.spot import Spot, ConfigurationRestAPI, SPOT_REST_API_PROD_URL
from binance_sdk_spot.rest_api.models import OrderListOpoWorkingTypeEnum
from binance_sdk_spot.rest_api.models import OrderListOpoWorkingSideEnum
from binance_sdk_spot.rest_api.models import OrderListOpoPendingTypeEnum
from binance_sdk_spot.rest_api.models import OrderListOpoPendingSideEnum
from binance_sdk_spot.rest_api.models import OrderListOpoWorkingTimeInForceEnum
from binance_sdk_spot.rest_api.models import OrderListOpoPendingTimeInForceEnum


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


def order_list_opo():
    try:
        response = client.rest_api.order_list_opo(
            symbol="BNBUSDT",
            working_type=OrderListOpoWorkingTypeEnum["LIMIT"].value,
            working_side=OrderListOpoWorkingSideEnum["BUY"].value,
            working_time_in_force=OrderListOpoWorkingTimeInForceEnum["GTC"].value,
            working_price=800.0,
            working_quantity=1.0,
            pending_type=OrderListOpoPendingTypeEnum["LIMIT"].value,
            pending_side=OrderListOpoPendingSideEnum["SELL"].value,
            pending_time_in_force=OrderListOpoPendingTimeInForceEnum["GTC"].value,
            pending_price=805.0,
        )

        rate_limits = response.rate_limits
        logging.info(f"order_list_opo() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"order_list_opo() response: {data}")
    except Exception as e:
        logging.error(f"order_list_opo() error: {e}")


if __name__ == "__main__":
    order_list_opo()
