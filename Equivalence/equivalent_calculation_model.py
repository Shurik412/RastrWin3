# -*- coding: utf-8 -*-

from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.calculation.equivalent import Equivalent
from RastrWinLib.calculation.regim import SteadyState
# from RastrWinLib.getting.get import G
from RastrWinLib.loading.load import load_file
from RastrWinLib.loading.save import save_file
from RastrWinLib.loading.shablon import shablon_file_regime
from RastrWinLib.settings.equivalence import set_com_ekviv
from RastrWinLib.variables.removal_marked_objects import RemoveSelObjects
from gen_equivalent import equivalent_gen
# from gen_equivalent import equivalent_smart

print('*********************************************')
print('*********** Эквивалентирование **************')
print('*********************************************')

regime = SteadyState(rastr_win=RASTR, switch_command_line=False)
equivalent = Equivalent(rastr_win=RASTR, switch_command_line=False)

file_rg2 = r'C:\Users\Ohrimenko_AG\Desktop\Test_equiPy\test_123.rg2'
load_file(rastr_win=RASTR, file_path=file_rg2, shablon=shablon_file_regime, switch_command_line=True)

# common_info = GetTableCommonInfo(rastr_win=RASTR, switch_command_line=False)
# common_info.get()

regime.rgm()

remove_obj_sel = RemoveSelObjects(rastr_win=RASTR, switch_command_line=False)
remove_obj_sel.remove_sel_node()
remove_obj_sel.remove_sel_vetv()
#
# set_com_ekviv(selekv=0,
#               met_ekv=0,
#               tip_ekv=0,
#               ekvgen=0,
#               tip_gen=1,
#               kfc_x='',
#               pot_gen=0,
#               kpn='',
#               tip_sxn=0,
#               smart=0,
#               zmax=1000,
#               otm_n=0)


equivalent_gen(viborka_gen='(na=102 | na=103 | na=104 | na=105 | na=106 | na=107 | na=108 | na=109)')
# equivalent_smart(viborka_rayon = '(na=102 | na=103 | na=104 | na=105 | na=106 | na=107 | na=108 | na=109)')
regime.rgm()
# common_info.get()

save_file(rastr_win=RASTR,
          file_path=r'C:\Users\Ohrimenko_AG\Desktop\Test_equiPy\test_100.rg2',
          shablon=shablon_file_regime,
          switch_command_line=True)
