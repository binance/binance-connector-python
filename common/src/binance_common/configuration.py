import ssl

from typing import Optional, Dict, Union
from http.client import HTTPSConnection

from binance_common.constants import TimeUnit, WebsocketMode


class ConfigurationRestAPI:
    """
    Configuration for the Binance REST API client.

    Supports:
    - API authentication
    - Keep-Alive
    - Timeout handling
    - Compression (gzip, deflate, br)
    - HTTPS Agent
    - Time Unit
    - Proxy support
    - Retries & Backoff
    """

    def __init__(
        self,
        api_key: str = None,
        api_secret: Optional[str] = None,
        base_path: str = None,
        timeout: int = 1000,
        proxy: Optional[Dict[str, Union[str, int, Dict[str, str]]]] = None,
        keep_alive: bool = True,
        compression: bool = True,
        retries: int = 3,
        backoff: int = 1000,
        https_agent: Optional[Union[bool, HTTPSConnection]] = None,
        time_unit: Optional[str] = None,
        private_key: Optional[Union[bytes, str]] = None,
        private_key_passphrase: Optional[str] = None,
    ):
        """
        Initialize the API configuration.

        Args:
            api_key (str): API key for authentication.
            api_secret (Optional[str]): API secret for authentication (default: None).
            base_path (str): Base API URL (default: None).
            timeout (int): Request timeout in milliseconds (default: 1000).
            proxy (Optional[Dict[str, Union[str, int, Dict[str, str]]]]): Proxy settings (default: None).
            keep_alive (bool): Enable Keep-Alive (default: True).
            compression (bool): Enable response compression (default: True).
            retries (int): Number of retry attempts for failed requests (default: 3).
            backoff (int): Delay (ms) between retries (default: 1000).
            https_agent (Optional[Union[bool, HTTPSConnection]]): Custom HTTPS Agent (default: None).
            time_unit (Optional[str]): Time unit for time-based responses (default: None).
            private_key (Optional[Union[bytes, str]]): Private key for authentication (default: None).
            private_key_passphrase (Optional[str]): Passphrase for private key (default: None).
        """

        self.api_key = api_key
        self.api_secret = api_secret
        self.base_path = base_path
        self.timeout = timeout
        self.proxy = proxy
        self.keep_alive = keep_alive
        self.compression = compression
        self.retries = retries
        self.backoff = backoff
        self.https_agent = https_agent
        self.time_unit = time_unit
        self.private_key = private_key
        self.private_key_passphrase = private_key_passphrase

        self.base_headers = {
            "Accept": "application/json",
            "X-MBX-APIKEY": str(self.api_key) if self.api_key else "",
        }


class ConfigurationWebSocketAPI:
    """
    Configuration for the Binance Websocket API client.

    Supports:
    - API authentication
    - Keep-Alive
    - Timeout handling
    - Compression (gzip, deflate, br)
    - HTTPS Agent
    - WebSocket Pool
    - Time Unit
    - Proxy support
    """

    def __init__(
        self,
        api_key: str = None,
        api_secret: Optional[str] = None,
        private_key: Optional[Union[bytes, str]] = None,
        private_key_passphrase: Optional[str] = None,
        stream_url: str = "wss://ws-api.binance.com/ws-api/v3",
        timeout: int = 5,
        reconnect_delay: int = 5,
        compression: int = 0,
        proxy: Optional[Dict[str, Union[str, int, Dict[str, str]]]] = None,
        mode: WebsocketMode = WebsocketMode.SINGLE,
        pool_size: int = 2,
        time_unit: TimeUnit = None,
        https_agent: Optional[ssl.SSLContext] = None,
    ):
        """
        Initialize the API configuration.

        Args:
            api_key (str): API key for authentication.
            api_secret (Optional[str]): API secret for authentication (default: None).
            private_key (Optional[Union[bytes, str]]): Private key for authentication (default: None).
            private_key_passphrase (Optional[str]): Passphrase for private key (default: None).
            stream_url (str): Base WebSocket API URL (default: "wss://ws-api.binance.com/ws-api/v3").
            timeout (int): Request timeout in milliseconds (default: 5000).
            reconnect_delay (int): Delay (ms) between reconnections (default: 5000).
            compression (int): Compression level (default: 0).
            proxy (Optional[Dict[str, Union[str, int, Dict[str, str]]]]): Proxy settings (default: None).
            mode (WebsocketMode): WebSocket mode ("single" or "pool") (default: "single").
            pool_size (int): Number of WebSocket connections in pool (default: 2).
            time_unit (Optional[TimeUnit]): Time unit for time-based responses (default: None).
            https_agent (Optional[ssl.SSLContext]): Custom HTTPS Agent (default: None).
        """

        self.api_key = api_key
        self.api_secret = api_secret
        self.private_key = private_key
        self.private_key_passphrase = private_key_passphrase
        self.stream_url = stream_url
        self.timeout = timeout
        self.reconnect_delay = reconnect_delay
        self.compression = compression
        self.proxy = proxy
        self.mode = mode
        self.pool_size = pool_size
        self.time_unit = time_unit
        self.https_agent = https_agent
        self.user_agent = ""


class ConfigurationWebSocketStreams:
    """
    Configuration for the Binance Websocket Stream client.

    Supports:
    - Keep-Alive
    - Compression (gzip, deflate, br)
    - HTTPS Agent
    - WebSocket Pool
    - Time Unit
    """

    def __init__(
        self,
        stream_url: str = "wss://stream.binance.com:9443/stream",
        reconnect_delay: int = 5,
        compression: int = 0,
        proxy: Optional[Dict[str, Union[str, int, Dict[str, str]]]] = None,
        mode: WebsocketMode = WebsocketMode.SINGLE,
        pool_size: int = 2,
        time_unit: TimeUnit = None,
        https_agent: Optional[ssl.SSLContext] = None,
    ):
        """
        Initialize the Websocket Stream configuration.

        Args:
            stream_url (str): Base WebSocket Stream URL (default: "wss://stream.binance.com:9443").
            reconnect_delay (int): Delay (ms) between reconnections (default: 5000).
            compression (int): Compression level (default: 0).
            proxy (Optional[Dict[str, Union[str, int, Dict[str, str]]]]): Proxy settings (default: None).
            mode (WebsocketMode): WebSocket mode ("single" or "pool") (default: "single").
            pool_size (int): Number of WebSocket connections in pool (default: 2).
            time_unit (Optional[TimeUnit]): Time unit for time-based responses (default: None).
            https_agent (Optional[ssl.SSLContext]): Custom HTTPS Agent (default: None).
        """

        self.stream_url = stream_url
        self.reconnect_delay = reconnect_delay
        self.compression = compression
        self.proxy = proxy
        self.mode = mode
        self.pool_size = pool_size
        self.time_unit = time_unit
        self.https_agent = https_agent
        self.user_agent = ""
