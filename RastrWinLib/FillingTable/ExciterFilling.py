# -*- coding: utf-8 -*-
# Модуль заполнения таблицы  "Возбудитель (ИД)" RastrWin3

from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.tables.Dynamic.Exciter import Exciter, ExciterDescription
from RastrWinLib.variables.variable_parametrs import Variable


def filling_exciter(
        rastr_win=RASTR,
        row_id=None,
        Id: int = None,
        sel: bool = None,
        sta: bool = None,
        Name: str = None,
        CustomModel: str = None,
        ModelType: str = None,
        Brand: str = None,
        ExcControlId: int = None,
        ForcerId: int = None,
        Texc: float = None,
        Kig: float = None,
        Kif: float = None,
        Uf_min: float = None,
        Uf_max: float = None,
        If_min: float = None,
        If_max: float = None,
        Karv: float = None,
        T2exc: float = None,
        T3exc: float = None,
        Type_rg_max: int = None,
        Udop2: float = None,
        Uexc: float = None,
        Urvi_max: float = None,
        Urvi_min: float = None,
        Type_rg: int = None,
        switch_command_line: bool = False):
    f"""
    Функция заполнения таблицы: "Возбудитель (ИД)"
    
    :param rastr_win: COM - объект Rastr.Astra (win32com);
    :param row_id: Порядковый номер в таблице Генераторы(ИД): возвращается функцией FindNexSel;
    :param Id: Номер возбудителя [N];
    :param table: Имя таблицы "Возбудитель (ИД)";
    :param sel: Отметка [O];
    :param sta: Состояние возбудителя [S];
    :param Name: Название возбудителя [Название];
    :param CustomModel: Модель в конструкторе [Конструктор];
    :param ModelType: Модель возбудителя [Модель];
    :param Brand: Марка возбудителя [Марка];
    :param ExcControlId: N_АРВ [N_АРВ];
    :param ForcerId: Номер форсировки [N форс];
    :param Texc: Постоянная времени возбудителя [T_возб];
    :param Kig: Коэффициент регулирования по отклонению тока статора [K_iг];
    :param Kif: Коэффициент регулирования по отклонению тока ротора [K_if];
    :param Uf_min: Минимальное значение напряжения возбуждения [Uf_min]; 
    :param Uf_max: Максимальное значение напряжения возбуждения [Uf_max];
    :param If_min: Минимальное значение тока возбуждения [If_min];
    :param If_max: Максимальное значение тока возбуждения [If_max];
    :param Karv: Коэффициент усиления по сигналу АРВ [Karv]; 
    :param T2exc: Постоянная времени Т2 (Ig) [T2(Ig)]; 
    :param T3exc: Постоянная времени Т3(If) [Т3(If)]; 
    :param Type_rg_max: Тип Uf_max [ТипUf_max];
    :param Udop2: Дополнительный сигнал на вход [Udop2];
    :param Uexc: Выход возбудителя [Uf];
    :param Urvi_max: Максимальное значение сигнала РВ [Urv_max];
    :param Urvi_min: Минимальное значение сигнала РВ [Urv_min]; 
    :param Type_rg: Тип возбуждения [Тип]; 
    :param switch_command_line: True/False - вывод сообщений в протокол;
    :return: 
    """
    variable_ = Variable(rastr_win=rastr_win)

    variable_.make_changes_row(table=Exciter.table,
                               column=Exciter.Id,
                               row_id=row_id,
                               value=Id)

    variable_.make_changes_row(table=Exciter.table,
                               column=Exciter.sel,
                               row_id=row_id,
                               value=sel)

    variable_.make_changes_row(table=Exciter.table,
                               column=Exciter.sta,
                               row_id=row_id,
                               value=sta)

    variable_.make_changes_row(table=Exciter.table,
                               column=Exciter.Name,
                               row_id=row_id,
                               value=Name)

    variable_.make_changes_row(table=Exciter.table,
                               column=Exciter.CustomModel,
                               row_id=row_id,
                               value=CustomModel)

    variable_.make_changes_row(table=Exciter.table,
                               column=Exciter.ModelType,
                               row_id=row_id,
                               value=ModelType)

    variable_.make_changes_row(table=Exciter.table,
                               column=Exciter.Brand,
                               row_id=row_id,
                               value=Brand)

    variable_.make_changes_row(table=Exciter.table,
                               column=Exciter.ExcControlId,
                               row_id=row_id,
                               value=ExcControlId)

    variable_.make_changes_row(table=Exciter.table,
                               column=Exciter.ForcerId,
                               row_id=row_id,
                               value=ForcerId)

    variable_.make_changes_row(table=Exciter.table,
                               column=Exciter.Texc,
                               row_id=row_id,
                               value=Texc)

    variable_.make_changes_row(table=Exciter.table,
                               column=Exciter.Kig,
                               row_id=row_id,
                               value=Kig)

    variable_.make_changes_row(table=Exciter.table,
                               column=Exciter.Kif,
                               row_id=row_id,
                               value=Kif)

    variable_.make_changes_row(table=Exciter.table,
                               column=Exciter.Uf_min,
                               row_id=row_id,
                               value=Uf_min)

    variable_.make_changes_row(table=Exciter.table,
                               column=Exciter.Uf_max,
                               row_id=row_id,
                               value=Uf_max)

    variable_.make_changes_row(table=Exciter.table,
                               column=Exciter.If_min,
                               row_id=row_id,
                               value=If_min)

    variable_.make_changes_row(table=Exciter.table,
                               column=Exciter.If_max,
                               row_id=row_id,
                               value=If_max)

    variable_.make_changes_row(table=Exciter.table,
                               column=Exciter.Karv,
                               row_id=row_id,
                               value=Karv)

    variable_.make_changes_row(table=Exciter.table,
                               column=Exciter.T2exc,
                               row_id=row_id,
                               value=T2exc)

    variable_.make_changes_row(table=Exciter.table,
                               column=Exciter.T3exc,
                               row_id=row_id,
                               value=T3exc)

    variable_.make_changes_row(table=Exciter.table,
                               column=Exciter.Type_rg_max,
                               row_id=row_id,
                               value=Type_rg_max)

    variable_.make_changes_row(table=Exciter.table,
                               column=Exciter.Udop2,
                               row_id=row_id,
                               value=Udop2)

    variable_.make_changes_row(table=Exciter.table,
                               column=Exciter.Uexc,
                               row_id=row_id,
                               value=Uexc)

    variable_.make_changes_row(table=Exciter.table,
                               column=Exciter.Urvi_max,
                               row_id=row_id,
                               value=Urvi_max)

    variable_.make_changes_row(table=Exciter.table,
                               column=Exciter.Urvi_min,
                               row_id=row_id,
                               value=Urvi_min)

    variable_.make_changes_row(table=Exciter.table,
                               column=Exciter.Type_rg,
                               row_id=row_id,
                               value=Type_rg)
