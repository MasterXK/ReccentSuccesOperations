import pytest
from src.widget import make_operation_name, get_date

@pytest.fixture
def data():
    return '2019-07-03T18:35:29.512364'


@pytest.mark.parametrize("operation, expected_result", [
                                ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
                                ('Счет 64686473678894779589', 'Счет **9589'),
                                ('Visa Platinum 8990922113665229', 'Visa Platinum 8990 92** **** 5229')
                                ])
def test_make_operation_name(operation, expected_result):
    assert make_operation_name(operation) == expected_result


def test_get_date(data):
    assert get_date(data) == '03.07.2019'
