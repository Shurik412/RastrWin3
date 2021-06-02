# -*- coding: utf-8 -*-
# Модуль заполнения таблицы  "ОМВ" RastrWin3

from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.tables.Dynamic.DFW421UEL import DFW421UEL, DFW421UEL_Description
from RastrWinLib.variables.variable_parametrs import Variable


def filling_DFW421UEL(
        rastr_win=RASTR,
        row_id: int = None,
        sel: bool = None,
        sta: bool = None,
        Id: int = None,
        Name: str = None,
        ModelType: str = None,
        Brand: str = None,
        CustomModel: str = None,
        Dependency_F1: str = None,
        Output: str = None,
        K1: float = None,
        K2: float = None,
        Kul: float = None,
        Kui: float = None,
        Kuf: float = None,
        Kur: float = None,
        Kuc: float = None,
        Kl: float = None,
        Tu1: float = None,
        Tu2: float = None,
        Tu3: float = None,
        Tu4: float = None,
        Tuf: float = None,
        TuV: float = None,
        TuP: float = None,
        TuQ: float = None,
        Vurmax: float = None,
        Vucmax: float = None,
        Vulmax: float = None,
        Vulmin: float = None,
        Vuimin: float = None,
        Vuimax: float = None,
        switch_command_line: bool = False
):
    """

    :param rastr_win: COM - объект Rastr.Astra (win32com);
    :param row_id: Порядковый номер в таблице: возвращается функцией FindNexSel;
    :param sel: Отметка [O];
    :param sta:
    :param Id:
    :param Name:
    :param ModelType:
    :param Brand:
    :param CustomModel:
    :param Dependency_F1:
    :param Output:
    :param K1:
    :param K2:
    :param Kul:
    :param Kui:
    :param Kuf:
    :param Kur:
    :param Kuc:
    :param Kl:
    :param Tu1:
    :param Tu2:
    :param Tu3:
    :param Tu4:
    :param Tuf:
    :param TuV:
    :param TuP:
    :param TuQ:
    :param Vurmax:
    :param Vucmax:
    :param Vulmax:
    :param Vulmin:
    :param Vuimin:
    :param Vuimax:
    :param switch_command_line:
    :return:
    """

    variable_ = Variable(rastr_win=rastr_win)

    variable_.make_changes_row(table=DFW421UEL.table,
                               column=DFW421UEL.sel,
                               row_id=row_id,
                               value=sel)

    variable_.make_changes_row(table=DFW421UEL.table,
                               column=DFW421UEL.sta,
                               row_id=row_id,
                               value=sta)

    variable_.make_changes_row(table=DFW421UEL.table,
                               column=DFW421UEL.Id,
                               row_id=row_id,
                               value=Id)

    variable_.make_changes_row(table=DFW421UEL.table,
                               column=DFW421UEL.Name,
                               row_id=row_id,
                               value=Name)

    variable_.make_changes_row(table=DFW421UEL.table,
                               column=DFW421UEL.ModelType,
                               row_id=row_id,
                               value=ModelType)

    variable_.make_changes_row(table=DFW421UEL.table,
                               column=DFW421UEL.Brand,
                               row_id=row_id,
                               value=Brand)

    variable_.make_changes_row(table=DFW421UEL.table,
                               column=DFW421UEL.CustomModel,
                               row_id=row_id,
                               value=CustomModel)

    variable_.make_changes_row(table=DFW421UEL.table,
                               column=DFW421UEL.Dependency_F1,
                               row_id=row_id,
                               value=Dependency_F1)

    variable_.make_changes_row(table=DFW421UEL.table,
                               column=DFW421UEL.Output,
                               row_id=row_id,
                               value=Output)

    variable_.make_changes_row(table=DFW421UEL.table,
                               column=DFW421UEL.K1,
                               row_id=row_id,
                               value=K1)

    variable_.make_changes_row(table=DFW421UEL.table,
                               column=DFW421UEL.K2,
                               row_id=row_id,
                               value=K2)

    variable_.make_changes_row(table=DFW421UEL.table,
                               column=DFW421UEL.Kul,
                               row_id=row_id,
                               value=Kul)

    variable_.make_changes_row(table=DFW421UEL.table,
                               column=DFW421UEL.Kui,
                               row_id=row_id,
                               value=Kui)

    variable_.make_changes_row(table=DFW421UEL.table,
                               column=DFW421UEL.Kuf,
                               row_id=row_id,
                               value=Kuf)

    variable_.make_changes_row(table=DFW421UEL.table,
                               column=DFW421UEL.Kur,
                               row_id=row_id,
                               value=Kur)

    variable_.make_changes_row(table=DFW421UEL.table,
                               column=DFW421UEL.Kuc,
                               row_id=row_id,
                               value=Kuc)

    variable_.make_changes_row(table=DFW421UEL.table,
                               column=DFW421UEL.Kl,
                               row_id=row_id,
                               value=Kl)

    variable_.make_changes_row(table=DFW421UEL.table,
                               column=DFW421UEL.Tu1,
                               row_id=row_id,
                               value=Tu1)

    variable_.make_changes_row(table=DFW421UEL.table,
                               column=DFW421UEL.Tu2,
                               row_id=row_id,
                               value=Tu2)

    variable_.make_changes_row(table=DFW421UEL.table,
                               column=DFW421UEL.Tu3,
                               row_id=row_id,
                               value=Tu3)

    variable_.make_changes_row(table=DFW421UEL.table,
                               column=DFW421UEL.Tu4,
                               row_id=row_id,
                               value=Tu4)

    variable_.make_changes_row(table=DFW421UEL.table,
                               column=DFW421UEL.Tuf,
                               row_id=row_id,
                               value=Tuf)

    variable_.make_changes_row(table=DFW421UEL.table,
                               column=DFW421UEL.TuV,
                               row_id=row_id,
                               value=TuV)

    variable_.make_changes_row(table=DFW421UEL.table,
                               column=DFW421UEL.TuP,
                               row_id=row_id,
                               value=TuP)

    variable_.make_changes_row(table=DFW421UEL.table,
                               column=DFW421UEL.TuQ,
                               row_id=row_id,
                               value=TuQ)

    variable_.make_changes_row(table=DFW421UEL.table,
                               column=DFW421UEL.Vurmax,
                               row_id=row_id,
                               value=Vurmax)

    variable_.make_changes_row(table=DFW421UEL.table,
                               column=DFW421UEL.Vucmax,
                               row_id=row_id,
                               value=Vucmax)

    variable_.make_changes_row(table=DFW421UEL.table,
                               column=DFW421UEL.Vulmax,
                               row_id=row_id,
                               value=Vulmax)

    variable_.make_changes_row(table=DFW421UEL.table,
                               column=DFW421UEL.Vulmin,
                               row_id=row_id,
                               value=Vulmin)

    variable_.make_changes_row(table=DFW421UEL.table,
                               column=DFW421UEL.Vuimin,
                               row_id=row_id,
                               value=Vuimin)

    variable_.make_changes_row(table=DFW421UEL.table,
                               column=DFW421UEL.Vuimax,
                               row_id=row_id,
                               value=Vuimax)
