import re


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


def get_transactions_by_key(transactions: list[dict], key_word: str) -> list[dict]:
    """
    Функция ищет транзакци, в описании которых есть search_str и возвращает их список
    :param transactions: список транзакций
    :param key_word: ключевое слово
    :return: список транзакций
    """
    transactions_filtered = []
    pattern = re.compile(r'\b' + key_word.title() + r'\b')

    for transaction in transactions:
        try:
            if re.search(pattern, transaction['description']) is None:
                continue

            else:
                transactions_filtered.append(transaction)

        except KeyError:

            continue

    return transactions_filtered


def get_categories(transactions: list[dict], categories: dict[str, int]) -> dict:
    """
    Функция делит транзакции по описанию на категории
    и считает количество транзакций в каждой категории
    :param categories: словарь с категориями
    :param transactions: список транзакций
    :return: словарь {категория: количество}
    """
    if all([type(x) is int for x in categories.values()]):
        for transaction in transactions:
            for category in categories:
                try:
                    if category in transaction['description']:
                        categories[category] += 1

                    else:
                        continue

                except KeyError:

                    continue

    return categories
