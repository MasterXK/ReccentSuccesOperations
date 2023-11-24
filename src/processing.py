import re
import collections


def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Фунция фильтрует список операций по статутсу
    :param operations: список операций
    :param state: статус для фильтра
    :return: отфильтрованный список операций
    """
    return [operation for operation in operations if operation["state"] == state]


def sort_by_date(operations: list[dict], reverse_: bool = False) -> list[dict]:
    """
    Функция сортирует список операций по дате
    :param operations: список операций
    :param reverse_: флаг для сортировки по возрастанию
    :return: отсортированный список операций
    """
    return sorted(operations, key=lambda x: x["date"], reverse=reverse_)


def get_categories(transactions: list[dict]) -> dict:

