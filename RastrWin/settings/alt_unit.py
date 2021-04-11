# -*- coding: utf-8 -*-
from RastrWin.AstraRastr import RASTR
from RastrWin.variables.variable_parametrs import VariableDefRowId
from RastrWin.tables.tables_attributes import alt_unit_table, alt_unit_attributes


class AltUnit(VariableDefRowId):
    """
    Класс выставляет параметров настройки "Описание альтернативных единиц измерения"
    """

    def __init__(self, rastr_win=RASTR, table=alt_unit_table, switch_command_line=False):
        self.rastr_win = rastr_win
        self.list_key = []
        for key in alt_unit_attributes.keys():
            self.list_key.append(key)
        self.switch_command_line = switch_command_line
        VariableDefRowId.__init__(self, rastr_win=rastr_win, table=table, switch_command_line=switch_command_line)

    def set(self,
            row_id=0,
            Active='',
            Unit='',
            Alt='',
            Formula='',
            Prec='',
            Tabl=''):
        VariableDefRowId.make_changes(self, column=self.list_key[0], row_id=row_id, value=int(Active))
        VariableDefRowId.make_changes(self, column=self.list_key[1], row_id=row_id, value=str(Unit))
        VariableDefRowId.make_changes(self, column=self.list_key[2], row_id=row_id, value=str(Alt))
        VariableDefRowId.make_changes(self, column=self.list_key[3], row_id=row_id, value=str(Formula))
        VariableDefRowId.make_changes(self, column=self.list_key[4], row_id=row_id, value=str(Prec))
        VariableDefRowId.make_changes(self, column=self.list_key[5], row_id=row_id, value=str(Tabl))
