import os
from datetime import datetime


def get_dir_content(path: str = ".", count_all: bool = False) -> dict:
    """
    Функция считает количество директорий и файлов.
    :param path: директория для подсчета
    :param count_all: флаг для подсчета в глубину
    :return: словарь с количеством директорий и файлов
    """
    content = {"files": 0, "folders": 0}
    for dir_path, dir_names, file_names in os.walk(path):
        # перебираем каталоги
        for dir_name in dir_names:
            content["folders"] += 1
        # перебираем файлы
        for file_name in file_names:
            content["files"] += 1
        if not count_all:
            break
    return content


def get_similar_start_end_words(words: list[str]) -> list[str]:
    """
    Функция фильтрует список слов
    :param words: список слов
    :return: список слов с одиннаковой буквой в начале и конце
        """
    simillar_start_end_words = []
    if words:
        for word in words:
            if word:
                if word[0] == word[-1]:
                    simillar_start_end_words.append(word)
        return simillar_start_end_words
    return []


def get_max_multiply(numbers: list[int]) -> int:
    """
    Функция ищет максимальное произведение двух чисел
    :param numbers: список чисел
    :return: масимальное произведение
    """
    nums = sorted(numbers)
    if len(nums) < 2:
        return 0
    if nums[-1] * nums[-2] > nums[0] * nums[1]:
        return nums[-1] * nums[-2]
    return nums[0] * nums[1]


def sort_by_price(products: list[dict], category: str = None) -> list[dict]:
    """
    Функция сортирует продукты по цене
    :param products: список продуктов
    :param category: категория продуктов для сортировки
    :return: отсортированный список продуктов выбранной категории
    """
    if category:
        products_to_sort = [product for product in products if product['category'] == category]
        return sorted(products_to_sort, key=lambda x: x['price'], reverse=True)

    return sorted(products, key=lambda x: x['price'], reverse=True)


def get_months_statistic(orders: list[dict]) -> dict:
    """
    Функция получает статистику заказов по месяцам
    :param orders: список заказов
    :return:
    """
    months_statistic: dict[str, dict] = {}
    pattern_in = '%Y-%m-%dT%H:%M:%S.%f'
    pattern_out = '%Y.%m'

    for order in orders:
        date_in = datetime.strptime(order['date'], pattern_in)
        date = date_in.strftime(pattern_out)

        if date in months_statistic.keys():
            months_statistic[date]['order_count'] += 1
            for item in order['items']:
                months_statistic[date]['average_order_value'] += item['price'] * item['quantity']
        else:
            for item in order['items']:
                months_statistic[date] = {'average_order_value': item['price'] * item['quantity'], 'order_count': 1}

    for month in months_statistic.values():
        month['average_order_value'] /= month['order_count']

    return months_statistic
