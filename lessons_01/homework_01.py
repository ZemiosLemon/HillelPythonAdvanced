import random
from functools import wraps


def mydecor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('ggg')
        return result

    return wrapper


@mydecor
def some_func(a, b):
    return [random.randint(0, b) for _ in range(a)]


print(some_func(9, 100))