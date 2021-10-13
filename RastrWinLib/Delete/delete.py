# -*- coding: utf-8 -*-
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.tables.Vetv.vetv import Vetv
from RastrWinLib.tables.Node.node import Node
from RastrWinLib.tables.Dynamic.Generator import Generator


class Delete:
    def __init__(self, rastr_win=RASTE,
                 switch_command_line=False):
        self.rastr_win = rastr_win
        self.switch_command_line = switch_command_line

    def delete_by_SetSel_vetv(self, key: str):
        table_ = self.rastr_win.Tables(Vetv.table)
        table_.SetSel(key)
        table_.delete()

    def delete_by_SetSel_node(self, key: str):
        table_ = self.rastr_win.Tables(Node.table)
        table_.SetSel(key)
        table_.delete()

    def delete_by_SetSel_generator(self):
        table_ = self.rastr_win.Tables(Generator.table)
        table_.SetSel(key)
        table_.delete()

    def delete_SetSel_obj(self, table: str, key: str):
        table_ = self.rastr_win.Tables(table)
        table_.SetSel(key)
        table_.delete()

