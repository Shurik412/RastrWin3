# -*- coding: utf-8 -*-
# Модуль переменных таблицы  "Возбудитель" RastrWin3

class Exciter:
    """

    """
    table: str = 'Exciter'  # название таблицы
    table_name: str = '"Возбудитель"'

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
    Ku: str = 'Ku'  # Коэффициент усиления по сигналу АРВ
    T2exc: str = 'T2exc'  # Постоянная времени Т2 (Ig)
    T3exc: str = 'T3exc'  # Постоянная времени Т3( If)
    Type_rg_max: str = 'Type_rg_max'  # Тип Uf_max
    Udop2: str = 'Udop2'  # Дополнительный сигнал на вход
    Uexc: str = 'Uexc'  # Uf Выход возбудителя
    Urvi_max: str = 'Urvi_max'  # Максимальное значение сигнала РВ
    Urvi_min: str = 'Urvi_min'  # Минимальное значение сигнала РВ
    Type_rg: str = 'Type_rg'  # Тип возбуждения
