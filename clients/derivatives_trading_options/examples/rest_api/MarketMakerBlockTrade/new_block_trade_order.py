import os
import logging

from binance_sdk_derivatives_trading_options.derivatives_trading_options import (
    DerivativesTradingOptions,
    ConfigurationRestAPI,
    DERIVATIVES_TRADING_OPTIONS_REST_API_PROD_URL,
)
from binance_sdk_derivatives_trading_options.rest_api.models import (
    NewBlockTradeOrderSideEnum,
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


def new_block_trade_order():
    try:
        response = client.rest_api.new_block_trade_order(
            liquidity="liquidity_example",
            legs=[
                [
                    {
                        "symbol": "BTC-210115-35000-C",
                        "price": "100",
                        "quantity": "0.0002",
                        "side": "BUY",
                        "type": "LIMIT",
                    }
                ]
            ],
            symbol="symbol_example",
            side=NewBlockTradeOrderSideEnum["BUY"].value,
            price=1.0,
            quantity=1.0,
        )

        rate_limits = response.rate_limits
        logging.info(f"new_block_trade_order() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"new_block_trade_order() response: {data}")
    except Exception as e:
        logging.error(f"new_block_trade_order() error: {e}")


if __name__ == "__main__":
    new_block_trade_order()
