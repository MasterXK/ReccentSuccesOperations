import time
import os

from src.decorator import log

FILENAME = os.path.join('..', 'data', 'Log.txt')


def test_log_default_with_file():
    @log(FILENAME)
    def my_function(x, y):
        return x + y

    time_ = time.localtime()

    my_function(1, 2)

    response = time.strftime("%m-%d-%Y %H:%M:%S", time_) + ' my_function ok\n'
    with open(FILENAME) as file:
        lines = file.readlines()
        assert lines[-1] == response


def test_log_default_without_file(capfd):
    @log()
    def my_function(x, y):
        return x + y

    time_ = time.localtime()

    my_function(1, 2)

    captured = capfd.readouterr()
    expect_response = time.strftime("%m-%d-%Y %H:%M:%S", time_) + ' my_function ok\n'

    assert captured.out == expect_response


def test_log_wrong_type_with_file():
    @log(FILENAME)
    def my_function(x, y):
        return x + y

    time_ = time.localtime()

    my_function(1, '2')

    expect_response = (time.strftime("%m-%d-%Y %H:%M:%S", time_) +
                       " my_function error: unsupported operand type(s) for +: 'int' and 'str'. " +
                       "Inputs: ((1, '2'), {})\n")

    with open(FILENAME) as file:
        lines = file.readlines()
        assert lines[-1] == expect_response


def test_log_wrong_type_without_file(capfd):
    @log()
    def my_function(x, y):
        return x + y

    time_ = time.localtime()

    my_function(1, '2')

    captured = capfd.readouterr()
    expect_response = (time.strftime("%m-%d-%Y %H:%M:%S", time_) +
                       " my_function error: unsupported operand type(s) for +: 'int' and 'str'. " +
                       "Inputs: ((1, '2'), {})\n")

    assert captured.out == expect_response
