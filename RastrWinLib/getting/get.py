# -*- coding: utf-8 -*-
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.tables.tables_attributes import node_table, generator_table, vetv_table


class GettingParameter:
    def __init__(self, rastr_win=RASTR):
        self.rastr_win = rastr_win
        """
        Класс предназначен для работы с ячейками таблиц в RastrWin3.
        1. Метод get_cell - возвращает значение ячейки из таблицы.
        2. Метод get_row_vetv - возвращает порядковый номер из таблицы "Ветви".
        3. Метод get_row_node - возвращает порядковый номер из таблицы "Узлы".
        4. Метод get_row_gen - возвращает порядковый номер из таблицы "Генераторы".
        """

    def get_cell(self, table, column, row_id):
        """
        Метод get_cell - возвращает значение ячейки.
        :param table: название таблицы RastrWin3 (generator)
        :param column: навание колонки (столбца) RastrWin3 (Num)
        :param row_id: порядковый номер в таблице (от 0 до max.count)
        :return: value_cell_of_row - возвращает значение ячейки по номеру row_id
        """
        table_ = self.rastr_win.Tables(table)
        value_cell_of_row = table_.Cols(column).Z(row_id)
        return value_cell_of_row

    def get_row_vetv(self, ip, iq, np):
        """
        Метод get_row_line - возвращает порядковый номер строки таблицы "Ветви".
        :param ip: начало ветви;
        :param iq: конец ветви;
        :param np: номер паралельности ветви;
        :return: row_vetv: номер строки в таблице ветви.
        """
        table_ = self.rastr_win.Tables(vetv_table)
        table_.SetSel(f'(ip={ip};iq={iq};np={np})|(ip={iq};iq={ip};np={np})')
        row_vetv = table_.FindNextSel(-1)
        return row_vetv

    def get_row_node(self, node_ny):
        """
        Метод get_row_node - возвращает порядковый номер узла.
        :param node_ny: номер узла;
        :return: row_node: порядковый номер узла.
        """
        table_ = self.rastr_win.Tables(node_table)
        table_.SetSel(f'(ny={node_ny})')
        row_node = table_.FindNextSel(-1)
        return row_node

    def get_row_gen(self, num):
        """
        Метод get_row_gen - возвращает порядковый номер генератора.
        :param num: номер генератора;
        :return: row_gen: порядковый номер генератора.
        """
        table_ = self.rastr_win.Tables(generator_table)
        table_.SetSel(f'(Num={num})')
        row_gen = table_.FindNextSel(-1)
        return row_gen
