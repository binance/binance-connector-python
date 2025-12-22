import os
import logging

from binance_sdk_derivatives_trading_usds_futures.derivatives_trading_usds_futures import (
    DerivativesTradingUsdsFutures,
    ConfigurationRestAPI,
    DERIVATIVES_TRADING_USDS_FUTURES_REST_API_PROD_URL,
)

from binance_sdk_derivatives_trading_usds_futures.rest_api.models import (
    ModifyMultipleOrdersBatchOrdersParameterInner,
)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv(
        "BASE_PATH", DERIVATIVES_TRADING_USDS_FUTURES_REST_API_PROD_URL
    ),
)

# Initialize DerivativesTradingUsdsFutures client
client = DerivativesTradingUsdsFutures(config_rest_api=configuration_rest_api)


def modify_multiple_orders():
    try:
        response = client.rest_api.modify_multiple_orders(
            batch_orders=[
                ModifyMultipleOrdersBatchOrdersParameterInner(
                    order_id="1",
                    orig_client_order_id="1",
                    symbol="",
                    side="BUY",
                    quantity="1.0",
                    price="1.0",
                    price_match="NONE",
                    recv_window="5000",
                )
            ],
        )

        rate_limits = response.rate_limits
        logging.info(f"modify_multiple_orders() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"modify_multiple_orders() response: {data}")
    except Exception as e:
        logging.error(f"modify_multiple_orders() error: {e}")


if __name__ == "__main__":
    modify_multiple_orders()
