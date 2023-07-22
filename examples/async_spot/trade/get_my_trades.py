#!/usr/bin/env python

import logging
import asyncio
from binance.async_spot import AsyncSpot as Client
from binance.lib.utils import config_logging
from examples.utils.prepare_env import get_api_key

config_logging(logging, logging.DEBUG)

async def main():
    api_key, api_secret = get_api_key()

    client = Client(api_key, api_secret, base_url="https://testnet.binance.vision")
    logging.info(await client.my_trades("BTCUSDT"))

    # set the limit
    logging.info(await client.my_trades("BTCUSDT", limit=2))

    # set the fromId
    logging.info(await client.my_trades("BTCUSDT", fromId="10"))

    # set startTime and endTime
    logging.info(
        await client.my_trades(
            "BTCUSDT", limit=2, startTime="1585282456000", endTime="1585368856000"
        )
    )


if __name__ == "__main__":
    asyncio.run(main())
