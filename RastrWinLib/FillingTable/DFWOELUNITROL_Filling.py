# -*- coding: utf-8 -*-
# Модуль заполнения таблицы  "БОР UNITROL" RastrWin3

from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.Tables.Dynamic.DFWOELUNITROL import DFWOELUNITROL
from RastrWinLib.ActionsObject.Variable import Variable


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
    Функция filling_DFWOELUNITROL - вносит изменения в таблицу "БОР UNITROL".

    :param rastr_win: COM - объект Rastr.Astra (win32com);
    :param row_id: Порядковый номер в таблице: возвращается функцией FindNexSel;
    :param sel: Отметка [O];
    :param sta: Состояние БОР [S];
    :param Id: Номер БОР [N БОР];
    :param Name: Название БОР [Название];
    :param ModelType: Модель БОР [Модель];
    :param Brand: Марка БОР [Марка];
    :param CustomModel: Модель в конструкторе [Конструктор];
    :param IfMax: Максимальный ток возбуждения [IfMax];
    :param Ifth: Максимальный ток возбуждения по нагреву [Ifth];
    :param KexpIf: Показатель степени тепловой характеристики [KexpIf];
    :param KR3: Коэффициент усиления ограничения [KR3];
    :param KR3i: Дополнительный коэффициент усиления ограничения [KR3i];
    :param Kth: Коэффициент усиления переключателя теплового канала [Kth];
    :param KToF: Постоянная интегрирования [KTof];
    :param KcF: Постоянная охлаждения [KcF];
    :param KhF: Постоянная обратной время-токовой зависимости [KhF];
    :param Tc13: Постоянная времени [Tc13];
    :param Tc23: Постоянная времени [Tc23];
    :param Tb13: Постоянная времени [Tb13];
    :param Tb23: Постоянная времени [Tb23];
    :param Tdel: Выдержка времени [Tвыд];
    :param Vamax: Максимальное ограничение регулятора [Vamax];
    :param Vamin: Минимальное ограничение регулятора [Vamin];
    :param TRFout: Тип регулятора [TRFout];
    :param Tr: Постоянная времени измерительного фильтра [Tr];
    :param Output: Режим выхода [Выход];
    :param switch_command_line: True/False - вывод сообщений в протокол;
    :return: Noting return.
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
