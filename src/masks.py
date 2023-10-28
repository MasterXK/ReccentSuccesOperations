import os


def create_card_mask(card_number: int) -> str:
    """Создает маску для карты с пробелами"""
    number_list = list(str(card_number))
    for i in range(len(number_list)):
        if 5 < i < 12:
            number_list[i] = "*"

    for i in range(4):
        # вставляем пробел помле каждого 4 знака
        number_list.insert(i * 4 + i, " ")
    del number_list[0]

    card_mask = "".join(number_list)
    return card_mask


def create_account_mask(account_number: int) -> str:
    """Создает маску для счета"""
    account_mask = f"**{account_number % 10000}"
    return account_mask


def get_dir_content(path: str = ".", count_all: bool = False) -> dict:
    """Считает количество директорий и файлов.
    Есди стоит флаг count_all, считает в глубину"""
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
