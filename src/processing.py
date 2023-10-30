from datetime import datetime


def filter_by_state(operations: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """
    Фунция фильтрует список операций по статутсу
    :param operations: список операций
    :param state: статус для фильтра
    :return: отфильтрованный список операций
    """
    return [operation for operation in operations if operation['state'] == state]


def sort_by_date(operations: list[dict], reverse_: bool = False) -> list[dict]:
    """
    Функция сортирует список операций по дате
    :param operations: список операций
    :param reverse_: флаг для сортировки по возрастанию
    :return: отсортированный список операций
    """
    return sorted(operations, key=lambda x: x['date'], reverse=reverse_)


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
