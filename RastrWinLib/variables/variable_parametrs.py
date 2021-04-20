# -*- coding: utf-8 -*-
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.log_tools.tools import separator_star, error_text


class FindNextSel:
    """
    FindNextSel
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


class VariableSetSel:
    """
    Данный класс вносит изменения если известен Num, Node и тд
    Пример: key = 'Num=51700241'
    """

    def __init__(self, table, column, rastr_win=RASTR, key=None, switch_command_line=False):
        self.rastr_win = rastr_win
        self.column_name = column
        self.table = self.rastr_win.Tables(table)
        self.column = self.table.Cols(column)
        if key is not None:
            self.table.SetSel(key)
            self.row_id = self.table.FindNextSel(-1)
            if self.row_id != (-1):
                self.row_id = self.row_id
            else:
                self.row_id = None
        else:
            self.row_id = None
        self.switch_command_line = switch_command_line

    def make_changes(self, value=None):
        if self.row_id == (-1):
            return print(f'Ошибка: return FindNextSel = (-1)')
        if value and self.row_id is not None:
            self.column.SetZ(self.row_id, value)  # вместо column.Z(row_id) = value
            self.rastr_win.rgm('')
        if self.switch_command_line is not None:
            print(f'Внесены изменения:'
                  f'\t таблица: {self.table.Description} => параметр: {self.column_name} => индекс объекта: {self.row_id}')

    def get(self, row_id=None):
        if self.row_id == (-1):
            return print(f'Ошибка: return FindNextSel = (-1)')
        if row_id is not None:
            return self.column.Z(row_id)
        else:
            return self.column.Z(self.row_id)


class VariableRowId:
    """
    Данный класс вносит изменения с известным id_row
    это (index => от 0 до ...)
    """

    def __init__(self, table, column, rastr_win=RASTR, row_id=None, switch_command_line=False):
        self.rastr_win = rastr_win
        self.table_name = table
        self.column_name = column
        self.table = self.rastr_win.Tables(table)
        self.column = self.table.Cols(column)
        self.row_id = row_id
        self.switch_command_line = switch_command_line

    def make_changes(self, value=None):
        if value is not None:
            self.column.SetZ(self.row_id, value)  # вместо column.Z(row_id) = value
            self.rastr_win.rgm('')

        if self.switch_command_line is not None:
            print(f'Внесены изменения:\n'
                  f'\t таблица: {self.table.Description} => параметр: {self.column_name} => индекс объекта: {self.row_id}')

    def get(self, row_id):
        if self.row_id is not None:
            return self.column.Z(self.row_id)
        else:
            return self.column.Z(row_id)





class Variable:
    """
    Класс для внесени изменений
    """

    def __init__(self,
                 rastr_win=RASTR,
                 switch_command_line=False):

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
        print(separator_star)
        switch_command_line_def = True
        if table is not None:
            table = self.rastr_win.Tables(table)
        else:
            switch_command_line_def = False
            print(f'{error_text} Variable -> def make_changes_row(): Не задано название "table".')

        if column is not None:
            col = table.Cols(column)
            if row_id and value is not None:
                col.SetZ(row_id, value)
            else:
                switch_command_line_def = False
                print(f'{error_text} Variable -> def make_changes_row(): Не задано значение "row_id или value".')
        else:
            switch_command_line_def = False
            print(f'{error_text} Variable -> def make_changes_row(): Не задано значение "column".')

        if self.switch_command_line and switch_command_line_def is not False:
            print(f'Внесены изменения:\n'
                  f'\t таблица: <{table.Description}> => параметр: [{column}] => индекс объекта: [{row_id}]\n'
                  f'\t значение => [{value}]')
        print(separator_star)

    def make_changes_setsel(self,
                            table=None,
                            column=None,
                            key=None,
                            value=None):
        """
        make_changes_setsel -> изменение параметра по выборки SetSel(key) -> key = "ny=6516516"
        :param table: название таблицы RastrWin3
        :param column: название колонки RastrWin3
        :param key: выборка SetSel("ny=52135156") -> задается в виде value='ny=52135156'
        :param value: значение для замены
        :return: Nothing returns
        """
        switch_command_line_def = True
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
                              f'                   - значение => [{value}]\n')
                else:
                    print(f'{error_text} Variable -> def make_changes_setsel(): значение value = None.')
        else:
            print(f'{error_text} Variable -> def make_changes_setsel(): значение table = None.')
        print(separator_star)


if __name__ == '__main__':
    from RastrWinLib.loading.load import load_file
    from RastrWinLib.loading.save import save_file
    from RastrWinLib.loading.shablon import shablon_file_regime as sh_rg2
    from RastrWinLib.directory_rastrwin.dir_test_rastr import file_RUSTab_9_rst, file_RUSTab_9_scn
    from RastrWinLib.AstraRastr import RASTR
    from RastrWinLib.tables.tables_attributes import generator_table

    file = r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\cx195.rg2'
    load_file(rastr_win=RASTR, file_path=file_RUSTab_9_rst, shablon=sh_rg2, switch_command_line=True)
    var1 = Variable(rastr_win=RASTR,
                    switch_command_line=True)
    # var1.make_changes_row(table=generator_table,
    #                       column='P',
    #                       row_id=1,
    #                       value=851.12)
    var1.make_changes_setsel(table=generator_table,
                             column='P',
                             key='Num=2',
                             value=150.12)
    save_file(rastr_win=RASTR,
              file_path=r'C:\Users\Ohrimenko_AG\Desktop\Test_equiPy\t3.rg2',
              shablon=sh_rg2,
              switch_command_line=True)
