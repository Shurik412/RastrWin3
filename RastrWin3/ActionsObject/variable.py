# -*- coding: utf-8 -*-
from RastrWin3.ActionsObject.get import GettingParameter
from RastrWin3.AstraRastr import RASTR
from RastrWin3.Tables.Vetv.vetv import Vetv
from RastrWin3.Tools.tools import TableOutput


class FindNextSelection:
    """ Класс FindNextSelection - поиск номера строки по выборке SetSel(key) """

    def __init__(self,
                 table: str = None,
                 rastr_win=RASTR):
        f"""
        Класс для поиска по выборке порядкового номера в таблице.\n
        Метод "row" возвращает порядковый номер строки в таблице.\n
        :param table: название таблицы;\n
        :param rastr_win: True/False - вывод сообщений в протокол;\n
        """
        self.rastr_win = rastr_win
        if table is not None:
            self.table = self.rastr_win.Tables(table)

    def row(self,
            table: str = None,
            select: str = None) -> int:
        f"""
        Метод "row" - возвращает порядковый  номер из таблицы.\n
        :param table: 
        :param select: выборка SetSel;\n
        :return: row_: возвращает порядковый номер или -1 в случае отсутствия искомого элемента;\n
        """
        if table is not None:
            self.table = self.rastr_win.Tables(table)
            self.table.SetSel(select)
            row_ = self.table.FindNextSel(-1)
        else:
            table_ = self.rastr_win.Tables(table)
            table_.SetSel(select)
            row_ = table_.FindNextSel(-1)

        if row_ == (-1):
            return -1
        else:
            return row_


class Variable(GettingParameter):
    """ Класс "Variable" изменяет параметры в таблицах RastrWin3 """

    def __init__(self,
                 rastr_win=RASTR):
        f"""
        Класс для изменений значений ячеек в таблице.\n
        :param rastr_win: COM - объект Rastr.Astra (win32com);\n
        :param switch_command_line: True/False - вывод сообщений в протокол;
        """
        super().__init__()
        self.rastr_win = rastr_win
        self._getting_parameter = GettingParameter(rastr_win=self.rastr_win)

    def __bool__(self):
        return self.switch_command_line

    def make_changes_row(self,
                         table: str = None,
                         column: str = None,
                         row: int = None,
                         value=None,
                         switch_command_line: bool = False) -> None:
        f"""
        Метод: make_changes_row - изменение параметра по заданному номеру строки (row)\n
        
        :param table: название таблицы;\n
        :param column: название колонки (столбец, параметр);\n
        :param row: значение порядкового номера строки в таблице;\n
        :param value: значение новой величины заменяемого значения;\n
        :param switch_command_line: True/False - выводит сообщения в протокол;\n
        :return: Nothing returns
        """

        if (table and column and row) is not None:
            if switch_command_line:
                _parametr_old = self._getting_parameter.get_cell_row(table=table,
                                                                     column=column,
                                                                     row_id=row,
                                                                     rounding_to=2)
            else:
                _parametr_old = ''

            _table = self.rastr_win.Tables(table)
            _col = _table.Cols(column)
            _col.SetZ(row, value)

            if switch_command_line:
                _name_parametr = self._getting_parameter.get_cell_row(table=table,
                                                                      column='name',
                                                                      row_id=row,
                                                                      rounding_to=None)

                _parametr_new = self._getting_parameter.get_cell_row(table=table,
                                                                     column=column,
                                                                     row_id=row,
                                                                     rounding_to=2)
                _pretty_table = TableOutput(
                    fieldName=['id', 'Название', 'Параметр', 'Значение праметра старое -> новое'])
                _pretty_table.row_add([row, _name_parametr, column, f'{_parametr_old} -> {_parametr_new}'])
                _pretty_table.show(title_table=f'Изменения в таблице {table}')
        else:
            _pretty_table = TableOutput(fieldName=['ERROR', 'Описание'])
            _pretty_table.row_add(['Таблица', table])
            _pretty_table.row_add(['Колонка (стоблец)', column])
            _pretty_table.row_add(['Порядковый номер в таблице', row])
            _pretty_table.row_add(['Значение', value])
            _pretty_table.show(title_table='ERROR: class Variable')

    def make_changes_setsel(self,
                            table: str = None,
                            column: str = None,
                            select: str = None,
                            value=None,
                            switch_command_line: bool = False) -> None:
        f"""
        Метод: make_changes_setsel - изменение параметра по выборки SetSel(key) -> key = "ny=6516516";\n
        :param switch_command_line: True/False - выводит сообщения в протокол;\n
        :param table: название таблицы;\n
        :param column: название колонки (столбец, параметр);\n
        :param select: выборка SetSel("ny=52135156") - задается в виде value='ny=52135156';\n
        :param value: значение для замены;\n
        :return: Nothing returns.\n
        """

        if (table and column and select and value) is not None:

            if switch_command_line:
                _name_parametr = self._getting_parameter.get_cell_SetSel(table=table,
                                                                         column='name',
                                                                         key=select,
                                                                         rounding_to=None)

                _parametr_old = self._getting_parameter.get_cell_SetSel(table=table,
                                                                        column=column,
                                                                        key=select,
                                                                        rounding_to=2)
            else:
                _parametr_old = ''
                _name_parametr = ''

            _table = self.rastr_win.Tables(table)
            _table.SetSel(select)
            _row = _table.FindNextSel(-1)
            if _row != (-1):
                _col = _table.Cols(column)
                _col.SetZ(_row, value)

                if switch_command_line:
                    _parametr_new = self._getting_parameter.get_cell_SetSel(table=table,
                                                                            column=column,
                                                                            key=select,
                                                                            rounding_to=2)

                    _pretty_table = TableOutput(fieldName=['id', 'Название', 'Параметр',
                                                           'Значение праметра: старое -> новое'])
                    _pretty_table.row_add([_row, _name_parametr, column, f'{_parametr_old} -> {_parametr_new}'])
                    _pretty_table.show(title_table=f'Изменения в таблице: {table}')
            else:
                _pretty_table = TableOutput(fieldName=['ERROR', 'Описание'])
                _pretty_table.row_add(['Таблица', table])
                _pretty_table.row_add(['Колонка (стоблец)', column])
                _pretty_table.row_add(['Выборка', select])
                _pretty_table.row_add(['Значение', value])
                _pretty_table.show(title_table='ERROR: class Variable method make_changes_setsel\n'
                                               f'Не найдена строка с выборкой:"{select}" -> row=(-1).')
        else:
            _pretty_table = TableOutput(fieldName=['ERROR', 'Описание'])
            _pretty_table.row_add(['Таблица', table])
            _pretty_table.row_add(['Колонка (стоблец)', column])
            _pretty_table.row_add(['Выборка', select])
            _pretty_table.row_add(['Значение', value])
            _pretty_table.show(title_table='ERROR: class Variable method make_changes_setsel')

    def make_changes_vetv(self,
                          table: str = Vetv.table,
                          column: str = None,
                          ip: int = None,
                          iq: int = None,
                          np: int = None,
                          value=None,
                          switch_command_line: bool = False) -> None:
        f"""
        Метод изменяет значение выбранного параметра ветви.\n
        :param switch_command_line: True/False - выводит сообщения в протокол;\n
        :param table: название таблицы;\n
        :param column: название колонки (столбец, параметр);\n
        :param ip: номер начала ветви;\n
        :param iq: номер конца ветви;\n
        :param np: номер параллельности ветви;\n
        :param value: значение;\n
        :return: Nothing returns.\n
        """
        if (table and column and ip and iq and np and value) is not None:
            _key = f'(ip={ip}&iq={iq}&np={np})|(ip={iq}&iq={ip}&np={np})'

            if switch_command_line:
                _name_parametr = self._getting_parameter.get_cell_SetSel(table=table,
                                                                         column=Vetv.name,
                                                                         key=_key,
                                                                         rounding_to=None)

                _parametr_old = self._getting_parameter.get_cell_SetSel(table=table,
                                                                        column=column,
                                                                        key=_key,
                                                                        rounding_to=2)
            else:
                _parametr_old = ''
                _name_parametr = ''

            _table = self.rastr_win.Tables(table)
            _table.SetSel(_key)
            _row = _table.FindNextSel(-1)
            if _row != (-1):
                _cols = _table.Cols(column)
                _cols.SetZ(_row, value)
                if switch_command_line:
                    _parametr_new = self._getting_parameter.get_cell_SetSel(table=table,
                                                                            column=column,
                                                                            key=_key,
                                                                            rounding_to=2)

                    _pretty_table = TableOutput(fieldName=['id', 'Нач_ip', 'Кон_iq',
                                                           'Номер.парр_np', 'Название', 'Параметр',
                                                           'Значение праметра: старое -> новое'])

                    _pretty_table.row_add([_row, ip, iq, np, _name_parametr, column,
                                           f'{_parametr_old} -> {_parametr_new}'])

                    _pretty_table.show(title_table=f'Изменения в таблице: {table}')
            else:
                _pretty_table = TableOutput(fieldName=['ERROR', 'Описание'])
                _pretty_table.row_add(['Таблица', table])
                _pretty_table.row_add(['Колонка (стоблец)', column])
                _pretty_table.row_add(['Выборка', f'ip={ip} iq={iq} np={np}'])
                _pretty_table.row_add(['Значение', value])
                _pretty_table.show(title_table='ERROR: class Variable; Метод: make_changes_setsel\n'
                                               f'Не найдена строка с выборкой:"ip={ip} iq={iq} np={np}" -> row=(-1).')
        else:
            _pretty_table = TableOutput(fieldName=['ERROR', 'Описание'])
            _pretty_table.row_add(['Таблица', table])
            _pretty_table.row_add(['Колонка (стоблец)', column])
            _pretty_table.row_add(['Выборка', f'ip={ip} iq={iq} np={np}'])
            _pretty_table.row_add(['Значение', value])
            _pretty_table.show(title_table='ERROR: class Variable; Метод: make_changes_setsel')
