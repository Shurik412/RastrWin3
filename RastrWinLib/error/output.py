# -*- coding: utf-8 -*-
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.log_tools.tools import separator_star


class Errors:

    def __init__(self,
                 rastr_win=RASTR,
                 switch_command_line=False
                 ):
        """
        Класс вывода ошибок и исключений!
        :param rastr_win: COM - объект Rastr.Astra (win32com);
        :param switch_command_line: True/False - вывод сообщений в протокол.
        """
        self.rastr_win = rastr_win

    def __bool__(self,
                 switch_command_line):
        self.switch_command_line = switch_command_line

    @staticmethod
    def name_is_not_tables(table=None):
        if table is not None:
            try:
                assert table is not str, table
            except AssertionError as err:
                print(separator_star)
                print(f'Error: название таблицы не соответствует типу: "str" - строковому типу!')
                print(f'\t\tЗаданное название таблицы: <{err}>; Type: <{type(table)}>.')
                print(separator_star)

    @staticmethod
    def name_is_not_column(column=None):
        if column is not None:
            print(separator_star)
            print(f'Error: Не задано или не верно задано название колонки (столбца)!')
            print(f'Название столбца: {column}.')
            print(separator_star)


if __name__ == '__main__':
    er = Errors()
    er.name_is_not_tables(table=int(22))
