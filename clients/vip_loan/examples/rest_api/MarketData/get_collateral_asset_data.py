import os
import logging

from binance_sdk_vip_loan.vip_loan import (
    VipLoan,
    ConfigurationRestAPI,
    VIP_LOAN_REST_API_PROD_URL,
)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv("BASE_PATH", VIP_LOAN_REST_API_PROD_URL),
)

# Initialize VipLoan client
client = VipLoan(config_rest_api=configuration_rest_api)


def get_collateral_asset_data():
    try:
        response = client.rest_api.get_collateral_asset_data()

        rate_limits = response.rate_limits
        logging.info(f"get_collateral_asset_data() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"get_collateral_asset_data() response: {data}")
    except Exception as e:
        logging.error(f"get_collateral_asset_data() error: {e}")


if __name__ == "__main__":
    get_collateral_asset_data()
