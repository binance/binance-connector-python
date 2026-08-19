import os
import logging

from binance_sdk_stocks.stocks import (
    Stocks,
    ConfigurationRestAPI,
    STOCKS_REST_API_PROD_URL,
)


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


def cancel_equity_order():
    try:
        response = client.rest_api.cancel_equity_order(
            order_id="c3c58f49-7b0d-4b9e-a2db-1a2f9a3b8c71",
        )

        rate_limits = response.rate_limits
        logging.info(f"cancel_equity_order() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"cancel_equity_order() response: {data}")
    except Exception as e:
        logging.error(f"cancel_equity_order() error: {e}")


if __name__ == "__main__":
    cancel_equity_order()
