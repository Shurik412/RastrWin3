# # -*- coding: utf-8 -*-

from RastrWinLib.loading.load import load_file
from RastrWinLib.calculation.regim import SteadyState
from RastrWinLib.calculation.dynamic import Dynamic
from RastrWinLib.loading.shablon import Shabl
from RastrWinLib.AstraRastr import RASTR

file_rst = r'C:\Users\Ohrimenko_AG\Desktop\тест АР\test9.rst'
file_scn = r'C:\Users\Ohrimenko_AG\Desktop\тест АР\test9.scn'

file_rst2 = r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.rst'
file_scn2 = r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.scn'

load_file(file_path=file_rst2, shabl=Shabl.shablon_file_dynamic, switch_command_line=True)
load_file(file_path=file_scn2, shabl=Shabl.shablon_file_scenario, switch_command_line=True)
load_file(shabl=Shabl.shablon_file_automation, switch_command_line=True)

dyn = Dynamic(switch_command_line=True)
st = SteadyState(switch_command_line=True)

# st.rgm()
print(dyn.run())


# FWDynamic = RASTR.FWDynamic()
# FWDynamic.Run()
# print(f'TimeReached = {FWDynamic.TimeReached}')
# print(f'FWDynamic.Run() = {FWDynamic.Run()}')
# ResultMessage = FWDynamic.ResultMessage
# print(f'ResultMessage = {ResultMessage}')
