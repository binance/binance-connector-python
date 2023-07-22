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
    logging.info(
        await spot_client.sub_account_futures_asset_transfer(
            fromEmail="",
            toEmail="",
            futuresType=1,  # 1:USDT-maringed Futues，2: Coin-margined Futures
            asset="USDT",
            amount=0.01,
        )
    )


if __name__ == "__main__":
    asyncio.run(main())
