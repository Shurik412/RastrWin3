# -*- coding: utf-8 -*-
# Модуль заполнения таблицы  "Зависимость Q(P)" RastrWin3

from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.tables.Dynamic.FuncPQ import FuncPQ, FuncPQ_Description
from RastrWinLib.variables.variable_parametrs import Variable


def filling_FuncPQ(
        rastr_win=RASTR,
        row_id: int = None,
        Id: int = None,
        P: float = None,
        Q: float = None,
        switch_command_line: bool = False
):
    """

    :param rastr_win:
    :param row_id:
    :param Id:
    :param P:
    :param Q:
    :param switch_command_line:
    :return:
    """
    variable_ = Variable(rastr_win=rastr_win)

    variable_.make_changes_row(table=FuncPQ.table,
                               column=FuncPQ.Id,
                               row_id=row_id,
                               value=Id)

    variable_.make_changes_row(table=FuncPQ.table,
                               column=FuncPQ.P,
                               row_id=row_id,
                               value=P)

    variable_.make_changes_row(table=FuncPQ.table,
                               column=FuncPQ.Q,
                               row_id=row_id,
                               value=Q)
