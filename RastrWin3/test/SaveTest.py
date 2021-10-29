from RastrWin3.Load import load_file
from RastrWin3.AstraRastr import RASTR
from RastrWin3.Save import save_file

load_file(rastr_win=RASTR,
          path_file=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.scn',
          shabl='сценарий',
          switch_command_line=True)

load_file(rastr_win=RASTR,
          path_file=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.rst',
          shabl='динамика',
          switch_command_line=True)

save_file(path_file=r'C:\Users\Ohrimenko_AG\Desktop\test_913.rst',
          switch_command_line=True,
          shabl='динамика')
