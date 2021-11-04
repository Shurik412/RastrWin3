# -*- coding: utf-8 -*-
from RastrWin3.AstraRastr import RASTR
from RastrWin3.Tools.tools import changing_number_of_semicolons


class GettingParameter:
    f"""
        Класс предназначен для работы с ячейками таблиц в RastrWin3.\n
        1.Метод "get_cell_row" - возвращает значение ячейки из таблицы по номеру строки;\n
        2.Метод "get_cell_setsel" - для получения значения ячейки, с помощью поиска table.SetSel("Num=2351513");\n
        3.Метод "get_cell_index" - возвращает порядковый номер таблицы;\n
        4.Метод "get_count_table_starting_zero" - возвращает максимальное число строк начиная с нуля (от 0 до max-1);\n
        5.Метод "get_count_table" - возвращает количество строк таблице начиная от одно (от 1 до max).\n
    """

    def __init__(self, rastr_win=RASTR):
        self.rastr_win = rastr_win

        f"""
         :param rastr_win: COM - объект Rastr.Astra (win32com);\n
        """

    def get_cell_row(self,
                     table: str,
                     column: str,
                     row_id: int,
                     rounding_to: int = None):
        f"""
        Метод get_cell_row - возвращает значение ячейки по индексу в таблице.\n
        Индекс в таблице - это порядковый номер строки в таблице.\n
        
        :param table: название таблицы RastrWin3 ("Generator");\n
        :param column: навание колонки (столбца) RastrWin3 ("Num");\n
        :param row_id: индекс в таблице (порядковый номер в таблице (от 0 до table.count-1));\n
        :param rounding_to: количетво символов после запятой;
        :return: value_cell_of_row - возвращает значение ячейки по номеру row_id.\n
        """

        table_ = self.rastr_win.Tables(table)
        _value_cell_of_row = table_.Cols(column).Z(row_id)
        if rounding_to is not None and type(_value_cell_of_row) is (float or int):
            value_cell_of_row = changing_number_of_semicolons(number=_value_cell_of_row, digits=rounding_to)
            return value_cell_of_row
        else:
            value_cell_of_row = _value_cell_of_row
            return value_cell_of_row

    def get_cell_SetSel(self,
                        table: str,
                        column: str,
                        key: str,
                        rounding_to: int = None):
        f"""
        Метод get_cell_setsel - метод для получения значения ячейки, с помощью поиска table.SetSel("Num=2351513").\n
        :param rounding_to: ;\n
        :param table: название таблицы RastrWin3 ("Generator");\n
        :param column: навание колонки (столбца) RastrWin3 ("Num");\n
        :param key: выборка ("Num=5170004");\n
        :return: value_cell_of_set_sel - значение ячейки, с помощью поиска table.SetSel("Num=2351513").\n
        """
        _table = self.rastr_win.Tables(table)
        _table.SetSel(key)
        _row = _table.FindNextSel(-1)
        if _row != (-1):
            _value_cell_of_set_sel = _table.Cols(column).Z(_row)
            if rounding_to is not None and type(_value_cell_of_set_sel) is (float or int):
                value_cell_of_set_sel = changing_number_of_semicolons(number=_value_cell_of_set_sel, digits=rounding_to)
                return value_cell_of_set_sel
            else:
                value_cell_of_set_sel = _value_cell_of_set_sel
                return value_cell_of_set_sel
        else:
            return None

    def get_cell_index(self,
                       table: str,
                       key: str) -> (int or None):
        f"""
        Метод get_cell_index - метод возвращает порядковый номер таблицы.\n
        :param key: формула выборки;\n
        :param table: название таблицы RastrWin3 (generator);\n
        :return: row - порядковый номер таблицы.\n
        """
        _table = self.rastr_win.Tables(table)
        _table.SetSel(key)
        _row = _table.FindNextSel(-1)
        if _row != (-1):
            return _row
        else:
            return None

    def get_count_table_starting_zero(self, table: str) -> int:
        f"""
            Метод get_count_table_starting_zero - возвращает количество строк таблице начиная с нуля.\n
            :param table: название таблицы RastrWin3 (generator);\n
            :return: count - максимальное число строк в таблице.\n
        """
        table_ = self.rastr_win.Tables(table)
        count = table_.Count - 1
        return count

    def get_count_table(self, table: str) -> int:
        f"""
           Метод get_count_table - метод возвращает количество строк таблице.\n
           :param table: название таблицы RastrWin3 (generator);\n
           :return: count - максимальное число строк в таблице.\n
        """
        table_ = self.rastr_win.Tables(table)
        count = table_.Count
        return count
