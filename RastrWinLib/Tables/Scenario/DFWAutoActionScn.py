# -*- coding: utf-8 -*-
# Модуль переменных параметров тыблицы "Сценарий-Действия" RastrWin3

class DFWAutoActionScn:
    """

    """
    table: str = 'DFWAutoActionScn'  # название таблицы
    State: str = 'State'  # Сост Действие активно
    Id: str = 'Id'  # N Номер действия
    ParentId: str = 'ParentId'  # N группы Номер группы
    Type: str = 'Type'  # Тип Тип действия
    Name: str = 'Name'  # Название Название
    Formula: str = 'Formula'  # Формула Формула
    ObjectClass: str = 'ObjectClass'  # Тип объекта Тип объекта
    ObjectProp: str = 'ObjectProp'  # Свойство объекта
    ObjectKey: str = 'ObjectKey'  # Ключ объекта
    OutputMode: str = 'OutputMode'  # Режим  Режим выхода
    RunsCount: str = 'RunsCount'  # N сраб   Количество срабатываний
    TimeStart: str = 'TimeStart'  # Время начала  Время начала действия упрощенного сценария
    DT: str = 'DT'  # Длительность  Длительность действия упрощенного сценария
    Tag: str = 'Tag'  # Тэг  Тэг упрощенного сценария
