import os
import logging

from binance_sdk_sub_account.sub_account import (
    SubAccount,
    ConfigurationRestAPI,
    SUB_ACCOUNT_REST_API_PROD_URL,
)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv("BASE_PATH", SUB_ACCOUNT_REST_API_PROD_URL),
)

# Initialize SubAccount client
client = SubAccount(config_rest_api=configuration_rest_api)


def get_futures_position_risk_of_sub_account_v2():
    try:
        response = client.rest_api.get_futures_position_risk_of_sub_account_v2(
            email="sub-account-email@email.com",
            futures_type=56,
        )

        rate_limits = response.rate_limits
        logging.info(
            f"get_futures_position_risk_of_sub_account_v2() rate limits: {rate_limits}"
        )

        data = response.data()
        logging.info(f"get_futures_position_risk_of_sub_account_v2() response: {data}")
    except Exception as e:
        logging.error(f"get_futures_position_risk_of_sub_account_v2() error: {e}")


if __name__ == "__main__":
    get_futures_position_risk_of_sub_account_v2()
