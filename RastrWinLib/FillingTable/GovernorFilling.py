# -*- coding: utf-8 -*-
# Модуль заполнения таблицы  "АРС (ИД)" RastrWin3

from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.tables.Dynamic.Governor import Governor
from RastrWinLib.variables.variable_parametrs import Variable


def filling_Governor(
        rastr_win=RASTR,
        row_id: int = None,
        sel: bool = None,
        sta: bool = None,
        Id: int = None,
        Name: str = None,
        ModelType: str = None,
        CustomModel: str = None,
        Brand: str = None,
        strs: str = None,
        zn: str = None,
        Tr: str = None,
        otmax: str = None,
        otmin: str = None,
        CVmin: str = None,
        CVmax: str = None,
        T1: str = None,
        K1: str = None,
        K2: str = None,
        BoilerId: str = None,
        switch_command_line: bool = False
):
    """

    :param rastr_win:
    :param row_id:
    :param sel:
    :param sta:
    :param Id:
    :param Name:
    :param ModelType:
    :param CustomModel:
    :param Brand:
    :param strs:
    :param zn:
    :param Tr:
    :param otmax:
    :param otmin:
    :param CVmin:
    :param CVmax:
    :param T1:
    :param K1:
    :param K2:
    :param BoilerId:
    :param switch_command_line:
    :return:
    """
    variable_ = Variable(rastr_win=rastr_win)

    variable_.make_changes_row(table=Governor.table,
                               column=Governor.sel,
                               row_id=row_id,
                               value=sel)

    variable_.make_changes_row(table=Governor.table,
                               column=Governor.sta,
                               row_id=row_id,
                               value=sta)

    variable_.make_changes_row(table=Governor.table,
                               column=Governor.Id,
                               row_id=row_id,
                               value=Id)

    variable_.make_changes_row(table=Governor.table,
                               column=Governor.Name,
                               row_id=row_id,
                               value=Name)

    variable_.make_changes_row(table=Governor.table,
                               column=Governor.ModelType,
                               row_id=row_id,
                               value=ModelType)

    variable_.make_changes_row(table=Governor.table,
                               column=Governor.CustomModel,
                               row_id=row_id,
                               value=CustomModel)

    variable_.make_changes_row(table=Governor.table,
                               column=Governor.Brand,
                               row_id=row_id,
                               value=Brand)

    variable_.make_changes_row(table=Governor.table,
                               column=Governor.strs,
                               row_id=row_id,
                               value=strs)

    variable_.make_changes_row(table=Governor.table,
                               column=Governor.zn,
                               row_id=row_id,
                               value=zn)

    variable_.make_changes_row(table=Governor.table,
                               column=Governor.Tr,
                               row_id=row_id,
                               value=Tr)

    variable_.make_changes_row(table=Governor.table,
                               column=Governor.otmax,
                               row_id=row_id,
                               value=otmax)

    variable_.make_changes_row(table=Governor.table,
                               column=Governor.otmin,
                               row_id=row_id,
                               value=otmin)

    variable_.make_changes_row(table=Governor.table,
                               column=Governor.CVmin,
                               row_id=row_id,
                               value=CVmin)

    variable_.make_changes_row(table=Governor.table,
                               column=Governor.CVmax,
                               row_id=row_id,
                               value=CVmax)

    variable_.make_changes_row(table=Governor.table,
                               column=Governor.T1,
                               row_id=row_id,
                               value=T1)

    variable_.make_changes_row(table=Governor.table,
                               column=Governor.K1,
                               row_id=row_id,
                               value=K1)

    variable_.make_changes_row(table=Governor.table,
                               column=Governor.K2,
                               row_id=row_id,
                               value=K2)

    variable_.make_changes_row(table=Governor.table,
                               column=Governor.BoilerId,
                               row_id=row_id,
                               value=BoilerId)
