import datetime

from . import masks


def make_operation_name(operation: str) -> str:
    """
    Функция создает сообщение операции
    :param operation: операция с номером карты(счета)
    :return: сообщение с маской карты(счета)
    """
    words = operation.split()
    for letter in words[-1]:
        if not letter.isdigit():
            return "Номер должен состоять из цифр"
    if len(words[-1]) == 16:
        words[-1] = masks.create_card_mask(int(words[-1]))
    else:
        words[-1] = masks.create_account_mask(int(words[-1]))
    return " ".join(words)


def get_date(date_time: str) -> str:
    """
    Функция переформатирует дату
    :param date: Дата для изменения
    :return: Отформатированная дата
    """
    pattern_in = "%Y-%m-%dT%H:%M:%S.%f"
    pattern_out = "%d.%m.%Y"
    date = datetime.datetime.strptime(date_time, pattern_in)
    return datetime.datetime.strftime(date, pattern_out)
