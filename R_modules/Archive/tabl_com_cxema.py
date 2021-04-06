tb_com_cxema = 'com_cxema'

par_tb_com_cxema = {'ny': 'Узлов: (Ny)',
                    'nv': 'Ветвей: (Nv)',
                    'na': 'Районов: (Na)',
                    'ny_o': 'Число отключенных узлов: (Ny_откл)',
                    'nv_o': 'Число отключенных ветвей: (Nv_откл)',
                    'nby': 'Число балансир. узлов : (N_бу)',
                    'ngen': 'Число узлов с заданн. V: (N_ген)',
                    'ntran': 'Число трансформаторов : (N_Тр)',
                    'nlep': 'Число ЛЭП : (N_ЛЭП)',
                    'nvikl': 'Число выключателей : (N_выкл.)',
                    'pg': 'P_ген: (Pg)',
                    'pn': 'P_наг: (Pn)',
                    'dp': 'Потери P (переменные): (dP)',
                    'pby': 'P_баланс. узла: (P_бу)',
                    'dpsh': 'Постоянные Потери : (dP_пост)',
                    'dv_min': 'Минимальное отклонение V (%) (dV_min)',
                    'dv_max': 'Максимальное отклонение V (%) (dV_max)',
                    'nt_max': 'Число перегруженных тр-ров (по I_доп) (I_тр)',
                    'max_it': 'Макс загрузка по току ТР (%) (I/I_доп-тр)',
                    'nl_nax': 'Число перегруженных ЛЭП (по I_доп) (I_лэп)',
                    'max_il': 'Макс загрузка по току ЛЭП (%) (I/I_доп-лэп)'}

if __name__ == '__main__':
    import win32com.client
    from R_modules.load_and_save_file.load_file_rastrwin import load_file
    from R_modules.load_and_save_file.shablons_dir import shablon_file_regime
    from R_modules.getting_parameters.get_parameter import GettingParameter

    rastr = win32com.client.Dispatch('Astra.Rastr')

    load_file(rastr_win=rastr,
              file_path=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\cx195.rg2',
              shablon=shablon_file_regime,
              switch_command_line=True)

    for i in par_tb_com_cxema:
        par_obj = GettingParameter(rastr_win=rastr,
                                   table=tb_com_cxema,
                                   column=i, switch_command_line=True)
        par = par_obj.get(row_id=0)
        print(f'{par_tb_com_cxema[i]} = {par}')

