# -*- coding: utf-8 -*-
from prettytable import PrettyTable

pt = PrettyTable()


def output_of_results_in_the_protocol():
    pass


def output_function_save_in_the_protocol(name_file, shabl):
    pt.title = 'Сохранен файл данных RastrWin3'
    pt.field_names = ['Файл', 'Шаблон']
    pt.add_row([name_file, shabl])
    print(pt)


