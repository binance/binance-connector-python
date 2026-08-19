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


def latest_quote():
    try:
        response = client.rest_api.latest_quote(symbol="AAPL")

        rate_limits = response.rate_limits
        logging.info(f"latest_quote() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"latest_quote() response: {data}")
    except Exception as e:
        logging.error(f"latest_quote() error: {e}")


if __name__ == "__main__":
    latest_quote()
