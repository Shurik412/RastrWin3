# -*- coding: utf-8 -*-
# Модуль переменных таблицы "АРС(ИД)" RastrWin3

class Governor:
    """

    """
    table: str = 'Governor'  # название таблицы
    table_name: str = '"АРС(ИД)"'

    sel: str = 'sel'  #
    sta: str = 'sta'  #
    Id: str = 'Id'  #
    Name: str = 'Name'  # Название регулятора скорости
    ModelType: str = 'ModelType'  # Модель регулятора скорости
    CustomModel: str = 'CustomModel'  # Конструктор Модель в конструкторе
    Brand: str = 'Brand'  # Марка регулятора скорости
    strs: str = 'strs'  # Статизм регулятора скорости турбины
    zn: str = 'zn'  # Зона нечувствительности
    Tr: str = 'Tr'  # Трег Постоянная времени регулятора
    otmax: str = 'otmax'  # Pt_max Максимальная мощность турбины
    otmin: str = 'otmin'  # Pt_min Минимальная мощность турбины
    CVmin: str = 'CVmin'  # CVmin Минимальная скорость перемещения клапана
    CVmax: str = 'CVmax'  # CVmax Максимальная скорость перемещения клапана
    T1: str = 'T1'  # Постоянная ОС
    K1: str = 'K1'  # K1 ОС
    K2: str = 'K2'  # K2 ОС
    BoilerId: str = 'BoilerId'  # N котла Номер котла
