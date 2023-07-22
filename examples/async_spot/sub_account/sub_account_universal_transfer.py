#!/usr/bin/env python

import logging
import asyncio
from binance.async_spot import AsyncSpot as Client
from binance.lib.utils import config_logging
from examples.utils.prepare_env import get_api_key

config_logging(logging, logging.DEBUG)

async def main():
    api_key, api_secret = get_api_key()

    spot_client = Client(api_key, api_secret)

    # From master account to sub-account alice@test.com
    logging.info(
        await spot_client.sub_account_universal_transfer(
            toEmail="alice@test.com",
            fromAccountType="SPOT",
            toAccountType="USDT_FUTURE",
            asset="USDT",
            amount=1,
            clientTranId="test",
        )
    )


if __name__ == "__main__":
    asyncio.run(main())
