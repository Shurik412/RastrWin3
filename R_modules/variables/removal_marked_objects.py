# -*- coding: utf-8 -*-
from R_modules.Tables_Parametrs.Tables_and_parametrs import table_name_node, table_name_vetv, table_name_generator
from R_modules.object_rastr import RASTR


class RemoveSelObjects:
    """
    Данный класс убирает галочки (отчетки) sel в
    таблицах Узлы, Ветви, Генераторы.
    Также убирает галочки (отчетки) sel по заданой таблице.
    """

    def __init__(self, rastr_win=RASTR, switch_command_line=False):
        self.rastr_win = rastr_win

    def remove_sel(self, table, column='sel'):
        table = self.rastr_win.Tables(table)
        table.SetSel('')
        table.Cols(column).Calc('0')

    def remove_sel_node(self):
        table = self.rastr_win.Tables(table_name_node)
        table.SetSel('')
        table.Cols('sel').Cals('0')

    def remove_sel_vetv(self):
        table = self.rastr_win.Tables(table_name_vetv)
        table.SetSel('')
        table.Cols('sel').Cals('0')

    def remove_sel_generator(self):
        table = self.rastr_win.Tables(table_name_generator)
        table.SetSel('')
        table.Cols('sel').Cals('0')
