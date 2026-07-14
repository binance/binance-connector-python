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


def vip_loan_fixed_rate_borrow():
    try:
        response = client.rest_api.vip_loan_fixed_rate_borrow(
            supply_request="1212:0.12:100;3434:0.13:50",
            borrow_coin="BUSD",
            loan_term=30,
            borrow_uid=12345678,
            collateral_coin="BNB,ETH,BTC",
            collateral_account_id="12345,67890,13579",
        )

        rate_limits = response.rate_limits
        logging.info(f"vip_loan_fixed_rate_borrow() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"vip_loan_fixed_rate_borrow() response: {data}")
    except Exception as e:
        logging.error(f"vip_loan_fixed_rate_borrow() error: {e}")


if __name__ == "__main__":
    vip_loan_fixed_rate_borrow()
