#!/usr/bin/env python

import logging
import asyncio
from binance.async_spot import AsyncSpot as Client
from binance.lib.utils import config_logging
from examples.utils.prepare_env import get_api_key

config_logging(logging, logging.DEBUG)

async def main():
    # HMAC authentication with API key and secret
    api_key, api_secret = get_api_key()

    client = Client(api_key, api_secret, base_url="https://testnet.binance.vision")
    logging.info(await client.account(recvWindow=6000))


    # RSA authentication with RSA key
    api_key = ""
    with open("/Users/john/ssl/private_key.pem", "r") as f:
        private_key = f.read()

    client = Client(
        api_key, base_url="https://testnet.binance.vision", private_key=private_key
    )
    logging.info(await client.account())


    api_key = ""
    with open("/Users/john/ssl/private_key.pem", "r") as f:
        private_key = f.read()

    client = Client(
        api_key=api_key,
        base_url="https://testnet.binance.vision",
        private_key=private_key,
        private_key_pass="password",
    )
    logging.info(await client.account())


if __name__ == "__main__":
    asyncio.run(main())
