# -*- coding: utf-8 -*-
from RastrWinLib.AstraRastr import RASTR
from RastrWin3.Tools.tools import TableOutput


class GroupCorr:
    """ Класс групповой коррекции параметров в таблице """

    def __init__(self, rastr_win=RASTR):
        f"""
        :param rastr_win: COM - объект Rastr.Astra (win32com);\n
        """
        self.rastr_win = rastr_win

    def calc(self, table: str, column: str, key: str, formula: str, switch_command_line: bool = False):
        f"""
        Универсальный метод для всех талиц и различной групповой коррекцией;\n
        :param table: название таблицы ("Generator" или "node");\n
        :param column:  название параметра (vzd,P,pl_ip ...);\n
        :param key: название района или диапазон знчений ("na > 1");\n
        :param formula: "pn*1.15";\n
        :param switch_command_line: True/False - вывод сообщений в протокол;\n
        :return: Nothing returns;\n
        """
        _table = self.rastr_win.Tables(table)
        _cols = self.table.Cols(column)
        _table.SetSel(key)
        _column.Calc(formula)

        if switch_command_line:
            _pretty_table = TableOutput(fieldName=['Таблица', 'Параметр', 'Выбока', 'Формула'])
            _pretty_table.row_add([table, _cols.name, key, formula])
            _pretty_table.show(title_table='Групповая коррекция')