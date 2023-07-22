#!/usr/bin/env python

import logging
import asyncio
from binance.async_spot import AsyncSpot as Client
from binance.lib.utils import config_logging
from examples.utils.prepare_env import get_api_key

config_logging(logging, logging.DEBUG)

async def main():
    api_key, api_secret = get_api_key()


    client = Client(api_key, api_secret)
    logging.info(
        await client.loan_adjust_ltv(
            orderId=756783308056935434, amount=5.235, direction="ADDITIONAL"
        )
    )


if __name__ == "__main__":
    asyncio.run(main())


