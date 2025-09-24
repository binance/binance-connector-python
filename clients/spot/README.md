# Binance Python SPOT SDK

[![Build Status](https://img.shields.io/github/actions/workflow/status/binance/binance-connector-python/ci.yaml)](https://github.com/binance/binance-connector-python/actions)
[![Open Issues](https://img.shields.io/github/issues/binance/binance-connector-python)](https://github.com/binance/binance-connector-python/issues)
[![Code Style: Black](https://img.shields.io/badge/code_style-black-black)](https://black.readthedocs.io/en/stable/)
[![PyPI version](https://img.shields.io/pypi/v/binance-sdk-spot)](https://pypi.python.org/pypi/binance-sdk-spot)
[![PyPI Downloads](https://img.shields.io/pypi/dm/binance-sdk-spot.svg)](https://pypi.org/project/binance-sdk-spot/)
[![Python version](https://img.shields.io/pypi/pyversions/binance-sdk-spot)](https://www.python.org/downloads/)
[![Known Vulnerabilities](https://img.shields.io/badge/security-scanned-brightgreen)](https://github.com/binance/binance-connector-python/security)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is a client library for the Binance Spot SDK API, enabling developers to interact programmatically with Binance's SPOT trading platform. The library provides tools for retrieving market data, executing trades, and managing orders through three distinct endpoints:

- [REST API](./src/binance_sdk_spot/rest_api/rest_api.py)
- [Websocket API](./src/binance_sdk_spot/websocket_api/websocket_api.py)
- [Websocket Stream](./src/binance_sdk_spot/websocket_streams/websocket_streams.py)

## Table of Contents

- [Supported Features](#supported-features)
- [Installation](#installation)
- [Documentation](#documentation)
- [REST APIs](#rest-apis)
- [Websocket APIs](#websocket-apis)
- [Websocket Streams](#websocket-streams)
- [Testing](#testing)
- [Migration Guide](#migration-guide)
- [Contributing](#contributing)
- [Licence](#licence)

## Supported Features

- REST API Endpoints:
  - `/api/*`
- WebSocket Endpoints: Real-time data streaming and request-response communication.
- Inclusion of test cases and examples for quick onboarding.

## Installation

To use this library, ensure your environment is running Python version **3.9** or later.

```bash
pip install binance-sdk-spot
```

## Documentation

For detailed information, refer to the [Binance API Documentation](https://developers.binance.com/docs/binance-spot-api-docs/README).

### REST APIs

All REST API endpoints are available through the [`rest_api`](./src/binance_sdk_spot/rest_api/rest_api.py) module. The REST API enables you to fetch market data, manage trades, and access account information. Note that some endpoints require authentication using your Binance API credentials.

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_common.constants import SPOT_REST_API_PROD_URL
from binance_sdk_spot.spot import Spot
from binance_sdk_spot.rest_api.models import ExchangeInfoResponse, RateLimits

logging.basicConfig(level=logging.INFO)
configuration = ConfigurationRestAPI(api_key="your-api-key", api_secret="your-api-secret", base_path=SPOT_REST_API_PROD_URL)

client = Spot(config_rest_api=configuration)

try:
    response = client.rest_api.exchange_info(symbol="BNBUSDT")

    rate_limits: List[RateLimits] = response.rate_limits
    logging.info(f"exchange_info() rate limits: {rate_limits}")

    data: ExchangeInfoResponse = response.data()
    logging.info(f"exchange_info() response: {data}")
except Exception as e:
    logging.error(f"exchange_info() error: {e}")
```

More examples can be found in the [`examples/rest_api`](./examples/rest_api/) folder.

#### Configuration Options

The REST API supports the following advanced configuration options:

- `timeout`: Timeout for requests in milliseconds (default: 1000 ms).
- `proxy`: Proxy configuration:
  - `host`: Proxy server hostname.
  - `port`: Proxy server port.
  - `protocol`: Proxy protocol (http or https).
  - `auth`: Proxy authentication credentials:
    - `username`: Proxy username.
    - `password`: Proxy password.
- `keep_alive`: Enable HTTP keep-alive (default: true).
- `compression`: Enable response compression (default: true).
- `retries`: Number of retry attempts for failed requests (default: 3).
- `backoff`: Delay in milliseconds between retries (default: 1000 ms).
- `https_agent`: Custom HTTPS agent for advanced TLS configuration.
- `time_unit`: Specify the time unit for timestamps (e.g., milliseconds or microseconds).
- `private_key`: RSA or ED25519 private key for authentication.
- `private_key_passphrase`: Passphrase for the private key, if encrypted.

##### Timeout

You can configure a timeout for requests in milliseconds. If the request exceeds the specified timeout, it will be aborted. See the [Timeout example](./docs/rest_api/timeout.md) for detailed usage.

##### Proxy

The REST API supports HTTP/HTTPS proxy configurations. See the [Proxy example](./docs/rest_api/proxy.md) for detailed usage.

##### Keep-Alive

Enable HTTP keep-alive for persistent connections. See the [Keep-Alive example](./docs/rest_api/keepAlive.md) for detailed usage.

##### Compression

Enable or disable response compression. See the [Compression example](./docs/rest_api/compression.md) for detailed usage.

##### Retries

Configure the number of retry attempts and delay in milliseconds between retries for failed requests. See the [Retries example](./docs/rest_api/retries.md) for detailed usage.

##### HTTPS Agent

Customize the HTTPS agent for advanced TLS configurations. See the [HTTPS Agent example](./docs/rest_api/httpsAgent.md) for detailed usage.

##### Key Pair Based Authentication

The REST API supports key pair-based authentication for secure communication. You can use `RSA` or `ED25519` keys for signing requests. See the [Key Pair Based Authentication example](./docs/rest_api/key-pair-authentication.md) for detailed usage.

##### Time Unit

The REST API supports different time units for timestamp values. See the [Time Unit example](./docs/rest_api/time-unit.md) for more details.

##### Certificate Pinning

To enhance security, you can use certificate pinning with the `https_agent` option in the configuration. This ensures the client only communicates with servers using specific certificates. See the [Certificate Pinning example](./docs/rest_api/certificate-pinning.md) for detailed usage.

#### Error Handling

The REST API provides detailed error types to help you handle issues effectively:

- `ClientError`: Represents an error that occurred in the SDK client.
- `RequiredError`: Thrown when a required parameter is missing or undefined.
- `UnauthorizedError`: Indicates missing or invalid authentication credentials.
- `ForbiddenError`: Access to the requested resource is forbidden.
- `TooManyRequestsError`: Rate limit exceeded.
- `RateLimitBanError`: IP address banned for exceeding rate limits.
- `ServerError`: Internal server error, optionally includes a status code.
- `NetworkError`: Issues with network connectivity.
- `NotFoundError`: Resource not found.
- `BadRequestError`: Invalid request or one that cannot be served.

See the [Error Handling example](./docs/rest_api/error-handling.md) for detailed usage.

#### Testnet

For testing purposes, `/api/*` endpoints can be used in the [Spot Testnet](https://testnet.binance.vision/). Update the `base_path` in your configuration:

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_common.constants import SPOT_REST_API_TESTNET_URL
from binance_sdk_spot.spot import Spot

configuration = ConfigurationRestAPI(api_key="your-api-key", api_secret="your-api-secret", base_path=SPOT_REST_API_TESTNET_URL)
client = Spot(config_rest_api=configuration)
```

If `base_path` is not provided, it defaults to `https://api.binance.com`.

### Websocket APIs

The WebSocket API provides request-response communication for market data and trading actions. Use the [`websocket_api`](./src/binance_sdk_spot/websocket_api/websocket_api.py) module to interact with these endpoints.

```python
import asyncio
import logging

from binance_common.configuration import ConfigurationWebSocketAPI
from binance_common.constants import SPOT_WS_API_PROD_URL
from binance_sdk_spot.spot import Spot
from binance_sdk_spot.websocket_api.models import AccountCommissionResponse

logging.basicConfig(level=logging.INFO)

configuration_ws_api = ConfigurationWebSocketAPI(api_key="your-api-key", api_secret="your-api-secret", stream_url=SPOT_WS_API_PROD_URL)
client = Spot(config_ws_api=configuration_ws_api)

async def exchange_info():
    connection = None
    try:
        connection = await client.websocket_api.create_connection()

        response = await connection.account_commission(
            symbol="BNBUSDT",
        )
        result: AccountCommissionResponse = response.data()
        print(f"Exchange Info: {result}")

    except Exception as e:
        print(f"exchange_info() error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)

if __name__ == "__main__":
    asyncio.run(exchange_info())
```

More examples are available in the [`examples/websocket_api`](./examples/websocket_api/) folder.

#### Configuration Options

The WebSocket API supports the following advanced configuration options:

- `timeout`: Set the timeout for WebSocket requests (default: 5000 ms).
- `reconnect_delay`: Delay (ms) between reconnections.
- `compression`: Enable response compression.
- `proxy`: Proxy configuration:
  - `host`: Proxy server hostname.
  - `port`: Proxy server port.
  - `protocol`: Proxy protocol (http or https).
  - `auth`: Proxy authentication credentials:
    - `username`: Proxy username.
    - `password`: Proxy password.
- `mode`: Choose between `single` and `pool` connection modes.
  - `single`: A single WebSocket connection.
  - `pool`: A pool of WebSocket connections.
- `pool_size`: Define the number of WebSocket connections in pool mode.
- `time_unit`: Specify the time unit for timestamps (e.g., milliseconds or microseconds).
- `private_key`: RSA or ED25519 private key for authentication.
- `private_key_passphrase`: Passphrase for the private key, if encrypted.
- `https_agent`: Custom HTTPS agent for advanced TLS configuration.
- `user_agent`: Custom user agent string for WebSocket Streams.

##### Timeout

Set the timeout for WebSocket API requests in milliseconds. See the [Timeout example](./docs/websocket_api/timeout.md) for detailed usage.

##### Reconnect Delay

Specify the delay in milliseconds between WebSocket reconnection attempts. See the [Reconnect Delay example](./docs/websocket_api/reconnect-delay.md) for detailed usage.

##### Compression

Enable or disable compression for WebSocket messages. See the [Compression example](./docs/websocket_api/compression.md) for detailed usage.

##### Proxy

The WebSocket API supports HTTP/HTTPS proxy configurations. See the [Proxy example](./docs/websocket_api/proxy.md) for detailed usage.


##### Connection Mode

Choose between `single` and `pool` connection modes for WebSocket connections. The `single` mode uses a single WebSocket connection, while the `pool` mode uses a pool of WebSocket connections. See the [Connection Mode example](./docs/websocket_api/connection-mode.md) for detailed usage.

##### Time Unit

Specify the time unit for WebSocket API timestamps (e.g., milliseconds or microseconds). See the [Time Unit example](./docs/websocket_api/time-unit.md) for detailed usage.

##### Key Pair Based Authentication

Use RSA or ED25519 private keys for WebSocket API authentication. See the [Key Pair Authentication example](./docs/websocket_api/key-pair-authentication.md) for detailed usage.

##### WebSocket Http Agent

Customize the agent for advanced configurations. See the [WebSocket Http Agent example](./docs/websocket_api/agent.md) for detailed usage.

#### Testnet

For testing purposes, the Websocket API also supports a testnet environment. Update the `wsURL` in your configuration:

```python
from binance_common.configuration import ConfigurationWebSocketAPI
from binance_common.constants import SPOT_WS_API_TESTNET_URL
from binance_sdk_spot.spot import Spot

configuration_ws_api = ConfigurationWebSocketAPI(
    api_key="your-api-key",
    api_secret="your-api-secret",
    stream_url=SPOT_WS_API_TESTNET_URL
)
client = Spot(config_ws_api=configuration_ws_api)
```

If `wsURL` is not provided, it defaults to `wss://ws-api.binance.com:443/ws-api/v3`.

### Websocket Streams

WebSocket Streams provide real-time data feeds for market trades, candlesticks, and more. Use the [websocket-streams](./src/binance_sdk_spot/websocket_streams/websocket_streams.py) module to subscribe to these streams.

```python
import asyncio
import logging

from binance_common.configuration import ConfigurationWebSocketStreams
from binance_common.constants import SPOT_WS_STREAMS_PROD_URL
from binance_sdk_spot.spot import Spot

logging.basicConfig(level=logging.INFO)

configuration_ws_streams = ConfigurationWebSocketStreams(
    stream_url=SPOT_WS_STREAMS_PROD_URL,
)

client = Spot(config_ws_streams=configuration_ws_streams)


async def agg_trade():
    connection = None
    try:
        connection = await client.websocket_streams.create_connection()

        stream = await connection.agg_trade(
            symbol="bnbusdt",
        )
        stream.on("message", lambda data: print(f"{data}"))

        await asyncio.sleep(5)
        await stream.unsubscribe()
    except Exception as e:
        logging.error(f"agg_trade() error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


if __name__ == "__main__":
    asyncio.run(agg_trade())
```

More examples are available in the [`examples/websocket-streams`](./examples/websocket_streams/) folder.

#### Configuration Options

The WebSocket Streams API supports the following advanced configuration options:

- `reconnect_delay`: Delay (ms) between reconnections.
- `compression`: Enable response compression.
- `proxy`: Proxy configuration:
  - `host`: Proxy server hostname.
  - `port`: Proxy server port.
  - `protocol`: Proxy protocol (http or https).
  - `auth`: Proxy authentication credentials:
    - `username`: Proxy username.
    - `password`: Proxy password.
- `mode`: Choose between `single` and `pool` connection modes.
  - `single`: A single WebSocket connection.
  - `pool`: A pool of WebSocket connections.
- `pool_size`: Define the number of WebSocket connections in pool mode.
- `time_unit`: Specify the time unit for timestamps (e.g., milliseconds or microseconds).
- `https_agent`: Custom HTTPS agent for advanced TLS configuration.
- `user_agent`: Custom user agent string for WebSocket Streams.

##### Reconnect Delay

Specify the delay in milliseconds between WebSocket reconnection attempts for streams. See the [Reconnect Delay example](./docs/websocket_streams/reconnect-delay.md) for detailed usage.

##### Compression

Enable or disable compression for WebSocket Streams messages. See the [Compression example](./docs/websocket_streams/compression.md) for detailed usage.

##### Proxy

The WebSocket Streams supports HTTP/HTTPS proxy configurations. See the [Proxy example](./docs/websocket_streams/proxy.md) for detailed usage.

##### Connection Mode

Choose between `single` and `pool` connection modes for WebSocket Streams. The `single` mode uses a single WebSocket connection, while the `pool` mode uses a pool of WebSocket connections. See the [Connection Mode example](./docs/websocket_streams/connection-mode.md) for detailed usage.

##### Time Unit

Specify the time unit for WebSocket Streams timestamps (e.g., milliseconds or microseconds). See the [Time Unit example](./docs/websocket_streams/time-unit.md) for detailed usage.

##### WebSocket Http Agent

Customize the agent for advanced configurations. See the [WebSocket Http Agent example](./docs/websocket_streams/agent.md) for detailed usage.

#### Unsubscribing from Streams

You can unsubscribe from specific WebSocket streams using the `unsubscribe` method. This is useful for managing active subscriptions without closing the connection.

```python
import asyncio
import logging

from binance_common.configuration import ConfigurationWebSocketStreams
from binance_sdk_spot.spot import Spot

logging.basicConfig(level=logging.INFO)

client = Spot(config_ws_streams=ConfigurationWebSocketStreams())


async def agg_trade():
    connection = None
    try:
        connection = await client.websocket_streams.create_connection()

        stream = await connection.agg_trade(
            symbol="bnbusdt",
        )
        stream.on("message", lambda data: print(f"{data}"))

        await asyncio.sleep(5)
        await stream.unsubscribe()
    except Exception as e:
        logging.error(f"agg_trade() error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


if __name__ == "__main__":
    asyncio.run(agg_trade())
```

#### Testnet

Websocket Streams also support a testnet environment for development and testing. Update the `wsURL` in your configuration:

```python
from binance_common.configuration import ConfigurationWebSocketStreams
from binance_common.constants import SPOT_WS_API_TESTNET_URL
from binance_sdk_spot.spot import Spot

config_ws_streams = ConfigurationWebSocketStreams(
    stream_url=SPOT_WS_STREAMS_TESTNET_URL
)

client = Spot(config_ws_streams=config_ws_streams)
```

If `wsURL` is not provided, it defaults to `wss://stream.binance.com:9443`.

### Automatic Connection Renewal

The WebSocket connection is automatically renewed for both WebSocket API and WebSocket Streams connections, before the 24 hours expiration of the API key. This ensures continuous connectivity.

## Testing

To run the tests, ensure you have [Poetry](https://python-poetry.org/) installed, then execute the following commands:

```bash
poetry install
poetry run pytest ./tests
```

The tests cover: - REST API endpoints - WebSocket API and Streams - Error handling and edge cases

## Migration Guide

If you are upgrading to the new modularized structure, refer to the [Migration Guide](./docs/migration_guide_spot_sdk.md) for detailed steps.

## Contributing

Contributions are welcome!

Since this repository contains auto-generated code, we encourage you to start by opening a GitHub issue to discuss your ideas or suggest improvements. This helps ensure that changes align with the project's goals and auto-generation processes.

To contribute:

1. Open a GitHub issue describing your suggestion or the bug you've identified.
2. If it's determined that changes are necessary, the maintainers will merge the changes into the main branch.

Please ensure that all tests pass if you're making a direct contribution. Submit a pull request only after discussing and confirming the change.

Thank you for your contributions!

## Licence

This project is licensed under the MIT License. See the [LICENCE](./LICENCE) file for details.
