# -*- coding: utf-8 -*-
from RastrWin3.ActionsObject.selection import Selection
from RastrWin3.AstraRastr import RASTR
from RastrWin3.Load import LoadFile
from RastrWin3.Save import save_file

_load = LoadFile(rastr_win=RASTR)
_load.load(path_file=r'C:\Users\Ohrimenko_AG\Desktop\cx195.rg2', name_shabl_russian='режим')

sel = Selection(rastr_win=RASTR)
sel.select_by_viborka(table='vetv', viborka='', switch_command_line=False)
# sel.remove_all_selection(table='vetv', switch_command_line=True)

save_file(rastr_win=RASTR,
          path_file=r'C:\Users\Ohrimenko_AG\Desktop\cx195_3.rg2',
          name_shabl_russian='режим')
