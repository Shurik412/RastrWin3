# -*- coding: utf-8 -*-

class GroupCorr:
    """
    Класс GroupCorr - групповая коррекция
      Данный класс изменяет значения в соотвтетсии с
    заданной формулой и выборкой.
      Пример вызова класса:
    >> rastr_moduls.GroupCorr(Rastr=<объект RastrWin3>,
                                table=< название таблицы ("Generator" или "node")>,
                                column=< название параметра (vzd,P,pl_ip ...)>,
                                viborka=< название района или диапазон знчений ("na > 1") >,
                                formula=< pn*1.15 >)
    """

    def __init__(self, rastr_win, table, column, switch_command_line=False):
        self.rastr_win = rastr_win
        self.table = self.rastr_win.Tables(table)
        self.column = self.table.Cols(column)
        self.switch_command_line = switch_command_line

    def calc(self, key, formula):
        self.table.SetSel(key)
        self.column.Calc(formula)
        if self.switch_command_line is not False:
            print(f'Изменение параметра {self.column.name}: выборка {key}; формула: {formula}.')