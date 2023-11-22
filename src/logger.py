import logging
import os
from logging import Logger

from data import PATH_DATA


def setup_logger(name: str = __name__) -> Logger:
    """
    Функция создает экземпляр Logger
    :param name:
    :return: Logger
    """
    logger = logging.getLogger(name)

    file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
    file_handler = logging.FileHandler(os.path.join(os.getcwd(), PATH_DATA, "logs.log"), "w")

    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    logger.setLevel(logging.DEBUG)

    return logger
