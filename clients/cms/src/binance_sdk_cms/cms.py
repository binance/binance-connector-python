import platform
from importlib.metadata import version

from binance_common.configuration import (
    ConfigurationWebSocketStreams,
)
from binance_common.constants import (
    CMS_WS_STREAMS_PROD_URL,
)
from . import metadata
from .websocket_streams import CmsWebSocketStreams

LIB_NAME = metadata.NAME
LIB_VERSION = version(LIB_NAME)


class Cms:
    """Cms API that exposes Stream APIs in a single interface."""

    def __init__(
        self,
        config_ws_streams: ConfigurationWebSocketStreams = None,
    ) -> None:
        self._websocket_streams = None
        self._websocket_streams_config = (
            ConfigurationWebSocketStreams()
            if config_ws_streams is None
            else config_ws_streams
        )

    @property
    def websocket_streams(self) -> CmsWebSocketStreams:
        if self._websocket_streams is None and self._websocket_streams_config:
            self._websocket_streams_config.user_agent = f"{LIB_NAME}/{LIB_VERSION} (Python/{platform.python_version()}; {platform.system()}; {platform.machine()})"
            self._websocket_streams_config.stream_url = (
                CMS_WS_STREAMS_PROD_URL
                if self._websocket_streams_config.stream_url is None
                else self._websocket_streams_config.stream_url
            )
            self._websocket_streams = CmsWebSocketStreams(
                self._websocket_streams_config
            )

        return self._websocket_streams
