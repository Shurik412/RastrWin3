# -*- coding: utf-8 -*-
import RastrWinLib.tables.Dynamic.DFWIEEE421 as DFWIEEE421
import RastrWinLib.tables.Dynamic.Generator as Generator
import RastrWinLib.tables.Node.node as node
import RastrWinLib.tables.Vetv.vetv as vetv
from RastrWinLib.AstraRastr import RASTR


class GettingParameter:
    """
    Класс предназначен для работы с ячейками таблиц в RastrWin3.
    1. Метод get_cell - возвращает значение ячейки из таблицы по номеру строки.
    2. Метод get_param - возвращает значение ячейки из таблицы по номеру объекта.
    2. Метод get_row_vetv - возвращает порядковый номер из таблицы "Ветви".
    3. Метод get_row_node - возвращает порядковый номер из таблицы "Узлы".
    4. Метод get_row_gen - возвращает порядковый номер из таблицы "Генераторы".
    """

    def __init__(self, rastr_win=RASTR):
        self.rastr_win = rastr_win
        """
         :param rastr_win: COM - объект Rastr.Astra (win32com).
        """

    def get_cell_row(self, table, column, row_id):
        """
        Метод get_cell - возвращает значение ячейки.
        :param table: название таблицы RastrWin3 (generator);
        :param column: навание колонки (столбца) RastrWin3 (Num);
        :param row_id: порядковый номер в таблице (от 0 до max.count);
        :return: value_cell_of_row - возвращает значение ячейки по номеру row_id.
        """
        table_ = self.rastr_win.Tables(table)
        value_cell_of_row = table_.Cols(column).Z(row_id)
        return value_cell_of_row

    def get_cell_param(self, table, column, key):
        """
        get_param - метод для получения значения ячейки.
        :param table: название таблицы RastrWin3 (generator);
        :param column: навание колонки (столбца) RastrWin3 (Num);
        :param key: выборка;
        :return: значение ячейки.
        """
        table_ = self.rastr_win.Tables(table)
        table_.SetSel(key)
        row_ = table_.FindNextSel(-1)
        value_cell_of_set_sel = table_.Cols(column).Z(row_)
        return value_cell_of_set_sel

    def get_cell_id(self, table, column, Id):
        """
        Метод get_param - метод для получения значения ячейки.
        :param table: название таблицы RastrWin3 (generator);
        :param column: навание колонки (столбца) RastrWin3 (Num);
        :param Id: номер оборудования;
        :return: значение ячейки.
        """
        table_ = self.rastr_win.Tables(table)
        table_.SetSel(f'Id={Id}')
        row_ = table_.FindNextSel(-1)
        value_cell_of_set_sel = table_.Cols(column).Z(row_)
        return value_cell_of_set_sel

    def get_row_vetv(self, ip, iq, np):
        """
        Метод get_row_line - возвращает порядковый номер строки таблицы "Ветви".
        :param ip: начало ветви;
        :param iq: конец ветви;
        :param np: номер паралельности ветви;
        :return: row_vetv: номер строки в таблице ветви.
        """
        table_ = self.rastr_win.Tables(vetv.table)
        table_.SetSel(f'({vetv.ip}={ip};{vetv.iq}={iq};{vetv.np}={np})|({vetv.ip}={iq};{vetv.iq}={ip};{vetv.np}={np})')
        row_vetv = table_.FindNextSel(-1)
        return row_vetv

    def get_row_node(self, node_ny):
        """
        Метод get_row_node - возвращает порядковый номер узла.
        :param node_ny: номер узла;
        :return: row_node: порядковый номер узла.
        """
        table_ = self.rastr_win.Tables(node.table)
        table_.SetSel(f'({node.ny}={node_ny})')
        row_node = table_.FindNextSel(-1)
        return row_node

    def get_row_gen(self, Num):
        """
        Метод get_row_gen - возвращает порядковый номер генератора.
        :param Num: номер генератора;
        :return: row_gen: порядковый номер генератора.
        """
        table_ = self.rastr_win.Tables(Generator.table)
        table_.SetSel(f'({Generator.Num}={Num})')
        row_gen = table_.FindNextSel(-1)
        return row_gen

    def get_row_vozb_IEEE(self, Id):
        """
        Метод get_row_gen - возвращает порядковый номер "Возбудитель IEEE".
        :param Id: Nвзб - Номер возбудителя;
        :return: row_vozb_IEEE: порядковый номер генератора.
        """
        table_ = self.rastr_win.Tables(DFWIEEE421.table)
        table_.SetSel(f'{DFWIEEE421.Id}={Id}')
        row_vozb_IEEE = table_.FindNextSel(-1)
        return row_vozb_IEEE