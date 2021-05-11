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
