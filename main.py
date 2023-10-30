from src import masks, widget, processing


def main() -> None:
    card_number = 7000792289606361
    account_number = 73654108430135874305
    card_mask = masks.create_card_mask(card_number)
    account_mask = masks.create_account_mask(account_number)
    operations = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    products = [{'name': '', 'price': 10, 'category': 'q', 'quantity': 1},
                {'name': '', 'price': 25, 'category': 'w', 'quantity': 2},
                {'name': '', 'price': 12, 'category': 'q', 'quantity': 3},
                {'name': '', 'price': 55, 'category': 'e', 'quantity': 4},
                {'name': '', 'price': 6, 'category': 'q', 'quantity': 5}]
    orders = [{'id': '1', 'date': '2019-04-03T18:35:29.512364', 'items': [{'name': '', 'price': 1, 'quantity': 2}]},
                {'id': '2', 'date': '2019-05-03T18:35:29.512364', 'items': [{'name': '', 'price': 2, 'quantity': 3}]},
                {'id': '3', 'date': '2019-05-03T18:35:29.512364', 'items': [{'name': '', 'price': 3, 'quantity': 3}]},
                {'id': '4', 'date': '2019-07-03T18:35:29.512364', 'items': [{'name': '', 'price': 3, 'quantity': 2}]},
                {'id': '5', 'date': '2019-07-03T18:35:29.512364', 'items': [{'name': '', 'price': 10, 'quantity': 1}]}]
    for operation in processing.filter_by_state(operations):
        print(operation)
    print()
    for operation in processing.filter_by_state(operations, 'CANCELED'):
        print(operation)
    print()
    for operation in processing.sort_by_date(operations):
        print(operation)
    print()
    for operation in processing.sort_by_date(operations, True):
        print(operation)
    print()
    print(processing.get_months_statistic(orders))


if __name__ == "__main__":
    main()
