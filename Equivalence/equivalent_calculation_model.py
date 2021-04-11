# -*- coding: utf-8 -*-

from RastrWinLib.loading.load import load_file
from RastrWinLib.loading.shablon import shablon_file_regime
from RastrWinLib.getting.get import GetTableCommonInfo
from RastrWinLib.calculation.dyn_rgm_ekv_calc import SteadyState
from RastrWinLib.variables.removal_marked_objects import RemoveSelObjects
from RastrWinLib.calculation.dyn_rgm_ekv_calc import Equivalent
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.settings.calculation import SetEkviv


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


