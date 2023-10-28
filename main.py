from src import masks


def main():
    card_number = 7000792289606361
    account_number = 73654108430135874305
    card_mask = masks.create_card_mask(card_number)
    account_mask = masks.create_account_mask(account_number)
    print(card_mask)
    print(account_mask)
    print(masks.get_dir_content("."))
    print(masks.get_dir_content(".", True))


if __name__ == "__main__":
    main()
