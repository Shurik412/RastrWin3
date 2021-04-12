# -*- coding: utf-8 -*-
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.tables.tables_attributes import node_table, vetv_table, generator_table


class RemoveSelObjects:
    """
    Данный класс удаляет галочки (отчетки) sel.
    Метод: remove_sel -> удаляет выделение [sel] в заданной таблицe [par: table] и возвращяет True.
    Метод: remove_sel_node -> удаляет выделение [sel] в таблицe [node] и возвращяет True.
    Метод: remove_sel_vetv -> удаляет выделение [sel] в таблицe [vetv] и возвращяет True.
    Метод: remove_sel_generator -> удаляет выделение [sel] в таблицe [Generator] и возвращяет True.
    """

    def __init__(self, rastr_win=RASTR, switch_command_line=False):
        self.rastr_win = rastr_win
        self.switch_command_line = switch_command_line

    def remove_sel(self, table):
        """
        Removes the selection of objects in the specified table.

        :param table: Name table Software RastrWin3
        :type table: string
        :return: True
        :rtype: bool
        """
        table_ = self.rastr_win.Tables(table)
        table_.SetSel('')
        if self.switch_command_line is not False:
            print(f'В таблице "{table_.name}", были изменены все выделения в столбце [sel].')
        return True

    def remove_sel_node(self):
        """
        Removes the selection of objects in the table "node".

        :return: True                                            
        :rtype: bool
        """
        table_name = node_table
        table = self.rastr_win.Tables(table_name)
        table.SetSel('')
        table.Cols('sel').Calc(0)
        if self.switch_command_line is not False:
            print(f'В таблице "{table_name}", были удалены все выделения в столбце [sel].')
        return True

    def remove_sel_vetv(self):
        """
        Removes the selection of objects in the table "vetv".

        :return: True
        :rtype: bool
        """
        table_name = vetv_table
        table = self.rastr_win.Tables(table_name)
        table.SetSel('')
        table.Cols('sel').Calc(0)
        if self.switch_command_line is not False:
            print(f'В таблице "{table_name}", были изменены все выделения в столбце [sel].')
        return True

