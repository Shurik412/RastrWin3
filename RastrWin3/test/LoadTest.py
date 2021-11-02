# -*- coding: utf-8 -*-
from RastrWin3.AstraRastr import RASTR
from RastrWin3.Load import LoadFile

load_obj = LoadFile(rastr_win=RASTR, switch_command_line=True)

# Проверка параметра path_file (результат - выполнено)
print('Проверка параметра path_file')

load_obj.load(kod_rg=1,
              path_file='',
              name_shabl_russian='режим')

load_obj.load(kod_rg=1,
              path_file=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\cx195.rg2',
              name_shabl_russian='режим')

# Проверка параметра switch_command_line=False and True (результат - выполнено)
print('Проверка параметра switch_command_line=False and True')
load_obj_two = LoadFile(rastr_win=RASTR, switch_command_line=False)
load_obj_two.load(kod_rg=1,
                  path_file=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.rst',
                  name_shabl_russian='динамика')

load_obj_two.load(kod_rg=1,
                  path_file=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.scn',
                  name_shabl_russian='сценарий')

# Проверка параметра shabl = '' (результат - выполнено)
print('Проверка параметра shabl = ""')
load_obj.load(kod_rg=1,
              path_file=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.rst',
              name_shabl_russian='динамика')

load_obj.load(kod_rg=1,
              path_file=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.scn',
              name_shabl_russian='сценарий')
