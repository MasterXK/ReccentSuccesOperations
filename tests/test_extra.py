import pytest

from src.extra import get_dir_content, get_similar, get_max_multiply, sort_by_price, get_months_statistic


@pytest.fixture
def products():
    return [
        {"name": "", "price": 10, "category": "q", "quantity": 1},
        {"name": "", "price": 25, "category": "w", "quantity": 2},
        {"name": "", "price": 12, "category": "q", "quantity": 3},
        {"name": "", "price": 55, "category": "e", "quantity": 4},
        {"name": "", "price": 6, "category": "q", "quantity": 5},
    ]


@pytest.fixture
def orders():
    return [
        {
            "id": "1",
            "date": "2019-04-03T18:35:29.512364",
            "items": [
                {"name": "", "price": 1, "quantity": 2},
                {"name": "", "price": 3, "quantity": 3},
                {"name": "", "price": 4, "quantity": 5},
            ],
        },
        {"id": "2", "date": "2019-05-03T18:35:29.512364", "items": [{"name": "", "price": 2, "quantity": 3}]},
        {"id": "3", "date": "2019-05-06T18:35:29.512364", "items": [{"name": "", "price": 3, "quantity": 3}]},
        {"id": "4", "date": "2019-07-10T18:35:29.512364", "items": [{"name": "", "price": 3, "quantity": 2}]},
        {"id": "5", "date": "2019-07-12T18:35:29.512364", "items": [{"name": "", "price": 10, "quantity": 1}]},
    ]


def test_get_dir_content():
    assert get_dir_content(".") == {"files": 6, "folders": 7}
    assert get_dir_content(".", count_all=True) == {"files": 2747, "folders": 340}


@pytest.mark.parametrize(
    "words, result",
    [
        (["hello", "world", "apple", "pear", "banana", "pop"], ["pop"]),
        ([" ", "madam", "racecar", "noon", "level", " "], [" ", "madam", "racecar", "noon", "level", " "]),
        ([], []),
    ],
)
def test_get_similar(words, result):
    assert get_similar(words) == result


@pytest.mark.parametrize("nums, result", [([2, 3, 5, 7, 11], 77), ([-5, -7, -9, -13], 117), ([1, 2], 2), ([4], 0)])
def test_get_max_multiply(nums, result):
    assert get_max_multiply(nums) == result


def test_sort_by_price(products):
    assert sort_by_price(products) == [
        {"name": "", "price": 55, "category": "e", "quantity": 4},
        {"name": "", "price": 25, "category": "w", "quantity": 2},
        {"name": "", "price": 12, "category": "q", "quantity": 3},
        {"name": "", "price": 10, "category": "q", "quantity": 1},
        {"name": "", "price": 6, "category": "q", "quantity": 5},
    ]
    assert sort_by_price(products, category="q") == [
        {"name": "", "price": 12, "category": "q", "quantity": 3},
        {"name": "", "price": 10, "category": "q", "quantity": 1},
        {"name": "", "price": 6, "category": "q", "quantity": 5},
    ]


def test_get_months_statistic(orders):
    assert get_months_statistic(orders) == {
        "2019.04": {"average_order_value": 20.0, "order_count": 1},
        "2019.05": {"average_order_value": 7.5, "order_count": 2},
        "2019.07": {"average_order_value": 8.0, "order_count": 2},
    }
