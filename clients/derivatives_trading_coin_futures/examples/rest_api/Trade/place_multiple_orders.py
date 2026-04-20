import os
import logging

from binance_sdk_derivatives_trading_coin_futures.derivatives_trading_coin_futures import (
    DerivativesTradingCoinFutures,
    ConfigurationRestAPI,
    DERIVATIVES_TRADING_COIN_FUTURES_REST_API_PROD_URL,
)

from binance_sdk_derivatives_trading_coin_futures.rest_api.models import (
    PlaceMultipleOrdersBatchOrdersParameterInner,
)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv(
        "BASE_PATH", DERIVATIVES_TRADING_COIN_FUTURES_REST_API_PROD_URL
    ),
)

# Initialize DerivativesTradingCoinFutures client
client = DerivativesTradingCoinFutures(config_rest_api=configuration_rest_api)


def place_multiple_orders():
    try:
        response = client.rest_api.place_multiple_orders(
            batch_orders=[
                PlaceMultipleOrdersBatchOrdersParameterInner(
                    symbol="",
                    side="BUY",
                    position_side="BOTH",
                    type="LIMIT",
                    time_in_force="GTC",
                    quantity="1.0",
                    reduce_only="False",
                    price="1.0",
                    new_client_order_id="1",
                    stop_price="1.0",
                    activation_price="1",
                    callback_rate="1.0",
                    working_type="MARK_PRICE",
                    price_protect="False",
                    new_order_resp_type="ACK",
                    price_match="NONE",
                    self_trade_prevention_mode="NONE",
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
