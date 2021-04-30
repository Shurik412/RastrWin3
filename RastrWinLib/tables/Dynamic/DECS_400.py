# -*- coding: utf-8 -*-
# Модуль переменных таблицы "Возбудитель DECS-400" RastrWin3


class DFWDECS400:
    """

    """
    table: str = 'DFWDECS400'  # название таблицы
    table_name: str = '"Возбудитель DECS-400"'

    sel: str = 'sel'  #
    sta: str = 'sta'  # Состояние возбудителя
    Id: str = 'Id'  # Номер возбудителя
    Name: str = 'Name'  # Название возбудителя
    ModelType: str = 'ModelType'  # Модель возбудителя
    Brand: str = 'Brand'  #
    CustomModel: str = 'CustomModel'  # Модель в конструкторе
    PSSId: str = 'PSSId'  # Номер системного стабилизатора
    UELId: str = 'UELId'  # Номер ОМВ
    OELId: str = 'OELId'  # Номер БОР
    ForcerId: str = 'ForcerId'  # Номер РФ
    Xl: str = 'Xl'  # Потери в выпрямителе
    DRP: str = 'DRP'  # Статизм
    VrMin: str = 'VrMin'  # Минимальное ограничение потери напряжения (? цитата НИИПТ)
    VrMax: str = 'VrMax'  # Максимальное ограничение потери напряжения (? цитата НИИПТ)
    VmMax: str = 'VmMax'  # Максимальное ограничение тока контроллера
    VmMin: str = 'VmMin'  # Минимальное ограничение тока контроллера
    VbMax: str = 'VbMax'  # Максимальное напряжение возбудителя
    Kc: str = 'Kc'  # Коэффициент усиления
    Kp: str = 'Kp'  # Коэффициент усиления
    Kpm: str = 'Kpm'  # Коэффициент усиления
    Kpr: str = 'Kpr'  # Пропорциональный коэффициент усиления
    Kir: str = 'Kir'  # Интегральный коэффициент усиления
    Kpd: str = 'Kpd'  # Дифференциальный коэффициент усиления
    Ta: str = 'Ta'  # Постоянная времени тиристорного моста
    Td: str = 'Td'  # Постоянная времени дифференциального канала
    Tr: str = 'Tr'  # Постоянная времени фильтров
    SelfExc: str = 'SelfExc'  # Самовозбуждение
    Del: str = 'Del'  # Самовозбуждение
