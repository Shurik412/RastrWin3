# -*- coding: utf-8 -*-
# Модуль переменных параметров тыблицы "Сценарий-Логика" RastrWin3


class DFWAutoLogicScn:
    """

    """
    table: str = 'DFWAutoLogicScn'  # название таблицы
    Id: str = 'Id'  # N Номер элемента логики
    Name: str = 'Name'  # Название
    ParentId: str = 'ParentId'  # N модуля Номер модуля
    Type: str = 'Type'  # Тип Тип логики
    Formula: str = 'Formula'  # Формула
    Actions: str = 'Actions'  # Действия  Список действий элемента
    Delay: str = 'Delay'  # Выдержка Выдержка времени
    UnitStarters: str = 'UnitStarters'  # ПО мод  Список ПО модуля
    UnitConstants: str = 'UnitConstants'  # Const мод  Список констант модуля
    UnitActions: str = 'UnitActions'  # Дейст мод  Список действий модуля
    OutputMode: str = 'OutputMode'  # Режим  Режим выхода
