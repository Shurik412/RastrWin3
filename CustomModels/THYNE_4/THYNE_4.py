# -*- coding: utf-8 -*-
# Модель системы возбуждения типа THYNE_4, реализованная в ПК RUSTab, состоит из одного макроблока:
# 1.Система возбуждения: THYNE_4.xmldev.
# Параметры модели THYNE_4.xmldev заносятся в таблицу «ВозбудителиIEEE».
# Типовые значение параметров настройки, приняты согласно информации от
# производителя системы возбуждения. В случае наличия листинга настроек для
# конкретного энергообъекта необходимо использовать фактические параметры настройки.
from RastrWinLib.Tables.Dynamic.DFWIEEE421 import DFWIEEE421


class Parameters:
    """
    Модель системы возбуждения типа THYNE_4, реализованная в ПК RUSTab, состоит из одного макроблока:
    1.Система возбуждения: THYNE_4.xmldev.
    Параметры модели THYNE_4.xmldev заносятся в таблицу «ВозбудителиIEEE».

    Типовые значение параметров настройки, приняты согласно информации от производителя системы возбуждения.
    В случае наличия листинга настроек для конкретного энергообъекта необходимо
    использовать фактические параметры настройки.
    """
    Kp: float = 0  #
    Kr: float = 0  #
    Tk: float = 0.0226  #
    Tj: float = 0.0226  #
    Tr: float = 0.0226  #
    Kd: float = 16.125  #
    Vamax: float = 7.76  #
    Vamin: float = -7.76  #
    Kir: float = 1.0  #
    Kdr: float = 0.2002  #
    Tdr: float = 0.2002  #
    Kb: float = 1.2403  #
    Ka: float = 21.854  #
    Ta: float = 0.0017  #
    Vrmax: float = 21.7713  #
    Vrmin: float = -18.9264
    Te: float = 0.55  #
    Th: float = 0.0177  #
    Kc: float = 2.225  #