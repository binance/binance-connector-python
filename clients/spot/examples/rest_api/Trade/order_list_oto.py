import os
import logging

from binance_spot.spot import Spot, ConfigurationRestAPI, SPOT_REST_API_PROD_URL
from binance_spot.rest_api.models import OrderListOtoWorkingTypeEnum
from binance_spot.rest_api.models import OrderListOtoWorkingSideEnum
from binance_spot.rest_api.models import OrderListOtoPendingTypeEnum
from binance_spot.rest_api.models import OrderListOtoPendingSideEnum


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


def order_list_oto():
    try:
        response = client.rest_api.order_list_oto(
            symbol="BNBUSDT",
            working_type=OrderListOtoWorkingTypeEnum["LIMIT"].value,
            working_side=OrderListOtoWorkingSideEnum["BUY"].value,
            working_price=1.0,
            working_quantity=1.0,
            pending_type=OrderListOtoPendingTypeEnum["LIMIT"].value,
            pending_side=OrderListOtoPendingSideEnum["BUY"].value,
            pending_quantity=1.0,
        )

        rate_limits = response.rate_limits
        logging.info(f"order_list_oto() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"order_list_oto() response: {data}")
    except Exception as e:
        logging.error(f"order_list_oto() error: {e}")


if __name__ == "__main__":
    order_list_oto()
