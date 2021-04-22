# -*- coding: utf-8 -*-
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.tables.tables_attributes import alt_unit_table, alt_unit_attributes_list
from RastrWinLib.variables.variable_parametrs import Variable


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
    """

    :param row_id:
    :param Active:
    :param Unit:
    :param Alt:
    :param Formula:
    :param Prec:
    :param Tabl:
    :param switch_command_line:
    :return:
    """
    variable_def_rowid = Variable(rastr_win=RASTR, switch_command_line=switch_command_line)

    variable_def_rowid.make_changes_row(table=alt_unit_table,
                                        column=alt_unit_attributes_list[0],
                                        row_id=row_id,
                                        value=int(Active))
    variable_def_rowid.make_changes_row(table=alt_unit_table,
                                        column=alt_unit_attributes_list[1],
                                        row_id=row_id,
                                        value=str(Unit))
    variable_def_rowid.make_changes_row(table=alt_unit_table,
                                        column=alt_unit_attributes_list[2],
                                        row_id=row_id,
                                        value=str(Alt))
    variable_def_rowid.make_changes_row(table=alt_unit_table,
                                        column=alt_unit_attributes_list[3],
                                        row_id=row_id,
                                        value=str(Formula))
    variable_def_rowid.make_changes_row(table=alt_unit_table,
                                        column=alt_unit_attributes_list[4],
                                        row_id=row_id,
                                        value=str(Prec))
    variable_def_rowid.make_changes_row(table=alt_unit_table,
                                        column=alt_unit_attributes_list[5],
                                        row_id=row_id,
                                        value=str(Tabl))

    if switch_command_line is not False:
        return print(f'Внесены изменения в настройки "Описание альтернативных единиц измерения"')
    else:
        return True
