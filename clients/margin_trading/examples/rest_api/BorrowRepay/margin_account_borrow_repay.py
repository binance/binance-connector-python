import os
import logging

from binance_sdk_margin_trading.margin_trading import (
    MarginTrading,
    ConfigurationRestAPI,
    MARGIN_TRADING_REST_API_PROD_URL,
)
from binance_sdk_margin_trading.rest_api.models import (
    MarginAccountBorrowRepayIsIsolatedEnum,
)
from binance_sdk_margin_trading.rest_api.models import MarginAccountBorrowRepayTypeEnum


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


def margin_account_borrow_repay():
    try:
        response = client.rest_api.margin_account_borrow_repay(
            asset="USDT",
            is_isolated=MarginAccountBorrowRepayIsIsolatedEnum["TRUE"].value,
            amount="1.0",
            type=MarginAccountBorrowRepayTypeEnum["BORROW"].value,
        )

        rate_limits = response.rate_limits
        logging.info(f"margin_account_borrow_repay() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"margin_account_borrow_repay() response: {data}")
    except Exception as e:
        logging.error(f"margin_account_borrow_repay() error: {e}")


if __name__ == "__main__":
    margin_account_borrow_repay()
