import win32com.client
from RastrWinLib.loading.load import load_file, shablon_file_regime, shablon_file_automation, \
    shablon_file_dynamic
from RastrWinLib.calculation.regim import SteadyState
from RastrWinLib.variables.variable_parametrs import VariableDefRowId, VariableSetSel, FindNextSel
from RastrWinLib.loading.save import save_file
from RastrWinLib.variables.group_correction import GroupCorr

dir = r'L:\SER\Охрименко\03. RastrWinLib\16\14'
file_one_rg2 = rf'{dir}\14 АДТН обр обр.rg2'
file_two_rst = rf'{dir}\Дин модель Лето минимум.rst'
file_log_gen = rf'{dir}\log_set_gen.txt'
file_log_vetv = rf'{dir}\log_set_vetv.txt'
file_log_node = rf'{dir}\log_set_node.txt'
file_log_area = rf'{dir}\log_set_area.txt'

n = open(file_log_node, 'w')
f = open(file_log_gen, 'w')
g = open(file_log_vetv, 'w')
area = open(file_log_area, 'w')

one_rastr = win32com.client.Dispatch("Astra.Rastr")
two_rastr = win32com.client.Dispatch("Astra.Rastr")

rgm_one = SteadyState(rastr_win=one_rastr, switch_command_line=False)
rgm_two = SteadyState(rastr_win=two_rastr, switch_command_line=False)

load_file(rastr_win=one_rastr, file_path=file_one_rg2, shablon=shablon_file_regime, switch_command_line=False)
load_file(rastr_win=two_rastr, file_path=file_two_rst, shablon=shablon_file_dynamic, switch_command_line=False)

# ********** Генератор ****************
gen_table_file_one = one_rastr.Tables("Generator")
max_col_gen_file_one = gen_table_file_one.Count - 1
print(f'Max Gen file_one: {max_col_gen_file_one}')

name_obj_gen_file_one = VariableSetSel(rastr_win=one_rastr, table='Generator', column='Name', switch_command_line=False)
num_obj_gen_file_one = VariableSetSel(rastr_win=one_rastr, table='Generator', column='Node', switch_command_line=False)
sta_obj_gen_file_one = VariableSetSel(rastr_win=one_rastr, table='Generator', column='sta', switch_command_line=False)
p_gen_obj_gen_file_one = VariableSetSel(rastr_win=one_rastr, table='Generator', column='P', switch_command_line=False)
q_gen_obj_gen_file_one = VariableSetSel(rastr_win=one_rastr, table='Generator', column='Q', switch_command_line=False)

for i in range(0, max_col_gen_file_one):
    # файл 1
    name_gen_file_one = name_obj_gen_file_one.get(row_id=i)
    num_gen_file_one = num_obj_gen_file_one.get(row_id=i)
    sta_gen_file_one = sta_obj_gen_file_one.get(row_id=i)
    p_gen_gen_file_one = p_gen_obj_gen_file_one.get(row_id=i)
    q_gen_gen_file_one = p_gen_obj_gen_file_one.get(row_id=i)

    # файл 2
    row_obj_gen_file_two = FindNextSel(rastr_win=two_rastr, table='Generator', key=f"Num={num_gen_file_one}")
    row_gen_file_two = row_obj_gen_file_two.row()

    if row_gen_file_two != (-1):
        p_gen_obj_gen_file_two = VariableSetSel(rastr_win=two_rastr, table='Generator', column='P',
                                                switch_command_line=False)
        p_gen_gen_file_two = p_gen_obj_gen_file_two.get(row_id=i)

        p_gen_obj_gen_file_two = VariableDefRowId(rastr_win=two_rastr, table='Generator', switch_command_line=False)
        p_gen_obj_gen_file_two.make_changes(column='P', row_id=row_gen_file_two, value=p_gen_gen_file_one)

        q_gen_obj_gen_file_two = VariableDefRowId(rastr_win=two_rastr, table='Generator', switch_command_line=False)
        q_gen_obj_gen_file_two.make_changes(column='Q', row_id=row_gen_file_two, value=q_gen_gen_file_one)

        sta_gen_obj_gen_file_two = VariableDefRowId(rastr_win=two_rastr, table='Generator', switch_command_line=False)
        sta_gen_obj_gen_file_two.make_changes(column='sta', row_id=row_gen_file_two, value=sta_gen_file_one)

        name_obj_gen_file_two = VariableSetSel(rastr_win=two_rastr, table='Generator', column='Name',
                                               switch_command_line=False)
        name_gen_file_two = name_obj_gen_file_two.get(row_id=row_gen_file_two)

        p_gen_obj_gen_file_one_afte = VariableSetSel(rastr_win=two_rastr, table='Generator', column='P',
                                                     switch_command_line=False)
        pg_afte = p_gen_obj_gen_file_one_afte.get(row_id=row_gen_file_two)

        f.write(
            f'{i}. Row_id={row_gen_file_two} - Num={num_gen_file_one} - Name={name_gen_file_one}: P до = {p_gen_gen_file_two} => P после = {pg_afte}\n')
f.close()

# ********** Ветвь ****************
vetv_table_file_one = one_rastr.Tables("vetv")
max_col_vetv_file_one = vetv_table_file_one.Count - 1
print(f'Max VETV file_one: {max_col_vetv_file_one}')

ip_obj_vetv_file_one = VariableSetSel(rastr_win=one_rastr, table='vetv', column='ip', switch_command_line=False)
iq_obj_vetv_file_one = VariableSetSel(rastr_win=one_rastr, table='vetv', column='iq', switch_command_line=False)
np_obj_vetv_file_one = VariableSetSel(rastr_win=one_rastr, table='vetv', column='np', switch_command_line=False)
sta_obj_vetv_file_one = VariableSetSel(rastr_win=one_rastr, table='vetv', column='sta', switch_command_line=False)
name_obj_vetv_file_one = VariableSetSel(rastr_win=one_rastr, table='vetv', column='name', switch_command_line=False)

for j in range(0, max_col_vetv_file_one):
    # файл 1
    ip_vetv_file_one = ip_obj_vetv_file_one.get(row_id=j)
    iq_vetv_file_one = iq_obj_vetv_file_one.get(row_id=j)
    np_vetv_file_one = np_obj_vetv_file_one.get(row_id=j)
    name_vetv_file_one = name_obj_vetv_file_one.get(row_id=j)
    sta_vetv_file_one = sta_obj_vetv_file_one.get(row_id=j)

    # файл 2
    row_obj_vetv_file_two = FindNextSel(rastr_win=two_rastr, table='vetv',
                                        key=f"(ip={ip_vetv_file_one}&iq={iq_vetv_file_one}&np={np_vetv_file_one})|(ip={iq_vetv_file_one}&iq={ip_vetv_file_one}&np={np_vetv_file_one})")
    row_vetv_file_two = row_obj_vetv_file_two.row()

    if row_vetv_file_two != (-1):
        sta_vetv_obj_file_two_do = VariableSetSel(rastr_win=two_rastr, table='vetv', column='sta',
                                                  switch_command_line=False)
        sta_vetv_file_two_do = sta_vetv_obj_file_two_do.get(row_id=row_vetv_file_two)

        sta_vetv_obj_vetv_file_two = VariableDefRowId(rastr_win=two_rastr, table='vetv', switch_command_line=False)
        sta_vetv_obj_vetv_file_two.make_changes(column='sta', row_id=row_vetv_file_two, value=sta_vetv_file_one)

        sta_vetv_obj_file_two_posle = VariableSetSel(rastr_win=two_rastr, table='vetv', column='sta',
                                                     switch_command_line=False)
        sta_vetv_file_two_posle = sta_vetv_obj_file_two_posle.get(row_id=row_vetv_file_two)

        g.write(
            f'{j}. Row_id={row_vetv_file_two} - Name={name_vetv_file_one}: sta_FILE 1 = {sta_vetv_file_one} => sta_FILE 2 = {sta_vetv_file_two_do} => sta_FILE New = {sta_vetv_file_two_posle}\n')
g.close()

# # ********** Узлы ****************
node_table_file_one = one_rastr.Tables("node")
max_col_node_file_one = node_table_file_one.Count - 1
print(f'Max Node file_one: {max_col_node_file_one}')

ny_obj_node_file_one = VariableSetSel(rastr_win=one_rastr, table='node', column='ny', switch_command_line=False)
name_obj_node_file_one = VariableSetSel(rastr_win=one_rastr, table='node', column='name', switch_command_line=False)
sta_obj_node_file_one = VariableSetSel(rastr_win=one_rastr, table='node', column='sta', switch_command_line=False)
vzd_obj_node_file_one = VariableSetSel(rastr_win=one_rastr, table='node', column='vzd', switch_command_line=False)
p_obj_node_file_one = VariableSetSel(rastr_win=one_rastr, table='node', column='pg', switch_command_line=False)
q_obj_node_file_one = VariableSetSel(rastr_win=one_rastr, table='node', column='qg', switch_command_line=False)

for y in range(0, max_col_node_file_one):
    # файл 1
    ny_node_file_one = ny_obj_node_file_one.get(row_id=y)
    p_node_file_one = p_obj_node_file_one.get(row_id=y)
    q_node_file_one = q_obj_node_file_one.get(row_id=y)
    name_node_file_one = name_obj_node_file_one.get(row_id=y)
    sta_node_file_one = sta_obj_node_file_one.get(row_id=y)
    vzd_node_file_one = vzd_obj_node_file_one.get(row_id=y)

    # файл 2
    row_obj_node_file_two = FindNextSel(rastr_win=two_rastr, table='node', key=f"ny={ny_node_file_one}")
    row_node_file_two = row_obj_node_file_two.row()

    if row_node_file_two != (-1):
        ny_obj_node_file_two = VariableSetSel(rastr_win=one_rastr, table='node', column='ny', switch_command_line=False)
        name_obj_node_file_two = VariableSetSel(rastr_win=one_rastr, table='node', column='name',
                                                switch_command_line=False)
        ny_node_file_two = ny_obj_node_file_two.get(row_id=row_node_file_two)
        name_node_file_two = name_obj_node_file_two.get(row_id=row_node_file_two)

        sta_node_obj_file_two_do = VariableSetSel(rastr_win=two_rastr, table='node', column='sta',
                                                  switch_command_line=False)
        sta_node_file_two_do = sta_node_obj_file_two_do.get(row_id=row_node_file_two)

        p_obj_node_file_two = VariableDefRowId(rastr_win=two_rastr, table='node', switch_command_line=False)
        p_obj_node_file_two.make_changes(column='pg', row_id=row_node_file_two, value=p_node_file_one)

        q_obj_node_file_two = VariableDefRowId(rastr_win=two_rastr, table='node', switch_command_line=False)
        q_obj_node_file_two.make_changes(column='qg', row_id=row_node_file_two, value=q_node_file_one)

        sta_obj_node_file_two = VariableDefRowId(rastr_win=two_rastr, table='node', switch_command_line=False)
        sta_obj_node_file_two.make_changes(column='sta', row_id=row_node_file_two, value=sta_node_file_one)

        vzd_obj_node_file_two = VariableDefRowId(rastr_win=two_rastr, table='node', switch_command_line=False)
        vzd_obj_node_file_two.make_changes(column='vzd', row_id=row_node_file_two, value=vzd_node_file_one)

        sta_node_obj_file_two_posle = VariableSetSel(rastr_win=two_rastr, table='node', column='sta',
                                                     switch_command_line=False)
        sta_node_file_two_posle = sta_node_obj_file_two_posle.get(row_id=row_node_file_two)

        vzd_node_obj_file_two_posle = VariableSetSel(rastr_win=two_rastr, table='node', column='vzd',
                                                     switch_command_line=False)
        vzd_node_file_two_posle = vzd_node_obj_file_two_posle.get(row_id=row_node_file_two)

        n.write(
            f'{y}. Row_id={row_node_file_two}; File_1: ny={ny_node_file_one}; name={name_node_file_one}; sta={sta_node_file_one}; vzd={vzd_node_file_one} -> File_2 ny={ny_node_file_two}; name={name_node_file_two}; sta_FILE До = {sta_node_file_two_do} => sta_FILE New = {sta_node_file_two_posle}; vzd_posle={vzd_node_file_two_posle}\n')
n.close()

# ********** Районы ****************
area_table_file_one = one_rastr.Tables("area")
max_col_area_file_one = area_table_file_one.Count - 1
print(f'Max Area file_one: {max_col_area_file_one}')

for x in range(0, max_col_area_file_one):
    na_area_obj_file_one = VariableSetSel(rastr_win=one_rastr, table='area', column='na', switch_command_line=True)
    na_area_node_file_one = na_area_obj_file_one.get(row_id=x)

    name_area_obj_file_one = VariableSetSel(rastr_win=one_rastr, table='area', column='name', switch_command_line=True)
    name_area_node_file_one = name_area_obj_file_one.get(row_id=x)

    pg_area_obj_file_one = VariableSetSel(rastr_win=one_rastr, table='area', column='pg', switch_command_line=True)
    pg_area_node_file_one = pg_area_obj_file_one.get(row_id=x)

    pn_area_obj_file_one = VariableSetSel(rastr_win=one_rastr, table='area', column='pn', switch_command_line=True)
    pn_area_file_one = pn_area_obj_file_one.get(row_id=x)

    if na_area_node_file_one > 0:
        row_obj_area_file_two = FindNextSel(rastr_win=two_rastr, table='area', key=f"na={pn_area_file_one}")
        row_area_file_two = row_obj_area_file_two.row()

        if row_area_file_two != (-1):
            na_obj_file_two = VariableSetSel(rastr_win=two_rastr, table='area', column='na', switch_command_line=True)
            na_file_two = na_obj_file_two.get(row_id=row_area_file_two)

            pg_area_file_two = VariableSetSel(rastr_win=two_rastr, table='area', column='pg', switch_command_line=True)
            pg_area_file_two = pg_area_file_two.get(row_id=row_area_file_two)

            if pg_area_file_two > 0:
                k_pg = pg_area_node_file_one / pg_area_file_two
            else:
                k_pg = 1

            grupCorr_pg_file_two = GroupCorr(rastr_win=two_rastr, table='node', column='pg', switch_command_line=True)
            grupCorr_pg_file_two.calc(key=f'na={na_file_two}', formula=f'pg*{k_pg}')

            na_area_obj_file_two = VariableSetSel(rastr_win=two_rastr, table='area', column='na',
                                                  switch_command_line=True)
            na_area_node_file_two = na_area_obj_file_two.get(row_id=row_area_file_two)

            name_area_obj_file_two = VariableSetSel(rastr_win=two_rastr, table='area', column='name',
                                                    switch_command_line=True)
            name_area_file_two = name_area_obj_file_two.get(row_id=row_area_file_two)

            pg_area_obj_file_two = VariableSetSel(rastr_win=two_rastr, table='area', column='pg',
                                                  switch_command_line=True)
            pg_area_node_file_two = pg_area_obj_file_two.get(row_id=row_area_file_two)

            pn_area_obj_file_two = VariableSetSel(rastr_win=two_rastr, table='area', column='pn',
                                                  switch_command_line=True)
            pn_area_node_file_two = pn_area_obj_file_two.get(row_id=row_area_file_two)

            area.write(
                f'{x}. na_f1={na_area_node_file_one}; name_f1={name_area_node_file_one}; pg_f1={pg_area_node_file_one} => na_f2={na_area_node_file_two}; name_f2={name_area_file_two}; pg_f2={pg_area_node_file_two}; k_pg={k_pg}\n')

area.close()

save_file(rastr_win=two_rastr, file_path=rf'{dir}\Режим 14.rst',
          shablon=shablon_file_dynamic, switch_command_line=True)
