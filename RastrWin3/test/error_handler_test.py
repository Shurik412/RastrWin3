from RastrWin3.AstraRastr import RASTR
from RastrWin3.Load import load_file
from RastrWin3.Tools.error_handler import error_load_file
from RastrWin3.Templates import directory_shabl

# @error_load_file
# def load(path='', kd=1):
#     RASTR.Load(kd, path, directory_shabl(rus_name_shabl='автоматика'))
#
#
# load(path='sd', kd=1)

# RASTR.Load(1, r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\cx195.rg2', '')

load_file(rastr_win=RASTR,
          path_file=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\cx195_.rg2',
          shabl="",
          switch_command_line=True)

load_file(rastr_win=RASTR,
          path_file=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\cx195.rg2',
          shabl="sd",
          switch_command_line=True)
