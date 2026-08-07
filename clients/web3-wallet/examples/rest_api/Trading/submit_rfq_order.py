import os
import logging

from binance_sdk_web3_wallet.web3_wallet import (
    Web3Wallet,
    ConfigurationRestAPI,
    WEB3_WALLET_REST_API_PROD_URL,
)
from binance_sdk_web3_wallet.rest_api.models import SubmitRfqOrderVendorEnum


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


def submit_rfq_order():
    try:
        response = client.rest_api.submit_rfq_order(
            request_id="request_id_example",
            user_signature="user_signature_example",
            vendor=SubmitRfqOrderVendorEnum["vendor_example"].value,
            quote_id="quote_id_example",
        )

        rate_limits = response.rate_limits
        logging.info(f"submit_rfq_order() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"submit_rfq_order() response: {data}")
    except Exception as e:
        logging.error(f"submit_rfq_order() error: {e}")


if __name__ == "__main__":
    submit_rfq_order()
