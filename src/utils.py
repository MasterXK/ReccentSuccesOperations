import json
import os

import pandas as pd

from src.logger import setup_logger

logger = setup_logger()


def read_json(json_path: str | os.PathLike) -> list[dict]:
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


def read_table(file_path: str | os.PathLike) -> dict | None:
    """
    Функция считывает данные из тублиц .csv и .xlsx(.xls)
    :param file_path: путь до файла с таблицей
    :return: объект Python
    """
    if not os.path.exists(file_path):
        logger.error("Файл не найден")
        return None

    _, ext = os.path.splitext(file_path)

    if ext == ".csv":
        data = pd.read_csv(file_path, encoding="UTF-8", sep=";")

    elif ext in [".xls", ".xlsx"]:
        data = pd.read_excel(file_path)

    else:
        logger.error("Неизвестное расширение файла")
        return None

    df_operation_amount = data.loc[:, ["amount", "currency_name", "currency_code"]]
    data.drop(["amount", "currency_code", "currency_name"], axis=1, inplace=True)

    return_data: dict = json.loads(data.to_json(orient="records", force_ascii=False))

    for i in range(len(return_data)):
        amount, name, code = df_operation_amount.iloc[i]
        return_data[i]["operationAmount"] = {"amount": amount, "currency": {"name": name, "code": code}}

    return return_data
