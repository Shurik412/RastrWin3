# -*- coding: utf-8 -*-
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.Tables.Vetv.vetv import Vetv
from RastrWinLib.Tools.tools import Tools
from prettytable import PrettyTable


class FindNextSelection:
    """
    Класс возвращает
    """

    def __init__(self,
                 table: str = None,
                 rastr_win=RASTR):
        f"""
        Класс для поиска по выборки key.
        Метод row возвращает row_id - порядковый номер строки в таблице.
        :param table: название таблицы RastrWin3;
        :param rastr_win: True/False - вывод сообщений в протокол;
        """
        self.rastr_win = rastr_win
        if table is None:
            self.table = self.rastr_win.Tables(table)

    def row(self,
            key: str):
        """
        Метод 'row' возвращает порядковый  номер из таблицы.
        :param key: выборка SetSel;
        :return: row_id: возвращает порядковый номер или -1 в случае отсутствия искомого элемента;
        """
        self.table.SetSel(key)
        row_id = self.table.FindNextSel(-1)
        if row_id == (-1):
            return -1
        else:
            return row_id

    def row_with_table(self, table: str, key: str):
        table_ = self.rastr_win.Tables(table)
        table_.SetSel(key)
        if row_id == (-1):
            return -1
        else:
            return row_id


class Variable(FindNextSelection):
    """

    """

    def __init__(self,
                 rastr_win=RASTR,
                 switch_command_line: bool = False):
        f"""
        Класс для изменений значений ячеек.
        :param rastr_win: COM - объект Rastr.Astra (win32com);
        :param switch_command_line: True/False - вывод сообщений в протокол;
        """
        super().__init__(rastr_win=RASTR)
        self.rastr_win = rastr_win
        self.switch_command_line = switch_command_line
        self.pt = PrettyTable()

    def __bool__(self):
        return self.switch_command_line

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
                        self.pt.title = f'Ошибка при выполнении <{self.__class__.make_changes_row.__qualname__}>'
                        self.pt.field_names = ['Метод', 'Ошибка']
                        self.pt.add_row([f'При выполнении класса <{self.__class__.make_changes_row.__qualname__}> '
                                         f'возникла следующая ОШИБКА!',
                                         f'ERROR: {self.__class__.make_changes_row.__qualname__}: '
                                         f'Не задано значение "value".'
                                         ])
                        print(self.pt)

                else:
                    switch_command_line_def = False
                    self.pt.title = f'Ошибка при выполнении <{self.__class__.make_changes_row.__qualname__}>'
                    self.pt.field_names = ['Метод', 'Ошибка']
                    self.pt.add_row([f'При выполнении класса <{self.__class__.make_changes_row.__qualname__}> '
                                     f'возникла следующая ОШИБКА!',
                                     f'{Tools.error_text}{self.__class__.make_changes_row.__qualname__}: '
                                     f'Не задано значение порядкового номера строки "row_id".'
                                     ])
                    print(self.pt)
            else:
                switch_command_line_def = False
                self.pt.title = f'Ошибка при выполнении <{self.__class__.make_changes_row.__qualname__}>'
                self.pt.field_names = ['Метод', 'Ошибка']
                self.pt.add_row([f'При выполнении класса <{self.__class__.make_changes_row.__qualname__}> '
                                 f'возникла следующая ОШИБКА!',
                                 f'ERROR: {self.__class__.make_changes_row.__qualname__}: '
                                 f'Не задано название колонки (столбца) "column".'
                                 ])
                print(self.pt)
        else:
            switch_command_line_def = False
            self.pt.title = f'Ошибка при выполнении <{self.__class__.make_changes_row.__qualname__}>'
            self.pt.field_names = ['Метод', 'Ошибка']
            self.pt.add_row([f'При выполнении класса <{self.__class__.make_changes_row.__qualname__}> '
                             f'возникла следующая ОШИБКА!.',
                             f'ERROR: {self.__class__.make_changes_row.__qualname__}: '
                             f'Не задано название таблицы "table".'
                             ])
            print(self.pt)

        if self.switch_command_line and switch_command_line_def:
            self.pt.title = f'Внесены изменения в таблицу {table}'
            self.pt.field_names = ['Таблица', 'Название параметр', 'Порядковый номер в таблице', 'Значение']
            self.pt.add_row([table, column, row_id, value])
            print(self.pt)

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

        if table is not None:
            row_id = row_with_table(table=table, key=key)
            if row_id == (-1):
                self.pt.title = f'Ошибка при выполнении <{self.__class__.make_changes_row.__qualname__}>'
                self.pt.field_names = ['Метод', 'Ошибка']
                self.pt.add_row([
                    f'ERROR: {self.__class__.make_changes_row.__qualname__}: значение "row_id" равно -1.',
                    'Значения заданой выборки - отсутствуют.'
                ])
                print(self.pt)
            else:
                if column is not None:
                    value_before = table.Cols(column).Z(row_id)
                else:
                    value_before = 'Значение отсутствует!'
                if value is not None:
                    col = table.Cols(column)
                    col.SetZ(row_id, value)
                    if self.switch_command_line and switch_command_line_def:
                        self.pt.title = f'Внесены изменения в таблицу <{table.Description}>'
                        self.pt.field_names = ['Таблица', 'Название параметра', '']
                        self.pt.add_row([table.Description, column, row_id, value_before, value])
                        print(self.pt)
                else:
                    print(f'ERROR: {self.__class__.make_changes_row.__qualname__}: значение value = None.')
        else:
            print(f'ERROR: {self.__class__.make_changes_row.__qualname__}: значение table = None.')

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

        row = row_with_table(table=table, key=f'(ip={ip};iq={iq};np={np})|(ip={iq};iq={ip};np={np})')
        if row != (-1):
            col = table_.Cols(column)
            col.SetZ(row, value)
        else:
            print('Error')


if __name__ == '__main__':
    from RastrWinLib.AstraRastr import RASTR

    name = RASTR.Tables.Description(1).Name
    print(name)