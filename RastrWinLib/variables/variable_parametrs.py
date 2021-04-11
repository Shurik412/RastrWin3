# -*- coding: utf-8 -*-
from RastrWinLib.AstraRastr import RASTR


class FindNextSel:
    """

    """

    def __init__(self, table, rastr_win=RASTR):
        self.RastrWin = rastr_win
        self.Tables = self.RastrWin.Tables(str(table))

    def row(self, key):
        self.Tables.SetSel(f'{key}')
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


class VariableDefRowId:
    """
    Данный класс вносит изменения с известным id_row
    это (index => от 0 до ...)
    """

    def __init__(self, table, rastr_win=RASTR, switch_command_line=False):
        self.rastr_win = rastr_win
        self.table_name = table
        self.table = self.rastr_win.Tables(table)
        self.switch_command_line = switch_command_line

    def make_changes(self, column, row_id, value=None):
        column_ = self.table.Cols(column)
        if value is not None:
            column_.SetZ(row_id, value)  # вместо column.Z(row_id) = value
        else:
            print(f'Ошибка: не задано значение value в методе make_changes.')
        if self.switch_command_line is not None:
            print(f'Внесены изменения:\n'
                  f'\t таблица: {self.table.Description} => параметр: {column} => индекс объекта: {row_id}')

    def get(self, column, row_id):
        column_ = self.table.Cols(column)
        pass


if __name__ == '__main__':
    import win32com.client
    from RastrWinLib.loading.load import load_file
    from RastrWinLib.loading.shablon import shablon_file_dynamic as sh_rst, \
        shablon_file_scenario as sh_scn, shablon_file_automation as sh_dfw
    from RastrWinLib.calculation.dynamic import Dynamic
    from RastrWinLib.directory_rastrwin.dir_test_rastr import file_RUSTab_9_rst, file_RUSTab_9_scn
    from icecream import ic

    Rastr = win32com.client.Dispatch('Astra.Rastr')

    load_file(rastr_win=Rastr, file_path=file_RUSTab_9_rst, shablon=sh_rst, switch_command_line=True)
    load_file(rastr_win=Rastr, file_path=file_RUSTab_9_scn, shablon=sh_scn, switch_command_line=True)
    load_file(rastr_win=Rastr, shablon=sh_dfw, switch_command_line=True)

    dyn = Dynamic(rastr_win=Rastr, calc_time=1, snap_max_count=1, switch_command_line=False)

    var1 = VariableSetSel(rastr_win=Rastr,
                          table='Generator',
                          column='P',
                          key='Num=2',
                          switch_command_line=True)
    ic(var1.get())
    var1.make_changes(value=153)
    ic(var1.get())

    var1.make_changes(value=180)
    ic(var1.get())
