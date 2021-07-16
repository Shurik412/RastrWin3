# -*- coding: utf-8 -*-
from functools import wraps


def decor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Работа Decor!')
        return func(*args, **kwargs)
    return wrapper

