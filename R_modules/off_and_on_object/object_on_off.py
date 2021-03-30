# -*- coding: utf-8 -*-

class SwitchLine:
    """ """

    def __init__(self, rastr_win, table='vetv', switch_command_line=False):
        self.rastr_win = rastr_win
        self.table = self.rastr_win.Tables(table)
        self.switch_command_line = switch_command_line

    def off(self, ip, iq, np=0):
        if self.switch_command_line is not False:
            print(f'Отключение объекта ip={ip}, iq={iq}, np={np}')
        self.table.SetSel(f"(ip={ip} & iq={iq} & np={np})|(ip={iq} & iq={ip} & np={np})")
        row_id = self.table.FindNextSel(-1)
        if row_id != (-1):
            switch_sta_off = self.table.Cols('sta').Z(row_id)
            if switch_sta_off != 1:
                self.table.Cols("sta").Calc("1")
            else:
                print(f'\t\tОбъект ip={ip},iq={iq},np={np} уже отключен!')
        else:
            print(f'\t\tОбъект ip={ip},iq={iq},np={np} не найдет в таблице {self.table.Name}')

    def on(self, ip, iq, np=0, type_of_line_switching=0):
        if self.switch_command_line is not False:
            print(f'Включение объекта ip={ip}, iq={iq}, np={np}')
        self.table.SetSel(f'(ip={ip} & iq={iq} & np={np})|(ip={iq} & iq={ip} & np={np})')
        row_id = self.table.FindNextSel(-1)
        if row_id != (-1):
            switch_sta_on = self.table.Cols('sta').Z(row_id)
            if switch_sta_on != 0:
                self.table.Cols("sta").Calc("0")
            else:
                print(f'\t\tОбъект ip={ip},iq={iq},np={np} уже отключен!')
        else:
            print(f'\t\tОбъект ip={ip},iq={iq},np={np} не найдет в таблице {self.table.Name}')


if __name__ == '__main__':
    import win32com.client
    from R_modules.load_and_save_file.load_file_rastrwin import load_file
    from R_modules.load_and_save_file.save_file_rastrwin import save_file
    from R_modules.load_and_save_file.shablons_dir import shablon_file_dynamic, shablon_file_scenario, \
        shablon_file_automation, shablon_file_regime
    from R_modules.directory_rastrwin.dir_test_rastr import file_RUSTab_9_rst, file_RUSTab_9_scn
    from R_modules.calculation.dyn_rgm_calc import SteadyState
    from R_modules.getting_parameters.get_parameter import GettingParameterAttribute
    from icecream import ic

    Rastr = win32com.client.Dispatch('Astra.Rastr')
    rstFile = 'C:\\Users\\Ohrimenko_AG\\Desktop\\Calc_ALAR_KurskAES\\test9.rst'
    load_file(rastr_win=Rastr, file_path=rstFile, shablon=shablon_file_dynamic)
    load_file(rastr_win=Rastr, file_path=file_RUSTab_9_scn, shablon=shablon_file_scenario)
    load_file(rastr_win=Rastr)
    regime = SteadyState(rastr_win=Rastr, switch_command_line=True)
    sta_ = SwitchLine(rastr_win=Rastr, table='vetv', switch_command_line=True)
    regime.rgm()
    sta_.off(ip=349, iq=319, np=0)
    regime.rgm()
    # sta_.on(ip=349, iq=319)
    # regime.rgm()

    vetv_ = GettingParameterAttribute(rastr_win=Rastr, table='vetv')

    ic(vetv_.getting(column='sta', key='(ip=349 & iq=319 & np=0)|(ip=319 & iq=349 & np=0)'))

    save_file(rastr_win=Rastr, file_path='C:\\Users\\Ohrimenko_AG\\Desktop\\21\\off_on2.rg2',
              shablon=shablon_file_regime)
