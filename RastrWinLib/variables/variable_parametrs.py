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
    from RastrWinLib.loading.load import load_file
    from RastrWinLib.loading.shablon import shablon_file_regime as sh_rg2
    from RastrWinLib.directory_rastrwin.dir_test_rastr import file_RUSTab_9_rst, file_RUSTab_9_scn
    from icecream import ic
    from RastrWinLib.AstraRastr import RASTR
    from RastrWinLib.tables.tables_attributes import com_ekviv_attributes, com_ekviv_table

    file = r'C:\Users\Ohrimenko_AG\Desktop\Test_equiPy\02-БРМ Зима максимум [уст].rg2'

    load_file(rastr_win=RASTR, file_path=file_RUSTab_9_rst, shablon=sh_rg2, switch_command_line=True)

    var1 = VariableDefRowId(rastr_win=RASTR,
                            table=com_ekviv_table,
                            switch_command_line=True)

    list_key = []
    for key in com_ekviv_attributes.keys():
        list_key.append(key)

    selekv = 0
    met_ekv = 0
    tip_ekv = 0
    ekvgen = 0
    tip_gen = 1
    kfc_x = ''
    pot_gen = 0
    kpn = ''
    tip_sxn = 0
    smart = 0
    zmax = 1000
    otm_n = 0

    var1.make_changes(column=list_key[0], row_id=0, value=selekv)
    var1.make_changes(column=list_key[1], row_id=0, value=met_ekv)
    var1.make_changes(column=list_key[2], row_id=0, value=tip_ekv)
    var1.make_changes(column=list_key[3], row_id=0, value=ekvgen)
    var1.make_changes(column=list_key[4], row_id=0, value=tip_gen)
    var1.make_changes(column=list_key[5], row_id=0, value=kfc_x)
    var1.make_changes(column=list_key[6], row_id=0, value=pot_gen)
    var1.make_changes(column=list_key[7], row_id=0, value=kpn)
    var1.make_changes(column=list_key[8], row_id=0, value=tip_sxn)
    var1.make_changes(column=list_key[9], row_id=0, value=smart)
    var1.make_changes(column=list_key[10], row_id=0, value=zmax)
    var1.make_changes(column=list_key[11], row_id=0, value=otm_n)
