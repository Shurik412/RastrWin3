# -*- coding: utf-8 -*-
# Модуль заполнения таблицы  "Стабилизаторы IEEE 4B" RastrWin3

from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.tables.Dynamic.DFWIEEE421PSS4B import DFWIEEE421PSS4B, DFWIEEE421PSS4B_Description
from RastrWinLib.variables.variable_parametrs import Variable


def filling_DFWIEEE421PSS4B(
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
        MBPSS1: str = None,
        MBPSS2: str = None,
        Vstmax: float = None,
        Vstmin: float = None,
        Vlmax: float = None,
        Vlmin: float = None,
        Vimax: float = None,
        Vimin: float = None,
        Vvlmax: float = None,
        Vvlmin: float = None,
        Vhmax: float = None,
        Vhmin: float = None,
        KL: float = None,
        KL1: float = None,
        KL2: float = None,
        KL11: float = None,
        KL17: float = None,
        KI: float = None,
        KI1: float = None,
        KI2: float = None,
        KI11: float = None,
        KI17: float = None,
        KH: float = None,
        KH1: float = None,
        KH2: float = None,
        KH11: float = None,
        KH17: float = None,
        TL1: float = None,
        TL2: float = None,
        TL3: float = None,
        TL4: float = None,
        TL5: float = None,
        TL6: float = None,
        TL7: float = None,
        TL8: float = None,
        TL9: float = None,
        TL10: float = None,
        TL11: float = None,
        TL12: float = None,
        TI1: float = None,
        TI2: float = None,
        TI3: float = None,
        TI4: float = None,
        TI5: float = None,
        TI6: float = None,
        TI7: float = None,
        TI8: float = None,
        TI9: float = None,
        TI10: float = None,
        TI11: float = None,
        TI12: float = None,
        TH1: float = None,
        TH2: float = None,
        TH3: float = None,
        TH4: float = None,
        TH5: float = None,
        TH6: float = None,
        TH7: float = None,
        TH8: float = None,
        TH9: float = None,
        TH10: float = None,
        TH11: float = None,
        TH12: float = None,
        switch_command_line: bool = False):
    """

    :param switch_command_line:
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
    :param MBPSS1:
    :param MBPSS2:
    :param Vstmax:
    :param Vstmin:
    :param Vlmax:
    :param Vlmin:
    :param Vimax:
    :param Vimin:
    :param Vvlmax:
    :param Vvlmin:
    :param Vhmax:
    :param Vhmin:
    :param KL:
    :param KL1:
    :param KL2:
    :param KL11:
    :param KL17:
    :param KI:
    :param KI1:
    :param KI2:
    :param KI11:
    :param KI17:
    :param KH:
    :param KH1:
    :param KH2:
    :param KH11:
    :param KH17:
    :param TL1:
    :param TL2:
    :param TL3:
    :param TL4:
    :param TL5:
    :param TL6:
    :param TL7:
    :param TL8:
    :param TL9:
    :param TL10:
    :param TL11:
    :param TL12:
    :param TI1:
    :param TI2:
    :param TI3:
    :param TI4:
    :param TI5:
    :param TI6:
    :param TI7:
    :param TI8:
    :param TI9:
    :param TI10:
    :param TI11:
    :param TI12:
    :param TH1:
    :param TH2:
    :param TH3:
    :param TH4:
    :param TH5:
    :param TH6:
    :param TH7:
    :param TH8:
    :param TH9:
    :param TH10:
    :param TH11:
    :param TH12:
    :return:
    """

    variable_ = Variable(rastr_win=rastr_win)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.sel,
                               row_id=row_id,
                               value=sel)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.sta,
                               row_id=row_id,
                               value=sta)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.Id,
                               row_id=row_id,
                               value=Id)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.Name,
                               row_id=row_id,
                               value=Name)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.ModelType,
                               row_id=row_id,
                               value=ModelType)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.Brand,
                               row_id=row_id,
                               value=Brand)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.CustomModel,
                               row_id=row_id,
                               value=CustomModel)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.Input1Type,
                               row_id=row_id,
                               value=Input1Type)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.Input2Type,
                               row_id=row_id,
                               value=Input2Type)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.MBPSS1,
                               row_id=row_id,
                               value=MBPSS1)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.MBPSS2,
                               row_id=row_id,
                               value=MBPSS2)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.Vstmax,
                               row_id=row_id,
                               value=Vstmax)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.Vstmin,
                               row_id=row_id,
                               value=Vstmin)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.Vlmax,
                               row_id=row_id,
                               value=Vlmax)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.Vlmin,
                               row_id=row_id,
                               value=Vlmin)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.Vimax,
                               row_id=row_id,
                               value=Vimax)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.Vimin,
                               row_id=row_id,
                               value=Vimin)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.Vvlmax,
                               row_id=row_id,
                               value=Vvlmax)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.Vvlmin,
                               row_id=row_id,
                               value=Vvlmin)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.Vhmax,
                               row_id=row_id,
                               value=Vhmax)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.Vhmin,
                               row_id=row_id,
                               value=Vhmin)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.KL,
                               row_id=row_id,
                               value=KL)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.KL1,
                               row_id=row_id,
                               value=KL1)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.KL2,
                               row_id=row_id,
                               value=KL2)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.KL11,
                               row_id=row_id,
                               value=KL11)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.KL17,
                               row_id=row_id,
                               value=KL17)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.KI,
                               row_id=row_id,
                               value=KI)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.KI1,
                               row_id=row_id,
                               value=KI1)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.KI2,
                               row_id=row_id,
                               value=KI2)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.KI11,
                               row_id=row_id,
                               value=KI11)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.KI17,
                               row_id=row_id,
                               value=KI17)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.KH,
                               row_id=row_id,
                               value=KH)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.KH1,
                               row_id=row_id,
                               value=KH1)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.KH2,
                               row_id=row_id,
                               value=KH2)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.KH11,
                               row_id=row_id,
                               value=KH11)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.KH17,
                               row_id=row_id,
                               value=KH17)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.TL1,
                               row_id=row_id,
                               value=TL1)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.TL2,
                               row_id=row_id,
                               value=TL2)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.TL3,
                               row_id=row_id,
                               value=TL3)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.TL4,
                               row_id=row_id,
                               value=TL4)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.TL5,
                               row_id=row_id,
                               value=TL5)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.TL6,
                               row_id=row_id,
                               value=TL6)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.TL7,
                               row_id=row_id,
                               value=TL7)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.TL8,
                               row_id=row_id,
                               value=TL8)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.TL9,
                               row_id=row_id,
                               value=TL9)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.TL10,
                               row_id=row_id,
                               value=TL10)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.TL11,
                               row_id=row_id,
                               value=TL11)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.TL12,
                               row_id=row_id,
                               value=TL12)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.TI1,
                               row_id=row_id,
                               value=TI1)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.TI2,
                               row_id=row_id,
                               value=TI2)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.TI3,
                               row_id=row_id,
                               value=TI3)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.TI4,
                               row_id=row_id,
                               value=TI4)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.TI5,
                               row_id=row_id,
                               value=TI5)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.TI6,
                               row_id=row_id,
                               value=TI6)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.TI7,
                               row_id=row_id,
                               value=TI7)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.TI8,
                               row_id=row_id,
                               value=TI8)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.TI9,
                               row_id=row_id,
                               value=TI9)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.TI10,
                               row_id=row_id,
                               value=TI10)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.TI11,
                               row_id=row_id,
                               value=TI11)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.TI12,
                               row_id=row_id,
                               value=TI12)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.TH1,
                               row_id=row_id,
                               value=TH1)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.TH2,
                               row_id=row_id,
                               value=TH2)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.TH3,
                               row_id=row_id,
                               value=TH3)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.TH4,
                               row_id=row_id,
                               value=TH4)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.TH5,
                               row_id=row_id,
                               value=TH5)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.TH6,
                               row_id=row_id,
                               value=TH6)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.TH7,
                               row_id=row_id,
                               value=TH7)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.TH8,
                               row_id=row_id,
                               value=TH8)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.TH9,
                               row_id=row_id,
                               value=TH9)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.TH10,
                               row_id=row_id,
                               value=TH10)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.TH11,
                               row_id=row_id,
                               value=TH11)

    variable_.make_changes_row(table=DFWIEEE421PSS4B.table,
                               column=DFWIEEE421PSS4B.TH12,
                               row_id=row_id,
                               value=TH12)