import random


def massege(func):
    def wrapper(*args, **kwargs):
        print(f'{func.__name__} была исполнена')
        result = func(*args, **kwargs)
        return result

    return wrapper


@massege
def some_func(a, b):
    return [random.randint(0, b) for _ in range(a)]


print(some_func(9, 100))
