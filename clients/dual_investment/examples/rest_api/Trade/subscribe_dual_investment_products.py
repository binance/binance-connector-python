import os
import logging

from binance_sdk_dual_investment.dual_investment import (
    DualInvestment,
    ConfigurationRestAPI,
    DUAL_INVESTMENT_REST_API_PROD_URL,
)
from binance_sdk_dual_investment.rest_api.models import (
    SubscribeDualInvestmentProductsAutoCompoundPlanEnum,
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


def subscribe_dual_investment_products():
    try:
        response = client.rest_api.subscribe_dual_investment_products(
            id="741590",
            order_id="8257205859",
            deposit_amount=1,
            auto_compound_plan=SubscribeDualInvestmentProductsAutoCompoundPlanEnum[
                "NONE"
            ].value,
        )

        rate_limits = response.rate_limits
        logging.info(f"subscribe_dual_investment_products() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"subscribe_dual_investment_products() response: {data}")
    except Exception as e:
        logging.error(f"subscribe_dual_investment_products() error: {e}")


if __name__ == "__main__":
    subscribe_dual_investment_products()
