import json
import os
from unittest.mock import Mock, patch

import pandas as pd
import pytest

from data import PATH_DATA
from src.utils import get_sum, read_json, read_table


@pytest.fixture
def transaction_rub() -> dict:
    with open(os.path.join(PATH_DATA, "test_2.json"), encoding="UTF-8") as json_file:
        json_content: dict = json.load(json_file)

    return json_content


@pytest.fixture
def transaction_usd() -> dict:
    with open(os.path.join(PATH_DATA, "test_1.json"), encoding="UTF-8") as json_file:
        json_content: list[dict] = json.load(json_file)

    return json_content[0]


@pytest.fixture
def data_in() -> dict[str, str]:
    return {
        "amount": "0.0",
        "currency_code": "",
        "currency_name": "",
        "date": "2023-09-05T11:30:32Z",
        "description": "Перевод ",
        "from": "Счет ",
        "id": "0.0",
        "state": "EXECUTED",
        "to": "Счет ",
    }


@pytest.fixture
def data_out() -> list[dict]:
    return [
        {
            "operationAmount": {"amount": "0.0", "currency": {"name": "", "code": ""}},
            "date": "2023-09-05T11:30:32Z",
            "description": "Перевод ",
            "from": "Счет ",
            "id": "0.0",
            "state": "EXECUTED",
            "to": "Счет ",
        }
    ]


@pytest.mark.parametrize(
    "json_path, expected_result",
    [
        (
            os.path.join(PATH_DATA, "test_1.json"),
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
        (os.path.join(PATH_DATA, "test_2.json"), []),
        (os.path.join(PATH_DATA, "test_3.json"), []),
        (os.path.join(PATH_DATA, "test_4.json"), []),
    ],
)
def test_from_json(json_path: str | os.PathLike, expected_result: list[dict]) -> None:
    assert read_json(json_path) == expected_result


def test_get_sum_correct(transaction_rub: dict) -> None:
    assert get_sum(transaction_rub) == 31957.58


def test_get_sum_err(transaction_usd: dict) -> None:
    with pytest.raises(ValueError):
        get_sum(transaction_usd)


@patch("os.path.exists")
@patch("pandas.read_csv")
@patch("pandas.read_excel")
def test_read_table(
    mock_read_excel: Mock,
    mock_read_csv: Mock,
    mock_exists: Mock,
    data_in: dict[str, str],
    data_out: list[dict],
) -> None:
    mock_exists.return_value = True

    df = pd.DataFrame(data_in, index=[0])
    mock_read_csv.return_value = df

    assert read_table("path.csv") == data_out

    mock_exists.assert_called_once()
    mock_read_csv.assert_called_once()

    df = pd.DataFrame(data_in, index=[0])
    mock_read_excel.return_value = df

    assert read_table("path.xls") == data_out

    mock_exists.assert_called()
    mock_read_excel.assert_called_once()
