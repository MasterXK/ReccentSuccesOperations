from src.decorator import log
import time


def test_log_default():
    @log('../Log.txt')
    def my_function(x, y):
        return x + y

    time_ = time.localtime()

    my_function(1, 2)

    response = time.strftime("%m-%d-%Y %H:%M:%S", time_) + f' my_function ok\n'
    with open('../Log.txt') as file:
        lines = file.readlines()
        assert lines[-1] == response
