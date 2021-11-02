# -*- coding: utf-8 -*-
from RastrWin3.AstraRastr import RASTR
from RastrWin3.Load import load_file, LoadFile
from RastrWin3.Save import save_file
from RastrWin3.ActionsObject.get import GettingParameter
from icecream import ic
from RastrWin3.Templates import directory_shabl
from win32com.client import Dispatch

load = LoadFile(rastr_win=RASTR)

load.load(path=r'C:\Program Files\RastrWin3\RastrWin3\test-rastr\cx195.rg2',
          shablon=r'C:\Program Files\RastrWin3\RastrWin3\SHABLON\режим.rg2',
          kod_rg=1)

load.load(path=r'',
          shablon=r'C:\Program Files\RastrWin3\RastrWin3\SHABLON\автоматика.dfw',
          kod_rg=1)

# load_file(rastr_win=RASTR,
#           path_file=r'C:\Program Files\RastrWin3\RastrWin3\test-rastr\cx195.rg2',
#           shabl='режим',
#           switch_command_line=True)
#
# RASTR.Load(1, r'C:\Program Files\RastrWin3\RastrWin3\test-rastr\cx195.rg2',
#                  r'C:\Program Files\RastrWin3\RastrWin3\SHABLON\режим.rg2')
# RASTR.Load(1, '',
#            r'C:\Program Files\RastrWin3\RastrWin3\SHABLON\автоматика.dfw')

tb = RASTR.Tables('node')
tb.SetSel('ny=1')
row = tb.FindNextSel(-1)
print(row)

# get_ = GettingParameter(rastr_win=RASTR)

# Получение фактическое количество строк в таблице

# ic(get_.get_count_table(table='Generator'))

# Получение фактическое количество строк в таблице
# ic(get_.get_cell_row(table='node',
#                      column='name',
#                      row_id=0))
