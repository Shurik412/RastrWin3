# -*- coding: utf-8 -*-
# Модуль заполнения таблицы  "Турбины (ИД)" RastrWin3

from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.tables.Dynamic.ARS import ARS, ARS_Description
from RastrWinLib.variables.variable_parametrs import Variable


def filling_ARS(
        rastr_win=RASTR,
        row_id: int = None,
        sel: bool = None,
        sta: bool = None,
        Id: int = None,
        Name: str = None,
        ModelType: str = None,
        CustomModel: str = None,
        Brand: str = None,
        GovernorId: int = None,
        ao: float = None,
        az: float = None,
        otmin: float = None,
        otmax: float = None,
        strs: float = None,
        zn: float = None,
        dpo: float = None,
        Thp: float = None,
        Trlp: float = None,
        Tw: float = None,
        pt: float = None,
        Mu: float = None,
        Psteam: float = None,
        Mupo: float = None,
        tpo: float = None,
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
    :param GovernorId:
    :param ao:
    :param az:
    :param otmin:
    :param otmax:
    :param strs:
    :param zn:
    :param dpo:
    :param Thp:
    :param Trlp:
    :param Tw:
    :param pt:
    :param Mu:
    :param Psteam:
    :param Mupo:
    :param tpo:
    :param switch_command_line:
    :return:
    """
    variable_ = Variable(rastr_win=rastr_win)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.sel,
                               row_id=row_id,
                               value=sel)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.sta,
                               row_id=row_id,
                               value=sta)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.Id,
                               row_id=row_id,
                               value=Id)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.Name,
                               row_id=row_id,
                               value=Name)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.ModelType,
                               row_id=row_id,
                               value=ModelType)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.CustomModel,
                               row_id=row_id,
                               value=CustomModel)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.Brand,
                               row_id=row_id,
                               value=Brand)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.GovernorId,
                               row_id=row_id,
                               value=GovernorId)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.ao,
                               row_id=row_id,
                               value=ao)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.az,
                               row_id=row_id,
                               value=az)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.otmin,
                               row_id=row_id,
                               value=otmin)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.otmax,
                               row_id=row_id,
                               value=otmax)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.strs,
                               row_id=row_id,
                               value=strs)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.zn,
                               row_id=row_id,
                               value=zn)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.dpo,
                               row_id=row_id,
                               value=dpo)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.Thp,
                               row_id=row_id,
                               value=Thp)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.Trlp,
                               row_id=row_id,
                               value=Trlp)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.Tw,
                               row_id=row_id,
                               value=Tw)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.pt,
                               row_id=row_id,
                               value=pt)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.Mu,
                               row_id=row_id,
                               value=Mu)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.Psteam,
                               row_id=row_id,
                               value=Psteam)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.Mupo,
                               row_id=row_id,
                               value=Mupo)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.tpo,
                               row_id=row_id,
                               value=tpo)
