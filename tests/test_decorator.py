import os
import time
import pytest

from typing import Generator

from src.decorator import log

TESTS_LOG = os.path.join('.', 'data', 'test.txt')


@pytest.mark.parametrize("arg_1, arg_2, expected_result",
                         [(1, 2, ' my_function ok'),
                          (1, '2',
                           " my_function error: TypeError. Inputs: ((1, '2'), {})")])
def test_log_with_file(arg_1: int, arg_2: int | str, expected_result: str) -> None:
    if os.path.exists(TESTS_LOG):
        os.remove(TESTS_LOG)

    @log(TESTS_LOG)
    def my_function(x: int, y: int) -> int:
        return x + y

    time_ = time.localtime()

    my_function(arg_1, arg_2)
    expected_log = time.strftime("%m-%d-%Y %H:%M:%S", time_) + expected_result
    with open(TESTS_LOG) as file:
        log_message = file.read().strip()
        assert log_message == expected_log


@pytest.mark.parametrize("arg_1, arg_2, expected_result",
                         [(1, 2, ' my_function ok'),
                          (1, '2',
                           " my_function error: TypeError. Inputs: ((1, '2'), {})")])
def test_log_default_without_file(capfd: Generator, arg_1: int, arg_2: int | str, expected_result: str) -> None:
    if os.path.exists(TESTS_LOG):
        os.remove(TESTS_LOG)

    @log()
    def my_function(x: int, y: int) -> int:
        return x + y

    time_ = time.localtime()

    my_function(arg_1, arg_2)

    captured = capfd.readouterr()
    log_message = captured.out.strip()
    expect_log = time.strftime("%m-%d-%Y %H:%M:%S", time_) + expected_result

    assert log_message == expect_log

