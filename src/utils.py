import json
import os

import pandas as pd

from src.logger import setup_logger

logger = setup_logger()


def read_json(json_path: str) -> list[dict]:
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
        logger.error(f"Ошибка: {e}")
        return []

    except FileNotFoundError as e:
        logger.error(f"Ошибка: {e}")
        return []

    if type(json_content) is list:
        logger.debug("Данные верны")
        return json_content

    logger.error("Ошибка: в файле не список")
    return []


def get_sum(transaction: dict) -> float:
    """
    Функция выводит транзакцию в рублях
    :param transaction: транзакция
    :return: сумма транзакции
    """
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])

    raise ValueError("Транзация выполнена не в рублях. " "Укажите транзакцию в рублях.")


def read_table(file_path: str) -> str | None:
    if not os.path.exists(file_path):
        logger.error("Файл не найден")
        return None

    _, ext = os.path.splitext(file_path)

    if ext == ".csv":
        data = pd.read_csv(file_path)

    elif ext in [".xls", ".xlsx"]:
        data = pd.read_excel(file_path)

    else:
        logger.error("Неизвестное расширение файла")
        return None

    return data.to_json(orient="records", force_ascii=False)
