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


def move_position_for_sub_account():
    try:
        response = client.rest_api.move_position_for_sub_account(
            from_user_email="from_user_email_example",
            to_user_email="to_user_email_example",
            product_type="product_type_example",
            order_args=[None],
        )

        rate_limits = response.rate_limits
        logging.info(f"move_position_for_sub_account() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"move_position_for_sub_account() response: {data}")
    except Exception as e:
        logging.error(f"move_position_for_sub_account() error: {e}")


if __name__ == "__main__":
    move_position_for_sub_account()
