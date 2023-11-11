import time
from functools import wraps
from typing import Any, Callable


def log(filename: str = None) -> Callable:
    def wrapper(func: Callable) -> Any:
        @wraps(func)
        def inner(*args, **kwargs) -> Any:
            time_now = time.localtime()
            response = time.strftime("%m-%d-%Y %H:%M:%S", time_now) + f' {func.__name__}'
            try:
                result = func(*args, **kwargs)
                response += ' ok'
            except Exception as e:
                response += f' error: {e}. Inputs: {args, kwargs}'
                if filename:
                    with open(filename, 'a') as file:
                        file.write(response + '\n')
                    return
                else:
                    print(response)
                    return
            else:
                if filename:
                    with open(filename, 'a') as file:
                        file.write(response + '\n')
                    return result
                else:
                    print(response)
                    return result

        return inner
    return wrapper
