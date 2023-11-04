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


if __name__ == '__main__':
    transactions = (
        [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                    "amount": "9824.07",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            },
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {
                    "amount": "79114.93",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188"
            },
            {
                "id": 873106923,
                "state": "EXECUTED",
                "date": "2019-03-23T01:09:46.296404",
                "operationAmount": {
                    "amount": "43318.34",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 44812258784861134719",
                "to": "Счет 74489636417521191160"
            },
            {
                "id": 895315941,
                "state": "EXECUTED",
                "date": "2018-08-19T04:27:37.904916",
                "operationAmount": {
                    "amount": "56883.54",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод с карты на карту",
                "from": "Visa Classic 6831982476737658",
                "to": "Visa Platinum 8990922113665229"
            },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
                "operationAmount": {
                    "amount": "67314.70",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод организации",
                "from": "Visa Platinum 1246377376343588",
                "to": "Счет 14211924144426031657"
            }
        ]
    )
    usd_transactions = filter_by_currency(transactions, "USD")

    for _ in range(2):
        print(next(usd_transactions)["id"])

    descriptions = transaction_descriptions(transactions)
    for _ in range(5):
        print(next(descriptions))

    for card_number in card_number_generator(1, 5):
        print(card_number)
