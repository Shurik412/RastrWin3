# -*- coding: utf-8 -*-
# Модуль заполнения таблицы  "Возбудитель (ИД)" RastrWin3

from RastrWinLib.AstraRastr import RASTR, RastrDoc
from RastrWinLib.tables.Dynamic.Exciter import Exciter, ExciterDescription
from RastrWinLib.tools.tools import Tools
from RastrWinLib.variables.variable_parametrs import Variable


def filling_exciter(
        rastr_win=RASTR,
        row_id=None,
        Id: int = None,
        table: str = Exciter.table,
        sel: int = None,
        sta: int = None,
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
        switch_command_line=False):
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

