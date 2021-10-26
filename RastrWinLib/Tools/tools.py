# -*- coding: utf-8 -*-
import time
from functools import wraps

from prettytable import PrettyTable


def changing_number_of_semicolons(number, digits=0):
    return f"{number:.{digits}f}"


class TableOutput(PrettyTable):
    """

    """

    def __init__(self, fieldName):
        """

        :param fieldName:
        """
        super().__init__()
        self.field_names = fieldName

    def row_add(self, message) -> None:
        """
        Add
        :param message:
        :return:
        """
        self.add_row(message)

    def show(self, title_table: str) -> None:
        """
        :return:
        """
        print(self.get_string(title=title_table))


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
    # Testing class TableOutput
    tb = TableOutput(fieldName=['Описание', 'Параметр'])
    tb.row_add(['Время расчета для динамики', 'cек.'])
    tb.row_add(['Время расчета для динамики', 'cек.'])
    tb.row_add(['Время расчета для динамики', 'cек.'])
    tb.row_add(['Время расчета для динамики', 'cек.'])
    tb.show(title_table='Параметры')

    # Testing function changing_number_of_semicolons
    print(changing_number_of_semicolons(number=15315.00515, digits=5))


    # Testing @timethis
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
