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


def get_categories(transactions: list[dict], key_word: str) -> dict:
    """
    Функция разбивает транзакции по категориям со словом search_str
    и считает количество транзакций в каждой полученной категории
    :param transactions: список транзакций
    :param key_word: ключевое слово
    :return: словарь {категория: количество}
    """
    suitable_descriptions = []
    pattern = re.compile(r'\b' + key_word.title() + r'\b')

    for transaction in transactions:
        try:
            if re.search(pattern, transaction['description']) is None:
                continue

            else:
                suitable_descriptions.append(transaction['description'])

        except KeyError as e:

            continue

    result = collections.Counter(suitable_descriptions)

    return dict(result)
