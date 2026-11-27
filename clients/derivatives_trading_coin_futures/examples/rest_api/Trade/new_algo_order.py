import os
import logging

from binance_sdk_derivatives_trading_coin_futures.derivatives_trading_coin_futures import (
    DerivativesTradingCoinFutures,
    ConfigurationRestAPI,
    DERIVATIVES_TRADING_COIN_FUTURES_REST_API_PROD_URL,
)
from binance_sdk_derivatives_trading_coin_futures.rest_api.models import (
    NewAlgoOrderAlgoTypeEnum,
)
from binance_sdk_derivatives_trading_coin_futures.rest_api.models import (
    NewAlgoOrderSideEnum,
)
from binance_sdk_derivatives_trading_coin_futures.rest_api.models import (
    NewAlgoOrderTypeEnum,
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


def new_algo_order():
    try:
        response = client.rest_api.new_algo_order(
            algo_type=NewAlgoOrderAlgoTypeEnum["CONDITIONAL"].value,
            symbol="BTCUSD_PERP",
            side=NewAlgoOrderSideEnum["BUY"].value,
            type=NewAlgoOrderTypeEnum["STOP_MARKET"].value,
        )

        rate_limits = response.rate_limits
        logging.info(f"new_algo_order() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"new_algo_order() response: {data}")
    except Exception as e:
        logging.error(f"new_algo_order() error: {e}")


if __name__ == "__main__":
    new_algo_order()
