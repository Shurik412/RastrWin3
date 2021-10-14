# -*- coding: utf-8 -*-
from prettytable import PrettyTable
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.tables.Vetv.vetv import Vetv
from RastrWinLib.tables.Node.node import Node
from RastrWinLib.tables.Dynamic.Generator import Generator


class Delete:
    """
    Удаляет заданный элемент (объект) из таблицы заданной таблицы
    """

    def __init__(self,
                 rastr_win=RASTE,
                 switch_command_line: bool = False):
        """
        :param rastr_win: COM - объект Rastr.Astra (win32com);
        :param switch_command_line: True/False - вывод сообщений в протокол.
        """
        self.rastr_win = rastr_win
        self.switch_command_line = switch_command_line

    def __bool__(self):
        return self.switch_command_line

    def delete_by_SetSel_vetv(self, formula: str = None):
        """
        Удаляет из таблицы "Ветви" выбранную ветв по формуле SetSel
        :param formula: формула ("ip=")
        :return: nothing returns;
        """
        if formula is not None:
            table_ = self.rastr_win.Tables(Vetv.table)
            table_.SetSel(formula)
            table_.delete()
            if self.switch_command_line:
                message(table=Vetv.table_name, number_or_formula=formula)
        else:
            message_error(table=Vetv.table_name, number_or_formula=formula)

    def delete_by_SetSel_node(self, formula: str = None):
        """
        Удаление из таблицы "Узлы" выбранный узел по формуле SetSel
        :param formula:
        :return: nothing returns;
        """
        if formula is not None:
            table_ = self.rastr_win.Tables(Node.table)
            table_.SetSel(formula)
            table_.delete()
            if self.switch_command_line:
                message(table=Node.table_name, number_or_formula=formula)
        else:
            message_error(table=Node.table_name, number_or_formula=formula)

    def delete_by_SetSel_generator(self, formula: str = None):
        """

        :param formula:
        :return: nothing returns;
        """
        if formula is not None:
            table_ = self.rastr_win.Tables(Generator.table)
            table_.SetSel(formula)
            table_.delete()
            if self.switch_command_line:
                message(table=Generator.table_name, number_or_formula=formula)
        else:
            message_error(table=Generator.table_name, number_or_formula=formula)

    def delete_SetSel_any_table(self, table: str = None, formula: str = None):
        """

        :param table:
        :param formula:
        :return: nothing returns;
        """
        if table and formula is not None:
            table_ = self.rastr_win.Tables(table)
            table_.SetSel(formula)
            table_.delete()
            if self.switch_command_line:
                message(table=table, number_or_formula=formula)
        else:
            message_error(table=table, number_or_formula=formula)

    def delete_by_node_ny(self, ny: int = None):
        """
        Удаление из таблицы "Узлы" выбранный узел по формуле SetSel
        :param ny: номер узла (ny=51700111)
        :return: nothing returns;
        """
        if ny is not None:
            table_ = self.rastr_win.Tables(Node.table)
            table_.SetSel(f'ny={ny}')
            table_.delete()
            if self.switch_command_line:
                message(table=Node.table_name, number_or_formula=ny)
        else:
            message_error(table=Node.table_name, number_or_formula=ny)

    @staticmethod
    def message(table, number_or_formula):
        """

        :param table:
        :param number_or_formula:
        :return: nothing returns;
        """
        pt = PrettyTable()
        pt.field_names = ['Таблица', 'Номер/Формула']
        pt.add_row([table, number_or_formula])
        print(pt.get_string(title="Удаление элемента из Таблицы RastrWin3"))

    @staticmethod
    def message_error(table, number_or_formula):
        """

        :param table:
        :param number_or_formula:
        :return: nothing returns;
        """
        pt = PrettyTable()
        pt.field_names = ['Таблица', 'Номер/Формула']
        pt.add_row([table, number_or_formula])
        print(pt.get_string(title="ERROR: Удаление элемента из Таблицы RastrWin3"))
