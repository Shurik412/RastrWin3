# -*- coding: utf-8 -*-

from R_modules.load_and_save_file.load_file_rastrwin import load_file
from R_modules.load_and_save_file.shablons_dir import shablon_file_dynamic, shablon_file_scenario, shablon_file_regime
from tabl_com_cxema import tb_com_cxema, par_tb_com_cxema
from R_modules.getting_parameters.get_parameter import GettingParameterAttribute, GettingParameter, GetTableCommonInfo
from R_modules.calculation.dyn_rgm_ekv_calc import SteadyState
from R_modules.Tables_Parametrs.Tables_and_parametrs import table_node, table_vetv, table_generator, table_name_node, \
    table_name_vetv, table_name_generator,
from R_modules.variables.removal_marked_objects import RemoveSelObjects
from R_modules.calculation.dyn_rgm_ekv_calc import Equivalent
from R_modules.object_rastr import RASTR
from R_modules.settings_parametrs.settings_ekv import SetEkviv


print('*********************************************')
print('*********** Эквивалентирование **************')
print('*********************************************')

regime = SteadyState(rastr_win=RASTR, switch_command_line=True)
equivalent = Equivalent(rastr_win=RASTR, switch_command_line=True)

file_rg2 = r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\cx195.rg2'
load_file(rastr_win=RASTR, file_path=file_rg2, shablon=shablon_file_regime, switch_command_line=True)

common_info = GetTableCommonInfo(rastr_win=RASTR, switch_command_line=True)
common_info.get()

regime.rgm()

remove_obj_sel = RemoveSelObjects(rastr_win=RASTR, switch_command_line=True)
remove_obj_sel.remove_sel_node()
remove_obj_sel.remove_sel_vetv()
remove_obj_sel.remove_sel_generator()

settings_com_ekviv = SetEkviv(rastr_win=RASTR)
settings_com_ekviv.set(selekv=0,
                       met_ekv=0,
                       tip_ekv=0,
                       ekvgen=0,
                       tip_gen=1,
                       kfc_x='',
                       pot_gen=0,
                       kpn='',
                       tip_sxn=0,
                       smart=0,
                       zmax=1000,
                       otm_n=0)
equivalent.ekv()


