# -*- coding: utf-8 -*-
# Модуль переменных таблицы  "Форсировка" RastrWin3


class Forcer:
    """

    """
    table: str = 'Forcer'
    table_name: str = '"Форсировка"'

    sel: str = 'sel'  # Отметка
    sta: str = 'sta'  # Состояние форсировки
    Id: str = 'Id'  # Номер форсировки
    Name: str = 'Name'  # Название форсировки
    ModelType: str = 'ModelType'  # Модель форсировки
    Brand: str = 'Brand'  # Марка форсировки
    CustomModel: str = 'CustomModel'  # Модель в конструкторе

    # Напряжения
    Ubf: str = 'Ubf'  # U_ввф Напряжение ввода форсировки
    Uef: str = 'Uef'  # U_снф Напряжение снятия форсировки
    Ubrf: str = 'Ubrf'  # U_вврф Напряжение ввода расфорсировки
    Uerf: str = 'Uerf'  # U_снрф Напряжение снятия расфорсировки
    Ufors: str = 'Ufors'  # Ufors Выход форсировки
    Rf: str = 'Rf'  # К_ф Кратность форсировки
    Rrf: str = 'Rrf'  # К_рф Кратность расфорсировки

    # Времена
    Texc_f: str = 'Texc_f'  # Т_ф Постоянная времени возбудит. при форсировке
    Tz_in: str = 'Tz_in'  # Тз_ввод Задержка времени возбудит. при форсировке
    Tz_out: str = 'Tz_out'  # Тз_снятия Задержка времени возбудит. при расфорсировке
    Texc_rf: str = 'Texc_rf'  # Т_рф Постоянная времени возбудит. при расфорсировке


class ForcerDescription:
    pass
