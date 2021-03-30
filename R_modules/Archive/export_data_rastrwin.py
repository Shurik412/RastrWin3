from rastr_variable import findNextSelFun


def exportData(rastr_win, work_sheet, tables, parameter, number_id, par_num_or_id='Num',
               snap_shot_file_index=0, col_add_arr_plot=1, row_add_arr_plot=2, switch_command_line=True):
    rastr_win = rastr_win
    tables: str
    parameter: str
    switch_command_line: bool
    col_add_arr_plot: int
    row_add_arr_plot: int
    row_id: int

    if tables == 'Generator':
        par_num_or_id = 'Num'
    elif tables == 'node':
        par_num_or_id = 'ny'
    elif tables == 'vetv':
        par_num_or_id = ''
    else:
        par_num_or_id = par_num_or_id

    row_id = findNextSelFun(rastr_win, tables, number_id, par_num_or_id, switch_command_line)

    list_param_and_time = rastr_win.GetChainedGraphSnapshot(tables, parameter, row_id, snap_shot_file_index)

    if tables == 'Generator':
        name_object = rastr_win.Tables(tables).Cols('Name').Z(row_id)
    elif tables == 'node':
        name_object = rastr_win.Tables(tables).Cols('name').Z(row_id)
    elif tables == 'vetv':
        name_object = rastr_win.Tables(tables).Cols('name').Z(row_id)
    else:
        name_object = 'Object.None'

    list_parameter = []
    list_time = []
    for i in range(len(list_param_and_time)):
        for j in range(len(list_param_and_time[i])):
            if j == 0:
                list_parameter.append(list_param_and_time[i][j])
            elif j == 1:
                list_time.append(list_param_and_time[i][j])

    for ind_t, t in enumerate(list_time):
        work_sheet.cell(column=col_add_arr_plot, row=row_add_arr_plot + ind_t).value = t
    work_sheet.cell(column=col_add_arr_plot, row=row_add_arr_plot - 1).value = 't, c'

    for ind_par, p in enumerate(list_parameter):
        work_sheet.cell(column=col_add_arr_plot + 1, row=row_add_arr_plot + ind_par).value = p
    work_sheet.cell(column=col_add_arr_plot + 1, row=row_add_arr_plot - 1).value = f'{name_object}, {parameter}'

    list_parameter.clear()
    list_time.clear()

    if switch_command_line is not False:
        print(f'График построен!')
