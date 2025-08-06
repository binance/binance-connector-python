# Binance Python Margin Trading SDK

[![Build Status](https://img.shields.io/github/actions/workflow/status/binance/binance-connector-python/ci.yaml)](https://github.com/binance/binance-connector-python/actions)
[![Open Issues](https://img.shields.io/github/issues/binance/binance-connector-python)](https://github.com/binance/binance-connector-python/issues)
[![Code Style: Black](https://img.shields.io/badge/code_style-black-black)](https://black.readthedocs.io/en/stable/)
[![PyPI version](https://img.shields.io/pypi/v/binance-sdk-margin-trading)](https://pypi.python.org/pypi/binance-sdk-margin-trading)
[![PyPI Downloads](https://img.shields.io/pypi/dm/binance-sdk-margin-trading.svg)](https://pypi.org/project/binance-sdk-margin-trading/)
[![Python version](https://img.shields.io/pypi/pyversions/binance-sdk-margin-trading)](https://www.python.org/downloads/)
[![Known Vulnerabilities](https://img.shields.io/badge/security-scanned-brightgreen)](https://github.com/binance/binance-connector-python/security)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is a client library for the Binance Margin Trading SDK API, enabling developers to interact programmatically with Binance's Margin Trading trading platform. The library provides tools to use funds provided by a third party to conduct asset transactions through the REST API:

- [REST API](./src/binance_sdk_margin_trading/rest_api/rest_api.py)
- [Websocket Stream](./src/binance_sdk_margin_trading/websocket_streams/websocket_streams.py)

## Table of Contents

- [Supported Features](#supported-features)
- [Installation](#installation)
- [Documentation](#documentation)
- [REST APIs](#rest-apis)
- [Websocket Streams](#websocket-streams)
- [Testing](#testing)
- [Migration Guide](#migration-guide)
- [Contributing](#contributing)
- [Licence](#licence)

## Supported Features

- REST API Endpoints:
  - `/sapi/v1/margin/*`
  - `/sapi/v1/bnbBurn/*`
  - `/sapi/v1/userDataStream/*`
- Inclusion of test cases and examples for quick onboarding.

## Installation

To use this library, ensure your environment is running Python version **3.9** or later.

```bash
pip install binance-sdk-margin-trading
```

## Documentation

For detailed information, refer to the [Binance API Documentation](https://developers.binance.com/docs/margin_trading/Introduction).

### REST APIs

All REST API endpoints are available through the [`rest_api`](./src/binance_sdk_margin_trading/rest_api/rest_api.py) module. The REST API enables you to fetch market data, manage trades, and access account information. Note that some endpoints require authentication using your Binance API credentials.

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_common.constants import MARGIN_TRADING_REST_API_PROD_URL
from binance_sdk_margin_trading.margin_trading import MarginTrading
from binance_sdk_margin_trading.rest_api.models import GetSummaryOfMarginAccountResponse

logging.basicConfig(level=logging.INFO)
configuration = ConfigurationRestAPI(api_key="your-api-key", api_secret="your-api-secret", base_path=MARGIN_TRADING_REST_API_PROD_URL)

client = MarginTrading(config_rest_api=configuration)

try:
    response = client.rest_api.get_summary_of_margin_account()

    data: GetSummaryOfMarginAccountResponse = response.data()
    logging.info(f"get_summary_of_margin_account() response: {data}")
except Exception as e:
    logging.error(f"get_summary_of_margin_account() error: {e}")
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

If `base_path` is not provided, it defaults to `https://api.binance.com`.

### Websocket Streams

WebSocket Streams in margin-trading is used for subscribing to risk and trade data streams. Use the [websocket-streams](./src/binance_sdk_margin_trading/websocket_streams/websocket_streams.py) module to interact with it.

#### Configuration Options

The WebSocket Streams API supports the following advanced configuration options:

- `reconnect_delay`: Delay (ms) between reconnections.
- `compression`: Enable response compression.
- `mode`: Choose between `single` and `pool` connection modes.
  - `single`: A single WebSocket connection.
  - `pool`: A pool of WebSocket connections.
- `pool_size`: Define the number of WebSocket connections in pool mode.
- `https_agent`: Custom HTTPS agent for advanced TLS configuration.
- `user_agent`: Custom user agent string for WebSocket Streams.

#### Subscribe to Risk and Trade Data Streams

You can consume the risk and trade data stream, which sends account-level events such as account and order updates. First create a listen-key via REST API; then:

```python
import asyncio
import logging

from binance_common.configuration import ConfigurationWebSocketStreams
from binance_common.constants import MARGIN_TRADING_WS_STREAMS_PROD_URL
from binance_sdk_margin_trading.margin_trading import MarginTrading

logging.basicConfig(level=logging.INFO)

configuration_ws_streams = ConfigurationWebSocketStreams(
    reconnect_delay=5000,
)

client = MarginTrading(config_ws_streams=configuration_ws_streams)

connection = None
try:
    connection = await client.websocket_streams.create_connection()

    stream = await connection.tradeData(listenKey="listen-key")
    stream.on("message", lambda data: {
        match data["e"]:
            case "balanceUpdate":
                print(f"Risk level change stream: {data}")
            case 'outboundAccountPosition':
                print(f"outbound account position stream {data}");
                break;
            # …handle other variants…
            case _:
                print(f"Unknown stream: {data}")
    })
except Exception as e:
    logging.error(f"Error in user data stream: {e}")
```

#### Unsubscribing from Streams

You can unsubscribe from specific WebSocket streams using the `unsubscribe` method. This is useful for managing active subscriptions without closing the connection.

```python
import asyncio
import logging

from binance_common.configuration import ConfigurationWebSocketStreams
from binance_sdk_margin_trading.margin_trading import MarginTrading

logging.basicConfig(level=logging.INFO)

client = MarginTrading(config_ws_streams=ConfigurationWebSocketStreams())

try:
    connection = await client.websocket_streams.create_connection()
    stream = connection.tradeData(listenKey="listen-key")
    stream.on("message", lambda data: {
        match data["e"]:
            case "riskLevelChange":
                print(f"Risk level change stream: {data}")
            case _:
                print(f"Unknown stream: {data}")
    })
    await asyncio.sleep(10)
    await stream.unsubscribe()
except Exception as e:
    logging.error(f"Error in user data stream: {e}")
finally:
    if connection:
        await connection.close_connection(close_session=True)
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

The tests cover:
* REST API endpoints
* Streams endpoints
* Error handling
* Edge cases

## Migration Guide

If you are upgrading to the new modularized structure, refer to the [Migration Guide](./docs/migration_guide_margin_trading_sdk.md) for detailed steps.

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
