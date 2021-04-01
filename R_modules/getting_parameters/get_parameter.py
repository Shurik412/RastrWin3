# -*- coding: utf-8 -*-
from R_modules.Tables_Parametrs.Tables_and_parametrs import table_com_cxema, table_name_com_cxema


class GettingParameterInstance:
    """
    Возвращает значение строки по номеру.
    """

    def __init__(self, rastr_win, tables, key, switch_command_line=False):
        self.RastrWin = rastr_win
        self.Tables = self.RastrWin.Tables(tables)
        self.key = key
        self.Tables.SetSel(key)
        self.switch_command_line = switch_command_line
        self.row_id = self.Tables.FindNextSel(-1)

    def row(self):
        return self.row_id

    def get(self, column='name'):
        name_par = self.Tables.Cols(column).Z(self.row_id)
        return name_par


class GettingParameterAttribute:
    """
    """

    def __init__(self, rastr_win, table, switch_command_line=False):
        self.rastr_win = rastr_win
        self.table = self.rastr_win.Tables(table)
        self.switch_command_line = switch_command_line

    def getting(self, column, key=None, ip=None, iq=None, np=None):
        if key is not None:
            self.table.SetSel(key)
            row = self.table.FindNextSel(-1)
            if row != (-1):
                parameter = self.table.Cols(column).Z(row)
                if self.switch_command_line is not False:
                    print(f'\tПолучен параметр таблицы "{self.table.Description}" => "{column}" => "{parameter}";')
                return parameter
            else:
                return print(f'Не найден параметр с таким номеров в таблице "{self.table.Description}".')
        elif ip and iq and np is not None and self.table.Name == 'vetv':
            self.table.SetSel(f'(ip={ip}&iq={iq}&np={np})|(ip={iq}&iq={ip}&np={np})')
            row = self.table.FindNextSel(-1)
            if row != (-1):
                parameter = self.table.Cols(column).Z(row)
                if self.switch_command_line is not False:
                    print(f'\tПолучен параметр таблицы "{self.table.Description}" => "{column}" => "{parameter}";')
                return parameter
            else:
                return print(f'Не найден параметр с таким номеров в таблице "{self.table.Description}".')


class GettingParameter:
    def __init__(self, rastr_win, table, column, key=None, switch_command_line=False):
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

    def get(self, row_id=None):
        if self.row_id == (-1):
            return print(f'Ошибка: return FindNextSel = (-1)')
        if row_id is not None:
            return self.column.Z(row_id)
        else:
            return self.column.Z(self.row_id)


class GetTableCommonInfo:
    def __init__(self, rastr_win, switch_command_line=False, return_log=False):
        self.rastr_win = rastr_win
        self.table = self.rastr_win.Tables(table_name_com_cxema)
        self.switch_command_line = switch_command_line
        self.return_log = return_log

    def get(self):
        print(f'Общая информация: {table_name_com_cxema}')
        for key_ in table_com_cxema:
            column = self.table.Cols(key_)
            parametr = column.Z(0)
            if type(parametr) == float:
                print(f'{table_com_cxema[key_]} = {"%.2f" % (parametr)}')
            else:
                print(f'{table_com_cxema[key_]} = {parametr}')


if __name__ == '__main__':
    import win32com.client
    from R_modules.load_and_save_file.load_file_rastrwin import load_file
    from R_modules.load_and_save_file.shablons_dir import shablon_file_dynamic as sh_rst, \
        shablon_file_scenario as sh_scn, shablon_file_automation as sh_dfw
    from R_modules.directory_rastrwin.dir_test_rastr import file_RUSTab_9_rst, file_RUSTab_9_scn
    from icecream import ic

    Rastr = win32com.client.Dispatch('Astra.Rastr')
    file_RUSTab_9_scn2 = 'C:\\Users\\Ohrimenko_AG\\Desktop\\Calc_ALAR_KurskAES\\1.scn'
    load_file(rastr_win=Rastr, file_path=file_RUSTab_9_rst, shablon=sh_rst, switch_command_line=True)
    load_file(rastr_win=Rastr, file_path=file_RUSTab_9_scn2, shablon=sh_scn, switch_command_line=True)
    load_file(rastr_win=Rastr, shablon=sh_dfw, switch_command_line=True)

    # get_gen = GettingParameterInstance(rastr_win=Rastr, tables='vetv',
    #                                    key='(ip=349 & iq=319 & np=0)')
    # get_name = get_gen.get(column='name')
    # print(get_name)
    # row_id = get_gen.row()
    # print(row_id)

    # get_vetv = GettingParameterAttribute(rastr_win=Rastr, table='DFWAutoActionScn')
    # get_name_vetv = get_vetv.getting(column='Type', key='Type=3')
    # ic(get_name_vetv)
    #
    # get_ = GettingParameterInstance(rastr_win=Rastr, tables='DFWAutoActionScn', key='Type=3')
    # get2 = get_.get(column='ObjectKey')
    # arr = get2.split(',')
    # ic(arr[0], arr[1], arr[2])
    # dict1 = dict(ip=arr[0], iq=arr[1], np=arr[2])
    # ic(get2)
    # ic(dict1)
    #
    # ic(dict1.get('ip'))

    get_new = GettingParameterAttribute(rastr_win=Rastr, table='vetv', switch_command_line=True)
    res_get_new = get_new.getting(column='ip', ip=349, iq=319, np=0)
    get_new_ = GettingParameterAttribute(rastr_win=Rastr, table='Generator', switch_command_line=True)
    res_get_new_ = get_new_.getting(column='P', key='Num=2')
    print(res_get_new)
    print(res_get_new_)
