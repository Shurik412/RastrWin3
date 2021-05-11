# -*- coding: utf-8 -*-
# Модуль переменных таблицы  "Районы электрической сети" RastrWin3


class Area:
    """
    Таблица "Районы"
    """
    table: str = 'area'
    table_name: str = '"Районы"'
    na: str = 'na'  #
    name: str = 'name'  # Район
    no: str = 'no'  # Nоб Номер объединения
    pg: str = 'pg'  # Pген Генерация P
    pn: str = 'pn'  # Pнаг Нагрузка P
    dp: str = 'dp'  # Dp Потери P
    pop: str = 'pop'  # Pпотр Потребление P
    vnp: str = 'vnp'  # Pвн Внешний переток P
    Tc: str = 'Tc'  # Температура
    pn_min: str = 'pn_min'  # Pн мин Минимум нагрузки, МВт
    pn_max: str = 'pn_max'  # Pн max Максимум нагрузки, МВт
    pg_min: str = 'pg_min'  # Pг мин Минимум генерации,  МВт
    pg_max: str = 'pg_max'  # Pг max Максимум генерации, МВт
    sel: str = 'sel'  #
    sta: str = 'sta'  #
    dp_nag: str = 'dp_nag'  # dP_нагр Нагрузочные потери
    dp_line: str = 'dp_line'  # dP_ЛЭП Потери в ЛЭП
    dq_line: str = 'dq_line'  # dQ_ЛЭП Потери Q в ЛЭП
    poq: str = 'poq'  # Qпотр Потребление Q
    dq: str = 'dq'  # Dq Потери Q
    qg: str = 'qg'  # Qген Генерация Q


class AreaDescription:
    pass
