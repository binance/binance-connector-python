import os
import logging

from binance_spot.spot import Spot, ConfigurationRestAPI, SPOT_REST_API_PROD_URL
from binance_spot.rest_api.models import SorOrderSideEnum
from binance_spot.rest_api.models import SorOrderTypeEnum


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


def sor_order():
    try:
        response = client.rest_api.sor_order(
            symbol="BNBUSDT",
            side=SorOrderSideEnum["BUY"].value,
            type=SorOrderTypeEnum["MARKET"].value,
            quantity=1.0,
        )

        rate_limits = response.rate_limits
        logging.info(f"sor_order() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"sor_order() response: {data}")
    except Exception as e:
        logging.error(f"sor_order() error: {e}")


if __name__ == "__main__":
    sor_order()
