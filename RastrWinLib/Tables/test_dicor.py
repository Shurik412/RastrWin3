import time
from functools import wraps


def decor_one(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if func.__name__ == 'countdown':
            print('Decor_1')
        else:
            print('No')
        return func(*args, **kwargs)

    return wrapper


def decor_two(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decor_2')
        return func(*args, **kwargs)

    return wrapper


@decor_two
@decor_one
def countdown(n):
    """
    :param n:
    :return:
    """
    while n > 0:
        n -= 1
        print(n)


countdown(10)
