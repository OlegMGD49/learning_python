import logging
import os
import sys
from logging.handlers import RotatingFileHandler
from typing import Union, Optional

from logger.logger_config import LoggerConfig


class Logger:
    __logger: Optional[logging.Logger] = None

    @classmethod
    def _init_logger(cls):
        if cls.__logger:
            return

        if not os.path.isdir(LoggerConfig.LOGS_DIR_NAME):
            os.makedirs(LoggerConfig.LOGS_DIR_NAME)

        logger = logging.getLogger(LoggerConfig.LOGGER_NAME)
        logger.setLevel(LoggerConfig.LOGS_LEVEL)

        file_handler = RotatingFileHandler(
            LoggerConfig.LOGS_FILE_NAME,
            maxBytes=LoggerConfig.MAX_BYTES,
            backupCount=LoggerConfig.BACKUP_COUNT
        )

        stream_handler = logging.StreamHandler(sys.stdout)

        formatter = logging.Formatter(
            fmt=LoggerConfig.FORMAT,
            datefmt=LoggerConfig.DATETIME_FORMAT
        )

        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

        cls.__logger = logger

    @staticmethod
    def _get_logger() -> logging.Logger:
        Logger._init_logger()
        return Logger.__logger

    @staticmethod
    def set_level(level: Union[str, int]) -> None:
        Logger._get_logger().setLevel(level)

    @staticmethod
    def info(message: str) -> None:
        Logger._get_logger().info(msg=message)

    @staticmethod
    def debug(message: str) -> None:
        Logger._get_logger().debug(msg=message)

    @staticmethod
    def warning(message: str) -> None:
        Logger._get_logger().warning(msg=message)

    @staticmethod
    def error(message: str) -> None:
        Logger._get_logger().error(msg=message)

    @staticmethod
    def critical(message: str) -> None:
        Logger._get_logger().critical(msg=message)
