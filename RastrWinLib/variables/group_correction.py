# -*- coding: utf-8 -*-
from RastrWinLib.AstraRastr import RASTR


class GroupCorr:
    """
    Класс GroupCorr - групповая коррекция
      Данный класс изменяет значения в соотвтетсии с заданной формулой и выборкой.
      Пример вызова класса:
    >> rastr_moduls.GroupCorr(Rastr=<объект RastrWinLib>,
                                table=< название таблицы ("Generator" или "node")>,
                                column=< название параметра (vzd,P,pl_ip ...)>,
                                viborka=< название района или диапазон знчений ("na > 1") >,
                                formula=< pn*1.15 >)
    """

    def __init__(self, table, column, rastr_win=RASTR, switch_command_line=False):
        """

        :param table:
        :param column:
        :param rastr_win: COM - объект Rastr.Astra (win32com);
        :param switch_command_line: True/False - вывод сообщений в протокол.
        """
        self.rastr_win = rastr_win
        self.table = self.rastr_win.Tables(table)
        self.column = self.table.Cols(column)
        self.switch_command_line = switch_command_line

    def calc(self, key, formula):
        """

        :param key:
        :param formula:
        :return:
        """
        self.table.SetSel(key)
        self.column.Calc(formula)
        if self.switch_command_line is not False:
            print(f'Изменение параметра {self.column.name}: выборка {key}; формула: {formula}.')