# -*- coding: utf-8 -*-
from RastrWin3.AstraRastr import RASTR
from RastrWin3.Tools.tools import TableOutput


class GroupCorr:
    """ Класс групповой коррекции параметров в таблице """

    def __init__(self, rastr_win=RASTR):
        f"""
        :param rastr_win: COM - объект Rastr.Astra (win32com);\n
        """
        self.rastr_win = rastr_win

    def calc(self, table: str, column: str, viborka: str, formula: str, switch_command_line: bool = False):
        f"""
        Универсальный метод для всех талиц и различной групповой коррекцией.\n
        
        :param table: название таблицы;\n
        :param column: название параметра;\n
        :param viborka: выбрка, например: название района или диапазон знчений ("na > 1");\n
        :param formula: формула "pn*1.15";\n
        :param switch_command_line: True/False - вывод сообщений в протокол;\n
        :return: Nothing returns;\n
        """

        _table = self.rastr_win.Tables(table)
        _cols = _table.Cols(column)
        _table.SetSel(viborka)
        _cols.Calc(formula)

        if switch_command_line:
            _pretty_table = TableOutput(fieldName=['Таблица', 'Параметр', 'Выбока', 'Формула'])
            _pretty_table.row_add([table, _cols.Name, viborka, formula])
            _pretty_table.show(title_table='Групповая коррекция')