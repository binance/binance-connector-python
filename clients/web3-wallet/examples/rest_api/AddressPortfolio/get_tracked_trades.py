import os
import logging

from binance_sdk_web3_wallet.web3_wallet import (
    Web3Wallet,
    ConfigurationRestAPI,
    WEB3_WALLET_REST_API_PROD_URL,
)
from binance_sdk_web3_wallet.rest_api.models import GetTrackedTradesTrackerTypeEnum


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv("BASE_PATH", WEB3_WALLET_REST_API_PROD_URL),
)

# Initialize Web3Wallet client
client = Web3Wallet(config_rest_api=configuration_rest_api)


def get_tracked_trades():
    try:
        response = client.rest_api.get_tracked_trades(
            tracker_type=GetTrackedTradesTrackerTypeEnum["TRACKER_TYPE_1"].value,
        )

        rate_limits = response.rate_limits
        logging.info(f"get_tracked_trades() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"get_tracked_trades() response: {data}")
    except Exception as e:
        logging.error(f"get_tracked_trades() error: {e}")


if __name__ == "__main__":
    get_tracked_trades()
