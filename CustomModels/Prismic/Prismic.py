# -*- coding: utf-8 -*-
# Модель системы возбуждения типа Prismic, реализованная в ПК RUSTab, состоит из одного макроблока:
# 1.Система возбуждения: Prismic.xmldev.
# Параметры модели Prismic.xmldev заносятся в таблицу «ВозбудителиIEEE».
# Типовые значение параметров настройки, приняты экспертно.
from RastrWinLib.Tables.Dynamic.DFWIEEE421 import DFWIEEE421


class Parameters:
    """
    Модель системы возбуждения типа Prismic, реализованная в ПК RUSTab, состоит из одного макроблока:
    1.Система возбуждения: Prismic.xmldev.
    Параметры модели Prismic.xmldev заносятся в таблицу «ВозбудителиIEEE».
    Типовые значение параметров настройки, приняты экспертно
    """
    Kpr: float = 35.0  # Пропорциональный коэффициент усиления ПИД-регулятора
    Kir: float = 5.0  # Интегральный коэффициент усиления ПИД-регулятора
    Kdr: float = 6.0  # Дифференциальный коэффициент усиления ПИД-регулятора
    Tdr: float = 0.1  # Постоянная времени дифференциального канала ПИД-регулятора
    Vrmax: float = 13.6  # Максимальное ограничение возбудителя
    Vrmin: float = 0  # Минимальное ограничение возбудителя
    Te: float = 0.32  # Постоянная времени интегратора возбудителя
    Kc: float = 0.31  # Коэффициент нагрузки выпрямителя, определяемый сопротивлением коммутации выпрямителя
    Ke: float = 1.0  # Коэффициент обратной связи возбудителя
    Kd: float = 1.09  # Коэффициент размагничивания
    Aex: float = 0.536770  # Коэффициент кривой насыщения
    Bex: float = 0.02363  # Коэффициент кривой насыщения