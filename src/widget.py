from . import masks
import datetime


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


def get_date(date_time: str) -> str:
    pattern_in = '%Y-%m-%dT%H:%M:%S.%f'
    pattern_out = '%d.%m.%Y'
    date = datetime.datetime.strptime(date_time, pattern_in) # 2018-07-11T02:26:18.671407 %Y-%m-%d %H:%M:%S.%f
    return datetime.datetime.strftime(date, pattern_out)
