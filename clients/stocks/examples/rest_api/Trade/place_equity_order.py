import os
import logging

from binance_sdk_stocks.stocks import (
    Stocks,
    ConfigurationRestAPI,
    STOCKS_REST_API_PROD_URL,
)
from binance_sdk_stocks.rest_api.models import PlaceEquityOrderSideEnum
from binance_sdk_stocks.rest_api.models import PlaceEquityOrderOrderTypeEnum


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv("BASE_PATH", STOCKS_REST_API_PROD_URL),
)

# Initialize Stocks client
client = Stocks(config_rest_api=configuration_rest_api)


def place_equity_order():
    try:
        response = client.rest_api.place_equity_order(
            symbol="AAPL",
            side=PlaceEquityOrderSideEnum["BUY"].value,
            order_type=PlaceEquityOrderOrderTypeEnum["LIMIT"].value,
        )

        rate_limits = response.rate_limits
        logging.info(f"place_equity_order() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"place_equity_order() response: {data}")
    except Exception as e:
        logging.error(f"place_equity_order() error: {e}")


if __name__ == "__main__":
    place_equity_order()
