import os
import logging

from binance_sdk_web3_wallet.web3_wallet import (
    Web3Wallet,
    ConfigurationRestAPI,
    WEB3_WALLET_REST_API_PROD_URL,
)
from binance_sdk_web3_wallet.rest_api.models import (
    BuildSolanaSwapInstructionsBinanceChainIdEnum,
)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv("BASE_PATH", WEB3_WALLET_REST_API_PROD_URL),
)

# Initialize Web3Wallet client
client = Web3Wallet(config_rest_api=configuration_rest_api)


def build_solana_swap_instructions():
    try:
        response = client.rest_api.build_solana_swap_instructions(
            binance_chain_id=BuildSolanaSwapInstructionsBinanceChainIdEnum[
                "CT_501"
            ].value,
            amount="12000000",
            from_token_address="EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
            to_token_address="So11111111111111111111111111111111111111112",
            slippage_percent="0.5",
            user_wallet_address="J5CBzXpcYn6WR2JBah8zU4Yxct985CAFGwXRcFaX2pbS",
            quote_id="a1b2c3d4e5f64a8b9c0d1e2f3a4b5c6d",
        )

        rate_limits = response.rate_limits
        logging.info(f"build_solana_swap_instructions() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"build_solana_swap_instructions() response: {data}")
    except Exception as e:
        logging.error(f"build_solana_swap_instructions() error: {e}")


if __name__ == "__main__":
    build_solana_swap_instructions()
