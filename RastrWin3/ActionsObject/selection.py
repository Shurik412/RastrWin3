# -*- coding: utf-8 -*-
from RastrWin3.ActionsObject.group_correction import GroupCorr
from RastrWin3.AstraRastr import RASTR
from RastrWin3.Tools.tools import TableOutput


class Selection:
    f""" 
    Класс предназначени для работы с выделением строк таблице,
    а именно включение/отключение параметра (Переключатель) Отметка О "sel".
    """

    def __init__(self, rastr_win=RASTR):
        f"""
        :param rastr_win: COM - объект Rastr.Astra (win32com);\n
        """
        self._rastr_win = rastr_win
        self._group_correction = GroupCorr(self._rastr_win)

    def remove_all_selection(self, table: str,
                             switch_command_line=False) -> None:
        f""" 
        Удление(отключения) всех отметок в таблице;\n
        
        :param table: название таблицы;\n
        :param switch_command_line: True/False - выводит сообщения в протокол;\n 
        :return: Nothing returns;\n
        """
        _column = "sel"
        _formula = "0"
        _viborka = ""

        self._group_correction.calc(table=table, column=_column,
                                    viborka=_viborka, formula=_formula)
        if switch_command_line:
            _pretty_table = TableOutput(fieldName=['Таблица', 'Параметр', 'Выбока', 'Формула'])
            if _viborka == "":
                _viborka = 'без выбоки'
            _pretty_table.add_row([table, _column, _viborka, _formula])
            _pretty_table.show(title_table='Удалены (сняты) отметки')

    def select_by_viborka(self, table: str, viborka: str, switch_command_line: bool = False) -> None:
        f"""
        Выделение (установка отметок) по выборке.\n
        
        :param table: название таблицы;\n
        :param viborka: выбрка, например: название района или диапазон знчений ("na > 1");\n
        :param switch_command_line: True/False - выводит сообщения в протокол;\n 
        :return:  ;\n
        """
        _column = "sel"
        _formula = '1'

        self._group_correction.calc(table=table, column=_column,
                                    viborka=viborka, formula=_formula)
        if switch_command_line:
            _pretty_table = TableOutput(fieldName=['Таблица', 'Параметр', 'Выбока', 'Формула'])
            _pretty_table.row_add([table, _column, viborka, _formula])
            _pretty_table.show(title_table='Установлены отметки')
