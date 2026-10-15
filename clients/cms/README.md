# Binance Python CMS SDK

[![Build Status](https://img.shields.io/github/actions/workflow/status/binance/binance-connector-python/ci.yaml)](https://github.com/binance/binance-connector-python/actions)
[![Open Issues](https://img.shields.io/github/issues/binance/binance-connector-python)](https://github.com/binance/binance-connector-python/issues)
[![Code Style: Black](https://img.shields.io/badge/code_style-black-black)](https://black.readthedocs.io/en/stable/)
[![PyPI version](https://img.shields.io/pypi/v/binance-sdk-cms)](https://pypi.python.org/pypi/binance-sdk-cms)
[![PyPI Downloads](https://img.shields.io/pypi/dm/binance-sdk-cms.svg)](https://pypi.org/project/binance-sdk-cms/)
[![Python version](https://img.shields.io/pypi/pyversions/binance-sdk-cms)](https://www.python.org/downloads/)
[![Known Vulnerabilities](https://img.shields.io/badge/security-scanned-brightgreen)](https://github.com/binance/binance-connector-python/security)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is a client library for the Binance CMS API, enabling developers to receive Binance announcements programmatically. The library provides real-time push notifications for new Binance announcements through the WebSocket Streams:

- [WebSocket Streams](./src/binance_sdk_cms/websocket_streams/websocket_streams.py)

## Table of Contents

- [Supported Features](#supported-features)
- [Installation](#installation)
- [Documentation](#documentation)
- [Websocket Streams](#websocket-streams)
- [Testing](#testing)
- [Contributing](#contributing)
- [Licence](#licence)

## Supported Features

- WebSocket Streams:
  - Real-time push notifications for Binance announcements (`com_announcement_en`).
- Inclusion of test cases and examples for quick onboarding.

## Installation

To use this library, ensure your environment is running Python version **3.10** or later.

```bash
pip install binance-sdk-cms
```

## Documentation

For detailed information, refer to the [Binance API Documentation](https://developers.binance.com/docs/cms).

### Websocket Streams

WebSocket Streams push a notification each time Binance publishes an announcement. Use the [websocket-streams](./src/binance_sdk_cms/websocket_streams/websocket_streams.py) module to subscribe to these streams.

The streams are signed: provide your Binance API credentials in the configuration. The connection URL is signed again on every connect and reconnect.

```python
import asyncio
import logging

from binance_common.configuration import ConfigurationWebSocketStreams
from binance_common.constants import CMS_WS_STREAMS_PROD_URL
from binance_sdk_cms.cms import Cms

logging.basicConfig(level=logging.INFO)

configuration_ws_streams = ConfigurationWebSocketStreams(
    api_key="your-api-key",
    api_secret="your-api-secret",
    stream_url=CMS_WS_STREAMS_PROD_URL,
)

client = Cms(config_ws_streams=configuration_ws_streams)


async def com_announcement_en():
    connection = None
    try:
        connection = await client.websocket_streams.create_connection()

        stream = await connection.com_announcement_en()
        stream.on("message", lambda data: print(f"{data}"))

        await asyncio.sleep(5)
    except Exception as e:
        logging.error(f"com_announcement_en() error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


if __name__ == "__main__":
    asyncio.run(com_announcement_en())
```

More examples are available in the [`examples/websocket_streams`](./examples/websocket_streams/) folder.

#### Configuration Options

The WebSocket Streams API supports the following advanced configuration options:

- `api_key`: Binance API key, sent with every connection.
- `api_secret`: Binance API secret, used to sign the connection URL.
- `private_key`: RSA or ED25519 private key, used to sign the connection URL instead of `api_secret`.
- `private_key_passphrase`: Passphrase for the private key, if encrypted.
- `reconnect_delay`: Delay (ms) between reconnections.
- `reconnect_attempts`: Maximum number of WebSocket reconnection attempts (max: 10).
- `compression`: Enable response compression.
- `mode`: Choose between `single` and `pool` connection modes.
  - `single`: A single WebSocket connection.
  - `pool`: A pool of WebSocket connections.
- `pool_size`: Define the number of WebSocket connections in pool mode.
- `proxy`: Proxy configuration (`host`, `port`, `protocol` and `auth`).
- `https_agent`: Custom HTTPS agent for advanced TLS configuration.
- `user_agent`: Custom user agent string for WebSocket Streams.

##### Key Pair Based Authentication

The WebSocket Streams support key pair-based authentication. You can use `RSA` or `ED25519` keys to sign the connection URL. See the [Key Pair Based Authentication example](./docs/websocket_streams/key-pair-authentication.md) for detailed usage.

##### Reconnect Delay

Specify the delay in milliseconds between WebSocket reconnection attempts for streams. See the [Reconnect Delay example](./docs/websocket_streams/reconnect-delay.md) for detailed usage.

##### Websocket Reconnect Attempts

Specify how many times a failed reconnection is retried before the connection is given up on. A value between `1` and `10` is accepted. See the [Reconnect Attempts example](./docs/websocket_streams/reconnect_attempts.md) for detailed usage.

##### Compression

Enable or disable compression for WebSocket Streams messages. See the [Compression example](./docs/websocket_streams/compression.md) for detailed usage.

##### Connection Mode

Choose between `single` and `pool` connection modes for WebSocket Streams. The `single` mode uses a single WebSocket connection, while the `pool` mode uses a pool of WebSocket connections. See the [Connection Mode example](./docs/websocket_streams/connection-mode.md) for detailed usage.

##### Proxy

The WebSocket Streams support HTTP/HTTPS proxy configurations. See the [Proxy example](./docs/websocket_streams/proxy.md) for detailed usage.

##### WebSocket Http Agent

Customize the agent for advanced configurations. See the [WebSocket Http Agent example](./docs/websocket_streams/agent.md) for detailed usage.

#### Unsubscribing from Streams

You can unsubscribe from specific WebSocket streams using the `unsubscribe` method. This is useful for managing active subscriptions without closing the connection.

```python
async def com_announcement_en():
    connection = None
    try:
        connection = await client.websocket_streams.create_connection()

        stream = await connection.com_announcement_en()
        stream.on("message", lambda data: print(f"{data}"))

        await asyncio.sleep(5)
        await stream.unsubscribe()
    except Exception as e:
        logging.error(f"com_announcement_en() error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)
```

## Testing

To run the tests, ensure you have [Poetry](https://python-poetry.org/) installed, then execute the following commands:

```bash
poetry install
poetry run pytest ./tests
```

The tests cover:
* WebSocket Streams endpoints
* Error handling
* Edge cases

## Contributing

Contributions are welcome!

Since this repository contains auto-generated code, we encourage you to start by opening a GitHub issue to discuss your ideas or suggest improvements. This helps ensure that changes align with the project's goals and auto-generation processes.

To contribute:

1. Open a GitHub issue describing your suggestion or the bug you've identified.
2. If it's determined that changes are necessary, the maintainers will merge the changes into the main branch.

Please ensure that all tests pass if you're making a direct contribution. Submit a pull request only after discussing and confirming the change.

Thank you for your contributions!

## Disclaimer

This SDK is provided by Binance on an "as is" and "as available" basis for use at your own risk. Binance makes no representations or warranties of any kind, whether express or implied, as to the operation of the SDK, its accuracy, reliability, completeness, or fitness for any particular purpose.

To the fullest extent permitted by law, Binance shall not be liable for any losses, damages, or expenses of any kind arising from or in connection with your use of, or inability to use, this SDK, including but not limited to any financial losses resulting from errors, bugs, interruptions, or inaccuracies in the SDK.

Your use of this SDK to access the Binance Platform is subject to the Binance API Key Terms and the Binance Terms of Use, which shall prevail in the event of any conflict with this disclaimer. You are solely responsible for any orders or transactions executed through the Binance Platform using this SDK.

This SDK is not intended to constitute investment advice or a recommendation to buy, sell, or hold any digital asset. You should independently evaluate and verify all information before acting.

- [Binance Terms of Use](https://www.binance.com/en/terms)
- [Binance API Key Terms](https://www.binance.com/en/about-legal/terms-binance-api)

## Licence

This project is licensed under the MIT License. See the [LICENCE](./LICENCE) file for details.
