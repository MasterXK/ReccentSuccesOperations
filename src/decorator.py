import time
from functools import wraps
from typing import Any, Callable


def log(filename: str = None) -> Callable:
    """
    Декоратор для записи логов
    :param filename: пть к файлу для записи логов
    :return: результат декорируемой функции
    """

    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            time_now = time.localtime()
            response = time.strftime("%m-%d-%Y %H:%M:%S", time_now) + f" {func.__name__}"
            try:
                result = func(*args, **kwargs)
                response += " ok"
            except Exception as e:
                response += f" error: {type(e).__name__}. Inputs: {args, kwargs}"
                result = None
            if filename:
                with open(filename, "w") as file:
                    file.write(response + "\n")
            else:
                print(response)
            return result

        return inner

    return wrapper
