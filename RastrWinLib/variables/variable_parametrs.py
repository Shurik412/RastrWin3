# -*- coding: utf-8 -*-
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.log_tools.tools import separator_star, error_text


class FindNextSel:
    """
    Класс для поиска по выборки key.
    Метод row возвращает row_id - порядковый номер строки в таблице.
    """

    def __init__(self, table, rastr_win=RASTR):
        self.RastrWin = rastr_win
        self.Tables = self.RastrWin.Tables(str(table))

    def row(self, key):
        self.Tables.SetSel(f'{str(key)}')
        row_id = self.Tables.FindNextSel(-1)
        if row_id == (-1):
            return -1
        else:
            return row_id


class Variable:
    """
    Класс для внесени изменений
    """

    def __init__(self,
                 rastr_win=RASTR,
                 switch_command_line=False):
        """

        :param rastr_win: com - объект Rastr.Astra;
        :param switch_command_line: True/False - вывод сообщений в протокол.
        """

        self.rastr_win = rastr_win
        self.switch_command_line = switch_command_line

    def make_changes_row(self,
                         table=None,
                         column=None,
                         row_id=None,
                         value=None):
        """
        make_changes_row - изменение параметра по заданному row_id
        :param table: название таблицы RastrWin3
        :param column: назваине колонки RastrWin3
        :param row_id: значение строки
        :param value: значение
        :return: Nothing returns
        """
        if self.switch_command_line is not False:
            print(separator_star)
        switch_command_line_def = True
        if table is not None:
            table = self.rastr_win.Tables(table)
        else:
            switch_command_line_def = False
            print(f'{error_text} Variable -> def make_changes_row(): Не задано название "table".')

        if column is not None:
            col = table.Cols(column)
            if row_id is not None:
                if value is not None:
                    col.SetZ(row_id, value)
                else:
                    switch_command_line_def = False
                    print(f'{error_text} Variable -> def make_changes_row(): Не задано значение "value".')
            else:
                switch_command_line_def = False
                print(f'{error_text} Variable -> def make_changes_row(): Не задано значение "row_id".')
        else:
            switch_command_line_def = False
            print(f'{error_text} Variable -> def make_changes_row(): Не задано значение "column".')

        if self.switch_command_line and switch_command_line_def is not False:
            print(f'Внесены изменения:\n'
                  f'\t таблица: <{table.Description}> => параметр: [{column}] => индекс объекта: [{row_id}]\n'
                  f'\t значение => [{value}]')
        if self.switch_command_line is not False:
            print(separator_star)

    def make_changes_setsel(self,
                            table=None,
                            column=None,
                            key=None,
                            value=None):
        """
        make_changes_setsel -> изменение параметра по выборки SetSel(key) -> key = "ny=6516516";
        :param table: название таблицы RastrWin3;
        :param column: название колонки RastrWin3;
        :param key: выборка SetSel("ny=52135156") -> задается в виде value='ny=52135156';
        :param value: значение для замены;
        :return: Nothing returns.
        """
        switch_command_line_def = True
        if self.switch_command_line is not False:
            print(separator_star)
        if table is not None:
            table = self.rastr_win.Tables(table)
            table.SetSel(key)
            row_id = table.FindNextSel(-1)
            if row_id == (-1):
                print(f'{error_text} Variable -> def make_changes_setsel(): значение row_id = (-1).')
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
                              f'                   - значение после: [{value}]\n')
                else:
                    print(f'{error_text} Variable -> def make_changes_setsel(): значение value = None.')
        else:
            print(f'{error_text} Variable -> def make_changes_setsel(): значение table = None.')
        if self.switch_command_line is not False:
            print(separator_star)


if __name__ == '__main__':
    from RastrWinLib.loading.load import load_file
    from RastrWinLib.loading.shablon import shablon_file_dynamic
    from RastrWinLib.tables.tables_attributes import com_dynamics_table, com_dynamics_attributes_list

    load_file(file_path=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.rst',
              shablon=shablon_file_dynamic,
              switch_command_line=True)

    var_ = Variable(switch_command_line=False)

    var_.make_changes_row(table=com_dynamics_table,
                          column=com_dynamics_attributes_list[0],
                          row_id=0,
                          value=1)
