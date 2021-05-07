# -*- coding: utf-8 -*-
# Модуль заполнения таблицы  "БОР UNITROL" RastrWin3

from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.tables.Dynamic.DFWOELUNITROL import DFWOELUNITROL, DFWOELUNITROL_Description
from RastrWinLib.variables.variable_parametrs import Variable


def filling_DFWOELUNITROL(
        rastr_win=RASTR,
        row_id: int = None,
        sel: bool = None,
        sta: bool = None,
        Id: int = None,
        Name: str = None,
        ModelType: str = None,
        Brand: str = None,
        CustomModel: str = None,
        IfMax: float = None,
        Ifth: float = None,
        KexpIf: float = None,
        KR3: float = None,
        KR3i: float = None,
        Kth: float = None,
        KToF: float = None,
        KcF: float = None,
        KhF: float = None,
        Tc13: float = None,
        Tc23: float = None,
        Tb13: float = None,
        Tb23: float = None,
        Tdel: float = None,
        Vamax: float = None,
        Vamin: float = None,
        TRFout: float = None,
        Tr: float = None,
        Output: float = None,
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
    :param IfMax:
    :param Ifth:
    :param KexpIf:
    :param KR3:
    :param KR3i:
    :param Kth:
    :param KToF:
    :param KcF:
    :param KhF:
    :param Tc13:
    :param Tc23:
    :param Tb13:
    :param Tb23:
    :param Tdel:
    :param Vamax:
    :param Vamin:
    :param TRFout:
    :param Tr:
    :param Output:
    :param switch_command_line:
    :return:
    """
    variable_ = Variable(rastr_win=rastr_win)

    variable_.make_changes_row(table=DFWOELUNITROL.table,
                               column=DFWOELUNITROL.sel,
                               row_id=row_id,
                               value=sel)

    variable_.make_changes_row(table=DFWOELUNITROL.table,
                               column=DFWOELUNITROL.sta,
                               row_id=row_id,
                               value=sta)

    variable_.make_changes_row(table=DFWOELUNITROL.table,
                               column=DFWOELUNITROL.Id,
                               row_id=row_id,
                               value=Id)

    variable_.make_changes_row(table=DFWOELUNITROL.table,
                               column=DFWOELUNITROL.Name,
                               row_id=row_id,
                               value=Name)

    variable_.make_changes_row(table=DFWOELUNITROL.table,
                               column=DFWOELUNITROL.ModelType,
                               row_id=row_id,
                               value=ModelType)

    variable_.make_changes_row(table=DFWOELUNITROL.table,
                               column=DFWOELUNITROL.Brand,
                               row_id=row_id,
                               value=Brand)

    variable_.make_changes_row(table=DFWOELUNITROL.table,
                               column=DFWOELUNITROL.CustomModel,
                               row_id=row_id,
                               value=CustomModel)

    variable_.make_changes_row(table=DFWOELUNITROL.table,
                               column=DFWOELUNITROL.IfMax,
                               row_id=row_id,
                               value=IfMax)

    variable_.make_changes_row(table=DFWOELUNITROL.table,
                               column=DFWOELUNITROL.Ifth,
                               row_id=row_id,
                               value=Ifth)

    variable_.make_changes_row(table=DFWOELUNITROL.table,
                               column=DFWOELUNITROL.KexpIf,
                               row_id=row_id,
                               value=KexpIf)

    variable_.make_changes_row(table=DFWOELUNITROL.table,
                               column=DFWOELUNITROL.KR3,
                               row_id=row_id,
                               value=KR3)

    variable_.make_changes_row(table=DFWOELUNITROL.table,
                               column=DFWOELUNITROL.KR3i,
                               row_id=row_id,
                               value=KR3i)

    variable_.make_changes_row(table=DFWOELUNITROL.table,
                               column=DFWOELUNITROL.Kth,
                               row_id=row_id,
                               value=Kth)

    variable_.make_changes_row(table=DFWOELUNITROL.table,
                               column=DFWOELUNITROL.KToF,
                               row_id=row_id,
                               value=KToF)

    variable_.make_changes_row(table=DFWOELUNITROL.table,
                               column=DFWOELUNITROL.KcF,
                               row_id=row_id,
                               value=KcF)

    variable_.make_changes_row(table=DFWOELUNITROL.table,
                               column=DFWOELUNITROL.KhF,
                               row_id=row_id,
                               value=KhF)

    variable_.make_changes_row(table=DFWOELUNITROL.table,
                               column=DFWOELUNITROL.Tc13,
                               row_id=row_id,
                               value=Tc13)

    variable_.make_changes_row(table=DFWOELUNITROL.table,
                               column=DFWOELUNITROL.Tc23,
                               row_id=row_id,
                               value=Tc23)

    variable_.make_changes_row(table=DFWOELUNITROL.table,
                               column=DFWOELUNITROL.Tb13,
                               row_id=row_id,
                               value=Tb13)

    variable_.make_changes_row(table=DFWOELUNITROL.table,
                               column=DFWOELUNITROL.Tb23,
                               row_id=row_id,
                               value=Tb23)

    variable_.make_changes_row(table=DFWOELUNITROL.table,
                               column=DFWOELUNITROL.Tdel,
                               row_id=row_id,
                               value=Tdel)

    variable_.make_changes_row(table=DFWOELUNITROL.table,
                               column=DFWOELUNITROL.Vamax,
                               row_id=row_id,
                               value=Vamax)

    variable_.make_changes_row(table=DFWOELUNITROL.table,
                               column=DFWOELUNITROL.Vamin,
                               row_id=row_id,
                               value=Vamin)

    variable_.make_changes_row(table=DFWOELUNITROL.table,
                               column=DFWOELUNITROL.TRFout,
                               row_id=row_id,
                               value=TRFout)

    variable_.make_changes_row(table=DFWOELUNITROL.table,
                               column=DFWOELUNITROL.Tr,
                               row_id=row_id,
                               value=Tr)

    variable_.make_changes_row(table=DFWOELUNITROL.table,
                               column=DFWOELUNITROL.Output,
                               row_id=row_id,
                               value=Output)
