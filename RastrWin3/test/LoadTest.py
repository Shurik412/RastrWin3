from RastrWin3.AstraRastr import RASTR
from RastrWin3.Load import load_file

# Проверка параметра path_file (результат - выполнено)
print('Проверка параметра path_file')
load_file(rastr_win=RASTR, rg_kod=1, path_file='', shabl='режим', switch_command_line=True)
load_file(rastr_win=RASTR, rg_kod=1, path_file='', shabl='динамика', switch_command_line=True)
load_file(rastr_win=RASTR, rg_kod=1, path_file=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\cx195_.rg2',
          shabl='режим', switch_command_line=True)

# Проверка параметра switch_command_line=False and True (результат - выполнено)
print('Проверка параметра switch_command_line=False and True')
load_file(rastr_win=RASTR, rg_kod=1, path_file='', shabl='динамика', switch_command_line=False)
load_file(rastr_win=RASTR, rg_kod=1, path_file=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\cx195_.rg2',
          shabl='режим', switch_command_line=False)

# Проверка параметра shabl = '' (результат - выполнено)
print('Проверка параметра shabl = ""')
load_file(rastr_win=RASTR, rg_kod=1, path_file=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.scn',
          shabl='сценарий', switch_command_line=True)
load_file(rastr_win=RASTR, rg_kod=1, path_file=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.rst',
          shabl='динамика', switch_command_line=True)
load_file(rastr_win=RASTR, rg_kod=1, path_file=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.rst',
          shabl='динамика', switch_command_line=False)