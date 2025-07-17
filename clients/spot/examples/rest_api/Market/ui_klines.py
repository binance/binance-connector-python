import os
import logging

from binance_sdk_spot.spot import Spot, ConfigurationRestAPI, SPOT_REST_API_PROD_URL
from binance_sdk_spot.rest_api.models import UiKlinesIntervalEnum


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


def ui_klines():
    try:
        response = client.rest_api.ui_klines(
            symbol="BNBUSDT",
            interval=UiKlinesIntervalEnum["INTERVAL_1s"].value,
        )

        rate_limits = response.rate_limits
        logging.info(f"ui_klines() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"ui_klines() response: {data}")
    except Exception as e:
        logging.error(f"ui_klines() error: {e}")


if __name__ == "__main__":
    ui_klines()
