# -*- coding: utf-8 -*-
from RastrWin3.AstraRastr import RASTR
from RastrWin3.Load import load_file
from RastrWin3.Save import save_file

# load_file(rastr_win=RASTR, rg_kod=1, path_file='', shabl='режим', switch_command_line=True)
# load_file(rastr_win=RASTR, rg_kod=1, path_file='', shabl='динамика', switch_command_line=True)

load_file(rastr_win=RASTR, rg_kod=1,
          path_file=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\cx195.rg2',
          shabl='режим', switch_command_line=True)

# load_file(rastr_win=RASTR, rg_kod=1, path_file=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.scn',
#           shabl='сценарий', switch_command_line=True)
# load_file(rastr_win=RASTR, rg_kod=1, path_file=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.rst',
#           shabl='динамика', switch_command_line=True)

save_file(path_file=r'C:\Users\Ohrimenko_AG\Desktop\cx195_1.rg2',
          switch_command_line=True,
          shabl='режим')

load_file(rastr_win=RASTR,
          path_file=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.scn',
          shabl='сценарий',
          switch_command_line=True)
print("Point 1")
load_file(rastr_win=RASTR,
          path_file=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.rst',
          shabl='динамика',
          switch_command_line=False)

save_file(path_file=r'C:\Users\Ohrimenko_AG\Desktop\test_9_2.rst',
          switch_command_line=True,
          shabl='динамика')

save_file(path_file=r'C:\Users\Ohrimenko_AG\Desktop\test_9_3.scn',
          switch_command_line=True,
          shabl='сценарий')

save_file(path_file=r'',
          switch_command_line=True,
          shabl='сценарий')

save_file(path_file=r'23',
          switch_command_line=True,
          shabl='сценарий')

print("Point 2")
save_file(path_file=r'',
          switch_command_line=False,
          shabl='сценарий')
