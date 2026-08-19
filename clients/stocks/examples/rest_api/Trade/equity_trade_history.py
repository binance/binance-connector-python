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


def equity_trade_history():
    try:
        response = client.rest_api.equity_trade_history(
            start_time=1735800000000,
            end_time=1735900000000,
        )

        rate_limits = response.rate_limits
        logging.info(f"equity_trade_history() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"equity_trade_history() response: {data}")
    except Exception as e:
        logging.error(f"equity_trade_history() error: {e}")


if __name__ == "__main__":
    equity_trade_history()
