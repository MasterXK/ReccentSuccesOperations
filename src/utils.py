import json
import os

from src.logger import setup_logger

logger = setup_logger()


def get_info(json_path: str) -> list[dict]:
    """
    Функция считывает содержимое json-файла
    :param json_path: пабсолютный путь до json-а
    :return: содержимое json
    """
    try:
        with open(json_path, encoding="UTF-8") as json_file:
            json_content = json.load(json_file)
            logger.debug("Получены данные")

    except json.JSONDecodeError as e:
        logger.debug(f"Ошибка: {e}")
        return []

    except FileNotFoundError as e:
        logger.debug(f"Ошибка: {e}")
        return []

    if type(json_content) is list:
        logger.debug("Данные верны")
        return json_content

    logger.debug("Ошибка: в файле не список")
    return []


def get_transaction_sum(transaction: dict) -> float:
    """
    Функция выводит транзакцию в рублях
    :param transaction: транзакция
    :return: сумма транзакции
    """
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])

    raise ValueError("Транзация выполнена не в рублях. Укажите транзакцию в рублях")
