from typing import Generator


def filter_by_currency(_transactions: list[dict], currency: str = "USD") -> filter:
    """
    Функция создает итератор операций, в которых указана заданная валюта
    :param _transactions: список операций
    :param currency: валюта для фильтра
    :return: операция
    """
    return filter(lambda x: x['operationAmount']['currency']['code'] == currency, _transactions)


def transaction_descriptions(_transactions: list[dict]) -> Generator:
    """
    Функция создает итератор описания операций
    :param _transactions: список операций
    :return: описания операции
    """
    return (x['description'] for x in _transactions)


def card_number_generator(start: int, end: int) -> Generator:
    """
    Функция генерирует номер карты
    :param start: начальное значение
    :param end: конечное значение
    :return: номер карты
    """
    for number in range(start, end + 1):
        _card_number = ['0'] * 16
        digit = -1
        while number > 0:
            _card_number[digit] = str(number % 10)
            number //= 10
            digit -= 1

        for i in range(4):
            _card_number.insert(i * 4 + i, " ")
        del _card_number[0]
        yield ''.join(_card_number)
