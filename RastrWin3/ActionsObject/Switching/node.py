# -*- coding: utf-8 -*-
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.ActionsObject.Get import GettingParameter
from RastrWinLib.Tables.Node.node import Node
from RastrWinLib.Tools.tools import Tools
from RastrWinLib.ActionsObject.Variable import Variable


class SwitchNode:

    def __init__(self,
                 rastr_win=RASTR,
                 table=Node.table,
                 switch_command_line=False):
        f"""
        Класс включает и отключает заданный узел.
        :param rastr_win: {Tools.RastrDoc};
        :param table: название таблицы;
        :param switch_command_line: {Tools.switch_command_line_doc};
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
