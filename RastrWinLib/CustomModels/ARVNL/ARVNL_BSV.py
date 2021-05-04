# -*- coding: utf-8 -*-
# Модель автоматического регулятора возбуждения типа АРВНЛ_БСВ,
# реализованная в ПК RUSTab, состоит из одного макроблока:
# 1.АРВ: ARVNL_BSV.xmldev.
# Параметры модели ARVNL_BSV.xmldev заносятся в таблицу «АРВ (ИД)».
# Типовые значение параметров настройки, приняты согласно информации от производителя системы
# возбуждения. В случае наличия листинга настроек для конкретного энергообъекта необходимо
# использовать фактические параметры настройки.

from RastrWinLib.tables.Dynamic.ExcControl import ExcControl


class Parameters:
    """
    Модель автоматического регулятора возбуждения типа АРВНЛ_БСВ,
    реализованная в ПК RUSTab, состоит из одного макроблока:
    1.АРВ: ARVNL_BSV.xmldev.
    Параметры модели ARVNL_BSV.xmldev заносятся в таблицу «АРВ (ИД)».
    Типовые значение параметров настройки, приняты согласно информации от производителя системы
    возбуждения. В случае наличия листинга настроек для конкретного энергообъекта необходимо
    использовать фактические параметры настройки.
    """
    KST: float = 2.0  # Уставка ограничителя напряжения ротора
    Ku: float = 10.0  # Коэффициент усиления регулятора
    Ku1: float = 2.0  # Коэффициент усиления канала по производной напряжения
    Kif1: float = 1.5  # Коэффициент усиления канала по производной тока ротора
    K_Ia: float = 2.0  # Уставка ограничителя максимального тока ротора
    K_Ir: float = 2.0  # Коэффициент усиления канала ограничителя максимального тока ротора
    TINT: float = 2.0  # Постоянная времени интегратора регулятора
    Kf: float = 5.0  # Коэффициент усиления в канале по частоте
    Kf1: float = 2.0  # Коэффициент усиления в канале по производной частоты
    Urv_max: float = 7.0  # Максимальное ограничение регулятора
    Ur_min: float = 0  # Минимальное ограничение регулятора
    U11: float = 0.85  # Напряжение ввода форсировки
    U22: float = 0.95  # Напряжение снятие форсировки
    Tbch: float = 0.1  # Задержка на снятие форсировки
    K_Q: float = 2.0  # Коэффициент усиления выходного сигнала ОМВ

