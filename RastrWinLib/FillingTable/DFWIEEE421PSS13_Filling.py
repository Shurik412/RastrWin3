# -*- coding: utf-8 -*-
# Модуль заполнения таблицы  "Стабилизаторы IEEE 1-3" RastrWin3

from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.tables.Dynamic.DFWIEEE421PSS13 import DFWIEEE421PSS13, DFWIEEE421PSS13_Description
from RastrWinLib.variables.variable_parametrs import Variable


def filling_DFWIEEE421PSS13(
        rastr_win=RASTR,
        row_id: int = None,
        sel: bool = None,
        sta: bool = None,
        Id: int = None,
        Name: str = None,
        ModelType: str = None,
        Brand: str = None,
        CustomModel: str = None,
        Input1Type: str = None,
        Input2Type: str = None,
        Ks1: float = None,
        Ks2: float = None,
        Ks3: float = None,
        T1: float = None,
        T2: float = None,
        T3: float = None,
        T4: float = None,
        T5: float = None,
        T6: float = None,
        T7: float = None,
        T8: float = None,
        T9: float = None,
        T10: float = None,
        T11: float = None,
        T12: float = None,
        T13: float = None,
        Tw1: float = None,
        Tw2: float = None,
        Tw3: float = None,
        Tw4: float = None,
        A1: float = None,
        A2: float = None,
        A3: float = None,
        A4: float = None,
        A5: float = None,
        A6: float = None,
        A7: float = None,
        A8: float = None,
        M: float = None,
        N: float = None,
        Vstmax: float = None,
        Vstmin: float = None,
        Vsi1max: float = None,
        Vsi1min: float = None,
        Vsi2max: float = None,
        Vsi2min: float = None):
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
    :param Input1Type:
    :param Input2Type:
    :param Ks1:
    :param Ks2:
    :param Ks3:
    :param T1:
    :param T2:
    :param T3:
    :param T4:
    :param T5:
    :param T6:
    :param T7:
    :param T8:
    :param T9:
    :param T10:
    :param T11:
    :param T12:
    :param T13:
    :param Tw1:
    :param Tw2:
    :param Tw3:
    :param Tw4:
    :param A1:
    :param A2:
    :param A3:
    :param A4:
    :param A5:
    :param A6:
    :param A7:
    :param A8:
    :param M:
    :param N:
    :param Vstmax:
    :param Vstmin:
    :param Vsi1max:
    :param Vsi1min:
    :param Vsi2max:
    :param Vsi2min:
    :return:
    """
    variable_ = Variable(rastr_win=rastr_win)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.sel,
                               row_id=row_id,
                               value=sel)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.sta,
                               row_id=row_id,
                               value=sta)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.Id,
                               row_id=row_id,
                               value=Id)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.Name,
                               row_id=row_id,
                               value=Name)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.ModelType,
                               row_id=row_id,
                               value=ModelType)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.Brand,
                               row_id=row_id,
                               value=Brand)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.CustomModel,
                               row_id=row_id,
                               value=CustomModel)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.Input1Type,
                               row_id=row_id,
                               value=Input1Type)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.Input2Type,
                               row_id=row_id,
                               value=Input2Type)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.Ks1,
                               row_id=row_id,
                               value=Ks1)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.Ks2,
                               row_id=row_id,
                               value=Ks2)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.Ks3,
                               row_id=row_id,
                               value=Ks3)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.T1,
                               row_id=row_id,
                               value=T1)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.T2,
                               row_id=row_id,
                               value=T2)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.T3,
                               row_id=row_id,
                               value=T3)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.T4,
                               row_id=row_id,
                               value=T4)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.T5,
                               row_id=row_id,
                               value=T5)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.T6,
                               row_id=row_id,
                               value=T6)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.T7,
                               row_id=row_id,
                               value=T7)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.T8,
                               row_id=row_id,
                               value=T8)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.T9,
                               row_id=row_id,
                               value=T9)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.T10,
                               row_id=row_id,
                               value=T10)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.T11,
                               row_id=row_id,
                               value=T11)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.T12,
                               row_id=row_id,
                               value=T12)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.T13,
                               row_id=row_id,
                               value=T13)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.Tw1,
                               row_id=row_id,
                               value=Tw1)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.Tw2,
                               row_id=row_id,
                               value=Tw2)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.Tw3,
                               row_id=row_id,
                               value=Tw3)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.Tw4,
                               row_id=row_id,
                               value=Tw4)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.A1,
                               row_id=row_id,
                               value=A1)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.A2,
                               row_id=row_id,
                               value=A2)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.A3,
                               row_id=row_id,
                               value=A3)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.A4,
                               row_id=row_id,
                               value=A4)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.A5,
                               row_id=row_id,
                               value=A5)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.A6,
                               row_id=row_id,
                               value=A6)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.A7,
                               row_id=row_id,
                               value=A7)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.A8,
                               row_id=row_id,
                               value=A8)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.M,
                               row_id=row_id,
                               value=M)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.N,
                               row_id=row_id,
                               value=N)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.Vstmax,
                               row_id=row_id,
                               value=Vstmax)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.Vstmin,
                               row_id=row_id,
                               value=Vstmin)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.Vsi1max,
                               row_id=row_id,
                               value=Vsi1max)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.Vsi1min,
                               row_id=row_id,
                               value=Vsi1min)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.Vsi2max,
                               row_id=row_id,
                               value=Vsi2max)

    variable_.make_changes_row(table=DFWIEEE421PSS13.table,
                               column=DFWIEEE421PSS13.Vsi2min,
                               row_id=row_id,
                               value=Vsi2min)
