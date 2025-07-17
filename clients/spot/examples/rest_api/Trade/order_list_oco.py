import os
import logging

from binance_sdk_spot.spot import Spot, ConfigurationRestAPI, SPOT_REST_API_PROD_URL
from binance_sdk_spot.rest_api.models import OrderListOcoSideEnum
from binance_sdk_spot.rest_api.models import OrderListOcoAboveTypeEnum
from binance_sdk_spot.rest_api.models import OrderListOcoBelowTypeEnum


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


def order_list_oco():
    try:
        response = client.rest_api.order_list_oco(
            symbol="BNBUSDT",
            side=OrderListOcoSideEnum["BUY"].value,
            quantity=1.0,
            above_type=OrderListOcoAboveTypeEnum["STOP_LOSS_LIMIT"].value,
            below_type=OrderListOcoBelowTypeEnum["STOP_LOSS"].value,
        )

        rate_limits = response.rate_limits
        logging.info(f"order_list_oco() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"order_list_oco() response: {data}")
    except Exception as e:
        logging.error(f"order_list_oco() error: {e}")


if __name__ == "__main__":
    order_list_oco()
