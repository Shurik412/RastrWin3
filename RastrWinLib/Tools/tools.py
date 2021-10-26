# -*- coding: utf-8 -*-
import re
import time
from functools import wraps
from os import listdir
from os.path import isfile, join, splitext, expanduser

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
            f'Название функции: {func.__name__}; время работы: '
            f'{changing_number_of_semicolons(number=(end - start), digits=3)} сек.')
        return result

    return wrapper


def file_extensions(path_file: str, extensions: str):
    only_files = [f for f in listdir(path_file) if isfile(join(path_file, f))]
    for file in only_files:
        file_name, file_extension = splitext(file)
        if file_extension == extensions:
            return file_name, file_extension
        else:
            file_name = 'Нет данных!'
            return file_name


class StandardRastrwin3:
    name_RUSTab_9_rst = 'test9.rst'
    name_RUSTab_9_scn = 'test9.scn'
    directory_file_RUSTab = expanduser('~\\Documents\\RastrWin3\\test-rastr\\RUSTab')

    file_RUSTab_9_rst = f'{directory_file_RUSTab}\\{name_RUSTab_9_rst}'
    file_RUSTab_9_scn = f'{directory_file_RUSTab}\\{name_RUSTab_9_scn}'


class DirectoryCheck:
    def __init__(self, name: str):
        self.name = name

    def get_expansion(self):
        p = re.compile(pattern=r'(?P<name>^[0-9а-яА-ЯёЁa-zA-Z_.])[.](?P<expansion>([s][c][n])$)',
                       flags=re.IGNORECASE | re.VERBOSE)
        p_search = p.search(self.name)
        print(p_search)
        return p_search.group("expansion")

    def get_full_name(self):
        return self.name

    def get_name(self):
        p = re.compile(pattern=r'^(?P<name>[0-9а-яА-ЯёЁa-zA-Z_.])[.](?P<expansion>([s][c][n]))$',
                       flags=re.IGNORECASE | re.VERBOSE)
        p_search = p.search(self.name)
        return p_search.group("name")

    def get_split(self):
        p = re.split(r'[.]', self.name)
        for index, expansion in enumerate(p):
            if expansion == 'scn':
                return expansion


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

    # Testing DirectoryCheck
    from icecream import ic

    test = DirectoryCheck(name='adfasdfasd.fs__.scn')
    for index, i in enumerate(test.get_split()):
        if i == 'scn':
            print(f'{i}')

    ic(test.get_split[1])
