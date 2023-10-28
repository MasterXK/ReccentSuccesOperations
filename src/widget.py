from . import masks


def make_operation_name(operation: str) -> str:
    words = operation.split()
    name = []
    for word in words:
        if len(word) == 16 or len(word) == 20:
            for letter in word:
                if not letter.isdigit():
                    return 'Номер должен состоять из цифр'
            if len(word) == 16:
                name.append(masks.create_card_mask(int(word)))
            else:
                name.append(masks.create_account_mask(int(word)))
        else:
            name.append(word)
    return ' '.join(name)
