# -*- coding: utf-8 -*-
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.settings.equivalence import SetEkviv, VariableDefRowId
from RastrWinLib.tables.tables_attributes import node_table, node_attributes


class ViborkaVetvEquivalent(SetEkviv):

    def __init__(self, rastr_win=RASTR):
        self.rastr_win = rastr_win

        SetEkviv.__init__(self, rastr_win=self.rastr_win)

    def get(self, row_id, ):
        pass
