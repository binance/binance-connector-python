import os
import logging

from binance_sdk_derivatives_trading_options.derivatives_trading_options import (
    DerivativesTradingOptions,
    ConfigurationRestAPI,
    DERIVATIVES_TRADING_OPTIONS_REST_API_PROD_URL,
)

from binance_sdk_derivatives_trading_options.rest_api.models import (
    PlaceMultipleOrdersOrdersParameterInner,
)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv("BASE_PATH", DERIVATIVES_TRADING_OPTIONS_REST_API_PROD_URL),
)

# Initialize DerivativesTradingOptions client
client = DerivativesTradingOptions(config_rest_api=configuration_rest_api)


def place_multiple_orders():
    try:
        response = client.rest_api.place_multiple_orders(
            orders=[
                PlaceMultipleOrdersOrdersParameterInner(
                    symbol="",
                    side="BUY",
                    type="LIMIT",
                    quantity=1.0,
                    price=1.0,
                    time_in_force="GTC",
                    reduce_only=False,
                    post_only=False,
                    new_order_resp_type="ACK",
                    client_order_id="1",
                    is_mmp=True,
                )
            ],
        )

        rate_limits = response.rate_limits
        logging.info(f"place_multiple_orders() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"place_multiple_orders() response: {data}")
    except Exception as e:
        logging.error(f"place_multiple_orders() error: {e}")


if __name__ == "__main__":
    place_multiple_orders()
