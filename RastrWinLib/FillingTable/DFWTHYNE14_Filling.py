# -*- coding: utf-8 -*-
# Модуль заполнения таблицы  "Возбудители Thyne 1-4" RastrWin3

from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.tables.Dynamic.DFWTHYNE14 import DFWTHYNE14, DFWTHYNE14_Description
from RastrWinLib.variables.variable_parametrs import Variable


def filling_DFWTHYNE14(
        rastr_win=RASTR,
        row_id: int = None,
        sel: bool = None,
        sta: bool = None,
        Id: int = None,
        Name: str = None,
        ModelType: str = None,
        Brand: str = None,
        UELId: int = None,
        PSSId: int = None,
        Aex: float = None,
        Bex: float = None,
        Alpha: float = None,
        Beta: float = None,
        IdfMin: float = None,
        Kc: float = None,
        Kd1: float = None,
        Kd2: float = None,
        Ke: float = None,
        Ketb: float = None,
        Kh: float = None,
        Kp1: float = None,
        Kp2: float = None,
        Kp3: float = None,
        Td1: float = None,
        Te1: float = None,
        Te2: float = None,
        Ti1: float = None,
        Ti2: float = None,
        Ti3: float = None,
        Tr1: float = None,
        Tr2: float = None,
        Tr3: float = None,
        Tr4: float = None,
        VO1Max: float = None,
        VO1Min: float = None,
        VO2Max: float = None,
        VO2Min: float = None,
        VO3Max: float = None,
        VO3Min: float = None,
        VD1Max: float = None,
        VD1Min: float = None,
        VI1Max: float = None,
        VI1Min: float = None,
        VI2Max: float = None,
        VI2Min: float = None,
        VI3Max: float = None,
        VI3Min: float = None,
        VP1Max: float = None,
        VP1Min: float = None,
        VP2Max: float = None,
        VP2Min: float = None,
        VP3Max: float = None,
        VP3Min: float = None,
        VrMax: float = None,
        VrMin: float = None,
        Xp: float = None,
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
    :param UELId:
    :param PSSId:
    :param Aex:
    :param Bex:
    :param Alpha:
    :param Beta:
    :param IdfMin:
    :param Kc:
    :param Kd1:
    :param Kd2:
    :param Ke:
    :param Ketb:
    :param Kh:
    :param Kp1:
    :param Kp2:
    :param Kp3:
    :param Td1:
    :param Te1:
    :param Te2:
    :param Ti1:
    :param Ti2:
    :param Ti3:
    :param Tr1:
    :param Tr2:
    :param Tr3:
    :param Tr4:
    :param VO1Max:
    :param VO1Min:
    :param VO2Max:
    :param VO2Min:
    :param VO3Max:
    :param VO3Min:
    :param VD1Max:
    :param VD1Min:
    :param VI1Max:
    :param VI1Min:
    :param VI2Max:
    :param VI2Min:
    :param VI3Max:
    :param VI3Min:
    :param VP1Max:
    :param VP1Min:
    :param VP2Max:
    :param VP2Min:
    :param VP3Max:
    :param VP3Min:
    :param VrMax:
    :param VrMin:
    :param Xp:
    :param switch_command_line:
    :return:
    """

    variable_ = Variable(rastr_win=rastr_win)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.sel,
                               row_id=row_id,
                               value=sel)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.sta,
                               row_id=row_id,
                               value=sta)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.Id,
                               row_id=row_id,
                               value=Id)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.Name,
                               row_id=row_id,
                               value=Name)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.ModelType,
                               row_id=row_id,
                               value=ModelType)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.Brand,
                               row_id=row_id,
                               value=Brand)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.UELId,
                               row_id=row_id,
                               value=UELId)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.PSSId,
                               row_id=row_id,
                               value=PSSId)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.Aex,
                               row_id=row_id,
                               value=Aex)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.Bex,
                               row_id=row_id,
                               value=Bex)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.Alpha,
                               row_id=row_id,
                               value=Alpha)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.Beta,
                               row_id=row_id,
                               value=Beta)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.IdfMin,
                               row_id=row_id,
                               value=IdfMin)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.Kc,
                               row_id=row_id,
                               value=Kc)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.Kd1,
                               row_id=row_id,
                               value=Kd1)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.Kd2,
                               row_id=row_id,
                               value=Kd2)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.Ke,
                               row_id=row_id,
                               value=Ke)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.Ketb,
                               row_id=row_id,
                               value=Ketb)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.Kh,
                               row_id=row_id,
                               value=Kh)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.Kp1,
                               row_id=row_id,
                               value=Kp1)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.Kp2,
                               row_id=row_id,
                               value=Kp2)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.Kp3,
                               row_id=row_id,
                               value=Kp3)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.Td1,
                               row_id=row_id,
                               value=Td1)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.Te1,
                               row_id=row_id,
                               value=Te1)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.Te2,
                               row_id=row_id,
                               value=Te2)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.Ti1,
                               row_id=row_id,
                               value=Ti1)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.Ti2,
                               row_id=row_id,
                               value=Ti2)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.Ti3,
                               row_id=row_id,
                               value=Ti3)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.Tr1,
                               row_id=row_id,
                               value=Tr1)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.Tr2,
                               row_id=row_id,
                               value=Tr2)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.Tr3,
                               row_id=row_id,
                               value=Tr3)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.Tr4,
                               row_id=row_id,
                               value=Tr4)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.VO1Max,
                               row_id=row_id,
                               value=VO1Max)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.VO1Min,
                               row_id=row_id,
                               value=VO1Min)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.VO1Min,
                               row_id=row_id,
                               value=VO1Min)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.VO2Max,
                               row_id=row_id,
                               value=VO2Max)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.VO2Min,
                               row_id=row_id,
                               value=VO2Min)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.VO3Max,
                               row_id=row_id,
                               value=VO3Max)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.VO3Min,
                               row_id=row_id,
                               value=VO3Min)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.VD1Max,
                               row_id=row_id,
                               value=VD1Max)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.VD1Min,
                               row_id=row_id,
                               value=VD1Min)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.VI1Max,
                               row_id=row_id,
                               value=VI1Max)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.VI1Min,
                               row_id=row_id,
                               value=VI1Min)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.VI2Max,
                               row_id=row_id,
                               value=VI2Max)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.VI2Min,
                               row_id=row_id,
                               value=VI2Min)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.VI3Max,
                               row_id=row_id,
                               value=VI3Max)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.VI3Min,
                               row_id=row_id,
                               value=VI3Min)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.VP1Max,
                               row_id=row_id,
                               value=VP1Max)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.VP1Min,
                               row_id=row_id,
                               value=VP1Min)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.VP2Max,
                               row_id=row_id,
                               value=VP2Max)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.VP2Min,
                               row_id=row_id,
                               value=VP2Min)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.VP3Max,
                               row_id=row_id,
                               value=VP3Max)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.VP3Min,
                               row_id=row_id,
                               value=VP3Min)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.VrMax,
                               row_id=row_id,
                               value=VrMax)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.VrMin,
                               row_id=row_id,
                               value=VrMin)

    variable_.make_changes_row(table=DFWTHYNE14.table,
                               column=DFWTHYNE14.Xp,
                               row_id=row_id,
                               value=Xp)
