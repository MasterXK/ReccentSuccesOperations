from src import masks
from src import widget


def main():
    card_number = 7000792289606361
    account_number = 73654108430135874305
    card_mask = masks.create_card_mask(card_number)
    account_mask = masks.create_account_mask(account_number)
    print(card_mask)
    print(account_mask)
    print(masks.get_dir_content("."))
    print(masks.get_dir_content(".", True))
    print(widget.make_operation_name('Maestro 15968378687051l9'))
    print(widget.make_operation_name('Maestro 1596837868705119'))
    print(widget.make_operation_name('Visa Classic 6831982476737658'))
    print(widget.make_operation_name('Счет 35383033474447895560'))


if __name__ == "__main__":
    main()
