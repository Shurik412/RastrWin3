# -*- coding: utf-8 -*-
# Модель автоматического регулятора возбуждения типа АВР-2_статика (Энергокомплект),
# реализованная в ПК RUSTab, состоит из следующих макроблоков:
# 1. АРВ: AVR-2.xmldev (таблица 45);
# 2. Релейная форсировка: AVR-2_RF.xmldev (таблица 46).
# Параметры модели AVR-2.xmldev заносятся в таблицу «АРВ (ИД)».
# Типовые значение параметров настройки, приняты согласно информации
# от производителя системы возбуждения. В случае наличия листинга настроек
# для конкретного энергообъекта необходимо использовать фактические параметры настройки.
from RastrWinLib.tables.Dynamic.DFWIEEE421 import DFWIEEE421


class Parameters:
    """
    Модель автоматического регулятора возбуждения типа АВР-2_статика (Энергокомплект),
     реализованная в ПК RUSTab, состоит из следующих макроблоков:
    1. АРВ: AVR-2.xmldev (таблица 45);
    2. Релейная форсировка: AVR-2_RF.xmldev (таблица 46).
    Параметры модели AVR-2.xmldev заносятся в таблицу «АРВ (ИД)».
    Типовые значение параметров настройки, приняты согласно информации от производителя системы возбуждения.
    В случае наличия листинга настроек для конкретного энергообъекта необходимо
    использовать фактические параметры настройки.
    """
    KST: float = 0.0  # Статизм по реактивной мощности генератора
    Ku: float = 15  # Коэффициент усиления регулятора по напряжению
    TINT: float = 2.0  # Постоянная времени интегратора регулятора
    Ku1: float = 4.0  # Коэффициент усиления канала по производной напряжения
    Kif1: float = 1.0  # Коэффициент усиления канала по производной тока ротора
    Kf: float = 4.0  # Коэффициент усиления канала по частоте
    Kf1: float = 1.5  # Коэффициент усиления канала по производной частоты

    # Параметры релейной форсировки возбуждения AVR-2_RF.xmldev заносятся в таблицу «Форсировка (ИД)».
    Ubf: float = 0.85  # Напряжение ввода форсировки
    Uef: float = 0.89  # Напряжение снятие форсировки
    Tz_out: float = 0.1  # Задержка на снятие форсировки
