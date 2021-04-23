# -*- coding: utf-8 -*-
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.getting.get import GettingParameter
from RastrWinLib.tables.tables_attributes import node_table, node_attributes_list
from RastrWinLib.variables.variable_parametrs import Variable


class SwitchNode:
    """
    Класс включает и отключает заданный узел.
    """

    def __init__(self, rastr_win=RASTR,
                 table=node_table,
                 switch_command_line=False):
        """

        :param rastr_win:
        :param table:
        :param switch_command_line:
        """
        self.rastr_win = rastr_win
        self.table = table
        self.variable_ = Variable()
        self.get_ = GettingParameter()
        self.switch_command_line = switch_command_line

    def on_node(self, node_ny):
        """

        :param node_ny:
        :return:
        """
        row_ = self.get_.get_row_node(node_ny=node_ny)
        sta_ny = self.get_.get_cell(table=self.table,
                                    column=node_attributes_list[1],
                                    row_id=row_)
        self.variable_.make_changes_row(table=self.table,
                                        column=node_attributes_list[1],
                                        row_id=row_)
        if self.switch_command_line is not False:
            pass

    def off_node(self, node_ny):
        """

        :param node_ny:
        :return:
        """
        row_ = self.get_.get_row_node(node_ny=node_ny)
        sta_ny = self.get_.get_cell(table=self.table,
                                    column=node_attributes_list[1],
                                    row_id=row_)
        self.variable_.make_changes_row(table=self.table,
                                        column=node_attributes_list[1],
                                        row_id=row_)
        if self.switch_command_line is not False:
            pass
