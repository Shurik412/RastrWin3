# -*- coding: utf-8 -*-
# Модель системы возбуждения типа UNITROL 6000_6800,
# реализованная в ПК RUSTab, состоит из одного макроблока:
# 1.Система возбуждения: U6800.xmldev.
# Параметры модели U6800.xmldev заносятся в таблицу «ВозбудителиIEEE».
# Типовые значение параметров настройки, приняты согласно информации от
# производителя системы возбуждения. В случае наличия листинга настроек для конкретного
# энергообъекта необходимо использовать фактические параметры настройки.

from RastrWinLib.Tables.Dynamic.DFWIEEE421 import DFWIEEE421


class Parameters:
    """
    Модель системы возбуждения типа UNITROL 6000_6800,
    реализованная в ПК RUSTab, состоит из одного макроблока:
    1.Система возбуждения: U6800.xmldev.
    Параметры модели U6800.xmldev заносятся в таблицу «ВозбудителиIEEE».
    Типовые значение параметров настройки, приняты согласно информации от
    производителя системы возбуждения. В случае наличия листинга настроек для конкретного
    энергообъекта необходимо использовать фактические параметры настройки.
    """
    Tr: float = 0.02  # Постоянная времени датчиков измерения
    Kp: float = 0  # Коэффициенты усиления в канале активной мощности
    Kr: float = 0  # Коэффициенты усиления в канале реактивной мощности
    Tc2: float = 1.0  # Постоянная времени инерционно-форсирующего звена регулятора напряжения
    Tb2: float = 1.0  # Постоянная времени инерционно-форсирующего звена регулятора
    Vamax: float = 0.1875  # Максимальное ограничение инерционно-форсирующего звена
    Vamin: float = -0.15  # Минимальное ограничение инерционно-форсирующего звена
    Tc1: float = 5.0  # Постоянная времени инерционно-форсирующего звена регулятора напряжения
    Tb1: float = 1.11  # Постоянная времени инерционно-форсирующего звена регулятора напряжения
    Vmmax: float = 6.5  # Максимальное ограничение инерционно-форсирующего звена
    Vmmin: float = -5.7  # Минимальное ограничение инерционно-форсирующего звена
    Ka: float = 500  # Коэффициент усиления регулятора напряжения
    Vimax: float = 0.1875  # Максимальное ограничение инерционно-форсирующего звена
    Vimin: float = -0.15  # Минимальное ограничение инерционно-форсирующего звена
    Vfemax: float = 0.025  # Максимальное ограничение инерционно-форсирующего звена
    Vemin: float = -0.02  # Минимальное ограничение инерционно-форсирующего звена
    Vrmax: float = 6.5  # Максимальное ограничение выходного сигнала регулятора напряжения и возбудителя
    Vrmin: float = -5.7  # Минимальное ограничение выходного сигнала регулятора напряжения и возбудителя
    Kc: float = 0.004  # Коэффициент нагрузки выпрямителя, определяемый сопротивлением коммутации выпрямителя
    Te: float = 0.004  # Постоянная времени интегратора возбудителя
    Samovozb: float = 0  # Режим самовозбуждения
    TRFout: float = 1  # Блокировка сигнала релейной форсировки
    Ifth: float = 3.0  # Уставка теплового ограничения
    Ifmax: float = 6.1  # Уставка максимального тока
    Klr: float = 300  # Коэффициент усиления регулятора БОР
    Toc2: float = 1  # Постоянная времени инерционно-форсирующего звена
    Tob2: float = 1  # Постоянная времени инерционно-форсирующего звена
    Toc1: float = 0.1  # Постоянная времени инерционно-форсирующего звена
    Tob1: float = 0.8  # Постоянная времени инерционно-форсирующего звена
    Ve1: float = 6.5  # Максимальное ограничение регулятора
    Ve2: float = -5.7  # Минимальное ограничение регулятора
    Theta: float = 1  # Выбор канала регулятора ОМВ (1 – TRF, 0 – пропорциональный)
    RIFlim: float = 1  # Блокировка (0) сигнала БОР
    Bex: float = 2.0  # Показатель степени теплового канала
    Kcf: float = 0.001  # Постоянная степени охлаждения
    Khf: float = 0.022  # Постоянная времени обратной время-токовой характеристики
    Klv: float = 300  # Коэффициент усиления регулятора ОМВ
    Tuc2: float = 0.1  # Постоянная времени инерционно-форсирующего звена
    Tub2: float = 0.1  # Постоянная времени инерционно-форсирующего звена
    Tuc1: float = 2.48  # Постоянная времени инерционно-форсирующего звена
    Tub1: float = 30.0  # Постоянная времени инерционно-форсирующего звена
    Kl: float = 1.0  # Коэффициент усиления канала БОР по отношению к коэффициенту усиления KR1
    RPQlim: float = 1.0  # Блокировка (0) сигнала ОМВ