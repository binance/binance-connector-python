import os
import logging

from binance_sdk_dual_investment.dual_investment import (
    DualInvestment,
    ConfigurationRestAPI,
    DUAL_INVESTMENT_REST_API_PROD_URL,
)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv("BASE_PATH", DUAL_INVESTMENT_REST_API_PROD_URL),
)

# Initialize DualInvestment client
client = DualInvestment(config_rest_api=configuration_rest_api)


def get_dual_investment_positions():
    try:
        response = client.rest_api.get_dual_investment_positions()

        rate_limits = response.rate_limits
        logging.info(f"get_dual_investment_positions() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"get_dual_investment_positions() response: {data}")
    except Exception as e:
        logging.error(f"get_dual_investment_positions() error: {e}")


if __name__ == "__main__":
    get_dual_investment_positions()
