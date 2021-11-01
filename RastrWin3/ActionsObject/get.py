# -*- coding: utf-8 -*-
from RastrWin3.AstraRastr import RASTR


class GettingParameter:
    """
        Класс предназначен для работы с ячейками таблиц в RastrWin3.\n
        1.Метод "get_cell_row" - возвращает значение ячейки из таблицы по номеру строки;\n
        2.Метод "get_cell_setsel" - для получения значения ячейки, с помощью поиска table.SetSel("Num=2351513");\n
        3.Метод "get_cell_index" - возвращает порядковый номер таблицы;\n
        4.Метод "get_count_table_starting_zero" - возвращает максимальное число строк начиная с нуля (от 0 до max-1); \n
        5.Метод "get_count_table" - возвращает количество строк таблице начиная от одно (от 1 до max).
    """

    def __init__(self, rastr_win=RASTR):
        self.rastr_win = rastr_win
        f"""
         :param rastr_win: COM - объект Rastr.Astra (win32com);
        """

    def get_cell_row(self,
                     table: str,
                     column: str,
                     row_id):
        """
        Метод get_cell_row - возвращает значение ячейки по индексу в таблице.\n
        Индекс в таблице - это порядковый номер строки в таблице.
        :param table: название таблицы RastrWin3 ("Generator");\n
        :param column: навание колонки (столбца) RastrWin3 ("Num");\n
        :param row_id: индекс в таблице (порядковый номер в таблице (от 0 до table.count-1));\n
        :return: value_cell_of_row - возвращает значение ячейки по номеру row_id.

        """
        table_ = self.rastr_win.Tables(table)
        value_cell_of_row = table_.Cols(column).Z(row_id)
        return value_cell_of_row

    def get_cell_SetSel(self,
                        table: str,
                        column: str,
                        key: str):
        """
        Метод get_cell_setsel - метод для получения значения ячейки, с помощью поиска table.SetSel("Num=2351513").\n
        :param table: название таблицы RastrWin3 ("Generator");\n
        :param column: навание колонки (столбца) RastrWin3 ("Num");\n
        :param key: выборка ("Num=5170004");\n
        :return: value_cell_of_set_sel - значение ячейки, с помощью поиска table.SetSel("Num=2351513").
        """
        table_ = self.rastr_win.Tables(table)
        table_.SetSel(key)
        row_ = table_.FindNextSel(-1)
        value_cell_of_set_sel = table_.Cols(column).Z(row_)
        return value_cell_of_set_sel

    def get_cell_index(self,
                       table: str,
                       column: str,
                       value: str):
        """
        Метод get_cell_index - метод возвращает порядковый номер таблицы.\n
        :param table: название таблицы RastrWin3 (generator);\n
        :param column: навание колонки (столбца) RastrWin3 (Num);\n
        :param value: значение, напрмер номер генератора;\n
        :return: row - порядковый номер таблицы.
        """
        table_ = self.rastr_win.Tables(table)
        table_.SetSel(f'{column}={value}')
        row = table_.FindNextSel(-1)
        return row

    def get_count_table_starting_zero(self, table: str) -> int:
        """
        Метод get_count_table_starting_zero - возвращает количество строк таблице начиная с нуля.\n
        :param table: название таблицы RastrWin3 (generator);\n
        :return: count - максимальное число строк в таблице.
        """
        table_ = self.rastr_win.Tables(table)
        count = table_.Count - 1
        return count

    def get_count_table(self, table: str) -> int:
        """
        Метод get_count_table - метод возвращает количество строк таблице.\n
        :param table: название таблицы RastrWin3 (generator);\n
        :return: count - максимальное число строк в таблице.
        """
        table_ = self.rastr_win.Tables(table)
        count = table_.Count
        return count