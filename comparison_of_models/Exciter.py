# -*- coding: utf-8 -*-
# Модуль переменных таблицы  "Возбудитель" RastrWin3

class Exciter:
    """

    """
    table: str = 'Exciter'  # название таблицы
    table_name: str = '"Возбудитель (ИД)"'

    sel: str = 'sel'  # Отметка
    sta: str = 'sta'  # Состояние возбудителя
    Id: str = 'Id'  # Номер возбудителя
    Name: str = 'Name'  # Название возбудителя
    CustomModel: str = 'CustomModel'  # Модель в конструкторе
    ModelType: str = 'ModelType'  # Модель возбудителя
    Brand: str = 'Brand'  # Марка возбудителя
    ExcControlId: str = 'ExcControlId'  # N_АРВ
    ForcerId: str = 'ForcerId'  # Номер форсировки
    Texc: str = 'Texc'  # Постоянная времени возбудителя
    Kig: str = 'Kig'  # Коэффициент регулирования по отклонению тока статора
    Kif: str = 'Kif'  # Коэффициент регулирования по отклонению тока ротора
    Uf_min: str = 'Uf_min'  # Минимальное значение напряжения возбуждения
    Uf_max: str = 'Uf_max'  # Максимальное значение напряжения возбуждения
    If_min: str = 'If_min'  # Минимальное значение тока возбуждения
    If_max: str = 'If_max'  # Максимальное значение тока возбуждения
    Karv: str = 'Karv'  # Ku Коэффициент усиления по сигналу АРВ
    T2exc: str = 'T2exc'  # Постоянная времени Т2 (Ig)
    T3exc: str = 'T3exc'  # Постоянная времени Т3( If)
    Type_rg_max: str = 'Type_rg_max'  # Тип Uf_max
    Udop2: str = 'Udop2'  # Дополнительный сигнал на вход
    Uexc: str = 'Uexc'  # Uf Выход возбудителя
    Urvi_max: str = 'Urvi_max'  # Максимальное значение сигнала РВ
    Urvi_min: str = 'Urvi_min'  # Минимальное значение сигнала РВ
    Type_rg: str = 'Type_rg'  # Тип возбуждения


class ExciterDescription:
    """

    """
    table: str = 'Имя таблицы: Exciter'
    table_name: str = 'Назване таблицы: "Возбудитель (ИД)"'

    row_id: str = f'Порядковый номер в таблице Генераторы(ИД): возвращается функцией FindNexSel'
    sel: str = f'Отметка [O]-[{Exciter.sel}]'
    sta: str = f'Состояние возбудителя [S]-[{Exciter.sta}]'
    Id: str = f'Номер возбудителя [N]-[{Exciter.Id}]'
    Name: str = f'Название возбудителя [Название]-[{Exciter.Name}]'
    CustomModel: str = f'Модель в конструкторе [Конструктор]-[{Exciter.CustomModel}]'
    ModelType: str = f'Модель возбудителя [Модель]-[{Exciter.ModelType}]'
    Brand: str = f'Марка возбудителя [Марка]-[{Exciter.Brand}]'
    ExcControlId: str = f'N_АРВ [N_АРВ]-[{Exciter.ExcControlId}]'
    ForcerId: str = f'Номер форсировки [N форс]-[{Exciter.ForcerId}]'
    Texc: str = f'Постоянная времени возбудителя [T_возб]-[{Exciter.Texc}]'
    Kig: str = f'Коэффициент регулирования по отклонению тока статора [K_iг]-[{Exciter.Kig}]'
    Kif: str = f'Коэффициент регулирования по отклонению тока ротора [K_if]-[{Exciter.Kif}]'
    Uf_min: str = f'Минимальное значение напряжения возбуждения [Uf_min]-[{Exciter.Uf_min}]'
    Uf_max: str = f'Максимальное значение напряжения возбуждения [Uf_max]-[{Exciter.Uf_max}]'
    If_min: str = f'Минимальное значение тока возбуждения [If_min]-[{Exciter.If_min}]'
    If_max: str = f'Максимальное значение тока возбуждения [If_max]-[{Exciter.If_max}]'
    Karv: str = f'Коэффициент усиления по сигналу АРВ [Karv]-[{Exciter.Karv}]'
    T2exc: str = f'Постоянная времени Т2 (Ig) [T2(Ig)]-[{Exciter.T2exc}]'
    T3exc: str = f'Постоянная времени Т3(If) [Т3(If)]-[{Exciter.T3exc}]'
    Type_rg_max: str = f'Тип Uf_max [ТипUf_max]-[{Exciter.Type_rg_max}]'
    Udop2: str = f'Дополнительный сигнал на вход [Udop2]-[{Exciter.Udop2}]'
    Uexc: str = f'Выход возбудителя [Uf]-[{Exciter.Uexc}]'
    Urvi_max: str = f'Максимальное значение сигнала РВ [Urv_max]-[{Exciter.Urvi_max}]'
    Urvi_min: str = f'Минимальное значение сигнала РВ [Urv_min]-[{Exciter.Urvi_min}]'
    Type_rg: str = f'Тип возбуждения [Тип]-[{Exciter.Type_rg}]'


param_exciter = [Exciter.Id, Exciter.Name, Exciter.ModelType, Exciter.CustomModel, Exciter.ExcControlId, Exciter.ForcerId,
                 Exciter.Texc, Exciter.Kig, Exciter.Kif, Exciter.Uf_min, Exciter.Uf_max, Exciter.If_max, Exciter.If_min,
                 Exciter.Type_rg, Exciter.Karv, Exciter.T3exc]

param_exciter_x = [Exciter.Texc, Exciter.Kig, Exciter.Kif, Exciter.Uf_min, Exciter.Uf_max,
                   Exciter.If_max, Exciter.If_min, Exciter.Karv, Exciter.T3exc]
