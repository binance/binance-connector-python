#!/usr/bin/env python

import logging
import asyncio
from binance.async_spot import AsyncSpot as Client
from binance.lib.utils import config_logging
from binance.error import ClientError

config_logging(logging, logging.DEBUG)

async def main():
    client = Client()

    try:
        response = await client.rolling_window_ticker("BNBUSDT", windowSize="1d", type="MINI")
        logging.info(response)
    except ClientError as error:
        logging.error(
            "Found error. status: {}, error code: {}, error message: {}".format(
                error.status_code, error.error_code, error.error_message
            )
        )


if __name__ == "__main__":
    asyncio.run(main())

