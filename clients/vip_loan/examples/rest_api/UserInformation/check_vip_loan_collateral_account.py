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


def check_vip_loan_collateral_account():
    try:
        response = client.rest_api.check_vip_loan_collateral_account()

        rate_limits = response.rate_limits
        logging.info(f"check_vip_loan_collateral_account() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"check_vip_loan_collateral_account() response: {data}")
    except Exception as e:
        logging.error(f"check_vip_loan_collateral_account() error: {e}")


if __name__ == "__main__":
    check_vip_loan_collateral_account()
