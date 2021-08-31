# -*- coding: utf-8 -*-
import time
from functools import wraps
from RastrWinLib.tools.tools import changing_number_of_semicolons


def timethis(func):
    """
    Декоратор для определения веремени работы функции.
    :param func: любая функция
    :return:
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(
            f'Название функции: {func.__name__}; время работы: {changing_number_of_semicolons(number=(end - start), digits=3)} сек.')
        return result

    return wrapper


if __name__ == '__main__':

    @timethis
    def countdown(n):
        """

        :param n:
        :return:
        """
        while n > 0:
            # print(n)
            n = n - 1


    countdown(1000000)
