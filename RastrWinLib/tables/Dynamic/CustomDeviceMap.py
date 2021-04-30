# -*- coding: utf-8 -*-
# Модуль переменных таблицы "Пользовательсие устройства" RastrWin3

class CustomDeviceMap:
    """

    """
    table: str = 'CustomDeviceMap'  # название таблиц
    table_name: str = '"Пользовательсие устройства"'

    Id: str = 'Id'  # Номер
    Name: str = 'Name'  # название
    Module: str = 'Module'  # Модуль пользовательского устройства
    InstanceTable: str = 'InstanceTable'  # Таблица экземпляров пользовательского устройства
    Tag: str = 'Tag'  # Тег связи с внешними устройствами
    LinkList: str = 'LinkList'  # Связи 1  Связи с ведомыми
    SiblingLinkList: str = 'SiblingLinkList'  # Связи 2 Связи с ведущими
