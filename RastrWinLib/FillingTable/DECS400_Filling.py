# -*- coding: utf-8 -*-
# Модуль заполнения таблицы  "Возбудитель DECS-400" RastrWin3

from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.tables.Dynamic.DECS_400 import DFWDECS400, DFWDECS400_Description
from RastrWinLib.variables.variable_parametrs import Variable


def filling_DECS400(
        rastr_win=RASTR,
        row_id: int = None,
        sel: bool = None,
        sta: bool = None,
        Id: int = None,
        Name: str = None,
        ModelType: str = None,
        Brand: str = None,
        CustomModel: str = None,
        PSSId: int = None,
        UELId: int = None,
        OELId: int = None,
        ForcerId: int = None,
        Xl: float = None,
        DRP: float = None,
        VrMin: float = None,
        VrMax: float = None,
        VmMax: float = None,
        VmMin: float = None,
        VbMax: float = None,
        Kc: float = None,
        Kp: float = None,
        Kpm: float = None,
        Kpr: float = None,
        Kir: float = None,
        Kpd: float = None,
        Ta: float = None,
        Td: float = None,
        Tr: float = None,
        SelfExc: float = None,
        Del: float = None,
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
    :param Brand:
    :param CustomModel:
    :param PSSId:
    :param UELId:
    :param OELId:
    :param ForcerId:
    :param Xl:
    :param DRP:
    :param VrMin:
    :param VrMax:
    :param VmMax:
    :param VmMin:
    :param VbMax:
    :param Kc:
    :param Kp:
    :param Kpm:
    :param Kpr:
    :param Kir:
    :param Kpd:
    :param Ta:
    :param Td:
    :param Tr:
    :param SelfExc:
    :param Del:
    :param switch_command_line:
    :return:
    """
    variable_ = Variable(rastr_win=rastr_win)

    variable_.make_changes_row(table=DFWDECS400.table,
                               column=DFWDECS400.sel,
                               row_id=row_id,
                               value=sel)

    variable_.make_changes_row(table=DFWDECS400.table,
                               column=DFWDECS400.sta,
                               row_id=row_id,
                               value=sta)

    variable_.make_changes_row(table=DFWDECS400.table,
                               column=DFWDECS400.Id,
                               row_id=row_id,
                               value=Id)

    variable_.make_changes_row(table=DFWDECS400.table,
                               column=DFWDECS400.Name,
                               row_id=row_id,
                               value=Name)

    variable_.make_changes_row(table=DFWDECS400.table,
                               column=DFWDECS400.ModelType,
                               row_id=row_id,
                               value=ModelType)

    variable_.make_changes_row(table=DFWDECS400.table,
                               column=DFWDECS400.Brand,
                               row_id=row_id,
                               value=Brand)

    variable_.make_changes_row(table=DFWDECS400.table,
                               column=DFWDECS400.CustomModel,
                               row_id=row_id,
                               value=CustomModel)

    variable_.make_changes_row(table=DFWDECS400.table,
                               column=DFWDECS400.PSSId,
                               row_id=row_id,
                               value=PSSId)

    variable_.make_changes_row(table=DFWDECS400.table,
                               column=DFWDECS400.UELId,
                               row_id=row_id,
                               value=UELId)

    variable_.make_changes_row(table=DFWDECS400.table,
                               column=DFWDECS400.OELId,
                               row_id=row_id,
                               value=OELId)

    variable_.make_changes_row(table=DFWDECS400.table,
                               column=DFWDECS400.ForcerId,
                               row_id=row_id,
                               value=ForcerId)

    variable_.make_changes_row(table=DFWDECS400.table,
                               column=DFWDECS400.Xl,
                               row_id=row_id,
                               value=Xl)

    variable_.make_changes_row(table=DFWDECS400.table,
                               column=DFWDECS400.DRP,
                               row_id=row_id,
                               value=DRP)

    variable_.make_changes_row(table=DFWDECS400.table,
                               column=DFWDECS400.VrMin,
                               row_id=row_id,
                               value=VrMin)

    variable_.make_changes_row(table=DFWDECS400.table,
                               column=DFWDECS400.VrMax,
                               row_id=row_id,
                               value=VrMax)

    variable_.make_changes_row(table=DFWDECS400.table,
                               column=DFWDECS400.VmMax,
                               row_id=row_id,
                               value=VmMax)

    variable_.make_changes_row(table=DFWDECS400.table,
                               column=DFWDECS400.VmMin,
                               row_id=row_id,
                               value=VmMin)

    variable_.make_changes_row(table=DFWDECS400.table,
                               column=DFWDECS400.VbMax,
                               row_id=row_id,
                               value=VbMax)

    variable_.make_changes_row(table=DFWDECS400.table,
                               column=DFWDECS400.Kc,
                               row_id=row_id,
                               value=Kc)

    variable_.make_changes_row(table=DFWDECS400.table,
                               column=DFWDECS400.Kp,
                               row_id=row_id,
                               value=Kp)

    variable_.make_changes_row(table=DFWDECS400.table,
                               column=DFWDECS400.Kpm,
                               row_id=row_id,
                               value=Kpm)

    variable_.make_changes_row(table=DFWDECS400.table,
                               column=DFWDECS400.Kpr,
                               row_id=row_id,
                               value=Kpr)

    variable_.make_changes_row(table=DFWDECS400.table,
                               column=DFWDECS400.Kir,
                               row_id=row_id,
                               value=Kir)

    variable_.make_changes_row(table=DFWDECS400.table,
                               column=DFWDECS400.Kpd,
                               row_id=row_id,
                               value=Kpd)

    variable_.make_changes_row(table=DFWDECS400.table,
                               column=DFWDECS400.Ta,
                               row_id=row_id,
                               value=Ta)

    variable_.make_changes_row(table=DFWDECS400.table,
                               column=DFWDECS400.Td,
                               row_id=row_id,
                               value=Td)

    variable_.make_changes_row(table=DFWDECS400.table,
                               column=DFWDECS400.Tr,
                               row_id=row_id,
                               value=Tr)

    variable_.make_changes_row(table=DFWDECS400.table,
                               column=DFWDECS400.SelfExc,
                               row_id=row_id,
                               value=SelfExc)

    variable_.make_changes_row(table=DFWDECS400.table,
                               column=DFWDECS400.Del,
                               row_id=row_id,
                               value=Del)
