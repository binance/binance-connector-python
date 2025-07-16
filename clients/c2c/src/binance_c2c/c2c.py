import platform
from importlib.metadata import version

from binance_common.configuration import ConfigurationRestAPI
from binance_common.constants import C2C_REST_API_PROD_URL
from . import metadata
from .rest_api import C2CRestAPI

LIB_NAME = metadata.NAME
LIB_VERSION = version(LIB_NAME)


class C2C:
    """C2C API that exposes REST APIs in a single interface."""

    def __init__(self, config_rest_api: ConfigurationRestAPI = None) -> None:
        self._rest_api = None
        self._rest_api_config = (
            ConfigurationRestAPI() if config_rest_api is None else config_rest_api
        )

    @property
    def rest_api(self) -> C2CRestAPI:
        if self._rest_api is None and self._rest_api_config:
            self._rest_api_config.base_headers["User-Agent"] = (
                f"{LIB_NAME}/{LIB_VERSION} (Python/{platform.python_version()}; {platform.system()}; {platform.machine()})"
            )
            self._rest_api_config.base_path = (
                C2C_REST_API_PROD_URL
                if self._rest_api_config.base_path is None
                else self._rest_api_config.base_path
            )
            self._rest_api = C2CRestAPI(self._rest_api_config)
        return self._rest_api
