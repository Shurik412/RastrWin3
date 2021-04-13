# -*- coding: utf-8 -*-
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.tables.tables_attributes import alt_unit_table, alt_unit_attributes
from RastrWinLib.variables.variable_parametrs import VariableDefRowId


def set_alt_unit(
        row_id=0,
        Active='',
        Unit='',
        Alt='',
        Formula='',
        Prec='',
        Tabl='',
        switch_command_line=False,
):
    list_key = []
    for key in alt_unit_attributes.keys():
        list_key.append(key)

    variable_def_rowid = VariableDefRowId(rastr_win=RASTR, table=alt_unit_table,
                                          switch_command_line=switch_command_line)

    variable_def_rowid.make_changes(column=list_key[0], row_id=row_id, value=int(Active))
    variable_def_rowid.make_changes(column=list_key[1], row_id=row_id, value=str(Unit))
    variable_def_rowid.make_changes(column=list_key[2], row_id=row_id, value=str(Alt))
    variable_def_rowid.make_changes(column=list_key[3], row_id=row_id, value=str(Formula))
    variable_def_rowid.make_changes(column=list_key[4], row_id=row_id, value=str(Prec))
    variable_def_rowid.make_changes(column=list_key[5], row_id=row_id, value=str(Tabl))

    if switch_command_line is not False:
        return print(f'Внесены изменения в настройки "Описание альтернативных единиц измерения"')
    else:
        return True


class SetAltUnit(VariableDefRowId):
    """
    Класс выставляет параметров настройки "Описание альтернативных единиц измерения"
    """

    def __init__(self, rastr_win=RASTR, table=alt_unit_table, switch_command_line=False):
        self.rastr_win = rastr_win
        self.list_key = []
        for key in alt_unit_attributes.keys():
            self.list_key.append(key)
        self.switch_command_line = switch_command_line
        self.variable_def_rowid = VariableDefRowId.__init__(self, rastr_win=rastr_win, table=table,
                                                            switch_command_line=switch_command_line)

    def set(self,
            row_id=0,
            Active='',
            Unit='',
            Alt='',
            Formula='',
            Prec='',
            Tabl=''):
        self.variable_def_rowid.make_changes(column=self.list_key[0], row_id=row_id, value=int(Active))
        self.variable_def_rowid.make_changes(column=self.list_key[1], row_id=row_id, value=str(Unit))
        self.variable_def_rowid.make_changes(column=self.list_key[2], row_id=row_id, value=str(Alt))
        self.variable_def_rowid.make_changes(column=self.list_key[3], row_id=row_id, value=str(Formula))
        self.variable_def_rowid.make_changes(column=self.list_key[4], row_id=row_id, value=str(Prec))
        self.variable_def_rowid.make_changes(column=self.list_key[5], row_id=row_id, value=str(Tabl))

        if self.switch_command_line is not False:
            return print(f'Внесены изменения в настройки "Описание альтернативных единиц измерения"')
        else:
            return True
