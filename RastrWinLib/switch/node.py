# -*- coding: utf-8 -*-
import RastrWinLib.tables.Node.node as node
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.getting.get import GettingParameter
from RastrWinLib.variables.variable_parametrs import Variable


class SwitchNode:

    def __init__(self, rastr_win=RASTR,
                 table=node.table,
                 switch_command_line=False):
        """
        Класс включает и отключает заданный узел.
        :param rastr_win: COM - объект Rastr.Astra (win32com);
        :param table: название таблицы;
        :param switch_command_line: True/False - выводит сообщения в протокол.
        """
        self.rastr_win = rastr_win
        self.table = table
        self.variable_ = Variable()
        self.get_ = GettingParameter()
        self.switch_command_line = switch_command_line

    def on_node(self, node_ny):
        """
        :param node_ny: номер узла.
        :return:
        """
        row_ = self.get_.get_row_node(node_ny=node_ny)
        sta_ny = self.get_.get_cell(table=self.table,
                                    column=node.sta,
                                    row_id=row_)
        self.variable_.make_changes_row(table=self.table,
                                        column=node.sta,
                                        row_id=row_)
        if self.switch_command_line is not False:
            print(sta_ny)

    def off_node(self, node_ny):
        """
        :param node_ny: номер узла.
        :return:
        """
        row_ = self.get_.get_row_node(node_ny=node_ny)
        sta_ny = self.get_.get_cell(table=self.table,
                                    column=node.sta,
                                    row_id=row_)
        self.variable_.make_changes_row(table=self.table,
                                        column=node.sta,
                                        row_id=row_)
        if self.switch_command_line is not False:
            print(sta_ny)
