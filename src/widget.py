from . import masks
import datetime


def make_operation_name(operation: str) -> str:
    """ Создает сообщение с названием карты и маской счета
        Возвращает: сообщение с типом карты(счета) и маской"""
    words = operation.split()
    for letter in words[-1]:
        if not letter.isdigit():
            return 'Номер должен состоять из цифр'
    if len(words[-1]) == 16:
        words[-1] = masks.create_card_mask(int(words[-1]))
    else:
        words[-1] = masks.create_account_mask(int(words[-1]))
    return ' '.join(words)


def get_date(date_time: str) -> str:
    """ преобраззует сообщение datetime-формата к DD.MM.YY
        Возвращает: сообщение вида DD.MM.YY """
    pattern_in = '%Y-%m-%dT%H:%M:%S.%f'
    pattern_out = '%d.%m.%Y'
    date = datetime.datetime.strptime(date_time, pattern_in)
    return datetime.datetime.strftime(date, pattern_out)


def get_simillar_start_end_words(words: list[str]) -> list[str]:
    """ Фильтрует список слов
        Возвращает: список слов с одиннаковой буквой в начале и конце"""
    simillar_start_end_words = []
    if words:
        for word in words:
            if word:
                if word[0] == word[-1]:
                    simillar_start_end_words.append(word)
        return simillar_start_end_words
    return []


def get_max_multiply(numbers: list[int]) -> int:
    """ Ищет максимальное произведение чисел
        Возвращает: масимальное произведение"""
    nums = sorted(numbers)
    if len(nums) < 2:
        return 0
    if nums[-1] * nums[-2] > nums[0] * nums[1]:
        return nums[-1] * nums[-2]
    return nums[0] * nums[1]
