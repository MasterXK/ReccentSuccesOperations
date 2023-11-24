import os.path
from pprint import pprint

from src import processing as pr, utils as ut
from data import PATH_DATA


def main() -> None:
    data = ut.read_json(os.path.join(PATH_DATA, 'operations.json'))
    descriptions = pr.get_categories(data, 'перевод')
    pprint(descriptions)


if __name__ == '__main__':
    main()
