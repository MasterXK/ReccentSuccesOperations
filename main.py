import os.path
from pprint import pprint

from data import PATH_DATA
from src import processing as pr
from src import utils as ut


def main() -> None:
    data = ut.read_json(os.path.join(PATH_DATA, 'operations.json'))
    descriptions = pr.get_transactions_by_key(data, 'перевод')
    pprint(descriptions)

    categories = {'Перевод': 0, 'Открытие': 0}
    
    categories_count = pr.get_categories(data, categories)
    pprint(categories_count)


if __name__ == '__main__':
    main()
