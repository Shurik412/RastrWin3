# -*- coding: utf-8 -*-
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.tables.Vetv.vetv import Vetv
from RastrWinLib.tools.tools import Tools


class FindNextSel:
    def __init__(self,
                 table: str,
                 rastr_win=RASTR):
        f"""
        Класс для поиска по выборки key.
        Метод row возвращает row_id - порядковый номер строки в таблице.
        :param table: название таблицы RastrWin3;
        :param rastr_win: {Tools.RastrDoc};
        """
        self.rastr_win = rastr_win
        self.table = self.rastr_win.Tables(table)

    def row(self,
            key: str):
        """
        Метож 'row'
        :param key: выборка SetSel
        :return: row_id: порядковый номер.
        """
        self.table.SetSel(f'{key}')
        row_id = self.table.FindNextSel(-1)
        if row_id == (-1):
            return -1
        else:
            return row_id


class FindNextSel_ROW:
    def __init__(self,
                 table: str,
                 rastr_win=RASTR):
        f"""
        Класс для поиска по выборки key.
        Метод row возвращает row_id - порядковый номер строки в таблице.
        :param table: название таблицы RastrWin3;
        :param rastr_win: ;
        """
        self.rastr_win = rastr_win
        self.table = self.rastr_win.Tables(table)

    def row(self,
            key: str,
            row_):
        """
        Метож 'row'
        :param key: выборка SetSel
        :return: row_id: порядковый номер.
        """
        self.table.SetSel(f'{key}')
        row_id = self.table.FindNextSel(row_)
        return row_id


class Variable:
    def __init__(self,
                 rastr_win=RASTR,
                 switch_command_line=False):
        f"""
        Класс для изменений значений ячеек.
        :param rastr_win: ;
        :param switch_command_line: ;
        """

        self.rastr_win = rastr_win
        self.switch_command_line = switch_command_line

    def make_changes_row(self,
                         table: str = None,
                         column: str = None,
                         row_id: int = None,
                         value=None):
        """
        Метод: make_changes_row - изменение параметра по заданному row_id
        :param table: название таблицы RastrWin3;
        :param column: назваине колонки RastrWin3;
        :param row_id: значение порядкового номера строки;
        :param value: значение новой величины заменяемого значения;
        :return: Nothing returns
        """
        if self.switch_command_line is not False:
            print(Tools.separator_star)
        switch_command_line_def = True
        if table is not None:
            table_ = self.rastr_win.Tables(table)
            if column is not None:
                col = table_.Cols(column)
                if row_id is not None:
                    if value is not None:
                        col.SetZ(row_id, value)
                    else:
                        switch_command_line_def = False
                        print(Tools.separator_noun)
                        print(
                            f'При выполнении класса <{self.__class__.make_changes_row.__qualname__}> '
                            f'возникла следующая ОШИБКА!'
                        )
                        print(
                            f'{Tools.error_text}{self.__class__.make_changes_row.__qualname__}: '
                            f'Не задано значение "value".'
                        )
                        print(Tools.separator_noun)
                else:
                    switch_command_line_def = False
                    print(Tools.separator_noun)
                    print(
                        f'При выполнении класса <{self.__class__.make_changes_row.__qualname__}> '
                        f'возникла следующая ОШИБКА!')
                    print(
                        f'{Tools.error_text}{self.__class__.make_changes_row.__qualname__}: '
                        f'Не задано значение порядкового номера строки "row_id".'
                    )
                    print(Tools.separator_noun)
            else:
                switch_command_line_def = False
                print(Tools.separator_noun)
                print(
                    f'При выполнении класса <{self.__class__.make_changes_row.__qualname__}> '
                    f'возникла следующая ОШИБКА!'
                )
                print(
                    f'{Tools.error_text}{self.__class__.make_changes_row.__qualname__}: '
                    f'Не задано название колонки (столбца) "column".'
                )
                print(Tools.separator_noun)
        else:
            switch_command_line_def = False
            print(Tools.separator_noun)
            print(
                f'При выполнении класса <{self.__class__.make_changes_row.__qualname__}> '
                f'возникла следующая ОШИБКА!.'
            )
            print(
                f'{error_text}{self.__class__.make_changes_row.__qualname__}: '
                f'Не задано название таблицы "table".'
            )
            print(Tools.separator_noun)

        if self.switch_command_line and switch_command_line_def is not False:
            print(
                f'Внесены изменения:\n'
                f'\t таблица: <{table}> => параметр: [{column}] => индекс объекта: [{row_id}]\n'
                f'\t значение => [{value}]'
            )
        if self.switch_command_line is not False:
            print(Tools.separator_star)

    def make_changes_filling_row(self,
                                 table: str = None,
                                 column: str = None,
                                 row_id: int = None,
                                 value=None):
        """
        Метод: make_changes_filling_row - изменение параметра по заданному row_id
        :param table: название таблицы RastrWin3;
        :param column: назваине колонки RastrWin3;
        :param row_id: значение порядкового номера строки;
        :param value: значение новой величины заменяемого значения;
        :return: Nothing returns
        """
        if self.switch_command_line is not False:
            print(Tools.separator_star)
        switch_command_line_def = True
        if table is not None:
            table_ = self.rastr_win.Tables(table)
            if column is not None:
                col = table_.Cols(column)
                if row_id is not None:
                    if value is not None:
                        col.SetZ(row_id, value)
                        if self.switch_command_line is not False:
                            print(Tools.separator_noun)
                            print(
                                f'Внесено изменение в таблицу: {table_.name} => {column}.'
                            )
                            print(Tools.separator_noun)
                    elif value is None:
                        if self.switch_command_line is not False:
                            print(Tools.separator_noun)
                            print(
                                f'Значение value = None, изменения не внесены.'
                            )
                            print(Tools.separator_noun)
                else:
                    switch_command_line_def = False
                    print(Tools.separator_noun)
                    print(
                        f'При выполнении класса <{self.__class__.make_changes_row.__qualname__}> '
                        f'возникла следующая ОШИБКА!')
                    print(
                        f'{Tools.error_text}{self.__class__.make_changes_row.__qualname__}: '
                        f'Не задано значение порядкового номера строки "row_id".'
                    )
                    print(Tools.separator_noun)
            else:
                switch_command_line_def = False
                print(Tools.separator_noun)
                print(
                    f'При выполнении класса <{self.__class__.make_changes_row.__qualname__}> '
                    f'возникла следующая ОШИБКА!'
                )
                print(
                    f'{Tools.error_text}{self.__class__.make_changes_row.__qualname__}: '
                    f'Не задано название колонки (столбца) "column".'
                )
                print(Tools.separator_noun)
        else:
            switch_command_line_def = False
            print(Tools.separator_noun)
            print(
                f'При выполнении класса <{self.__class__.make_changes_row.__qualname__}> '
                f'возникла следующая ОШИБКА!.'
            )
            print(
                f'{error_text}{self.__class__.make_changes_row.__qualname__}: '
                f'Не задано название таблицы "table".'
            )
            print(Tools.separator_noun)

        if self.switch_command_line and switch_command_line_def is not False:
            print(
                f'Внесены изменения:\n'
                f'\t таблица: <{table}> => параметр: [{column}] => индекс объекта: [{row_id}]\n'
                f'\t значение => [{value}]'
            )
        if self.switch_command_line is not False:
            print(Tools.separator_star)

    def make_changes_setsel(self,
                            table: str = None,
                            column: str = None,
                            key: str = None,
                            value=None):
        """
        Метод: make_changes_setsel - изменение параметра по выборки SetSel(key) -> key = "ny=6516516";
        :param table: название таблицы RastrWin3;
        :param column: название колонки RastrWin3;
        :param key: выборка SetSel("ny=52135156") - задается в виде value='ny=52135156';
        :param value: значение для замены;
        :return: Nothing returns.
        """
        switch_command_line_def = True
        if self.switch_command_line is not False:
            print(Tools.separator_star)
        if table is not None:
            table = self.rastr_win.Tables(table)
            table.SetSel(key)
            row_id = table.FindNextSel(-1)
            if row_id == (-1):
                print(
                    f'{Tools.error_text}{self.__class__.make_changes_row.__qualname__}: '
                    f'значение "row_id" равно -1.'
                )
                print(' Значения заданой выборки - отсутствуют.')
            else:
                if column is not None:
                    value_before = table.Cols(column).Z(row_id)
                else:
                    value_before = 'Значение отсутствует!'
                if value is not None:
                    col = table.Cols(column)
                    col.SetZ(row_id, value)
                    if self.switch_command_line and switch_command_line_def is not False:
                        print(f'Внесены изменения: '
                              f'                   - таблица <{table.Description}>\n'
                              f'                   - параметр: [{column}]\n'
                              f'                   - индекс объекта: [{row_id}]\n'
                              f'                   - значение до: [{value_before}]\n'
                              f'                   - значение после: [{value}]\n'
                              )
                else:
                    print(f'{Tools.error_text}{self.__class__.make_changes_row.__qualname__}: значение value = None.')
        else:
            print(f'{Tools.error_text}{self.__class__.make_changes_row.__qualname__}: значение table = None.')
        if self.switch_command_line is not False:
            print(Tools.separator_star)

    def make_changes_vetv(self,
                          table: str = Vetv.table,
                          column: str = None,
                          ip: int = None,
                          iq: int = None,
                          np: int = None,
                          value=None):
        """
        Метод изменяет значение ветви.
        :param table: название таблицы RastrWin3;
        :param column: название колонки (столбца) RastrWin3;
        :param ip: номер начала ветви;
        :param iq: номер конца ветви;
        :param np: номер параллельности ветви;
        :param value: значение;
        :return: Nothing returns
        """

        table_ = self.rastr_win.Tables(table)
        table_.SetSel(f'(ip={ip};iq={iq};np={np})|(ip={iq};iq={ip};np={np})')
        row = table_.FindNextSel(-1)
        if row != (-1):
            col = table_.Cols(column)
            col.SetZ(row, value)
        else:
            print(
                f'{Tools.error_text} '
            )
