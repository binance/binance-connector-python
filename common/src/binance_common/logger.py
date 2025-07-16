import logging
from enum import Enum


class LogLevel(Enum):
    NONE = 0
    DEBUG = 10
    INFO = 20
    WARN = 30
    ERROR = 40


class Logger:
    _instance = None

    def __init__(self):
        """Ensure only one instance is initialized."""
        if not Logger._instance:
            Logger._instance = self
            self._initialize()
        else:
            self.__dict__ = Logger._instance.__dict__  # Share attributes

    @classmethod
    def get_instance(cls):
        """Retrieve or initialize the singleton logger."""
        if not cls._instance:
            cls._instance = cls()
        return cls._instance

    def _initialize(self):
        """Initialize the logger settings."""
        self._logger = logging.getLogger("ConnectorLogger")

        # Prevent duplicate handlers if logger is re-initialized
        if not self._logger.hasHandlers():
            handler = logging.StreamHandler()
            formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s")
            handler.setFormatter(formatter)
            self._logger.addHandler(handler)

        self._logger.setLevel(LogLevel.INFO.value)
        self.min_log_level = LogLevel.INFO

    def set_min_log_level(self, level: LogLevel):
        """Set the minimum log level."""
        if not isinstance(level, LogLevel):
            raise ValueError(f"Invalid log level: {level}")
        self.min_log_level = level
        self._logger.setLevel(level.value)

    def debug(self, *message):
        if self._allow_level_log(LogLevel.DEBUG):
            self._logger.debug(" ".join(map(str, message)))

    def info(self, *message):
        if self._allow_level_log(LogLevel.INFO):
            self._logger.info(" ".join(map(str, message)))

    def warn(self, *message):
        if self._allow_level_log(LogLevel.WARN):
            self._logger.warning(" ".join(map(str, message)))

    def error(self, *message):
        if self._allow_level_log(LogLevel.ERROR):
            self._logger.error(" ".join(map(str, message)))

    def _allow_level_log(self, level: LogLevel) -> bool:
        return level.value >= self.min_log_level.value
