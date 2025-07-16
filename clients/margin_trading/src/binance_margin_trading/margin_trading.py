import platform
from importlib.metadata import version

from binance_common.configuration import (
    ConfigurationRestAPI,
    ConfigurationWebSocketStreams,
)
from binance_common.constants import (
    MARGIN_TRADING_REST_API_PROD_URL,
    MARGIN_TRADING_WS_STREAMS_PROD_URL,
)
from . import metadata
from .rest_api import MarginTradingRestAPI
from .websocket_streams import MarginTradingWebSocketStreams

LIB_NAME = metadata.NAME
LIB_VERSION = version(LIB_NAME)


class MarginTrading:
    """MarginTrading API that exposes REST, and Stream APIs in a single interface."""

    def __init__(
        self,
        config_rest_api: ConfigurationRestAPI = None,
        config_ws_streams: ConfigurationWebSocketStreams = None,
    ) -> None:
        self._rest_api = None
        self._rest_api_config = (
            ConfigurationRestAPI() if config_rest_api is None else config_rest_api
        )
        self._websocket_streams = None
        self._websocket_streams_config = (
            ConfigurationWebSocketStreams()
            if config_ws_streams is None
            else config_ws_streams
        )

    @property
    def rest_api(self) -> MarginTradingRestAPI:
        if self._rest_api is None and self._rest_api_config:
            self._rest_api_config.base_headers["User-Agent"] = (
                f"{LIB_NAME}/{LIB_VERSION} (Python/{platform.python_version()}; {platform.system()}; {platform.machine()})"
            )
            self._rest_api_config.base_path = (
                MARGIN_TRADING_REST_API_PROD_URL
                if self._rest_api_config.base_path is None
                else self._rest_api_config.base_path
            )
            self._rest_api = MarginTradingRestAPI(self._rest_api_config)
        return self._rest_api

    @property
    def websocket_streams(self) -> MarginTradingWebSocketStreams:
        if self._websocket_streams is None and self._websocket_streams_config:
            self._websocket_streams_config.user_agent = f"{LIB_NAME}/{LIB_VERSION} (Python/{platform.python_version()}; {platform.system()}; {platform.machine()})"
            self._websocket_streams_config.stream_url = (
                MARGIN_TRADING_WS_STREAMS_PROD_URL
                if self._websocket_streams_config.stream_url is None
                else self._websocket_streams_config.stream_url
            )
            self._websocket_streams = MarginTradingWebSocketStreams(
                self._websocket_streams_config
            )

        return self._websocket_streams
