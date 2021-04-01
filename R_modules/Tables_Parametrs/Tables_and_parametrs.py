# -*- coding: utf-8 -*-

table_name_node = 'node'
table_node = {'sel': '"О" Отметка узла',
              'sta': '"S" Состояние узла',
              'tip': '"Тип" Тип узла',
              'ny': '"Номер" Номер узла',
              'name': '"Название" Название узла',
              'uhom': '"U_ном" Номинальное напряжение'}

table_name_vetv = 'vetv'
table_vetv = {'sel': '"О" Отметка ветви',
              'sta': '"S" Состояние ветви',
              'tip': '"Тип" Тип ветви',
              'ip': '"N_нач" Номер начала',
              'iq': '"N_кон" Номер конца',
              'name': '"Название" Название ветви'}

table_name_generator = 'Generator'
table_generator = {'sel': '"О" Отметка генератора',
                   'sta': '"S" Состояние генератора',
                   'Num': '"N агр" Номер генератора',
                   'Name': '"Название" Название генератора',
                   'Node': '"N узла" Номер узла'}

table_name_com_cxema = 'com_cxema'
table_com_cxema = {'ny': 'Узлов: (Ny)',
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
    from R_modules.getting_parameters.get_parameter import GettingParameter, GetTableCommonInfo

    rastr = win32com.client.Dispatch('Astra.Rastr')

    load_file(rastr_win=rastr,
              file_path=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\cx195.rg2',
              shablon=shablon_file_regime,
              switch_command_line=True)

    get_t = GetTableCommonInfo(rastr_win=rastr,
                               switch_command_line=True,
                               path_file_log=r'C:\Users\Ohrimenko_AG\Desktop\EquivalentPy\com_cxema_log.txt')
    get_t.get()
