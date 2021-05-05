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


class DFWDECS400_Doc:
    """

    """
    dfwdecs400 = DFWDECS400()

    table: str = 'DFWDECS400'  # название таблицы
    table_name: str = 'Возбудитель DECS-400'

    sel: str = f'Отметка [O]-[{dfwdecs400.sel}]'
    sta: str = f'Состояние возбудителя [S]-[{dfwdecs400.sta}]'
    Id: str = f'Номер возбудителя [N взб]-[{dfwdecs400.Id}]'
    Name: str = f'Название возбудителя [Название]-[{dfwdecs400.Name}]'
    ModelType: str = f'Модель возбудителя [Модель]-[{dfwdecs400.ModelType}]'
    Brand: str = f'Марка возбудителя [Марка]-[{dfwdecs400.Brand}]'
    CustomModel: str = f'Модель в конструкторе [Конструктор]-[{dfwdecs400.CustomModel}]'
    PSSId: str = f'Номер системного стабилизатора [N стаб]-[{dfwdecs400.PSSId}]'
    UELId: str = f'Номер ОМВ [N ОМВ]-[{dfwdecs400.UELId}]'
    OELId: str = f'Номер БОР [N БОР]-[{dfwdecs400.OELId}]'
    ForcerId: str = f'Номер РФ [N РФ]-[{dfwdecs400.ForcerId}]'
    Xl: str = f'Потери в выпрямителе [Xl]-[{dfwdecs400.Xl}]'
    DRP: str = f'Статизм [DRP]-[{dfwdecs400.DRP}]'
    VrMin: str = f'Минимальное ограничение потери напряжения [VrMin]-[{dfwdecs400.VrMin}]'
    VrMax: str = f'Максимальное ограничение потери напряжения [VrMax]-[{dfwdecs400.VrMax}]'
    VmMax: str = f'Максимальное ограничение тока контроллера [VmMax]-[{dfwdecs400.VmMax}]'
    VmMin: str = f'Минимальное ограничение тока контроллера [VmMin]-[{dfwdecs400.VmMin}]'
    VbMax: str = f'Максимальное напряжение возбудителя [VbMax]-[{dfwdecs400.VbMax}]'
    Kc: str = f'Коэффициент усиления [Kc]-[{dfwdecs400.Kc}]'
    Kp: str = f'Коэффициент усиления [Kp]-[{dfwdecs400.Kp}]'
    Kpm: str = f'Коэффициент усиления [Kpm]-[{dfwdecs400.Kpm}]'
    Kpr: str = f'Пропорциональный коэффициент усиления [Kpr]-[{dfwdecs400.Kpr}]'
    Kir: str = f'Интегральный коэффициент усиления [Kir]-[{dfwdecs400.Kir}]'
    Kpd: str = f'Дифференциальный коэффициент усиления [Kpd]-[{dfwdecs400.Kpd}]'
    Ta: str = f'Постоянная времени тиристорного моста [Ta]-[{dfwdecs400.Ta}]'
    Td: str = f'Постоянная времени дифференциального канала [Td]-[{dfwdecs400.Td}]'
    Tr: str = f'Постоянная времени фильтров [Tr]-[{dfwdecs400.Tr}]'
    SelfExc: str = f'Самовозбуждение [СВ]-[{dfwdecs400.SelfExc}]'
    Del: str = f'Самовозбуждение [Del]-[{dfwdecs400.Del}]'
