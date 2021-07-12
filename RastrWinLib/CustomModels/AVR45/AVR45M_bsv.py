# -*- coding: utf-8 -*-
# Модель автоматического регулятора возбуждения типа АРВ-45М_БСВ (Силмаш),
# реализованная в ПК RUSTab, состоит из следующих макроблоков:
# 1. АРВ: AVR45M_bsv.xmldev (таблица 54);
# 2. Релейная форсировка: AVR-45M_RF.xmldev (таблица 55).
# Параметры модели AVR45M_bsv.xmldev заносятся в таблицу «АРВ (ИД)».
# Типовые значение параметров настройки, приняты согласно информации
# от производителя системы возбуждения. В случае наличия листинга настроек
# для конкретного энергообъекта необходимо использовать фактические параметры настройки.
from RastrWinLib.tables.Dynamic.DFWIEEE421 import DFWIEEE421


class Parameters:
    """
    Модель автоматического регулятора возбуждения типа АРВ-45М_БСВ (Силмаш),
    реализованная в ПК RUSTab, состоит из следующих макроблоков:
    1. АРВ: AVR45M_bsv.xmldev (таблица 54);
    2. Релейная форсировка: AVR-45M_RF.xmldev (таблица 55).
    Параметры модели AVR45M_bsv.xmldev заносятся в таблицу «АРВ (ИД)».
    Типовые значение параметров настройки, приняты согласно информации от производителя системы возбуждения.
    В случае наличия листинга настроек для конкретного энергообъекта необходимо
    использовать фактические параметры настройки.
    """
    Ku: float = 10.0  # Коэффициент усиления регулятора
    K_Q: float = 1.0  # Коэффициент усиления канала по производной тока ротора
    Kif1: float = 1.0  # Коэффициент усиления канала по производной тока ротора
    T1if: float = 0.05  # Постоянная времени дифференциру-ющего звена в канале по производной тока ротора
    Ku1: float = 3.0  # Коэффициент усиления канала по производной напряжения
    T1u1: float = 0.06  # Постоянная времени дифференциру-ющего звена в канале по производной напряжения
    K_P: float = 5.0  # Коэффициент усиления выходного сигнала ОМВ
    K_Ia: float = 2.0  # Уставка по току ротора
    Tf: float = 2.0  # Постоянная времени дифференциру-ющего звена в канале по частоте
    Kf: float = 1.0  # Коэффициент усиления в канале по частоте
    Kf1: float = 1.0  # Коэффициент усиления в канале по производной частоты

    # Параметры модели AVR-45M_RF.xmldev заносятся в таблицу «Форсировка (ИД)».
    Ubf: float = 0.85  # Напряжение ввода форсировки
    Uef: float = 0.9  # Напряжение снятие форсировки
    Tz_out: float = 0.1  # Задержка на снятие форсировки
