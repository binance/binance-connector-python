import os
import logging

from binance_sdk_margin_trading.margin_trading import (
    MarginTrading,
    ConfigurationRestAPI,
    MARGIN_TRADING_REST_API_PROD_URL,
)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv("BASE_PATH", MARGIN_TRADING_REST_API_PROD_URL),
)

# Initialize MarginTrading client
client = MarginTrading(config_rest_api=configuration_rest_api)


def query_liquidation_loan_repay_history():
    try:
        response = client.rest_api.query_liquidation_loan_repay_history()

        rate_limits = response.rate_limits
        logging.info(
            f"query_liquidation_loan_repay_history() rate limits: {rate_limits}"
        )

        data = response.data()
        logging.info(f"query_liquidation_loan_repay_history() response: {data}")
    except Exception as e:
        logging.error(f"query_liquidation_loan_repay_history() error: {e}")


if __name__ == "__main__":
    query_liquidation_loan_repay_history()
