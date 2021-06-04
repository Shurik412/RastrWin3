# -*- coding: utf-8 -*-
# Модуль заполнения таблицы  "Форсировка (ИД)" RastrWin3

from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.tables.Dynamic.Forcer import Forcer, ForcerDescription
from RastrWinLib.variables.variable_parametrs import Variable


def filling_Forcer(
        rastr_win=RASTR,
        row_id: int = None,
        sel: bool = None,
        sta: bool = None,
        Id: int = None,
        Name: str = None,
        ModelType: str = None,
        Brand: str = None,
        CustomModel: str = None,
        Ubf: float = None,
        Uef: float = None,
        Ubrf: float = None,
        Uerf: float = None,
        Ufors: float = None,
        Rf: float = None,
        Rrf: float = None,
        Texc_f: float = None,
        Tz_in: float = None,
        Tz_out: float = None,
        Texc_rf: float = None,
        switch_command_line: bool = False
):
    """

    :param rastr_win: COM - объект Rastr.Astra (win32com);
    :param row_id: Порядковый номер в таблице: возвращается функцией FindNexSel;
    :param sel: Отметка [O];
    :param sta: Состояние форсировки [S];
    :param Id: Номер форсировки [N];
    :param Name: Название форсировки [Название];
    :param ModelType: Модель форсировки [Модель];
    :param Brand: Марка форсировки [Марка];
    :param CustomModel: Модель в конструкторе [Конструктор];
    :param Ubf: Напряжение ввода форсировки [U_ввф];
    :param Uef: Напряжение снятия форсировки [U_снф];
    :param Ubrf: Напряжение ввода расфорсировки [U_вврф];
    :param Uerf: Напряжение снятия расфорсировки [U_снрф];
    :param Ufors:
    :param Rf: Кратность форсировки [К_ф];
    :param Rrf: Кратность расфорсировки [К_рф];
    :param Texc_f: Постоянная времени возбудит. при форсировке [Т_ф];
    :param Tz_in: Задержка времени возбудит. при форсировке [Тз_ввод];
    :param Tz_out: Задержка времени возбудит. при расфорсировке [Тз_снятия];
    :param Texc_rf: Постоянная времени возбудит. при расфорсировке
    :param switch_command_line:
    :return:
    """
    variable_ = Variable(rastr_win=rastr_win)

    variable_.make_changes_row(table=Forcer.table,
                               column=Forcer.sel,
                               row_id=row_id,
                               value=sel)

    variable_.make_changes_row(table=Forcer.table,
                               column=Forcer.sta,
                               row_id=row_id,
                               value=sta)

    variable_.make_changes_row(table=Forcer.table,
                               column=Forcer.Id,
                               row_id=row_id,
                               value=Id)

    variable_.make_changes_row(table=Forcer.table,
                               column=Forcer.Name,
                               row_id=row_id,
                               value=Name)

    variable_.make_changes_row(table=Forcer.table,
                               column=Forcer.ModelType,
                               row_id=row_id,
                               value=ModelType)

    variable_.make_changes_row(table=Forcer.table,
                               column=Forcer.Brand,
                               row_id=row_id,
                               value=Brand)

    variable_.make_changes_row(table=Forcer.table,
                               column=Forcer.CustomModel,
                               row_id=row_id,
                               value=CustomModel)

    variable_.make_changes_row(table=Forcer.table,
                               column=Forcer.Ubf,
                               row_id=row_id,
                               value=Ubf)

    variable_.make_changes_row(table=Forcer.table,
                               column=Forcer.Uef,
                               row_id=row_id,
                               value=Uef)

    variable_.make_changes_row(table=Forcer.table,
                               column=Forcer.Ubrf,
                               row_id=row_id,
                               value=Ubrf)

    variable_.make_changes_row(table=Forcer.table,
                               column=Forcer.Uerf,
                               row_id=row_id,
                               value=Uerf)

    variable_.make_changes_row(table=Forcer.table,
                               column=Forcer.Ufors,
                               row_id=row_id,
                               value=Ufors)

    variable_.make_changes_row(table=Forcer.table,
                               column=Forcer.Rf,
                               row_id=row_id,
                               value=Rf)

    variable_.make_changes_row(table=Forcer.table,
                               column=Forcer.Rrf,
                               row_id=row_id,
                               value=Rrf)

    variable_.make_changes_row(table=Forcer.table,
                               column=Forcer.Texc_f,
                               row_id=row_id,
                               value=Texc_f)

    variable_.make_changes_row(table=Forcer.table,
                               column=Forcer.Tz_in,
                               row_id=row_id,
                               value=Tz_in)

    variable_.make_changes_row(table=Forcer.table,
                               column=Forcer.Tz_out,
                               row_id=row_id,
                               value=Tz_out)

    variable_.make_changes_row(table=Forcer.table,
                               column=Forcer.Texc_rf,
                               row_id=row_id,
                               value=Texc_rf)
