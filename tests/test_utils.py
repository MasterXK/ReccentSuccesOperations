import json

import pytest

from src.utils import get_info, get_transaction_sum


@pytest.fixture
def transaction_rub():
    with open("./data/test_2.json", encoding="UTF-8") as json_file:
        json_content = json.load(json_file)

    return json_content


@pytest.fixture
def transaction_usd():
    with open("./data/test_1.json", encoding="UTF-8") as json_file:
        json_content = json.load(json_file)

    return json_content[0]


@pytest.mark.parametrize(
    "json_path, expected_result",
    [
        (
            "./data/test_1.json",
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                    "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "MasterCard 7158300734726758",
                    "to": "Счет 35383033474447895560",
                }
            ],
        ),
        ("./data/test_2.json", []),
        ("./data/test_3.json", []),
        ("./data/test_4.json", []),
    ],
)
def test_get_info(json_path, expected_result):
    assert get_info(json_path) == expected_result


def test_get_transaction_sum_correct(transaction_rub):
    assert get_transaction_sum(transaction_rub) == 31957.58


def test_get_transaction_sum_err(transaction_usd):
    with pytest.raises(ValueError):
        get_transaction_sum(transaction_usd)
